from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id, 
            "username": self.username
            }

class People(db.Model):
    __tablename__='people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(10))
    mass = db.Column(db.String(10))
    gender = db.Column(db.String(20))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "gender": self.gender
            }

class Planets(db.Model):
    __tablename__='planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120))
    terrain = db.Column(db.String(120))

    def serialize(self):
        return {
            "id": self.id, 
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain
            }

class Favorites(db.Model):
    __tablename__='favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "people_id": self.people_id,
            "planets_id": self.planets_id
        }
