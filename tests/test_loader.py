import pytest

from src.data.loader import load_processed_data


def test_load_processed_data():

    data = load_processed_data()

    assert isinstance(data, dict)

    assert "orders" in data
    assert "customers" in data
    assert "payments" in data

    assert not data["orders"].empty