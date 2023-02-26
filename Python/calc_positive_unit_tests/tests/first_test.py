# юнит тесты на калькулятор

from app.calculator import Calculator
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate(self):
        assert self.calc.multiply(self, 7, 6) == 42

    def test_multiply(self):
        assert self.calc.division(self, 12, 6) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 8, 6) == 2

    def test_adding(self):
        assert self.calc.adding(self, 7, 6) == 13
