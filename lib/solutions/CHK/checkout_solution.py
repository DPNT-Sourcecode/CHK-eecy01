
from collections import Counter

PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
# for item dict[count][price]
SPECIAL_OFFER = {'A': {3: 130}, 'B': {2: 45}}

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
    item_count = checkout_item[1]
    
    return PRICES[checkout_item[0]] * item_count





