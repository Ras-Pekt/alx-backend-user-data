#!/usr/bin/env python3
"""Testing endpoints module"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """test register route"""
    url = f"{BASE_URL}/users"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=data)
    assert response.json() == {"email": f"{email}", "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """test wrong login route"""
    url = f"{BASE_URL}/sessions"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """test login route"""
    url = f"{BASE_URL}/sessions"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=data)
    try:
        assert response.status_code == 200
        assert response.json() == {"email": f"{email}", "message": "logged in"}
        return response.cookies.get("session_id")
    except AssertionError:
        pass


def profile_unlogged() -> None:
    """test profile route"""
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """test profile route"""
    url = f"{BASE_URL}/profile"
    cookies = {
        "session_id": session_id
    }
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"email": f"{EMAIL}"}


def log_out(session_id: str) -> None:
    """test logout route"""
    url = f"{BASE_URL}/sessions"
    cookies = {
        "session_id": session_id
    }
    response = requests.delete(url, cookies=cookies)
    assert response.json() == {'message': 'Bienvenue'}
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """test get reset password token"""
    url = f"{BASE_URL}/reset_password"
    data = {
        "email": email
    }
    response = requests.post(url, data=data)
    token = response.json().get("reset_token")
    assert response.status_code == 200
    assert response.json() == {"email": email, "reset_token": token}
    return token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """test update password password"""
    url = f"{BASE_URL}/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }
    response = requests.put(url, data=data)
    assert response.status_code == 200
    assert response.json() == {
        "email": f"{email}", "message": "Password updated"
    }


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
