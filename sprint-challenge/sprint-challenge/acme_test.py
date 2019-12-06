# Data Science Unit 3 Sprint Challenge 1

## Software Engineering - the Acme Way

### Completed By: Ryan Zernach

"""
*Hint* - `test_legal_names` is the trickiest of these, but may not be as bad as
you think. Check out `assertIn` from `unittest`, and remember that Python is
pretty handy at string processing. But if you get stuck, move on and revisit.

Note that `inventory_report()` is pretty tricky to test, because it doesn't
*return* anything - it just prints (a "side-effect"). For the purposes of this
challenge, don't worry about testing it - but as a stretch goal/something to
think about, it's a good ponderer.
"""

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """
    Making sure Acme products are the tops!
    Add at least *2* more test methods to `AcmeProductTests` for the base
      `Product` class: at least 1 that tests default values (as shown), and one that
      builds an object with different values and ensures their `stealability()` and
      `explode()` methods function as they should
    """

    def test_default_product_price(self):
        """
        Test default product price being 10.
        """
        prod = Product()
        self.assertEqual(prod.price, 10)


class AcmeReportTests(unittest.TestCase):
    """
    -'test_default_num_products' - checks that it really does receive a list of
        length 30
    -'test_legal_names' - checks that the generated names for a default batch
        of products are all valid possible names to generate (adjective, space,
        noun, from the lists of possible words)
    """

    products_test_report = generate_products()

    def test_default_num_products(self):
        """
        checks that it really does receive a list of length 30
        """
        self.assertEqual(products_test_report.length, 30)


    def test_legal_names(self):
        """
        checks that the generated names for a default batch of products are
        all valid possible names to generate (adjective, space, noun, from the
        lists of possible words)
        """
        for product in products_test_report:
            self.assertIn(product.name, ADJECTIVES)

        for product in products_test_report:
            self.assertIn(product.name, NOUNS)

if __name__ == '__main__':
    unittest.main()
