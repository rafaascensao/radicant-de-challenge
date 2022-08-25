from src.models.ESGFund import ESGFund
from src.models.UserPreferences import UserPreferences

def get_esg_funds(
    fund_size: list[str], 
    dominant_sector: list[str], 
    page: int, 
    items_per_page: int
) -> list:
    """
    Returns ESG Funds based on fund_size and dominant economic sector

    Args:
        fund_size (list[str]): Size of the fund (small, medium, large)
        dominant_sector (list[str]): Financial Dominant sector of the fund
        page (int): The page for the API pagination
        items_per_page (int): Number of funds per page

    Returns:
        list: List of ESG Funds
    """
    all_funds = ESGFund.select().where(
        (ESGFund.size_type.in_(fund_size)) & 
        (ESGFund.dominant_sector.in_(dominant_sector))
    )
    total_items = all_funds.count()
    funds = all_funds.paginate(page, items_per_page)

    return {
        "funds" :[fund.to_dict() for fund in funds],
        "page_number": page,
        "items_per_page": items_per_page,
        "total_items": total_items
    }


def create_user_preference(user_preferences: dict):
    """
    Create a user preference on the DB

    Args:
        user_preferences (dict): User Preference object
    """
    UserPreferences.from_dict(user_preferences)
