from flask import render_template, request, redirect, url_for
from . import db
from .models import Nation, Tank, Rating, Comment
from app.wikipedia_service import get_tank_info  # Импорт сервиса Wikipedia


def setup_routes(app):
    @app.route('/')
    def index():
        nations = Nation.query.all()
        return render_template('index.html', nations=nations)

    @app.route('/nation/<int:nation_id>')
    def nation_detail(nation_id):
        nation = Nation.query.get_or_404(nation_id)
        tanks_query = Tank.query.filter_by(nation_id=nation.id)

        # Фильтрация и сортировка
        tank_type = request.args.get('type')
        if tank_type:
            tanks_query = tanks_query.filter_by(type=tank_type)

        sort_by = request.args.get('sort_by', 'name')
        if sort_by == 'rating':
            tanks_query = tanks_query.outerjoin(Rating).group_by(Tank.id).order_by(db.func.avg(Rating.score).desc())
        else:
            tanks_query = tanks_query.order_by(Tank.name)

        tanks = tanks_query.all()
        return render_template('nation_detail.html', nation=nation, tanks=tanks, tank_type=tank_type, sort_by=sort_by)

    @app.route('/tank/<int:tank_id>', methods=['GET', 'POST'])
    def tank_detail(tank_id):
        tank = Tank.query.get_or_404(tank_id)

        if request.method == 'POST':
            if 'score' in request.form:  # Добавление рейтинга
                score = int(request.form.get('score'))
                rating = Rating(score=score, tank_id=tank.id)
                db.session.add(rating)
                db.session.commit()
                return redirect(url_for('tank_detail', tank_id=tank.id))
            elif 'content' in request.form:  # Добавление комментария
                content = request.form.get('content')
                comment = Comment(content=content, tank_id=tank.id)
                db.session.add(comment)
                db.session.commit()
                return redirect(url_for('tank_detail', tank_id=tank.id))

        avg_rating = db.session.query(db.func.avg(Rating.score)).filter_by(tank_id=tank.id).scalar() or 0
        comments = Comment.query.filter_by(tank_id=tank.id).all()

        # Интеграция с Wikipedia API
        tank_info = get_tank_info(tank.name)

        return render_template(
            'tank_detail.html',
            tank=tank,
            avg_rating=avg_rating,
            comments=comments,
            tank_info=tank_info  # Передача данных из Wikipedia
        )