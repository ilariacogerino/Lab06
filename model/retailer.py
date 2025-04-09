from dataclasses import dataclass

@dataclass
class Retailer():
    Retailer_code: int
    Retailer_name: str
    Type: str
    Country: str

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)