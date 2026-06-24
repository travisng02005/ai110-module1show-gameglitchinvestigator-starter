from logic_utils import check_guess

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


# --- Tests targeting the swapped hint message bug ---
# The original bug: when guess > secret the hint said "Go HIGHER!" and
# when guess < secret it said "Go LOWER!" — both are backwards.

def test_too_high_hint_says_go_lower():
    _, message = check_guess(80, 50)
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message!r}"

def test_too_low_hint_says_go_higher():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message!r}"
