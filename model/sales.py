import datetime
from dataclasses import dataclass


@dataclass
class Sales():
    Date: datetime
    Ricavo: float
    Retailer_code: int
    Product_number: int
    Product_brand: str

    def __str__(self):
        return f"Data: {self.Date}, Ricavo: {self.Ricavo}, Retailer: {self.Retailer_code}, Product: {self.Product_number}"


    def __eq__(self):
        return self.Retailer_code == self.Product_number

    def __hash__(self):
        return hash(self.Retailer_code)
