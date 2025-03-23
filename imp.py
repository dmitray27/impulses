import json

try:
    with open('impuls.json', 'r') as f:
        data = json.load(f)
    print(data)
except FileNotFoundError:
    print("Файл 'impuls.json' не найден.")
except json.JSONDecodeError:
    print("Ошибка декодирования JSON. Проверьте формат файла.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
