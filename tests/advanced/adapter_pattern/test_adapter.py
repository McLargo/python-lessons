"""Tests for the adapter pattern implementation."""

import base64
import json

import pytest
from hypothesis import given
from hypothesis import strategies as st

from advanced.adapter_pattern import (
    AuthenticationInterface,
    Login,
    LoginAdapter,
)


def _b64url(data: dict) -> str:
    """Return a base64url-encoded JSON string of data."""
    raw = json.dumps(data).encode("utf-8")
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def _make_jwt(payload: dict) -> str:
    """Build a JWT-like string header.payload.signature for tests."""
    header_b64 = _b64url({"alg": "none", "typ": "JWT"})
    payload_b64 = _b64url(payload)
    signature_b64 = "signature"
    return f"{header_b64}.{payload_b64}.{signature_b64}"


class TestLogin:
    """Tests for the legacy Login adaptee."""

    def test_post_returns_true_with_valid_credentials(self):
        """Valid hardcoded credentials must authenticate successfully."""
        login = Login()

        assert login.post("admin", "admin") is True

    def test_post_returns_false_with_wrong_username(self):
        """A wrong username must not authenticate."""
        login = Login()

        assert login.post("root", "admin") is False

    def test_post_returns_false_with_wrong_password(self):
        """A wrong password must not authenticate."""
        login = Login()

        assert login.post("admin", "wrong") is False

    def test_post_returns_false_with_all_wrong(self):
        """Both wrong credentials must not authenticate."""
        login = Login()

        assert login.post("root", "wrong") is False

    def test_post_is_case_sensitive(self):
        """Login should be case sensitive on username and password."""
        login = Login()

        assert login.post("Admin", "admin") is False
        assert login.post("admin", "Admin") is False


class TestAuthenticationInterface:
    """Tests for the target abstract interface."""

    def test_cannot_be_instantiated_directly(self):
        """The abstract interface cannot be instantiated."""
        with pytest.raises(TypeError):
            AuthenticationInterface()  # type: ignore[abstract]

    def test_subclass_without_authenticate_cannot_instantiate(self):
        """A subclass that doesn't implement authenticate stays abstract."""

        class Incomplete(AuthenticationInterface):
            pass

        with pytest.raises(TypeError):
            Incomplete()  # type: ignore[abstract]

    def test_subclass_implementing_authenticate_works(self):
        """A concrete subclass that implements authenticate is usable."""

        class AlwaysTrue(AuthenticationInterface):
            def authenticate(self, jwt: str) -> bool:  # noqa: ARG002
                return True

        auth = AlwaysTrue()

        assert isinstance(auth, AuthenticationInterface)
        assert auth.authenticate("anything") is True


class TestLoginAdapter:
    """Tests for the LoginAdapter that adapts Login to the new interface."""

    def test_adapter_implements_authentication_interface(self):
        """The adapter must be a valid AuthenticationInterface."""
        adapter = LoginAdapter(Login())

        assert isinstance(adapter, AuthenticationInterface)

    def test_adapter_stores_login_reference(self):
        """The adapter keeps a reference to the wrapped Login instance."""
        login = Login()
        adapter = LoginAdapter(login)

        assert adapter.login is login

    def test_authenticate_with_valid_credentials_returns_true(self):
        """A JWT carrying the correct credentials must authenticate."""
        adapter = LoginAdapter(Login())
        jwt = _make_jwt({"username": "admin", "password": "admin"})

        assert adapter.authenticate(jwt) is True

    def test_authenticate_with_wrong_credentials_returns_false(self):
        """A JWT with wrong credentials must not authenticate."""
        adapter = LoginAdapter(Login())
        jwt = _make_jwt({"username": "admin", "password": "wrong"})

        assert adapter.authenticate(jwt) is False

    def test_authenticate_accepts_payload_needing_padding(self):
        """The adapter must decode payloads of any base64 length."""
        adapter = LoginAdapter(Login())
        jwt = _make_jwt({"username": "admin", "password": "admin", "x": 1})

        assert adapter.authenticate(jwt) is True

    @pytest.mark.parametrize(
        "invalid_jwt",
        [
            "part",
            "two.parts",
            "four.parts.here.extra",
            "",
        ],
    )
    def test_authenticate_raises_on_wrong_segment_count(
        self,
        invalid_jwt: str,
    ):
        """A JWT without exactly three dot-separated parts must raise."""
        adapter = LoginAdapter(Login())

        with pytest.raises(ValueError, match="Invalid JWT token format"):
            adapter.authenticate(invalid_jwt)

    def test_authenticate_raises_on_invalid_json_payload(self):
        """A JWT whose payload is not JSON must raise a credentials error."""
        adapter = LoginAdapter(Login())
        header_b64 = _b64url({"alg": "none", "typ": "JWT"})
        # base64url of the bytes "not-json" decodes fine but is not JSON.
        payload_b64 = (
            base64.urlsafe_b64encode(
                b"not-json",
            )
            .rstrip(b"=")
            .decode("ascii")
        )
        jwt = f"{header_b64}.{payload_b64}.signature"

        with pytest.raises(ValueError, match="Missing JWT credentials"):
            adapter.authenticate(jwt)

    def test_authenticate_raises_when_username_claim_missing(self):
        """A JWT missing the username claim must raise."""
        adapter = LoginAdapter(Login())
        jwt = _make_jwt({"password": "admin"})

        with pytest.raises(ValueError, match="Missing JWT credentials"):
            adapter.authenticate(jwt)

    def test_authenticate_raises_when_password_claim_missing(self):
        """A JWT missing the password claim must raise."""
        adapter = LoginAdapter(Login())
        jwt = _make_jwt({"username": "admin"})

        with pytest.raises(ValueError, match="Missing JWT credentials"):
            adapter.authenticate(jwt)

    def test_authenticate_delegates_to_wrapped_login(self):
        """The adapter must delegate authentication to the wrapped Login."""

        class TrackingLogin(Login):
            def __init__(self):
                self.calls: list[tuple[str, str]] = []

            def post(self, username: str, password: str) -> bool:
                self.calls.append((username, password))
                return super().post(username, password)

        login = TrackingLogin()
        adapter = LoginAdapter(login)
        jwt = _make_jwt({"username": "admin", "password": "admin"})

        adapter.authenticate(jwt)

        assert login.calls == [("admin", "admin")]

    def test_jwt_length_constant(self):
        """The adapter exposes the expected JWT segment count."""
        assert LoginAdapter.JWT_LENGTH == 3


class TestLoginAdapterProperties:
    """Property-based tests for the adapter using Hypothesis."""

    @given(
        parts=st.lists(
            st.text(
                alphabet=st.characters(blacklist_characters="."),
                max_size=10,
            ),
            min_size=0,
            max_size=8,
        ).filter(lambda p: len(p) != 3),
    )
    def test_any_token_without_three_segments_raises(
        self,
        parts: list[str],
    ):
        """Any string with a segment count != 3 must be rejected."""
        adapter = LoginAdapter(Login())
        token = ".".join(parts)

        with pytest.raises(ValueError, match="Invalid JWT token format"):
            adapter.authenticate(token)
