import doctest

"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        # creating the initial value and copy to manipulate - we will be incrementing next
        # learning that i can create new variables with self. that can be used in other places
        self.next = start
        self.start = start
        # self.start = self.next = start

    def __repr__(self):
        return f"self start = {self.start}, self next = {self.next}"

    def generate(self):
        """ creates a value that increments when called """
        self.next += 1
        # forgot to subtract 1 to keep value same as the initialization
        return self.next - 1

    def reset(self):
        """ resets value back to original """
        # where we reset the copy to the original
        self.next = self.start


newGen = SerialGenerator(start=100)

# initially i forgot to call generate multiple times when testing
# newGen.generate()
# newGen.generate()
# newGen.generate()


doctest.testmod(name="serial", verbose=True)
