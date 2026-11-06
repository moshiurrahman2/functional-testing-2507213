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

