def print_upper_words(words):
    """prints each words in uppercase on a separate line

            print_upper_words(["I", "like", "cheese"])

            I
            LIKE
            CHEESE
    """

    for word in words:
        print(word.upper())

def print_upper_e_words(words):
    """prints each words in uppercase on a separate line as long
        as it starts with an e or E

            print_upper_e_words(["Albert", "Einstein", "eats", "cheese"])

            EINSTEIN
            EATS
    """

        for word in words:
            if word.startswith("E") or word.startswith("e"):
                print(word.upper())

def print_upper_picky_words(words, must_start_with)
    """prints each words in uppercase on a separate line as long as it
        starts with one of given argument letters

            print_upper_picky_words(["Mice", "have", "entered", "the", "chat",], 
                                        must_start_with=["M", "e"])
            MICE
            ENTERED
    """
        for word in words:
            for letter in must_start_with:
                if word.startswith(letter):
                    print(word.upper)
                    break    

