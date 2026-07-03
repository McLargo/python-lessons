"""Tests for the state pattern implementation."""

import logging
from unittest.mock import MagicMock

import pytest
from hypothesis import given
from hypothesis import strategies as st

from advanced.state_pattern import (
    Active,
    Closed,
    Inactive,
    Pending,
    User,
    UserState,
)


class TestPendingState:
    """Test the Pending state behavior."""

    def test_pending_enable_transitions_to_active(self, caplog) -> None:
        """Test transition from pending to active state with logging."""
        user = User("alice")
        assert isinstance(user._state, Pending)

        with caplog.at_level(logging.INFO):
            user.enable()

        assert isinstance(user._state, Active)
        assert "Transitioning from pending to active state." in caplog.text

    def test_pending_disabled_stays_pending(self, caplog) -> None:
        """Test that disabled action on pending state doesn't change state."""
        user = User("bob")
        assert isinstance(user._state, Pending)

        with caplog.at_level(logging.INFO):
            user.disabled()

        assert isinstance(user._state, Pending)
        assert "Pending state cannot be disabled." in caplog.text

    def test_pending_close_transitions_to_closed(self, caplog) -> None:
        """Test transition from pending to closed state with logging."""
        user = User("charlie")
        assert isinstance(user._state, Pending)

        with caplog.at_level(logging.INFO):
            user.close()

        assert isinstance(user._state, Closed)
        assert "Transitioning from pending to closed state." in caplog.text


class TestActiveState:
    """Test the Active state behavior."""

    def test_active_enable_stays_active(self, caplog) -> None:
        """Test that enable action on active state doesn't change state."""
        user = User("alice")
        user.set_state(Active())
        assert isinstance(user._state, Active)

        with caplog.at_level(logging.INFO):
            user.enable()

        assert isinstance(user._state, Active)
        assert "Active state cannot be enabled again." in caplog.text

    def test_active_disabled_transitions_to_inactive(self, caplog) -> None:
        """Test transition from active to inactive state with logging."""
        user = User("bob")
        user.set_state(Active())
        assert isinstance(user._state, Active)

        with caplog.at_level(logging.INFO):
            user.disabled()

        assert isinstance(user._state, Inactive)
        assert "Transitioning from active to inactive state." in caplog.text

    def test_active_close_transitions_to_closed(self, caplog) -> None:
        """Test transition from active to closed state with logging."""
        user = User("charlie")
        user.set_state(Active())
        assert isinstance(user._state, Active)

        with caplog.at_level(logging.INFO):
            user.close()

        assert isinstance(user._state, Closed)
        assert "Transitioning from active to closed state." in caplog.text


class TestInactiveState:
    """Test the Inactive state behavior."""

    def test_inactive_enable_transitions_to_active(self, caplog) -> None:
        """Test transition from inactive to active state with logging."""
        user = User("alice")
        user.set_state(Inactive())
        assert isinstance(user._state, Inactive)

        with caplog.at_level(logging.INFO):
            user.enable()

        assert isinstance(user._state, Active)
        assert "Transitioning from inactive to active state." in caplog.text

    def test_inactive_disabled_stays_inactive(self, caplog) -> None:
        """Test that disabled action on inactive state doesn't change state."""
        user = User("bob")
        user.set_state(Inactive())
        assert isinstance(user._state, Inactive)

        with caplog.at_level(logging.INFO):
            user.disabled()

        assert isinstance(user._state, Inactive)
        assert "Inactive state cannot be disabled again." in caplog.text

    def test_inactive_close_transitions_to_closed(self, caplog) -> None:
        """Test transition from inactive to closed state with logging."""
        user = User("charlie")
        user.set_state(Inactive())
        assert isinstance(user._state, Inactive)

        with caplog.at_level(logging.INFO):
            user.close()

        assert isinstance(user._state, Closed)
        assert "Transitioning from inactive to closed state." in caplog.text


