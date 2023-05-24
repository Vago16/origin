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
    def __init__(self, start = 0):
        """Makes a new serial generator at the start point"""
        self.start = self.next = start

    def __repr__(self):
        """Shows representation"""
        return f"<SerialGenerator start={self.start} next=(self.next)>"

    def generate(self):
        """Returns the next serial"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets the number of the serial to the original start"""
        self.next = self.start
