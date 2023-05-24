"""Word Finder: finds random words from a dictionary."""
import random
#import words.txt

class WordFinder:
    """Gets all the words from a dictionary and returns them randomly
    
    >>> wf = WordFinder("/Users/student/words.txt")
3 words read

>>> wf.random()
'cat'

>>> wf.random()
'cat'

>>> wf.random()
'porcupine'

>>> wf.random()
'dog'
"""
     def __init__(self, path):
        """Reads a dictionary and reports the number of items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parses a  dict_file into a list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Returns a random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """A special subclass of WordFinder that excludes blank lines and comments.
    >>> wf = WordFinder("/Users/student/complex-words.txt")
4 words read (excluding those with blank linese and comments)

>>> wf.random()
'kale'

>>> wf.random()
'parsnips'

>>> wf.random()
'mango'

>>> wf.random()
'apple'
"""
    def parse(self, dict_file):
        """Parses a dict_file into a list of words, skipping blank lines and comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    