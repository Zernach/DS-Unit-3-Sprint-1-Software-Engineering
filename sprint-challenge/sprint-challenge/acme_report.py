# Data Science Unit 3 Sprint Challenge 1

# Software Engineering - the Acme Way

# Completed By: Ryan Zernach

"""
For the report, you should calculate and print the following values:
- Number of unique product names in the product list
- Average (mean) price, weight, and flammability of listed products
"""

from random import randint, sample, uniform, random
import random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    - `generate_products()` should generate a given number of products (default
      30), randomly, and return them as a list
      - `name` should be a random adjective from `['Awesome', 'Shiny',
    'Impressive', 'Portable', 'Improved']` followed by a space and then
    a random noun from `['Anvil', 'Catapult' 'Disguise' 'Mousetrap',
    '???']`eg `'Awesome Anvil'` & `Portable Catapult' are both possible
      - `price` and `weight` should both be from 5 to 100 (inclusive and
    independent, and remember - they're integers!)
      - `flammability` should be from 0.0 to 2.5 (floats)
    """
    num_products = 30
    products = []
    for x in range(0, num_products):
        name = (random.choice(ADJECTIVES))
        name += " "
        name += (random.choice(NOUNS))
        price = 10
        weight = (randint(5, 100))
        flammability = (random.uniform(0.0, 2.5))
        prod = Product(name, price, weight, flammability)
        products.append(prod)
    return products


def inventory_report(products):
    # """
    # for some reason I can't use a doc-string here, IDK why
    # inventory_report uses a list of products from generage_products above
    # and prints number of unique values in name values, averageweight,
    # averageprice, and averageflammability
    # """

    averageprice = 0
    for product in products:
        averageprice += product.price
    averageprice /= len(products)

    averageweight = 0
    for product in products:
        averageweight += product.weight
    averageweight /= len(products)

    averageflammability = 0
    for product in products:
        averageflammability += product.weight
    averageflammability /= len(products)

    list_of_names

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', products.name.isunique())
    print('Average price:', averageprice)
    print('Average weight:', averageweight)
    print('Average flammability:', averageflammability)

if __name__ == '__main__':
    inventory_report(generate_products())
