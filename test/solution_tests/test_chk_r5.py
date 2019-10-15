from collections import Counter

from solutions.CHK import checkout_solution


class TestCheckoutMachine():

    @classmethod
    def setup_class(cls):
        products = checkout_solution.Products()
        discounts = checkout_solution.DiscountStore()
        cls.cm = checkout_solution.CheckoutMachine(products, discounts)

    def test_apply_group_discount_S1T1(self):
        basket = Counter({'S': 1, 'T': 1})
        expected_basket = {'S': 1, 'T': 1}
        new_basket, price = self.cm.apply_free_discount(basket)
        assert new_basket == expected_basket
        assert price == 40
        
    def test_get_total_price_S1T1(self):
        basket = Counter({'S': 1, 'T': 1})
        assert self.cm.get_total_price(basket) == 40
