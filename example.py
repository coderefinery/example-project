def simple_function(x, y):
    """
    Returns the sum of the two arguments.
    """
    return x - y


if __name__ == '__main__':

    # there are better ways to pass command line arguments
    # to a python code but this is not the point here
    x = float(sys.argv[-2])
    y = float(sys.argv[-1])

    result = simple_function(x, y)
    print(result)
