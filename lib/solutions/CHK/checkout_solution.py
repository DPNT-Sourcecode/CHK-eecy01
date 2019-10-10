
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
    skus_sum = sum(map(count_price, basket.items()), 0)
    return skus_sum

def count_price(checkout_item):
    # checkout_item - tuple of (item, count)
    item = checkout_item[0]
    item_count = checkout_item[1]
    if item not in Products.get_skus():
        return 0
    total_price = 0
    promotion_price = 0
    remainder = item_count
    if item in DiscountStore.n_for_price_keys and item_count >= list(DiscountStore.n_for_price[item].keys())[0]:
        promo_count = list(DiscountStore.n_for_price[item].keys())[0]
        remainder = item_count % promo_count
        promotion_price = int(item_count / promo_count) * DiscountStore.n_for_price[item][promo_count]
    total_price = promotion_price + Products.get_price(item) * remainder
    return total_price

class Products():
    PRODUCT_PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    
    @classmethod
    def get_price(cls, sku):
        return cls.PRODUCT_PRICES[sku]

    @classmethod
    def get_skus(cls):
        return cls.PRODUCT_PRICES.keys()

class DiscountStore():
    n_for_price = {'A': {3: 130, 5: 200},
                            'B': {2: 45},
                   }
    n_for_price_keys = n_for_price.keys()

    xfree_for_y = {'E': {2: {'B': 1}}}
    
    


