from __future__ import annotations
import pytest
from challenges import (
    ActionStack,
    RequestQueue,
    is_note_balanced,
    process_request_line,
    undo_recent_actions,
)


# ──────────────────────────────────────────
# ActionStack tests
# ──────────────────────────────────────────

def test_action_stack_push_and_peek():
    stack = ActionStack()
    stack.push("open_ticket")
    assert stack.peek() == "open_ticket"


def test_action_stack_pop():
    stack = ActionStack()
    stack.push("open_ticket")
    stack.push("assign_agent")
    assert stack.pop() == "assign_agent"
    assert stack.peek() == "open_ticket"


def test_action_stack_pop_empty():
    stack = ActionStack()
    assert stack.pop() is None


def test_action_stack_peek_empty():
    stack = ActionStack()
    assert stack.peek() is None


def test_action_stack_is_empty():
    stack = ActionStack()
    assert stack.is_empty() is True
    stack.push("action")
    assert stack.is_empty() is False


# ──────────────────────────────────────────
# RequestQueue tests
# ──────────────────────────────────────────

def test_request_queue_enqueue_and_peek():
    queue = RequestQueue()
    queue.enqueue("Alice")
    assert queue.peek() == "Alice"


def test_request_queue_dequeue_order():
    queue = RequestQueue()
    queue.enqueue("Alice")
    queue.enqueue("Bob")
    assert queue.dequeue() == "Alice"
    assert queue.dequeue() == "Bob"


def test_request_queue_dequeue_empty():
    queue = RequestQueue()
    assert queue.dequeue() is None


def test_request_queue_peek_empty():
    queue = RequestQueue()
    assert queue.peek() is None


def test_request_queue_is_empty():
    queue = RequestQueue()
    assert queue.is_empty() is True
    queue.enqueue("Charlie")
    assert queue.is_empty() is False


# ──────────────────────────────────────────
# is_note_balanced tests
# ──────────────────────────────────────────

def test_balanced_parentheses():
    assert is_note_balanced("(hello)") is True


def test_balanced_mixed():
    assert is_note_balanced("{[()]}") is True


def test_unbalanced_missing_close():
    assert is_note_balanced("(hello") is False


def test_unbalanced_wrong_order():
    assert is_note_balanced("([)]") is False


def test_balanced_empty_string():
    assert is_note_balanced("") is True


def test_unbalanced_extra_close():
    assert is_note_balanced("())") is False


# ──────────────────────────────────────────
# process_request_line tests
# ──────────────────────────────────────────

def test_process_request_line_order():
    result = process_request_line(["Alice", "Bob", "Charlie"])
    assert result == ["Alice", "Bob", "Charlie"]


def test_process_request_line_empty():
    assert process_request_line([]) == []


def test_process_request_line_single():
    assert process_request_line(["Alice"]) == ["Alice"]


# ──────────────────────────────────────────
# undo_recent_actions tests
# ──────────────────────────────────────────

def test_undo_recent_actions_basic():
    actions = ["open", "assign", "close"]
    result = undo_recent_actions(actions, 1)
    assert result == ["open", "assign"]


def test_undo_recent_actions_all():
    actions = ["open", "assign"]
    result = undo_recent_actions(actions, 2)
    assert result == []


def test_undo_recent_actions_more_than_available():
    actions = ["open"]
    result = undo_recent_actions(actions, 5)
    assert result == []


def test_undo_recent_actions_zero():
    actions = ["open", "assign", "close"]
    result = undo_recent_actions(actions, 0)
    assert result == ["open", "assign", "close"]


def test_undo_recent_actions_empty():
    assert undo_recent_actions([], 3) == []