from models import db
from routes import register_routes  # Импортируем маршруты, если они есть
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:/progging/projects/uforaceclub/backend/instance/uforace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Регистрация маршрутов
with app.app_context():
    db.create_all()  # Создаст таблицы
    register_routes(app)  # Регистрация маршрутов

if __name__ == '__main__':
    app.run(debug=True)
