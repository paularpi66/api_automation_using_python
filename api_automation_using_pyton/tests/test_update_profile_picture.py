import requests

from config.config import BASE_URL, LOGIN_HEADERS, LOGIN_PAYLOAD
from data.update_profile_request import update_profile_req_body
from utils.logger import logger


def test_login_update_logout_flow():
    # Step 1: Login
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/login",
        json=LOGIN_PAYLOAD,
        headers=LOGIN_HEADERS().model_dump(),
    )
    assert response.status_code == 200, (
        f"Login failed with status code {response.status_code} and response {response.text}"
    )
    token = response.json().get("AuthenticationResult", {}).get("AccessToken")
    assert token, "Access token not found in response"
    logger.info("Login successful")

    # Step 2: Token as Cookie
    access_token_cookies = {"access_token": token}

    # Step 3: Update Profile
    response = requests.put(
        f"{BASE_URL}/api/v1/users/me/profile",
        cookies=access_token_cookies,
        json=update_profile_req_body,
    )
    assert response.status_code == 200, (
        f"Update profile failed with status code {response.status_code} and response {response.text}"
    )
    logger.info("Profile updated")

    # Step 4: Logout
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/logout",
        cookies=access_token_cookies,
    )
    assert response.status_code == 200, (
        f"Logout failed with status code {response.status_code} and response {response.text}"
    )
    logger.info("Logout successful")
