""" This is the standard way to include a multiple-line comment in your code."""

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idel"]]]

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list) == True:
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)
