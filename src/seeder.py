from app import app, db
from models import Users, People, Planets

def seed_users():

    db.session.query(Users).delete()
    db.session.commit()
    
    users = [
        Users(username='user1'),
        Users(username='user2'),
        Users(username='user3')
    ]
    db.session.bulk_save_objects(users)
    db.session.commit()
    print("Users table seeded!")

def seed_people():
    people = [
        People(name="Luke Skywalker", height="172", mass="77", gender="male"),
        People(name="Leia Organa", height="150", mass="49", gender="female"),
        People(name="Darth Vader", height="202", mass="136", gender="male"),
    ]
    db.session.bulk_save_objects(people)
    db.session.commit()
    print("People table seeded!")

def seed_planets():
    planets = [
        Planets(name="Tatooine", climate="arid", terrain="desert"),
        Planets(name="Hoth", climate="frozen", terrain="ice caves"),
        Planets(name="Dagobah", climate="murky", terrain="swamp"),
    ]
    db.session.bulk_save_objects(planets)
    db.session.commit()
    print("Planets table seeded!")

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")
        seed_users()
        seed_people()
        seed_planets()
        print("Seeding complete!")