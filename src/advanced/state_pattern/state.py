"""State pattern example in Python."""

import logging
from abc import ABC, abstractmethod


class UserState(ABC):
    """Abstract base class for a user state."""

    @abstractmethod
    def enable(self, user: "User") -> None:
        """Handle the enable action for the user state.

        Args:
            user (User): The user instance.
        """
        pass

    @abstractmethod
    def disabled(self, user: "User") -> None:
        """Handle the disabled action for the user state.

        Args:
            user (User): The user instance.
        """
        pass

    @abstractmethod
    def close(self, user: "User") -> None:
        """Handle the close action for the user state.

        Args:
            user (User): The user instance.
        """
        pass

    @abstractmethod
    def login(self, user: "User") -> bool:
        """Handle the login action for the user state.

        Args:
            user (User): The user instance.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        pass


class Pending(UserState):
    """Concrete state representing a pending user.

    A pending user is not yet been activated or disabled.
    It can transition to active or closed states.
    """

    def enable(self, user: "User") -> None:
        """Transition from pending to active state.

        Args:
            user (User): The user instance.
        """
        logging.info("Transitioning from pending to active state.")
        user.set_state(Active())

    def disabled(self, user: "User") -> None:  # noqa: ARG002
        """Pending state cannot be disabled.

        Args:
            user (User): The user instance.
        """
        logging.info("Pending state cannot be disabled.")

    def close(self, user: "User") -> None:
        """Transition from pending to closed state.

        Args:
            user (User): The user instance.
        """
        logging.info("Transitioning from pending to closed state.")
        user.set_state(Closed())

    def login(self, user: "User") -> bool:  # noqa: ARG002
        """Pending users cannot login.

        Args:
            user (User): The user instance.

        Returns:
            bool: False, pending users must be activated first.
        """
        logging.info("Pending users cannot login. Activate first.")
        return False


class Active(UserState):
    """Concrete state representing an active user.

    An active user can transition to inactive or closed states.
    """

    def enable(self, user: "User") -> None:  # noqa: ARG002
        """Active state cannot be enabled again.

        Args:
            user (User): The user instance.
        """
        logging.info("Active state cannot be enabled again.")

    def disabled(self, user: "User") -> None:
        """Transition from active to inactive state.

        Args:
            user (User): The user instance.
        """
        logging.info("Transitioning from active to inactive state.")
        user.set_state(Inactive())

    def close(self, user: "User") -> None:
        """Transition from active to closed state.

        Args:
            user (User): The user instance.
        """
        logging.info("Transitioning from active to closed state.")
        user.set_state(Closed())

    def login(self, user: "User") -> bool:
        """Active users can login successfully.

        Args:
            user (User): The user instance.

        Returns:
            bool: True, login successful.
        """
        logging.info("User %s logged in successfully.", user.username)
        return True


class Inactive(UserState):
    """Concrete state representing an inactive user.

    An inactive user can transition to active or closed states.
    """

    def enable(self, user: "User") -> None:
        """Transition from inactive to active state.

        Args:
            user (User): The user instance.
        """
        logging.info("Transitioning from inactive to active state.")
        user.set_state(Active())

    def disabled(self, user: "User") -> None:  # noqa: ARG002
        """Inactive state cannot be disabled again.

        Args:
            user (User): The user instance.
        """
        logging.info("Inactive state cannot be disabled again.")

    def close(self, user: "User") -> None:
        """Transition from inactive to closed state.

        Args:
            user (User): The user instance.
        """
        logging.info("Transitioning from inactive to closed state.")
        user.set_state(Closed())

    def login(self, user: "User") -> bool:  # noqa: ARG002
        """Inactive users cannot login.

        Args:
            user (User): The user instance.

        Returns:
            bool: False, inactive users must be reactivated first.
        """
        logging.info("Inactive users cannot login. Reactivate first.")
        return False


class Closed(UserState):
    """Concrete state representing a closed user.

    A closed user cannot transition to any other state.
    """

    def enable(self, user: "User") -> None:  # noqa: ARG002
        """Closed state cannot be enabled.

        Args:
            user (User): The user instance.
        """
        logging.info("Closed state cannot be enabled.")

    def disabled(self, user: "User") -> bool:  # noqa: ARG002
        """Closed state cannot be disabled.

        Args:
            user (User): The user instance.
        """
        logging.info("Closed state cannot be disabled.")

    def close(self, user: "User") -> bool:  # noqa: ARG002
        """Closed state is already closed.

        Args:
            user (User): The user instance.
        """
        logging.info("Closed state is already closed.")

    def login(self, user: "User") -> bool:  # noqa: ARG002
        """Closed users cannot login.

        Args:
            user (User): The user instance.

        Returns:
            bool: False, closed accounts cannot login.
        """
        logging.info("Closed accounts cannot login.")
        return False


class User:
    """Context class that maintains a reference to a UserState instance."""

    def __init__(self, username: str) -> None:
        """Initialize the User with pending state."""
        self._state: UserState = Pending()
        self.username = username

    def set_state(self, state: UserState) -> None:
        """Set a new state for the user.

        Args:
            state (UserState): The new state to set.
        """
        self._state = state

    def enable(self) -> None:
        """Delegate the enable action to the current state."""
        self._state.enable(self)

    def disabled(self) -> None:
        """Delegate the disabled action to the current state."""
        self._state.disabled(self)

    def close(self) -> None:
        """Delegate the close action to the current state."""
        self._state.close(self)

    def login(self) -> bool:
        """Delegate the login action to the current state.

        Returns:
            bool: True if login successful, False otherwise.
        """
        return self._state.login(self)
