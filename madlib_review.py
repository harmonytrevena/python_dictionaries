madlib_word_choices = {
    "name": "",
    "noun": "",
    "color": "",
    "verb": "",
    "adjective": ""
}

madlib_word_choices["name"] = input("Enter your name: ")
madlib_word_choices["noun"] = input("Enter a noun: ")
madlib_word_choices["color"] = input("Enter your favorite color: ")
madlib_word_choices["verb"] = input("Enter a verb: ")
madlib_word_choices["adjective"] = input("Enter an adjective: ")

print("I'm %s and I hail from %s. The best color in the galaxy is %s and I %s it! I am %s. " % (madlib_word_choices["name"], madlib_word_choices["noun"], madlib_word_choices["color"], madlib_word_choices["verb"], madlib_word_choices["adjective"]))
