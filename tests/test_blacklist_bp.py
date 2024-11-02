import os
import json

# -------------------------- 0. Mock data -----------------------------

blacklist_data = {
    "email": "test@gmail.com",
    "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
    "blocked_reason": "Spam",
}

headers = {"Authorization": f"Bearer {os.getenv('SECRET_TOKEN')}"}


# --------------------- 1. Add email to blacklist ---------------------


def test_add_email_no_token(test_client):
    response = test_client.post(
        "/blacklists",
        json=blacklist_data,
        content_type="application/json",
    )
    assert response.status_code == 403
    response_data = json.loads(response.data)
    assert response_data["msg"] == "Falta el token de autorización"
