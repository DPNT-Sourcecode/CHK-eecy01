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
        new_basket, total_discount_price = self.cm.apply_group_discount(basket)
        assert new_basket == expected_basket
        assert total_discount_price == 0
        
    def test_apply_group_discount_S1T1(self):
        basket = Counter({'S': 1, 'T': 1})
        expected_basket = {'S': 1, 'T': 1}
        new_basket, total_discount_price = self.cm.apply_group_discount(basket)
        assert new_basket == expected_basket
        assert total_discount_price == 0

    def test_apply_group_discount_S1T1X1(self):
        basket = Counter({'S': 1, 'T': 1, 'X': 1})
        expected_basket = {}
        new_basket, total_discount_price = self.cm.apply_group_discount(basket)
        assert new_basket == expected_basket
        assert total_discount_price == 45

    def test_apply_group_discount_S4T3Z2(self):
        basket = Counter({'S': 4, 'T': 3, 'Z': 2})
        expected_basket = {}
        new_basket, total_discount_price = self.cm.apply_group_discount(basket)
        assert new_basket == expected_basket
        assert total_discount_price == 135
        
    def test_get_total_price_S1T1(self):
        basket = Counter({'S': 1, 'T': 1})
        assert self.cm.get_total_price(basket) == 40