def calculate_marked_up_value(base_price, num_people, item_type):
    """ Accepts item information and returns marked up price.

        Arguments:
            base_price -- base price of item
            num_people -- number of people who have to do work on item
            item_type -- type of item
    """
    __validate_arguments(base_price=base_price, num_people=num_people, 
                         item_type=item_type)
    
    # constant rates
    FLAT_MARK_UP_RATE = 0.05
    PER_PERSON_MARK_UP_RATE = 0.012

    # get various mark up rates
    person_mark_up_rate = num_people * PER_PERSON_MARK_UP_RATE
    type_mark_up_rate = __get_type_mark_up_rate(item_type)

    # calculate flat mark up and subtotal 
    flat_mark_up = base_price * FLAT_MARK_UP_RATE
    subtotal = base_price + flat_mark_up

    # calculate other mark ups using updated base_price
    person_mark_up = subtotal * person_mark_up_rate
    type_mark_up = subtotal * type_mark_up_rate

    # calculate final marked_up_price
    marked_up_price = subtotal + person_mark_up + type_mark_up

    # round to marked_up_price to decimal places
    return float("%.2f" % marked_up_price)


def __get_type_mark_up_rate(item_type):
    """ Accepts item type and returns associated mark up rate. """
    rates = {
        'pharmaceutical': 0.075,
        'food': 0.13,
        'electronic': 0.02
    }
    return rates.get(item_type, 0)


def __validate_arguments(**kwargs):
    """ Provides simple validation of supplied arguments.
    """
    base_price = kwargs.get('base_price')
    valid_base_price = isinstance(base_price, (int, float)) and base_price >= 0
    if not valid_base_price:
        raise ValueError(
            "Supplied base_price must be a non-negative integer or float."
            )

    num_people = kwargs.get('num_people')
    valid_num_people = isinstance(num_people, int) and num_people >= 0
    if not valid_num_people:
        raise ValueError(
            "Supplied num_people must be a non-negative integer."
            )

    item_type = kwargs.get('item_type')
    valid_item_type = isinstance(item_type, str) and len(item_type) > 0
    if not valid_item_type:
        raise ValueError(
            "Supplied item_type must be a string of length > 1"
            )
