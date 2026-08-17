"""Adapter pattern example in Python.

This module showcases the Adapter pattern with a legacy Login class and a new
interface that adapts it. The Adapter pattern allows incompatible interfaces to
work together by converting the interface of a class into another interface that
clients expect.
"""

import base64
import json
from abc import ABC, abstractmethod


class Login:
    """Login class.

    It is the adaptee interface that we want to adapt to a new interface.
    """

    EXPECTED_USERNAME = "admin"
    EXPECTED_PASSWORD = "admin"  # noqa: S105

    def post(self, username: str, password: str) -> bool:
        """Authenticate a user with plain username and password.

        Args:
            username: The username sent by the client.
            password: The password sent by the client.

        Returns:
            True when the credentials are expected, False otherwise.
        """
        return (
            username == self.EXPECTED_USERNAME
            and password == self.EXPECTED_PASSWORD
        )


class AuthenticationInterface(ABC):
    """Target interface expected by modern authentication clients.

    Authentication is provided through a signed JWT (JSON Web Token), so it
    is compatible with modern authentication methods such as OAuth2 and
    OpenID Connect. Any interface not compatible with this new interface
    will need to be adapted.
    """

    @abstractmethod
    def authenticate(self, jwt: str) -> bool:
        """Authenticate a request based on the supplied JWT.

        Args:
            jwt: The JWT token to validate.

        Returns:
            True when the token grants access, False otherwise.

        Raises:
            ValueError: When the token is malformed or its signature does
                not verify.
        """


class LoginAdapter(AuthenticationInterface):
    """Adapt the Login class to the new AuthenticationInterface interface.

    Attributes:
        JWT_LENGTH: Number of dot-separated segments expected in a JWT.
        login: The wrapped legacy Login used for credential checks.
    """

    JWT_LENGTH = 3

    def __init__(self, login: Login) -> None:
        """Initialize the adapter with the wrapped Login.

        Args:
            login: The legacy Login to delegate credential checks to.
        """
        self.login = login

    def authenticate(self, jwt: str) -> bool:
        """Authenticate a request based on the JWT with the Login interface.

        Args:
            jwt: The JWT token to validate.

        Returns:
            True when the username/password claims match the
            credentials expected by the wrapped Login, False otherwise.

        Raises:
            ValueError: When the JWT is malformed or is missing
            the username/password claims.

        """
        jwt_items = jwt.split(".")
        if len(jwt_items) != self.JWT_LENGTH:
            raise ValueError("Invalid JWT token format")

        try:
            payload_b64 = jwt_items[1]
            payload = json.loads(base64.urlsafe_b64decode(payload_b64 + "=="))
            username = payload["username"]
            password = payload["password"]
        except (json.JSONDecodeError, KeyError) as exc:
            raise ValueError("Missing JWT credentials") from exc

        return self.login.post(username, password)
