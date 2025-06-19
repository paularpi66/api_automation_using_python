import logging
import requests

from config.config import BASE_URL, LOGIN_HEADERS, LOGIN_PAYLOAD

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def test_login():
    logger.info("Login test starting")
    response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=LOGIN_PAYLOAD, headers=LOGIN_HEADERS().model_dump())
    assert response.status_code == 200, f"Login failed with status code {response.status_code}"
    data = response.json()
    token = data.get("AuthenticationResult", {}).get("AccessToken")
    assert token is not None, "Access token not found in response"
    logger.info("Login Successfully")