class TestClosedState:
    """Test the Closed state behavior."""

    def test_closed_enable_stays_closed(self, caplog) -> None:
        """Test that enable action on closed state doesn't change state."""
        user = User("alice")
        user.set_state(Closed())
        assert isinstance(user._state, Closed)

        with caplog.at_level(logging.INFO):
            user.enable()

        assert isinstance(user._state, Closed)
        assert "Closed state cannot be enabled." in caplog.text

    def test_closed_disabled_stays_closed(self, caplog) -> None:
        """Test that disabled action on closed state doesn't change state."""
        user = User("bob")
        user.set_state(Closed())
        assert isinstance(user._state, Closed)

        with caplog.at_level(logging.INFO):
            user.disabled()

        assert isinstance(user._state, Closed)
        assert "Closed state cannot be disabled." in caplog.text

    def test_closed_close_stays_closed(self, caplog) -> None:
        """Test that close action on closed state doesn't change state."""
        user = User("charlie")
        user.set_state(Closed())
        assert isinstance(user._state, Closed)

        with caplog.at_level(logging.INFO):
            user.close()

        assert isinstance(user._state, Closed)
        assert "Closed state is already closed." in caplog.text


class TestLoginFunctionality:
    """Test the login functionality across all states."""

    def test_pending_user_cannot_login(self, caplog) -> None:
        """Test that pending users cannot login."""
        user = User("pending_user")
        assert isinstance(user._state, Pending)

        with caplog.at_level(logging.INFO):
            result = user.login()

        assert result is False
        assert "Pending users cannot login" in caplog.text

    def test_active_user_can_login(self, caplog) -> None:
        """Test that active users can login successfully."""
        user = User("active_user")
        user.enable()
        assert isinstance(user._state, Active)

        with caplog.at_level(logging.INFO):
            result = user.login()

        assert result is True
        assert "logged in successfully" in caplog.text
        assert "active_user" in caplog.text

    def test_inactive_user_cannot_login(self, caplog) -> None:
        """Test that inactive users cannot login."""
        user = User("inactive_user")
        user.enable()
        user.disabled()
        assert isinstance(user._state, Inactive)

        with caplog.at_level(logging.INFO):
            result = user.login()

        assert result is False
        assert "Inactive users cannot login" in caplog.text

    def test_closed_user_cannot_login(self, caplog) -> None:
        """Test that closed users cannot login."""
        user = User("closed_user")
        user.set_state(Closed())
        assert isinstance(user._state, Closed)

        with caplog.at_level(logging.INFO):
            result = user.login()

        assert result is False
        assert "Closed accounts cannot login." in caplog.text

    def test_multiple_successful_logins_for_active_user(
        self,
        caplog,
    ) -> None:
        """Test that active users can login multiple times."""
        user = User("multi_login")
        user.enable()
        assert isinstance(user._state, Active)

        # First login
        with caplog.at_level(logging.INFO):
            result1 = user.login()
        assert result1 is True

        caplog.clear()

        # Second login
        with caplog.at_level(logging.INFO):
            result2 = user.login()
        assert result2 is True

        # User should still be active
        assert isinstance(user._state, Active)

    def test_login_after_reactivation(self, caplog) -> None:
        """Test login after user reactivation."""
        user = User("reactivate_login")

        # Activate
        user.enable()
        assert isinstance(user._state, Active)

        # Deactivate
        user.disabled()
        assert isinstance(user._state, Inactive)

        # Cannot login while inactive
        result1 = user.login()
        assert result1 is False

        # Reactivate
        user.enable()
        assert isinstance(user._state, Active)

        # Can login after reactivation
        with caplog.at_level(logging.INFO):
            result2 = user.login()
        assert result2 is True
        assert "logged in successfully" in caplog.text

    @pytest.mark.parametrize(
        "state_class,expected_result",
        [
            (Pending, False),
            (Active, True),
            (Inactive, False),
            (Closed, False),
        ],
    )
    def test_login_behavior_by_state(
        self,
        state_class,
        expected_result: bool,
    ) -> None:
        """Parametrized test for login behavior in each state."""
        user = User("test_user")
        user.set_state(state_class())

        result = user.login()
        assert result is expected_result


