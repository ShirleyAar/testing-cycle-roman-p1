# test suite
import pytest
from roman.converter import to_roman, from_roman


def test_one():
    assert to_roman(1) == "I"


def test_two():
    assert to_roman(2) == "II"


def test_three():
    assert to_roman(3) == "III"


def test_five():
    assert to_roman(5) == "V"


def test_ten():
    assert to_roman(10) == "X"


def test_fifty():
    assert to_roman(50) == "L"


def test_hundred():
    assert to_roman(100) == "C"


def test_five_hundred():
    assert to_roman(500) == "D"


def test_thousand():
    assert to_roman(1000) == "M"


def test_from_one():
    assert from_roman("I") == 1


def test_from_five():
    assert from_roman("V") == 5


def test_from_two():
    assert from_roman("II") == 2


def test_roundtrip_small():
    assert from_roman(to_roman(7)) == 7


def test_roundtrip_medium():
    assert from_roman(to_roman(58)) == 58


def test_lowercase_input():
    assert from_roman("xi") == 11

from roman.converter import (
    RomanError, to_roman, from_roman, is_valid_roman,
    add_roman, subtract_roman, _roundtrip_differs, _count_char,
)


def test_to_roman_rejects_non_integer():
    with pytest.raises(RomanError):
        to_roman("10")

def test_to_roman_rejects_below_min():
    with pytest.raises(RomanError):
        to_roman(0)

def test_to_roman_rejects_above_max():
    with pytest.raises(RomanError):
        to_roman(4000)



def test_from_roman_rejects_non_string():
    with pytest.raises(RomanError):
        from_roman(123)

def test_from_roman_rejects_empty():
    with pytest.raises(RomanError):
        from_roman("")

def test_from_roman_rejects_invalid_char():
    with pytest.raises(RomanError):
        from_roman("IIA")



def test_from_roman_subtractive_pair():
    assert from_roman("IX") == 9




def test_from_roman_rejects_invalid_subtractive():
    with pytest.raises(RomanError):
        from_roman("IL")




def test_from_roman_rejects_out_of_range():
    with pytest.raises(RomanError):
        from_roman("MMMM")  



def test_is_valid_roman_true():
    assert is_valid_roman("XIV") is True

def test_is_valid_roman_false():
    assert is_valid_roman("IIA") is False




def test_add_roman():
    assert add_roman("II", "III") == "V"

def test_subtract_roman():
    assert subtract_roman("V", "II") == "III"



def test_roundtrip_differs_false_when_equal():
    assert _roundtrip_differs(9, "IX") is False

def test_roundtrip_differs_true_when_not_equal():
    assert _roundtrip_differs(9, "VIIII") is True

def test_count_char():
    assert _count_char("MMM", "M") == 3
    assert _count_char("MMM", "X") == 0


def test_integration_add_roman_matches_specification_example():

    result = add_roman("II", "II")
    assert result == "IV"
    assert is_valid_roman(result) is True


def test_acceptance_rejects_non_canonical_form():
    # Given a roman numeral string that is not in canonical form (section 4)
    # When it is validated with is_valid_roman
    # Then it must return False
    assert is_valid_roman("IIII") is False


def test_acceptance_trims_whitespace():
    # Given a roman numeral string with leading/trailing whitespace (section 3)
    # When it is converted with from_roman
    # Then the whitespace is trimmed and the value is returned correctly
    assert from_roman("  IV  ") == 4


def test_acceptance_add_roman_result_is_canonical():
    # Given two valid roman numerals (section 7)
    # When they are added with add_roman
    # Then the result must be canonical and accepted by is_valid_roman
    result = add_roman("IV", "VI")
    assert result == "X"
    assert is_valid_roman(result) is True