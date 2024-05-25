import stripe
import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_API_KEY")


def create_stripe_product(product_name):
    """Создание продукта"""
    stripe_product = stripe.Product.create(
        name="product_name"
    )  # если вставить в параметр name=product_name вылетает ошибка в постмане
    # Missing required param: name. поэтому сделал так
    return stripe_product


def create_stripe_price(amount, product):
    """Создание цены"""
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": product.get("id")},
    )
    return stripe_price


def create_stripe_session(price):
    """
    создает сессию в страйпе
    """
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
