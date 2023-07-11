import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    ## looks like that classes have to have something passed into it, in this case its path. ##
    def __init__(self, path):
        # create the file path
        # * sb solution was just to use file = open(path) but then i have to pass file around
        self.file = open(path)
        # initialize the function to parse/read - all funcitons have self prepended - within function, pass in the file
        # * sb solution was to use self.words = self.readwords(file) - passing in file for the function to use
        self.words = self.readwords()
        # project calls to print out something
        # print(f" There are {len(self.words)} words )
        print(len(self.words))

    # creating the array - returning this automatically returns the array back into self words
    # * sb solution was readwords(file) is passed in, so that we can use it in multiple functions
    # in previous examples we would just call self.file
    def readwords(self):
        """ function to return a list from our dictionary"""
        return [word for word in self.file]

    def random(self):
        """ function to return a random word from our dictionary"""
        print(random.choice(self.words))


word_dict = WordFinder("words.txt")
word_dict.random()

#     def __init__(self, path):
#         file = open(path)
#         self.words = self.read_words(file)

#         print(len(self.words))

#     def read_words(self, file):

#         return [word for word in file]


# wordfile = WordFinder("words.txt")
