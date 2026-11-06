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
