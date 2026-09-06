from pathlib import Path

from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

APP_PATH = Path(__file__).resolve().parent.parent / "app.py"


def test_new_game_resets_status_after_loss():
    at = AppTest.from_file(str(APP_PATH))
    at.run()

    # Simulate a game that just ended in a loss.
    at.session_state["status"] = "lost"
    at.session_state["attempts"] = at.session_state["attempts"] or 8
    at.run()

    new_game_button = next(b for b in at.button if "New Game" in b.label)
    new_game_button.click().run()

    assert at.session_state["status"] == "playing", (
        "Clicking New Game should reset status back to 'playing', "
        f"but it is still '{at.session_state['status']}' "
        "(New Game resets attempts/secret but never resets status)."
    )


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
