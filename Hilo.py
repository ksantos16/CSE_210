import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
"""A small cube with a different number of spots on each of its six sides.

The responsibility of Die is to keep track of the side facing up and calculate the points for 
it.
   
Attributes:
value (int): The number of spots on the side facing up.
points (int): The number of points the die is worth.
"""


class Die:

    # 2) Create the class constructor. Use the following method comment.
    """Constructs a new instance of Die with a value and points attribute.

    Args:
        self (Die): An instance of Die.
    """

    def __init__(self):

        # attribute needs to be set to zero
        self.value = 0
        self.points = 0

# 3) Create the roll(self) method. Use the following method comment.
    """Generates a new random value and calculates the points.

        Args:
            self (Die): An instance of Die.
        """

    def roll(self):
        # self.value = [1, 2, 3, 4, 5, 6]
        # using this allow us to set a range and get a random selection random.randint(1,6)
        # need to refer to the attributes to as they are our "variables"
        self.value = random.randint(1, 6)
        if self.value == 5:
            self.points = 50
        elif self.value == 1:
            self.points = 100
        else:
            self.points = 0
