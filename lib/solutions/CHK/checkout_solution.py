
from collections import Counter

PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
#
SPECIAL_OFFER = {'A': (3, 130), 'B': (2, 45)}
SPECIAL_OFFER_KEYS = SPECIAL_OFFER.keys()

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus or not str.isalpha(skus):
        return -1
    skus = skus.upper()
    
    skus_counter = Counter(skus)
    skus_sum = sum(map(count_price, skus_counter.items()))
    return skus_sum

def count_price(checkout_item):
    # checkout_item - tuple of (item, count)
    item = checkout_item[0]
    item_count = checkout_item[1]
    if item not in PRICES.keys():
        return 0
    total_price = 0
    promotion_price = 0
    remainder = item_count
    if item in SPECIAL_OFFER_KEYS and item_count >= SPECIAL_OFFER[item][0]:
        promo_count = SPECIAL_OFFER[item][0]
        remainder = item_count % promo_count
        promotion_price = int(item_count / promo_count) * SPECIAL_OFFER[item][1]
    total_price = promotion_price + PRICES[item] * remainder
    return total_price

