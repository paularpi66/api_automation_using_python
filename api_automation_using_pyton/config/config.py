import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()
BASE_URL = os.getenv("BASE_URL")

LOGIN_PAYLOAD = {
    "username": "touhedur.rahman@blockstak.ai",
    "password": "Shuvo@1234"
}

class LOGIN_HEADERS(BaseModel):
    content_type: str = Field(alias="Content-Type", default="application/json")
