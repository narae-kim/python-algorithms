# EXAMPLE 1
# If you store these names in a list, this function would eventually become really slow because it would have to run a simple search over the entire list.
# A hash table instantly tells you whether this person's name is in the hash table or not.
# checking for duplicates is very fast with a hash table.
voted = {}


def check_voter(name):
    if voted.get(name):
        print("{} already voted.".format(name))
    else:
        voted[name] = True
        print("Give a chance for vote to {}!".format(name))


# EXAMPLE 2
cache = {}


def get_data_from_server(url):
    # TODO - retrieve data from the server
    data = "DUMMY DATA"
    return data


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


if __name__ == '__main__':
    check_voter("Tom")
    check_voter("Narae")
    check_voter("Tom")

    cache["HOME"] = 123
    cache["Dashboard"] = None
    print(get_page("HOME"))
    print(get_page("Dashboard"))
