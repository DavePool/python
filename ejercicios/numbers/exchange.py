
def exchange_money(budget,exchange_rate ):
    return budget / exchange_rate

def get_change(budget,exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return int(denomination * number_of_bills)

def get_number_of_bills(budget, denomination):
    return int(budget/denomination)

def get_leftover_of_bills(budget, denomination):
    return budget % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    new_exchange_rate = exchange_rate * ((spread/100)+1)
    x = budget/new_exchange_rate
    return int((x//denomination)*denomination)


    # fee = exchange_rate+(exchange_rate/spread)
    # amount = budget / fee
    # return int(amount - get_leftover_of_bills(amount,denomination))