class TestUserContext:
    """Test the User context class behavior."""

    def test_user_initialization(self) -> None:
        """Test that user initializes with pending state."""
        user = User("test_user")
        assert user.username == "test_user"
        assert isinstance(user._state, Pending)

    @given(username=st.text(min_size=1, max_size=100))
    def test_user_accepts_any_valid_username(self, username: str) -> None:
        """Property: User should accept any non-empty string as username."""
        user = User(username)
        assert user.username == username
        assert isinstance(user._state, Pending)

    def test_user_set_state(self) -> None:
        """Test that set_state correctly changes user state."""
        user = User("alice")
        assert isinstance(user._state, Pending)

        user.set_state(Active())
        assert isinstance(user._state, Active)

        user.set_state(Inactive())
        assert isinstance(user._state, Inactive)

        user.set_state(Closed())
        assert isinstance(user._state, Closed)

    def test_user_delegates_enable_to_state(self) -> None:
        """Test that user.enable() delegates to current state."""
        user = User("test")
        mock_state = MagicMock(spec=UserState)
        user.set_state(mock_state)

        user.enable()
        mock_state.enable.assert_called_once_with(user)

    def test_user_delegates_disabled_to_state(self) -> None:
        """Test that user.disabled() delegates to current state."""
        user = User("test")
        mock_state = MagicMock(spec=UserState)
        user.set_state(mock_state)

        user.disabled()
        mock_state.disabled.assert_called_once_with(user)

    def test_user_delegates_close_to_state(self) -> None:
        """Test that user.close() delegates to current state."""
        user = User("test")
        mock_state = MagicMock(spec=UserState)
        user.set_state(mock_state)

        user.close()
        mock_state.close.assert_called_once_with(user)

    def test_user_delegates_login_to_state(self) -> None:
        """Test that user.login() delegates to current state."""
        user = User("test")
        mock_state = MagicMock(spec=UserState)
        mock_state.login.return_value = True
        user.set_state(mock_state)

        result = user.login()
        mock_state.login.assert_called_once_with(user)
        assert result is True


class TestStateTransitions:
    """Test complex state transition scenarios."""

    def test_full_lifecycle_pending_to_active_to_inactive_to_closed(
        self,
    ) -> None:
        """Test a complete user lifecycle."""
        user = User("lifecycle_user")

        # Start in pending
        assert isinstance(user._state, Pending)

        # Activate
        user.enable()
        assert isinstance(user._state, Active)

        # Deactivate
        user.disabled()
        assert isinstance(user._state, Inactive)

        # Close
        user.close()
        assert isinstance(user._state, Closed)

    def test_lifecycle_pending_to_active_to_closed(self) -> None:
        """Test direct path from active to closed."""
        user = User("direct_close_user")

        # Start in pending
        assert isinstance(user._state, Pending)

        # Activate
        user.enable()
        assert isinstance(user._state, Active)

        # Close directly
        user.close()
        assert isinstance(user._state, Closed)

    def test_lifecycle_pending_to_closed(self) -> None:
        """Test closing a user that was never activated."""
        user = User("never_active_user")

        # Start in pending
        assert isinstance(user._state, Pending)

        # Close directly
        user.close()
        assert isinstance(user._state, Closed)

    def test_inactive_can_be_reactivated(self) -> None:
        """Test that inactive users can be reactivated."""
        user = User("reactivate_user")

        # Pending -> Active
        user.enable()
        assert isinstance(user._state, Active)

        # Active -> Inactive
        user.disabled()
        assert isinstance(user._state, Inactive)

        # Inactive -> Active (reactivation)
        user.enable()
        assert isinstance(user._state, Active)

    def test_multiple_reactivation_cycles(self) -> None:
        """Test multiple activation/deactivation cycles."""
        user = User("cycle_user")

        # Pending -> Active
        user.enable()
        assert isinstance(user._state, Active)

        # Active -> Inactive
        user.disabled()
        assert isinstance(user._state, Inactive)

        # Inactive -> Active
        user.enable()
        assert isinstance(user._state, Active)

        # Active -> Inactive
        user.disabled()
        assert isinstance(user._state, Inactive)

        # Inactive -> Active
        user.enable()
        assert isinstance(user._state, Active)

    def test_closed_is_terminal_state(self) -> None:
        """Test that once closed, user cannot transition again."""
        user = User("terminal_user")

        # Close the user
        user.close()
        assert isinstance(user._state, Closed)

        # Try to enable - should stay closed
        user.enable()
        assert isinstance(user._state, Closed)

        # Try to disable - should stay closed
        user.disabled()
        assert isinstance(user._state, Closed)

        # Try to close again - should stay closed
        user.close()
        assert isinstance(user._state, Closed)


