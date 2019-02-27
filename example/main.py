import six


def only_covered_in_py2():
    print("Ran py2 function!")


def only_covered_in_py3():
    print("Ran py3 function!")


def main():
    if six.PY2:
        only_covered_in_py2()
    if six.PY3:
        only_covered_in_py3()
    return 1


def uncovered():
    pass
    pass
    pass
    pass
