import logging
import requests
import time

from config.config import BASE_URL, LOGIN_PAYLOAD, LOGIN_HEADERS


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def test_login_and_logout_flow():
    # Step 1: first try to login
    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=LOGIN_PAYLOAD, headers=LOGIN_HEADERS().model_dump())
    assert response.status_code == 200, f"Login failed with status code {response.status_code}"
    data = response.json()
    token = data.get("AuthenticationResult", {}).get("AccessToken")
    assert token is not None, "Access token not found in response"
    logger.info("Login Successfully")

    # Step 2: just wait for a sec
    time.sleep(1)

    # Step 3: Logout
    logout_cookies = {
        'access_token': token
    }
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/logout",
        cookies=logout_cookies
    )
    assert response.status_code == 200, f"Logout failed with status code {response.status_code}"
    logger.info("Logout successful.")
