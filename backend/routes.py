from flask import Blueprint, request, jsonify
from models import db, User

def register_routes(app):
    @app.route('/api/register', methods=['POST'])
    def register():
        try:
            data = request.get_json()
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            # Проверка, что все данные присутствуют
            if not username or not email or not password:
                return jsonify({'error': 'Все поля обязательны для заполнения'}), 400

            # Проверяем, существует ли уже пользователь с таким именем или email
            existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
            if existing_user:
                return jsonify({'error': 'Пользователь с таким именем или email уже существует'}), 400

            # Создаем нового пользователя
            new_user = User(username=username, email=email)
            new_user.set_password(password)  # Установка хешированного пароля
            
            # Добавляем пользователя в базу данных
            db.session.add(new_user)
            db.session.commit()  # Сохраняем изменения

            return jsonify({'message': 'Пользователь зарегистрирован!'}), 200
        except Exception as e:
            print(f"Ошибка при регистрации: {e}")  # Выводим ошибку в консоль
            return jsonify({'error': str(e)}), 500
