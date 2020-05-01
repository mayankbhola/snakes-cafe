from snakes_cafe.snakes_cafe import order, process, validate
import pytest

def test_validate_True() :
    expected = True
    actual = validate("tea")
    assert expected == actual


def test_validate_False() :
    expected = False
    actual = validate("Fries")
    assert expected == actual


def test_process_new_order_success() :
    process("tea")
    expected = 1
    actual = order["tea"]
    assert expected == actual


def test_process_repeat_order_success() :
    process("tea")
    expected = 2
    actual = order["tea"]
    assert expected == actual


def test_process_order_excpection() :
    with pytest.raises(Exception):
        process("fries")

