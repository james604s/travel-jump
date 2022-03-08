def replace_rating_score(x):
    """
    desc:
    :param kwargs:
    :return:
    """
    if x == 100:
        x = 5
    elif x == 80:
        x = 4
    elif x == 60:
        x = 3
    elif x == 40:
        x = 2
    elif x == 20:
        x = 1
    else:
        x = 0
    return x