class TestStateTypeChecking:
    """Test that all states properly implement UserState interface."""

    def test_all_states_are_userstate_instances(self) -> None:
        """Verify all state classes implement the UserState interface."""
        pending = Pending()
        active = Active()
        inactive = Inactive()
        closed = Closed()

        assert isinstance(pending, UserState)
        assert isinstance(active, UserState)
        assert isinstance(inactive, UserState)
        assert isinstance(closed, UserState)

    def test_all_states_have_required_methods(self) -> None:
        """Verify all states have the required methods."""
        states = [Pending(), Active(), Inactive(), Closed()]

        for state in states:
            assert hasattr(state, "enable")
            assert callable(state.enable)
            assert hasattr(state, "disabled")
            assert callable(state.disabled)
            assert hasattr(state, "close")
            assert callable(state.close)
            assert hasattr(state, "login")
            assert callable(state.login)


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_redundant_actions_are_safe(self) -> None:
        """Test that redundant state actions don't cause errors."""
        user = User("redundant_user")

        # Multiple disable attempts on pending (should be no-op)
        user.disabled()
        user.disabled()
        user.disabled()
        assert isinstance(user._state, Pending)

        # Activate
        user.enable()
        assert isinstance(user._state, Active)

        # Multiple enable attempts on active (should be no-op)
        user.enable()
        user.enable()
        user.enable()
        assert isinstance(user._state, Active)

    def test_user_with_empty_username(self) -> None:
        """Test that user can be created with empty username."""
        user = User("")
        assert user.username == ""
        assert isinstance(user._state, Pending)

    def test_user_with_special_characters_username(self) -> None:
        """Test that user can be created with special characters."""
        special_names = [
            "user@example.com",
            "user-name",
            "user_name",
            "user.name",
            "用户",  # Chinese characters
            "🚀",  # Emoji
        ]

        for name in special_names:
            user = User(name)
            assert user.username == name
            assert isinstance(user._state, Pending)

    @given(
        username=st.text(
            alphabet=st.characters(
                blacklist_categories=("Cs",),
                min_codepoint=0x0020,
            ),
            min_size=0,
            max_size=1000,
        ),
    )
    def test_user_handles_any_unicode_username(self, username: str) -> None:
        """Property: User should handle any valid Unicode string as username."""
        user = User(username)
        assert user.username == username
        assert isinstance(user._state, UserState)


class TestLoggingBehavior:
    """Test logging behavior across all state transitions."""

    def test_all_valid_transitions_produce_logs(self, caplog) -> None:
        """Test that all valid state transitions produce log messages."""
        user = User("logger_test")

        with caplog.at_level(logging.INFO):
            # Pending -> Active
            user.enable()
            assert len(caplog.records) == 1

            caplog.clear()

            # Active -> Inactive
            user.disabled()
            assert len(caplog.records) == 1

            caplog.clear()

            # Inactive -> Active
            user.enable()
            assert len(caplog.records) == 1

            caplog.clear()

            # Active -> Closed
            user.close()
            assert len(caplog.records) == 1


@pytest.mark.parametrize(
    "initial_state,action,expected_final_state",
    [
        (Pending, "enable", Active),
        (Pending, "disabled", Pending),
        (Pending, "close", Closed),
        (Active, "enable", Active),
        (Active, "disabled", Inactive),
        (Active, "close", Closed),
        (Inactive, "enable", Active),
        (Inactive, "disabled", Inactive),
        (Inactive, "close", Closed),
        (Closed, "enable", Closed),
        (Closed, "disabled", Closed),
        (Closed, "close", Closed),
    ],
)
def test_state_transition_matrix(
    initial_state,
    action: str,
    expected_final_state,
) -> None:
    """Parametrized test covering all state transition combinations."""
    user = User("matrix_test")
    user.set_state(initial_state())

    # Perform action
    getattr(user, action)()

    # Verify final state
    assert isinstance(user._state, expected_final_state)
