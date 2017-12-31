import functools

def ceilXX(value, ceiling):
    remainder = value % ceiling
    if remainder:
        return value + (ceiling - remainder)
    else:
        return value


ceil32 = functools.partial(ceilXX, ceiling=32)
