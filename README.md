# Практическая работа №15: Основы тестирования с pytest

##  Цель
Познакомиться с основами автоматического тестирования на примере простых функций.

##  Установка

# Установка зависимостей
pip install -r requirements.txt
 Запуск тестов
bash
# Запустить все тесты
pytest -v

# Запустить тесты из конкретного файла
pytest test_math.py -v

# Запустить конкретный тест
pytest test_math.py::test_add -v
 Результат выполнения
Все тесты должны проходить успешно:

test_math.py::test_add PASSED
test_math.py::test_subtract PASSED
test_math.py::test_multiply PASSED
test_math.py::test_divide PASSED
test_math.py::test_is_even PASSED
test_math.py::test_max_of_two PASSED
test_math.py::test_factorial PASSED
test_math.py::test_is_prime PASSED

 Содержание работы
 Установка pytest

 Создание файла math_functions.py с функциями

 Создание файла test_math.py с тестами

 Запуск тестов

 Намеренное "сломать" тест (демонстрация ошибки)

 Написание тестов для функции factorial

 Самостоятельная работа: функция is_prime и тесты для неё

 Функции для тестирования
Функция	Описание
add(a, b)	Сложение двух чисел
subtract(a, b)	Вычитание двух чисел
multiply(a, b)	Умножение двух чисел
divide(a, b)	Деление двух чисел (возвращает None при делении на 0)
is_even(n)	Проверка на чётность
max_of_two(a, b)	Максимальное из двух чисел
factorial(n)	Вычисление факториала
is_prime(n)	Проверка на простоту числа
 GitHub Actions
В репозитории настроен CI/CD с помощью GitHub Actions. Тесты автоматически запускаются при каждом push и pull request.

 Шпаргалка по pytest
Команда	Что делает
pytest	Запускает все тесты в папке
pytest test_math.py -v	Запускает тесты из файла с подробным выводом
pytest test_math.py::test_add -v	Запускает один конкретный тест
assert a == b	Проверяет равенство
assert a != b	Проверяет неравенство
assert a is None	Проверяет, что значение None
assert a is True	Проверяет, что значение True
assert a > b	Проверяет сравнение

### 5. `.github/workflows/test.yml` - CI/CD

```yaml
name: Run Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest test_math.py -v