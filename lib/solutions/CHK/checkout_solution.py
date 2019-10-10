
from collections import Counter



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0
    if not str.isalpha(skus) or not str.isupper(skus):
        return -1
    
    skus = skus.upper()
    
    basket = Counter(skus)
    cm = CheckoutMachine(Products(), DiscountStore())
    total_price = cm.get_total_price(basket)
    return total_price

class Products():
    PRODUCT_PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    
    def get_price(self, sku):
        return self.PRODUCT_PRICES.get(sku, 0)

    def get_skus(self):
        return self.PRODUCT_PRICES.keys()


class DiscountStore():
    n_for_price = {'A': {3: 130, 5: 200},
                            'B': {2: 45},
                   }
    n_for_price_keys = n_for_price.keys()

    xfree_for_y = {'E': {2: {'B': 1}}}
    

class CheckoutMachine():
    
    def __init__(self, products, discounts):
        self.products = products
        self.discounts = discounts

    def count_price(self, checkout_item):
        # checkout_item - tuple of (item, count)
        item = checkout_item[0]
        item_count = checkout_item[1]
        if item not in self.products.get_skus():
            return 0
        total_price = 0
        promotion_price = 0
        remainder = item_count
        if item in self.discounts.n_for_price_keys:
            print(sorted(self.discounts.n_for_price[item].keys(), reverse=True))
            for item_quantity in sorted(self.discounts.n_for_price[item].keys(), reverse=True):
                print(item_quantity,remainder, promotion_price)
                if remainder >= item_quantity:
                    promo_count = list(self.discounts.n_for_price[item].keys())[0]
                    remainder = item_count % promo_count
                    promotion_price += int(item_count / promo_count) * self.discounts.n_for_price[item][promo_count]
        total_price = promotion_price + self.products.get_price(item) * remainder
        return total_price    

    def apply_free_discount(self, basket):
        products = set(basket.keys())
        all_free_discount_prods = set(self.discounts.xfree_for_y.keys())
        free_discount_prods = products & all_free_discount_prods
        actual_discounts = {}
        for discount_prod in free_discount_prods:
            discount = self.discounts.xfree_for_y[discount_prod]
            for discount_quantity in discount.keys():
                if basket[discount_prod] >= discount_quantity:
                    actual_discounts.update(discount[discount_quantity])
        actual_discounts = Counter(actual_discounts)
        return basket - actual_discounts

    def get_total_price(self, basket):
        # internal basket for discounts and other operations
        cm_basket = basket.copy()
        self.apply_free_discount(cm_basket)
        total_price = sum(map(self.count_price, cm_basket.items()), 0)
        return total_price
