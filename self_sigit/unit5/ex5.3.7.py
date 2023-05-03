def chocolate_maker(small, big, x):
    if (big * 5 + small) < x or x % 5 > small:
        return False
    return True