
from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not str.isalpha(skus):
        return -1
    skus = skus.upper()
    skus_counter = Counter(skus)
    return skus_counter
