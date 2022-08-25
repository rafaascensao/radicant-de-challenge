import json

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel
from src.api.utils import create_user_preference, get_esg_funds

app = FastAPI()

class UserPreferences(BaseModel):
    user_id: str
    fund_size: str
    dominant_sector: str

dominant_sectors = [
    "basic_materials",
    "technology",
    "financial_services",
    "consumer_cyclical",
    "healthcare",
    "energy",
    "industrials",
    "consumer_defensive",
    "utilities",
    "real_estate",
    "communication_services"
]

@app.get("/esg/")
async def get_funds(
    fund_size: list[str] = Query(default=["small", "medium", "large"]), 
    dominant_sector: list[str] = Query(default=dominant_sectors),
    page: int = Query(default=1),
    items_per_page: int = Query(default=10)
):
    return get_esg_funds(fund_size, dominant_sector, page, items_per_page)


@app.post("/esg/")
async def create_preferences(user_preference: UserPreferences) -> UserPreferences:
    create_user_preference(user_preference.dict())
    return user_preference


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.api.app:app", host="0.0.0.0", port=8000, reload=True)
