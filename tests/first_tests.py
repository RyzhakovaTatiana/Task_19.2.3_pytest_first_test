import pytest

from app.calculator import Calculator

class TestCalc:
    #Определяем подготовительны метод сетап
    # в методе setup реализуются необходимые приготовления для запуска тестов:
    # настройка окружения, подготовка тестовых данных, инициализация соединения с БД и так далее
    def setup(self):
        self.calc = Calculator

    # Проверяем умножение, в скобках передаем аргументы, после скобок результат
    def test_multiply_calculator_correctly(self):
        # assert проверяет тест (совпадает ожидаемый результат с фактическим или нет)
        assert self.calc.multiply(self, 2, 2) == 4

    # Проверяем негативные тесты. 2*2=5 это явно негативный тест
    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    #Проверяем деление (позитивный тест)
    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    # Проверяем деление (негативный тест)
    def test_division_calculator_failed(self):
        assert self.calc.division(self, 7, 4) == 20

    # Проверяем вычитание (позитивный тест)
    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 20, 9) == 11

    # Проверяем вычитание (негативный тест)
    def test_subtraction_calculator_failed(self):
        assert self.calc.subtraction(self, 17, 5) == 0

    # Проверяем сложение (позитивный тест)
    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 12, 5) == 17

    # Проверяем сложение (негативный тест)
    def test_adding_calculator_failed(self):
        assert self.calc.adding(self, 12, 8) == 5














