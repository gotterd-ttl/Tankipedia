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

    # Список танков для добавления (только времен Второй мировой войны)
    tanks = [
        # Танки Германии
        {"name": "Тигр", "description": "Тяжелый танк Германии.", "photo": "tiger.jpg", "nation_id": germany.id,
         "type": "heavy"},
        {"name": "Пантера", "description": "Средний танк Германии.", "photo": "panther.jpg", "nation_id": germany.id,
         "type": "medium"},
        {"name": "Маус", "description": "Сверхтяжелый танк Германии.", "photo": "maus.jpg", "nation_id": germany.id,
         "type": "heavy"},
        {"name": "PzKpfw IV", "description": "Средний танк Германии.", "photo": "pz4.jpg", "nation_id": germany.id,
         "type": "medium"},
        {"name": "PzKpfw III", "description": "Средний танк Германии.", "photo": "pz3.jpg", "nation_id": germany.id,
         "type": "medium"},
        {"name": "StuG III", "description": "Штурмовая самоходка.", "photo": "stug3.jpg", "nation_id": germany.id,
         "type": "medium"},
        {"name": "Hetzer", "description": "Истребитель танков.", "photo": "hetzer.jpg", "nation_id": germany.id,
         "type": "light"},
        {"name": "Nashorn", "description": "Истребитель танков с мощной пушкой.", "photo": "nashorn.jpg",
         "nation_id": germany.id, "type": "light"},
        {"name": "VK 36.01", "description": "Прототип тяжелого танка.", "photo": "vk3601.jpg", "nation_id": germany.id,
         "type": "heavy"},
        {"name": "PzKpfw II", "description": "Легкий танк Германии.", "photo": "pz2.jpg", "nation_id": germany.id,
         "type": "light"},

        # Танки СССР
        {"name": "Т-34", "description": "Средний танк СССР.", "photo": "t34.jpg", "nation_id": soviet_union.id,
         "type": "medium"},
        {"name": "ИС-2", "description": "Тяжелый танк СССР.", "photo": "is2.jpg", "nation_id": soviet_union.id,
         "type": "heavy"},
        {"name": "КВ-1", "description": "Тяжелый танк СССР.", "photo": "kv1.jpg", "nation_id": soviet_union.id,
         "type": "heavy"},
        {"name": "Т-70", "description": "Легкий разведывательный танк.", "photo": "t70.jpg",
         "nation_id": soviet_union.id, "type": "light"},
        {"name": "ИСУ-152", "description": "Штурмовая самоходка с мощной пушкой.", "photo": "isu152.jpg",
         "nation_id": soviet_union.id, "type": "heavy"},
        {"name": "БТ-7", "description": "Быстроходный легкий танк.", "photo": "bt7.jpg",
         "nation_id": soviet_union.id, "type": "light"},
        {"name": "СУ-100", "description": "Истребитель танков.", "photo": "su100.jpg",
         "nation_id": soviet_union.id, "type": "medium"},
        {"name": "КВ-2", "description": "Штурмовой танк с мощной пушкой.", "photo": "kv2.jpg",
         "nation_id": soviet_union.id, "type": "heavy"},
        {"name": "Т-60", "description": "Легкий танк для поддержки пехоты.", "photo": "t60.jpg",
         "nation_id": soviet_union.id, "type": "light"},
    ]

    # Добавляем танки в базу данных
    for tank_data in tanks:
        tank = Tank(**tank_data)
        db.session.add(tank)
    db.session.commit()

    print("Танки успешно добавлены в базу данных.")
