import re

from src.models.BaseModel import BaseModel
from peewee import IdentityField, CharField, TextField, IntegerField, FloatField, DateField

class ESGFund(BaseModel):
    fund_symbol = IdentityField(primary_key = True)
    fund_long_name = TextField()
    fund_category = TextField(null = True)
    fund_family = CharField(null = True)
    exchange_code = CharField()
    avg_vol_3month = IntegerField()
    avg_vol_10day = IntegerField(null = True)
    day50_moving_average = FloatField(null = True)
    day200_moving_average = FloatField(null = True)
    fund_yield = FloatField(null = True)
    inception_date = DateField(formats=["%d.%m.%Y"])
    annual_holdings_turnover = FloatField(null = True)
    investment_type = CharField(null = True)
    size_type = CharField(null = True, index = True)
    fund_annual_report_net_expense_ratio = FloatField(null = True)
    top10_holdings = TextField(null = True)
    top10_holdings_total_assets = FloatField(null = True)
    returns_as_of_date = DateField(formats=["%d.%m.%Y"])
    fund_return_ytd = FloatField(null = True)
    fund_return_1month = FloatField(null = True)
    fund_return_3months = FloatField(null = True)
    fund_return_1year = FloatField(null = True)
    fund_return_3years = FloatField(null = True)
    fund_return_2020 = FloatField(null = True)
    fund_return_2019 = FloatField(null = True)
    fund_return_2018 = FloatField(null = True)
    fund_return_2017 = FloatField(null = True)
    fund_alpha_3years = FloatField(null = True)
    fund_beta_3years = FloatField(null = True)
    fund_r_squared_3years = FloatField(null = True)
    fund_stdev_3years = FloatField(null = True)
    fund_sharpe_ratio_3years = FloatField(null = True)
    fund_treynor_ratio_3years = FloatField(null = True)
    dominant_sector = CharField(null = True, index = True)
    dominant_sector_percentage = FloatField(null = True)

    def _pretty_top_holding(self) -> list[dict]:
        """
        Pretiffy top 10 holdings
        HACK: If it can't pretiffy for some reason, it returns the string
        as it is. With more time this should be changed

        Returns:
            list[dict]: _description_
        """
        if self.top10_holdings is None:
            return self.top10_holdings

        try:
            # Change "," into ";" to avoid conflicts
            top10_string = re.sub(r"(\d),", r"\1;", self.top10_holdings)

            # Remove text in brackets
            top10 = re.sub("\(.*?\)", "", top10_string).split(";")

            # Separate ticker and percentage 
            list_ticker_and_value = [holding.split(":") for holding in top10]

            return [{
                "ticker": holding[0].strip(),
                "fund_percentage": float(holding[1].strip()) 
            } for holding in list_ticker_and_value]
        
        except Exception:
            print("Couldn't format top10 holdings")
            return self.top10_holdings
             

    def to_dict(self):
        """
        Transform object into dict
        """
        return {
            "fund_symbol": self.fund_symbol,
            "fund_long_name": self.fund_long_name,
            "fund_category": self.fund_category,
            "fund_family": self.fund_family,
            "exchange_code": self.exchange_code,
            "fund_yield": self.fund_yield,
            "inception_date": self.inception_date,
            "annual_holdings_turnover": self.annual_holdings_turnover,
            "investment_type": self.investment_type,
            "size_type": self.size_type,
            "top10_holdings": self._pretty_top_holding(),
            "top10_holdings_total_assets": self.top10_holdings_total_assets,
            "dominant_sector": self.dominant_sector,
            "dominant_sector_percentage": self.dominant_sector_percentage,
            "averages": {
                "avg_vol_10day": self.avg_vol_10day,
                "avg_vol_3month": self.avg_vol_3month,
                "day50_moving_average": self.day50_moving_average,
                "day200_moving_average": self.day200_moving_average,
            },
            "returns": {
                "returns_as_of_date": self.returns_as_of_date,
                "fund_return_ytd": self.fund_return_ytd,
                "fund_return_1month": self.fund_return_1month, 
                "fund_return_3months": self.fund_return_3months,
                "fund_return_1year": self.fund_return_1year,
                "fund_return_3years": self.fund_return_3years,
                "fund_return_2020": self.fund_return_2020,
                "fund_return_2019": self.fund_return_2019,
                "fund_return_2018": self.fund_return_2018,
                "fund_return_2017": self.fund_return_2017,
            },
            "risk_metrics": {
                "fund_alpha_3years": self.fund_alpha_3years,
                "fund_beta_3years": self.fund_beta_3years,
                "fund_r_squared_3years": self.fund_r_squared_3years,
                "fund_stdev_3years": self.fund_stdev_3years,
                "fund_sharpe_ratio_3years": self.fund_sharpe_ratio_3years,
                "fund_treynor_ratio_3years": self.fund_treynor_ratio_3years,
            }
        }