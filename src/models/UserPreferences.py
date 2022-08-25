from src.models.BaseModel import BaseModel
from peewee import IdentityField, CharField

class UserPreferences(BaseModel):
    user_id = CharField(primary_key = True)
    fund_size = CharField()
    dominant_sector = CharField()

    @classmethod
    def from_dict(cls, data_dict : dict):
        """
        Creates UserPreferences in db from a dictionary
        """
        UserPreferences.create(
            user_id = data_dict["user_id"],
            fund_size = data_dict["fund_size"],
            dominant_sector = data_dict["dominant_sector"]
        )