
from collections import Counter

from solutions.CHK import checkout_solution


class TestCheckoutMachine():

    def setUp(self):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        self.cm = checkout_solution.CheckoutMachine(products, discounts)
        
    def test_apply_free_discount_not(self):
        basket = Counter({'B': 1, 'E': 1})
        expected_basket = {'B': 1, 'E': 1}
        assert self.cm.apply_free_discount(basket) == expected_basket

