import os

# CORS
CORS_ORIGIN_ALLOW_ALL = True
if os.getenv("CORS_ALLOWED_ORIGINS"):
    CORS_ALLOWED_ORIGINS = [
        origin for origin in os.getenv("CORS_ALLOWED_ORIGINS").split(",")
    ]
