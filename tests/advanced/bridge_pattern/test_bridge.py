"""Tests for the bridge pattern implementation."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from advanced.bridge_pattern import (
    ColorBlindMode,
    DarkMode,
    Element,
    Footer,
    LightMode,
    Mode,
    Navbar,
)

ALL_MODES = [DarkMode, LightMode, ColorBlindMode]
ALL_ELEMENTS = [Navbar, Footer]


@pytest.fixture(params=ALL_MODES, ids=["dark", "light", "colorblind"])
def mode(request: pytest.FixtureRequest) -> Mode:
    """Yield an instance of each concrete Mode."""
    return request.param()


@pytest.fixture(params=ALL_ELEMENTS, ids=["navbar", "footer"])
def element_cls(request: pytest.FixtureRequest) -> type[Element]:
    """Yield each concrete Element class (not yet instantiated)."""
    return request.param


class TestConcreteModes:
    """Each concrete Mode returns the palette and brightness defined by it."""

    def test_dark_mode_palette(self) -> None:
        dark = DarkMode()
        assert dark.get_background_color() == "black"
        assert dark.get_text_color() == "white"
        assert dark.get_highlight_color() == "darkgray"
        assert dark.get_brightness() == 0.5

    def test_light_mode_palette(self) -> None:
        light = LightMode()
        assert light.get_background_color() == "white"
        assert light.get_text_color() == "black"
        assert light.get_highlight_color() == "lightgray"
        assert light.get_brightness() == 1.0

    def test_color_blind_mode_palette(self) -> None:
        cb = ColorBlindMode()
        assert cb.get_background_color() == "lightyellow"
        assert cb.get_text_color() == "darkblue"
        assert cb.get_highlight_color() == "orange"
        assert cb.get_brightness() == 1.0

    def test_mode_is_abstract(self) -> None:
        """Mode cannot be instantiated directly."""
        with pytest.raises(TypeError):
            Mode()  # type: ignore[abstract]

    def test_brightness_is_in_valid_range(self, mode: Mode) -> None:
        """Brightness must be within the documented 0.0-1.0 range."""
        assert 0.0 <= mode.get_brightness() <= 1.0


class TestElementBaseContract:
    """Tests for the abstract Element and its intrinsic class attributes."""

    def test_element_is_abstract(self) -> None:
        """Element cannot be instantiated directly."""
        with pytest.raises(TypeError):
            Element(DarkMode())  # type: ignore[abstract]

    def test_navbar_intrinsic_shape(self) -> None:
        """Navbar carries element-intrinsic shape independent of any mode."""
        assert Navbar.position == "top"
        assert Navbar.height_px == 64

    def test_footer_intrinsic_shape(self) -> None:
        """Footer carries element-intrinsic shape independent of any mode."""
        assert Footer.position == "bottom"
        assert Footer.height_px == 40


class TestBridgeBehavior:
    """Cross-product tests: every element must work with every mode."""

    def test_apply_mode_syncs_all_style_attrs(
        self,
        element_cls: type[Element],
        mode: Mode,
    ) -> None:
        """After construction, the four style attributes match the mode."""
        element = element_cls(mode)

        assert element.background_color == mode.get_background_color()
        assert element.text_color == mode.get_text_color()
        assert element.highlight_color == mode.get_highlight_color()
        assert element.brightness == mode.get_brightness()

    def test_render_contains_mode_palette(
        self,
        element_cls: type[Element],
        mode: Mode,
    ) -> None:
        """The rendered string embeds every value coming from the Mode axis."""
        element = element_cls(mode)
        rendered = element.render()

        assert f"background:{mode.get_background_color()}" in rendered
        assert f"color:{mode.get_text_color()}" in rendered
        assert mode.get_highlight_color() in rendered
        assert f"opacity:{mode.get_brightness()}" in rendered

    def test_render_contains_element_shape(
        self,
        element_cls: type[Element],
        mode: Mode,
    ) -> None:
        """The rendered string embeds every value coming from Element axis."""
        element = element_cls(mode)
        rendered = element.render()

        assert f"position:{element_cls.position}" in rendered
        assert f"height:{element_cls.height_px}px" in rendered

    @pytest.mark.parametrize(
        ("element_cls", "open_tag", "close_tag"),
        [(Navbar, "<nav ", "</nav>"), (Footer, "<footer ", "</footer>")],
        ids=["navbar", "footer"],
    )
    def test_render_uses_correct_html_tag(
        self,
        element_cls: type[Element],
        open_tag: str,
        close_tag: str,
    ) -> None:
        """Each element renders with its own HTML-like tag."""
        rendered = element_cls(DarkMode()).render()

        assert open_tag in rendered
        assert rendered.endswith(close_tag)


class TestBridgeDecoupling:
    """The Bridge payoff: axes vary independently and share state cleanly."""

    def test_swapping_mode_at_runtime(self) -> None:
        """Re-assigning mode + calling apply_mode re-caches the style."""
        nav = Navbar(DarkMode())
        assert nav.background_color == "black"

        nav.mode = LightMode()
        nav.apply_mode()

        assert nav.background_color == "white"
        assert nav.text_color == "black"
        assert nav.brightness == 1.0

    def test_same_mode_shared_across_elements(self) -> None:
        """A single Mode instance drives every Element identically."""
        shared_mode = DarkMode()
        nav = Navbar(shared_mode)
        footer = Footer(shared_mode)

        assert nav.background_color == footer.background_color
        assert nav.text_color == footer.text_color
        assert nav.highlight_color == footer.highlight_color
        assert nav.brightness == footer.brightness

    def test_new_mode_requires_no_element_change(self) -> None:
        """Adding a new Mode does not require modifying any Element."""

        class HighContrastMode(Mode):
            def get_background_color(self) -> str:
                return "black"

            def get_text_color(self) -> str:
                return "yellow"

            def get_highlight_color(self) -> str:
                return "cyan"

            def get_brightness(self) -> float:
                return 1.0

        hc = HighContrastMode()
        nav = Navbar(hc)
        footer = Footer(hc)

        assert nav.background_color == "black"
        assert nav.text_color == "yellow"
        assert "cyan" in nav.render()
        assert footer.background_color == "black"
        assert footer.text_color == "yellow"
        assert "cyan" in footer.render()

    def test_new_element_requires_no_mode_change(self) -> None:
        """Adding a new Element does not require modifying any Mode."""

        class Sidebar(Element):
            position: str = "left"
            height_px: int = 800

            def render(self) -> str:
                return (
                    f"<aside style='position:{self.position}; "
                    f"height:{self.height_px}px; "
                    f"background:{self.background_color}; "
                    f"color:{self.text_color}'>Sidebar</aside>"
                )

        sidebar = Sidebar(LightMode())
        rendered = sidebar.render()

        assert sidebar.background_color == "white"
        assert sidebar.text_color == "black"
        assert "position:left" in rendered
        assert "height:800px" in rendered
        assert rendered.endswith("</aside>")


class TestBridgeProperties:
    """Property-based tests that prove the Bridge contract for any Mode."""

    @given(
        background=st.text(min_size=1, max_size=20),
        text=st.text(min_size=1, max_size=20),
        highlight=st.text(min_size=1, max_size=20),
        brightness=st.floats(
            min_value=0.0,
            max_value=1.0,
            allow_nan=False,
            allow_infinity=False,
        ),
    )
    def test_element_propagates_arbitrary_mode_values(
        self,
        background: str,
        text: str,
        highlight: str,
        brightness: float,
    ) -> None:
        """For any Mode, both Navbar and Footer carry its values faithfully.

        Property: whatever (background, text, highlight, brightness) tuple a
        Mode returns, every Element must (a) cache those exact values on its
        instance and (b) embed them in its rendered output. This is the
        Bridge contract expressed as an invariant.
        """

        class ArbitraryMode(Mode):
            def get_background_color(self) -> str:
                return background

            def get_text_color(self) -> str:
                return text

            def get_highlight_color(self) -> str:
                return highlight

            def get_brightness(self) -> float:
                return brightness

        mode = ArbitraryMode()

        for element_cls in (Navbar, Footer):
            element = element_cls(mode)

            assert element.background_color == background
            assert element.text_color == text
            assert element.highlight_color == highlight
            assert element.brightness == brightness

            rendered = element.render()
            assert f"background:{background}" in rendered
            assert f"color:{text}" in rendered
            assert highlight in rendered
            assert f"opacity:{brightness}" in rendered
