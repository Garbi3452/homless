import colorama
from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + "=== Інтроспекція модуля colorama ===")

print("Назва модуля:", colorama.__name__)
print("Файл модуля:", colorama.__file__)

print("Версія:", getattr(colorama, '__version__', 'Невідомо'))

attributes = dir(colorama)
print("\nУсі атрибути та методи модуля:")
print(attributes)

print("\nПеревірка типів:")
print("Тип Fore:", type(Fore))

print("Тип init:", type(init))

print("\nДокументація:")
print(init.__doc__)
