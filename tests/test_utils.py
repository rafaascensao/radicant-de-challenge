import peewee as pw
import pytest
from src.api.utils import get_esg_funds, create_user_preference
from src.models.UserPreferences import UserPreferences

db = pw.SqliteDatabase('db/radicant_challenge.db')
        

def test_get_esg_funds():
    fund_size = ["small"]
    dominant_sector = ["financial_services"]
    funds = get_esg_funds(fund_size, dominant_sector, 1, 10)
    assert len(funds["funds"]) == 10


def test_create_user_preference():
    create_user_preference({
        "user_id": "test",
        "fund_size": "test",
        "dominant_sector": "test",
    })

    user = UserPreferences.get(UserPreferences.user_id == "test")
    assert user.user_id == "test"
    assert user.fund_size == "test"
    assert user.dominant_sector == "test"
    user.delete_instance()
