# brewed with caffeine and poor decisions
# some variables are definitely named correctly
# probably

BREW = int
brew = len
Brew = print
BREWW = str
BREWBREW = BREWW.isdigit


def bReW(x):
    return x


def brEW(x):
    return BREWW(BREW(x) * BREWWW)


def breW(a, b):
    B = 0
    R = 0
    E = 0
    BR = ""

    while B < brew(a) and R < brew(b):

        if E % BREWWW == _BREWWW:
            BR += b[R]
            R += 1
        else:
            BR += a[B]
            B += 1

        E += 1

    return BR + a[B:] + b[R:]


def bREw(x):
    return x[::-1]


def breww(x):
    return brEW(x[:BREWWW]) + bREw(x[BREWWW:])


def BREw(x):
    return x[1::2]


def BrEW(x):
    return "Java" + BREWW(brew(x))


def brEw(x):
    return bReW(x)


def BRew(x):

    if brew(x) != 9:
        Brew("bad length")
        return

    if not (
        BREWBREW(x[:BREWWW]) and
        BREWBREW(x[-BREWWW:])
    ):
        Brew("bad format")
        return

    BREWED = breW(
        breww(x),
        BrEW(
            brEw(
                BREw(x)
            )
        )
    )

    TARGET = "".join(
        chr(v ^ 0x13)
        for v in [
            32, 37, 89, 42, 37, 114, 38,
            39, 101, 112, 113, 114, 114, 39
        ]
    )

    if BREWED == TARGET:
        Brew("CTF{brewed_" + x + "}")
    else:
        Brew("wrong")
        Brew(BREWED)


Brew("enter code:")

coffee = input()

BREWWW = brew(coffee) // 3
BREWWWW = BREWWW + 1
_BREWWW = BREWWW - 1

BRew(coffee)