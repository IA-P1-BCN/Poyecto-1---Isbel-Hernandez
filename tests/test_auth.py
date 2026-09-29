from src.infrastructure.auth import set_password, verify_password

def test_password_verification(tmp_path, monkeypatch):
    auth_file = tmp_path / "auth.json"

    monkeypatch.setattr(
        "src.infrastructure.auth.AUTH_PATH",
        auth_file
    )

    set_password("test123")

    assert verify_password("test123") is True
    assert verify_password("incorrecta") is False