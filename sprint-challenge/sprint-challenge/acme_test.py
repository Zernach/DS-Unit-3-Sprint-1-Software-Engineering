# Data Science Unit 3 Sprint Challenge 1

# Software Engineering - the Acme Way

# Completed By: Ryan Zernach

"""
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
    one tests default price, default weight, flammability, and explodability
    """

    def test_default_price(self):
        """
        Test default product price being 10.
        """
        prod = Product()
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        """
        Test default product weight being 20.
        """
        prod = Product()
        self.assertEqual(prod.weight, 20)

    def test_default_flammability(self):
        """
        Test default flammability being 0.5.
        """
        prod = Product()
        self.assertEqual(prod.flammability, 0.5)

    def test_explodability_function(self):
        """
        Test default product price being 10.
        """
        prod = Product()
        self.assertIn(prod.explodability, '...')


class AcmeReportTests(unittest.TestCase):
    """
    -'test_default_num_products' - checks that it really does receive a list of
        length 30
    -'test_legal_names' - checks that the generated names for a default batch
       of products are all valid possible names to generate (adjective, space,
       noun, from the lists of possible words)
    """

    def test_default_num_products(self):
        """
        checks that it really does receive a list of length 30
        """
        products_test_report = generate_products()

        self.assertEqual(len(products_test_report), 30)

    def test_legal_names(self):
        """
        checks that the generated names for a default batch of products are
        all valid possible names to generate (adjective, space, noun, from the
        lists of possible words)
        """
        products_test_report = generate_products()

        for product in products_test_report:
            self.assertIn(product.name, ADJECTIVES)

        for product in products_test_report:
            self.assertIn(product.name, NOUNS)


if __name__ == '__main__':
    unittest.main()
