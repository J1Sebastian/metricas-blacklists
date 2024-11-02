import os


class Config:
    db_user = "postgres"
    db_pass = "secret"
    db_host = "localhost"
    db_port = "5432"
    db_name = "blacklist_db"

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_database.db"
    TESTING = True
