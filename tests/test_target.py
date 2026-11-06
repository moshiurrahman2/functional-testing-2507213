import pytest

import target

# =========================================================
# 1. is_adult()
# =========================================================


@pytest.mark.parametrize(
    "age, expected",
    [
        (0, False),
        (17, False),
        (18, True),
        (100, True),
    ],
)
def test_is_adult(age, expected):
    result = target.is_adult(age)

    assert result is expected
    assert isinstance(result, bool)


def test_is_adult_negative():
    with pytest.raises(
        ValueError,
        match="age cannot be negative"
    ):
        target.is_adult(-1)


def test_is_adult_wrong_type():
    with pytest.raises(TypeError):
        target.is_adult("18")


# =========================================================
# 2. celsius_to_fahrenheit()
# =========================================================

@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32.00),
        (100, 212.00),
        (-40, -40.00),
        (37, 98.60),
        (25.5, 77.90),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    result = target.celsius_to_fahrenheit(celsius)

    assert result == pytest.approx(expected)
    assert isinstance(result, float)


def test_celsius_to_fahrenheit_wrong_type():
    with pytest.raises(TypeError):
        target.celsius_to_fahrenheit("100")


# =========================================================
# 3. count_vowels()
# =========================================================

@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 2),
        ("HELLO", 2),
        ("aeiou", 5),
        ("AEIOU", 5),
        ("xyz", 0),
        ("", 0),
        ("Hello World", 3),
    ],
)
def test_count_vowels(text, expected):
    result = target.count_vowels(text)

    assert result == expected
    assert isinstance(result, int)


def test_count_vowels_wrong_type():
    with pytest.raises(
        TypeError,
        match="text must be a string"
    ):
        target.count_vowels(123)


# =========================================================
# 4. invert()
# =========================================================

@pytest.mark.parametrize(
    "flag, expected",
    [
        (True, False),
        (False, True),
    ],
)
def test_invert(flag, expected):
    result = target.invert(flag)

    assert result is expected
    assert isinstance(result, bool)


def test_invert_wrong_type():
    with pytest.raises(
        TypeError,
        match="flag must be True or False"
    ):
        target.invert(1)


# =========================================================
# 5. greet()
# =========================================================

@pytest.mark.parametrize(
    "name, expected",
    [
        (None, "Hello, Guest!"),
        ("", "Hello, Guest!"),
        ("   ", "Hello, Guest!"),
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
    ],
)
def test_greet(name, expected):
    result = target.greet(name)

    assert result == expected
    assert isinstance(result, str)


def test_greet_default():
    result = target.greet()

    assert result == "Hello, Guest!"


# =========================================================
# 6. find_max()
# =========================================================

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 3),
        ([10, 5, 7], 10),
        ([-1, -5, -2], -1),
        ([42], 42),
    ],
)
def test_find_max(numbers, expected):
    result = target.find_max(numbers)

    assert result == expected


def test_find_max_empty():
    with pytest.raises(ValueError):
        target.find_max([])


def test_find_max_wrong_type():
    result = target.find_max("123")

    assert result == "3"


# =========================================================
# 7. get_price()
# =========================================================

@pytest.mark.parametrize(
    "prices, item, expected",
    [
        ({"apple": 10, "banana": 20}, "apple", 10),
        ({"pen": 5, "book": 50}, "book", 50),
        ({"milk": 30}, "milk", 30),
    ],
)
def test_get_price(prices, item, expected):
    result = target.get_price(prices, item)

    assert result == expected


def test_get_price_missing_item():
    with pytest.raises(KeyError):
        target.get_price({"apple": 10}, "orange")


# =========================================================
# 8. swap()
# =========================================================

@pytest.mark.parametrize(
    "pair, expected",
    [
        ((1, 2), (2, 1)),
        (("a", "b"), ("b", "a")),
        ((10, 20), (20, 10)),
    ],
)
def test_swap(pair, expected):
    result = target.swap(pair)

    assert result == expected


