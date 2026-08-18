"""Bridge pattern module.

This module shows an example of the Bridge design pattern with a simple
implementation of modes for a UI framework. Each mode (DarkMode, LightMode, and
ColorBlindMode) implements the Mode interface and provides specific color
schemes for UI elements (Navbar and Footer). If more modes or elements are
needed, they can be easily added without modifying the Element class or the
existing modes.

"""

from abc import ABC, abstractmethod


class Mode(ABC):
    """Abstract mode interface."""

    @abstractmethod
    def get_background_color(self) -> str:
        """Get the background color for the mode.

        Returns:
            str: The background color as a string.
        """
        pass

    @abstractmethod
    def get_text_color(self) -> str:
        """Get the text color for the mode.

        Returns:
            str: The text color as a string.
        """
        pass

    @abstractmethod
    def get_highlight_color(self) -> str:
        """Get the highlight color for the mode.

        Returns:
            str: The highlight color as a string.
        """
        pass

    @abstractmethod
    def get_brightness(self) -> float:
        """Get the brightness factor for the mode (0.0 to 1.0).

        Returns:
            float: The brightness factor as a float.
        """
        pass


class DarkMode(Mode):
    """Concrete dark mode implementation."""

    def get_background_color(self) -> str:
        """Get the background color for the mode.

        Returns:
            str: The background color as a string.
        """
        return "black"

    def get_text_color(self) -> str:
        """Get the text color for the mode.

        Returns:
            str: The text color as a string.
        """
        return "white"

    def get_highlight_color(self) -> str:
        """Get the highlight color for the mode.

        Returns:
            str: The highlight color as a string.
        """
        return "darkgray"

    def get_brightness(self) -> float:
        """Get the brightness factor for the mode.

        Returns:
            float: The brightness factor as a float.
        """
        return 0.5


class LightMode(Mode):
    """Concrete light mode implementation."""

    def get_background_color(self) -> str:
        """Get the background color for the mode.

        Returns:
            str: The background color as a string.
        """
        return "white"

    def get_text_color(self) -> str:
        """Get the text color for the mode.

        Returns:
            str: The text color as a string.
        """
        return "black"

    def get_highlight_color(self) -> str:
        """Get the highlight color for the mode.

        Returns:
            str: The highlight color as a string.
        """
        return "lightgray"

    def get_brightness(self) -> float:
        """Get the brightness factor for the mode.

        Returns:
            float: The brightness factor as a float.
        """
        return 1.0


class ColorBlindMode(Mode):
    """Concrete color blind mode implementation."""

    def get_background_color(self) -> str:
        """Get the background color for the mode.

        Returns:
            str: The background color as a string.
        """
        return "lightyellow"

    def get_text_color(self) -> str:
        """Get the text color for the mode.

        Returns:
            str: The text color as a string.
        """
        return "darkblue"

    def get_highlight_color(self) -> str:
        """Get the highlight color for the mode.

        Returns:
            str: The highlight color as a string.
        """
        return "orange"

    def get_brightness(self) -> float:
        """Get the brightness factor for the mode.

        Returns:
            float: The brightness factor as a float.
        """
        return 1.0


class Element(ABC):
    """Abstract element interface.

    Element-intrinsic attributes (position, height_px) describe *what* the
    element is and are independent from the mode. The mode-driven palette and
    brightness are applied by apply_mode and stay orthogonal to the element's
    shape, showing the Bridge pattern.
    """

    position: str = ""
    height_px: int = 0

    def __init__(self, mode: Mode) -> None:
        """Initialize the element with a mode.

        Args:
            mode (Mode): The mode to apply to the element.
        """
        self.mode = mode
        self.apply_mode()

    def apply_mode(self) -> None:
        """Apply the mode's palette and brightness to the element.

        Sets the background color, text color, highlight color, and brightness
        attributes based on the current mode.
        """
        self.background_color = self.mode.get_background_color()
        self.text_color = self.mode.get_text_color()
        self.highlight_color = self.mode.get_highlight_color()
        self.brightness = self.mode.get_brightness()

    @abstractmethod
    def render(self) -> str:
        """Render the element as an HTML-like string using its current style.

        Returns:
            str: The HTML-like string representation of the element.
        """
        pass


class Navbar(Element):
    """Concrete navigation bar element.

    Sits at the top of the page with a bottom shadow tinted by the mode's
    highlight color.
    """

    position: str = "top"
    height_px: int = 64

    def render(self) -> str:
        """Render the navigation bar as an HTML-like string.

        Returns:
            str: The HTML-like string representation of the element.
        """
        return (
            f"<nav style='position:{self.position}; "
            f"height:{self.height_px}px; "
            f"background:{self.background_color}; "
            f"color:{self.text_color}; "
            f"box-shadow:0 2px 4px {self.highlight_color}; "
            f"opacity:{self.brightness}'>Navbar</nav>"
        )


class Footer(Element):
    """Concrete footer element.

    Sits at the bottom of the page with a top border tinted by the mode's
    highlight color.
    """

    position: str = "bottom"
    height_px: int = 40

    def render(self) -> str:
        """Render the footer as an HTML-like string.

        Returns:
            str: The HTML-like string representation of the element.
        """
        return (
            f"<footer style='position:{self.position}; "
            f"height:{self.height_px}px; "
            f"background:{self.background_color}; "
            f"color:{self.text_color}; "
            f"border-top:1px solid {self.highlight_color}; "
            f"opacity:{self.brightness}'>Footer</footer>"
        )
