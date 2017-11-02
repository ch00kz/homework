def calculate_marked_up_value(base_price, num_people, item_type):
    """ Accepts item information and returns marked up price.

        Arguments:
            base_price -- base price of item
            num_people -- number of people who have to do work on item
            item_type -- type of item
    """
    pass

def __get_mark_up_rate(item_type):
    """ Accepts item type and returns associated mark up rate. """
    rates = {
        'pharmaceutical': 0.075,
        'food': 0.13,
        'electronic': 0.02
    }
    return rates.get(item_type, 0)