def test_swap_empty():
    with pytest.raises(ValueError):
        target.swap(())


def test_swap_one_value():
    with pytest.raises(ValueError):
        target.swap((1,))


def test_swap_three_values():
    with pytest.raises(ValueError):
        target.swap((1, 2, 3))


# =========================================================
# 9. common_items()
# =========================================================

@pytest.mark.parametrize(
    "set_a, set_b, expected",
    [
        ({1, 2, 3}, {2, 3, 4}, {2, 3}),
        ({"apple", "banana"}, {"banana", "orange"}, {"banana"}),
        ({1, 2}, {3, 4}, set()),
    ],
)
def test_common_items(set_a, set_b, expected):
    result = target.common_items(set_a, set_b)

    assert result == expected


# =========================================================
# 10. is_leap_year()
# =========================================================

@pytest.mark.parametrize(
    "year, expected",
    [
        (2000, True),
        (2024, True),
        (2023, False),
        (1900, False),
        (2028, True),
    ],
)
def test_is_leap_year(year, expected):
    result = target.is_leap_year(year)

    assert result is expected


def test_is_leap_year_zero():
    with pytest.raises(ValueError):
        target.is_leap_year(0)


def test_is_leap_year_negative():
    with pytest.raises(ValueError):
        target.is_leap_year(-2024)


def test_is_leap_year_wrong_type():
    with pytest.raises(TypeError):
        target.is_leap_year("2024")


# =========================================================
# 11. to_int()
# =========================================================

@pytest.mark.parametrize(
    "value, expected",
    [
        ("10", 10),
        ("25", 25),
        (10.5, 10),
        (0, 0),
    ],
)
def test_to_int(value, expected):
    result = target.to_int(value)

    assert result == expected
    assert isinstance(result, int)


def test_to_int_bool_true():
    with pytest.raises(TypeError):
        target.to_int(True)


def test_to_int_bool_false():
    with pytest.raises(TypeError):
        target.to_int(False)


# =========================================================
# 12. divide()
# =========================================================

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (20, 4, 5),
        (9, 3, 3),
        (7, 2, 3.5),
    ],
)
def test_divide(a, b, expected):
    result = target.divide(a, b)

    assert result == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        target.divide(10, 0)


# =========================================================
# 13. power()
# =========================================================

@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 3, 8),
        (5, 2, 25),
        (10, 0, 1),
        (2, -1, 0.5),
    ],
)
def test_power(base, exponent, expected):
    result = target.power(base, exponent)

    assert result == expected


def test_power_wrong_type():
    with pytest.raises(TypeError):
        target.power("2", 3)


# =========================================================
# 14. square_root()
# =========================================================

@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0),
        (4, 2),
        (9, 3),
        (25, 5),
    ],
)
def test_square_root(x, expected):
    assert target.square_root(x) == expected


def test_square_root_negative():
    with pytest.raises(ValueError):
        target.square_root(-4)


def test_square_root_wrong_type():
    with pytest.raises(TypeError):
        target.square_root("4")


# =========================================================
# 15. factorial()
# =========================================================

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (3, 6),
        (5, 120),
    ],
)
def test_factorial(n, expected):
    assert target.factorial(n) == expected


def test_factorial_negative():
    with pytest.raises(ValueError):
        target.factorial(-5)


def test_factorial_wrong_type():
    with pytest.raises(TypeError):
        target.factorial("5")


# =========================================================
# 16. average()
# =========================================================

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 2),
        ([10, 20, 30], 20),
        ([2, 4], 3),
        ([5], 5),
    ],
)
def test_average(numbers, expected):
    assert target.average(numbers) == expected


def test_average_empty():
    with pytest.raises(ValueError):
        target.average([])


def test_average_wrong_type():
    with pytest.raises(TypeError):
        target.average([1, "2", 3])
