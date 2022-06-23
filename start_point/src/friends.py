from operator import truediv


def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for favourite in person["favourites"]["snacks"]:
        if favourite == food:
            return True
    return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(persons):
    total_money = 0
    for person in persons:
        total_money += person["monies"]
    return total_money

def lend_money(lender, lendee, money):
    lender["monies"] -= money
    lendee["monies"] += money

def all_favourite_foods(people):
    favourites = []
    for person in people:
        for snack in person["favourites"]["snacks"]:
            if snack not in favourites:
                favourites.append(snack)
    return favourites

def find_no_friends(people):
    friendless = []
    for person in people:
        if len(person["friends"]) == 0:
            friendless.append(person)

    return friendless

def unique_favourite_tv_shows(people):
    favourites = set()
    for person in people:
        if person["favourites"]["tv_show"] not in favourites:
            favourites.add(person["favourites"]["tv_show"])
    return favourites