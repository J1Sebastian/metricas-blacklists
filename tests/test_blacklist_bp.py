import os
import json

# -------------------------- 0. Mock data -----------------------------

blacklist_data = {
    "email": "test@gmail.com",
    "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
    "blocked_reason": "Spam",
}

headers = {"Authorization": f"Bearer {os.getenv('SECRET_TOKEN')}"}
