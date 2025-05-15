from . import db

class Nation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Nation {self.name}>'

class Tank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200), nullable=True)
    nation_id = db.Column(db.Integer, db.ForeignKey('nation.id'), nullable=False)
    type = db.Column(db.String(50), nullable=True)

    nation = db.relationship('Nation', backref=db.backref('tanks', lazy=True))

    def __repr__(self):
        return f'<Tank {self.name}>'

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    tank_id = db.Column(db.Integer, db.ForeignKey('tank.id'), nullable=False)

    tank = db.relationship('Tank', backref=db.backref('ratings', lazy=True))

    def __repr__(self):
        return f'<Rating {self.score} for Tank {self.tank.name}>'

# Новая модель для комментариев
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    tank_id = db.Column(db.Integer, db.ForeignKey('tank.id'), nullable=False)

    tank = db.relationship('Tank', backref=db.backref('comments', lazy=True))

    def __repr__(self):
        return f'<Comment {self.content[:20]}... for Tank {self.tank.name}>'