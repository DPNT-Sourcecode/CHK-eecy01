
from collections import Counter

from solutions.CHK import checkout_solution

class TestCheckoutMachine():

    def test_apply_free_discount(self):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        cm = checkout_solution.CheckoutMachine(products, discounts)
        assert cm.count_price(('A', 5)) == 230