"""
    Global Variable overwritten inside the foo()
"""


x = 'global x'


def foo():

    # to use the global Variable
    global x

    x = 'local x'   # >> overwrites the global x

    print(x)


def main():

    foo()

    print(x)        # >> local x


main()
