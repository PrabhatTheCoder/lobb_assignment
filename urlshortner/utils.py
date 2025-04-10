import string

BASE62 = string.digits + string.ascii_letters

def encode_base62(num):
    if num == 0:
        return BASE62[0]
    base62 = ''
    while num:
        num, rem = divmod(num, 62)
        base62 = BASE62[rem] + base62
    return base62
