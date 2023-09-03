from models import Dog
from sqlalchemy import create_engine

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()
    session.close()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).all()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.name == id).all()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).all()

def update_breed(session, dog, breed):
    updateDog = session.query(Dog).filter(Dog.name == dog.name).first()
    updateDog.breed = breed
    session.commit()
    session.close()
