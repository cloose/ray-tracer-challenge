_EPSILON = 0.00001


def assert_float(actual, expected):
    """Asserts that two floats are equal."""
    assert equal(actual, expected), \
            f"{actual} is not {expected}"


def assert_tuple(actual, expected):
    """Asserts that two tuples are equal."""
    size = len(actual)
    for val in range(size):
        assert equal(actual[val], expected[val]), \
                f"error at index {val}: {actual} is not {expected}"


def assert_matrix(actual, expected):
    """Asserts that two matrices are equal."""
    rows = len(expected)
    columns = len(expected[0])

    for row in range(rows):
        for column in range(columns):
            assert equal(actual[row][column], expected[row][column]), \
                    f"error at position {row},{column}: {actual} is not {expected}"


def equal(left, right):
    return abs(left - right) < _EPSILON
