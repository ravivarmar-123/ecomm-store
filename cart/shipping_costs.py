from decimal import Decimal
from users.models import UserAddress

ADDRESS_ID = 'ADDRESS_ID'

class ShippingCost:
    CITY_COST ={
    'Don Valley': Decimal(0),
    'Uptown': Decimal(0.00),
    'High Park': Decimal(0.0),
    'Old Town': Decimal(0.0),
    }

    def get_city_cost(self, city_name):
        return self.CITY_COST.get(city_name.lower(), Decimal(15))
