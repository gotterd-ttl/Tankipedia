from app import create_app, db
from app.models import Nation, Tank

app = create_app()

with app.app_context():
    # Получаем существующие нации
    germany = Nation.query.filter_by(name="Германия").first()
    soviet_union = Nation.query.filter_by(name="СССР").first()

    # Проверяем, существуют ли нации, иначе создаем их
    if not germany:
        germany = Nation(name="Германия", description="Нация-участница Второй мировой войны.")
        db.session.add(germany)
    if not soviet_union:
        soviet_union = Nation(name="СССР", description="Советский Союз, участник Второй мировой войны.")
        db.session.add(soviet_union)
    db.session.commit()

    # Список танков для добавления
    tanks = [
        {"name": "Тигр", "description": "Тяжелый танк Германии.", "photo": "tiger.jpg", "nation_id": germany.id},
        {"name": "Пантера", "description": "Средний танк Германии.", "photo": "panther.jpg", "nation_id": germany.id},
        {"name": "Маус", "description": "Сверхтяжелый танк Германии.", "photo": "maus.jpg", "nation_id": germany.id},
        {"name": "Т-34", "description": "Средний танк СССР.", "photo": "t34.jpg", "nation_id": soviet_union.id},
        {"name": "ИС-2", "description": "Тяжелый танк СССР.", "photo": "is2.jpg", "nation_id": soviet_union.id},
        {"name": "КВ-1", "description": "Тяжелый танк СССР.", "photo": "kv1.jpg", "nation_id": soviet_union.id},
    ]

    # Добавляем танки в базу данных
    for tank_data in tanks:
        tank = Tank(**tank_data)
        db.session.add(tank)
    db.session.commit()

    print("Танки успешно добавлены в базу данных.")