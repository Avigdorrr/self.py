def filter_teens(a=13, b=13, c=13):
    if 13 <= a <= 14 or 16 <= a <= 19:
        a = fix_age(a)
    if 13 <= b <= 14 or 16 <= b <= 19:
        b = fix_age(b)
    if 13 <= c <= 14 or 16 <= c <= 19:
        c = fix_age(c)
    return a+b+c


def fix_age(age):
    return 0