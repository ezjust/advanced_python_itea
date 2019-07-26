class SuperMarket:

    overall_sales = 0

    def __init__(self, market_name, sold_products):
        self.market_name = market_name
        self.sold_products = sold_products

    def sell_new_product(self):
        self.sold_products += 1

    def set_overall_markets_sales(self):
        SuperMarket.overall_sales += self.sold_products


superm = SuperMarket('Products', 10)
superm.sell_new_product()
superm.set_overall_markets_sales()
print(superm.overall_sales)
