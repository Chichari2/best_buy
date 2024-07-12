import pytest
from products import Product

# Test that creating a normal product works
def test_create_normal_product():
    product = Product("Test Product", price=10, quantity=5)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 5
    assert product.is_active() is True

# Test that creating a product with invalid details (empty name, negative price) invokes an exception
def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-10)

# Test that when a product reaches 0 quantity, it becomes inactive
def test_product_becomes_inactive_when_quantity_zero():
    product = Product("Test Product", price=10, quantity=1)
    product.buy(1)
    assert product.quantity == 0
    assert product.is_active() is False

# Test that product purchase modifies the quantity and returns the right output
def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("Test Product", price=10, quantity=5)
    total_price = product.buy(3)
    assert product.quantity == 2
    assert total_price == 30

# Test that buying a larger quantity than exists invokes exception
def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product("Test Product", price=10, quantity=5)
    with pytest.raises(ValueError):
        product.buy(10)

# Additional test: Test that buying a negative quantity invokes exception
def test_buying_negative_quantity_invokes_exception():
    product = Product("Test Product", price=10, quantity=5)
    with pytest.raises(ValueError):
        product.buy(-1)
