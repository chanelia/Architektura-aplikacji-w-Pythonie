# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


# ========================================
# Szkielet pliku: product.py
# Uzupelnij implementacje!
# ========================================

class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        if price <= 0:
            raise ValueError("Cena nie moze byc ujemna")
        if quantity < 0:
            raise ValueError("Ilość nie moze byc ujemna")
        pass

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Ilość do dodania nie moze byc ujemna")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Ilość do usunięcia nie moze byc ujemna")
        if amount > self.quantity:
            raise ValueError("Zbyt mało towaru w magazynie")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self, percent: int):
        if percent < 0 or percent > 100:
            raise ValueError("Zniżka musi być między 0 a 100")
        self.price *= (1 - percent / 100)