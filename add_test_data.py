from app import create_app, db
from app.models import Nation, Tank

app = create_app()

with app.app_context():
    germany = Nation(name="Германия", description="Нация-участница Второй мировой войны.")
    soviet_union = Nation(name="СССР", description="Советский Союз, участник Второй мировой войны.")

    db.session.add_all([germany, soviet_union])
    db.session.commit()

    tiger = Tank(name="Тигр", description="Тяжелый танк Германии.", photo="tiger.jpg", nation_id=germany.id)
    t34 = Tank(name="Т-34", description="Средний танк СССР.", photo="t34.jpg", nation_id=soviet_union.id)

    db.session.add_all([tiger, t34])
    db.session.commit()
    print("Тестовые данные добавлены.")