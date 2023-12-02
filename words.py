def print_upper_words(words):
    """Print each word on its own line, uppercased.

        example:

        print_upper_words(["Programming", "is", "pretty", "fun"])
        
        should print:

        PROGRAMMING
        IS
        PRETTY
        FUN
    """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print each word on its own line, uppercased, if it starts with E or e.

        example:
        
        print_upper_words2(["eagle", "Edward", "Alfred"])
        
        should print:
        
        EAGLE
        EDWARD
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on its own line, uppercased, if starts with one of the given

        example:
        
        print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
                            must_start_with=["A", "E"])
        
        should print:
        
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
