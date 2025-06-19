import logging

import requests

from config.config import BASE_URL, LOGIN_HEADERS, LOGIN_PAYLOAD
from data.update_profile_request import update_profile_req_body


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_update_profile():
    # Step 1: first try to login
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/login",
        json=LOGIN_PAYLOAD,
        headers=LOGIN_HEADERS().model_dump(),
    )
    assert response.status_code == 200, (
        f"Login failed with status code {response.status_code}"
    )
    data = response.json()
    token = data.get("AuthenticationResult", {}).get("AccessToken")
    assert token is not None, "Access token not found in response"
    logger.info("Login Successfully")

    # Step 2: prepare the cookies object
    access_token_cookies = {"access_token": token}

    # Step 3: do update profile request
    response = requests.put(
        url=f"{BASE_URL}/api/v1/users/me/profile",
        cookies=access_token_cookies,
        json=update_profile_req_body,
    )
    assert response.status_code == 200, (
        f"Update profile req failed with status code {response.status_code}"
    )
    logger.info("Profile updated successful.")

    # Step 4: Logout
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/logout", cookies=access_token_cookies
    )
    assert response.status_code == 200, (
        f"Logout failed with status code {response.status_code}"
    )
    logger.info("Logout successful.")
