# Data Science Unit 3 Sprint Challenge 1

## Software Engineering - the Acme Way

### Completed By: Ryan Zernach

import random


class Product:
    """
    Acme Product Information
        - `name` (string with no default)
        - `price` (integer with default value 10)
        - `weight` (integer with default value 20)
        - `flammability` (float with default value 0.5)
        - `identifier` (integer, automatically genererated as a random (uniform)
        number anywhere from 1000000 to 9999999
    """

    def __init__(self, name='Untitled_Product', price=10, weight=20, flammability=0.5):
        """
        Product Constructor
        """
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)


    def stealability(self):
        """
        calculates the price divided by the weight, and then
          returns a message: if the ratio is less than 0.5: "Not so stealable...",
          if it is greater or equal to 0.5 but less than 1.0 return "Kinda
          stealable.", otherwise return "Very stealable! Or unknown. Use discretion."
        """

        self.stealability = self.price/self.weight

        if self.stealability < 0.5:
            message1 = "Not so stealable..."
        elif self.stealability >= 0.5 & (self.stealability < 1):
            message1 = "Kinda stealable."
        else:
            message1 = "Very stealable! Or unknown. Use discretion."
        return message1


    def explodability(self):
        """
        calculates the flammability times the weight, and then
          returns a message: if the product is less than 10 return "...fizzle.", if it is
          greater or equal to 10 but less than 50 return "...boom!", and otherwise
          return "...BABOOM!! Or unknown. Use discretion."
        """
        self.explodability = self.flammability*self.weight

        if self.explodability < 10:
            message2 = "...fizzle."
        elif (self.explodability >= 10) & (self.explodability < 50):
            message2 = "...boom!"
        else:
            message2 = "...BABOOM!! Or unknown. Use discretion."
        return message2


class BoxingGlove(Product):
    """
    - Change the default `weight` to 10 (but leave other defaults unchanged)
    - Override the `explode` method to always return "...it's a glove."
    """

    def __init__(self, name='Boxing Glove', price=10, weight=10, flammability=0.5):
        """
        Boxing Glove Constructor
        """
        super().__init__(name, price, weight, flammability)
        self.weight = weight
        self.explodability = "...it's a glove."

    def __init__(self, rounds=3, player1='Superman', player2='Stephanie'):
        super().__init__(rounds, player1, player2)

    def punchability(self):
        """
        - Add a `punch` method that returns "That tickles." if the weight is
        below 5, "Hey that hurt!" if the weight is greater or equal to 5 but
        less than 15, and "OUCH!" otherwise
        """

        self.punchability = self.weight

        if self.punchability < 5:
            message4 = "That tickles."
        elif (self.punchability >= 5) & (self.punchability < 15):
            message4 = "Hey that hurt!"
        else:
            message4 = "OUCH! Or unknown. Use discretion."
        return message4
