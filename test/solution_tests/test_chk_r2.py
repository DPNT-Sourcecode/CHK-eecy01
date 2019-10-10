
from collections import Counter

from solutions.CHK import checkout_solution

class TestCheckoutMachine():

    def test_apply_free_discount_not(self):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        cm = checkout_solution.CheckoutMachine(products, discounts)
        input_basket = {'B': 1, 'E': 1}
        expected_basket = {'B': 1, 'E': 1}
        basket = Counter({'B': 1, 'E': 1})
        assert cm.apply_free_discount(basket) == expected_basket