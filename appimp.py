from flask import Flask, render_template
import json

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    try:
        # Загружаем данные из файла impuls.json
        with open('impuls.json', 'r') as f:
            data = json.load(f)
        # Передаем данные в шаблон index.html
        return render_template('index.html', impulses=data['impulses'])
    except FileNotFoundError:
        return "Файл 'impuls.json' не найден.", 404
    except json.JSONDecodeError:
        return "Ошибка декодирования JSON. Проверьте формат файла.", 400
    except Exception as e:
        return f"Произошла ошибка: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)