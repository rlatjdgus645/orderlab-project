import pytest

from orderlab.pricing import final_total, subtotal


def test_subtotal_normal():
    assert subtotal(10_000, 2) == 20_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)


def test_final_total_below_free_shipping():
    assert final_total(49_999, 1, 0) == 52_999


def test_final_total_free_shipping_boundary():
    assert final_total(50_000, 1, 0) == 50_000


def test_final_total_above_free_shipping():
    assert final_total(50_001, 1, 0) == 50_001
