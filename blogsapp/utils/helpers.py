import secrets
import string


def random_n_token(n=5):
    """Generate a random string with numbers and characters with `n` length."""

    allowed_characters = (
        string.ascii_letters + string.digits
    )  # contains char and digits
    return "".join(secrets.choice(allowed_characters) for _ in range(n))
