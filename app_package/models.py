from flask_login import UserMixin
from sqlalchemy import Column, String, Nullable, PrimaryKeyConstraint
from app_package import app
from main import db, session



class users(db.Model, UserMixin):
    user_cod = db.Column(db.String(7),nullable=False, primary_key=True)
    nickname = db.Column(db.String(10), unique=True, nullable=False)
    password_ = db.Column(db.String(8), nullable=False)
    rol_us = db.Column(db.String(2), nullable=False)
    def get_id(self):
        return self.user_cod
    
class associated(db.Model):
    id_as = db.Column(db.String(5), nullable=False, primary_key = True)
    name_ = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    married_lastname = db.Column(db.String(15))
    gender_as = db.Column(db.String(2), nullable=False)
    birth_country = db.Column(db.String(3), nullable=False)
    birth_dept = db.Column(db.String(2), nullable=False)
    birth_muni = db.Column(db.String(2), nullable=False)
    birth_distr = db.Column(db.String(3), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    house_type = db.Column(db.String(2), nullable=False)
    time_to_res_months = db.Column(db.Integer)
    civil_state = db.Column(db.String(2), nullable=False)
    dui_profession = db.Column(db.String(40), nullable=False)
    economy_activity = db.Column(db.String(40))
    email = db.Column(db.String(75))
    phone_number = db.Column(db.String(15))
    ISS = db.Column(db.String(9))
    NUP = db.Column(db.String(9))
    n_people_to_maintance = db.Column(db.Integer)
    respon_us = db.Column(db.String(7), nullable=False)
    notes = db.Column(db.String(50))
    num_contribuyente = db.Column(db.String(7))
    cat_contribuyente = db.Column(db.String(14))

class doc_id(db.Model):
    number_id = db.Column(db.String(14),primary_key=True, nullable=False)
    id_as = db.Column(db.String(4), nullable=False)
    type_id = db.Column(db.String(2), nullable=False)
    expiration_date = db.Column(db.Date)
    
class res_as(db.Model):
    id_res = db.Column(db.String(5), primary_key = True, nullable=False)
    id_as = db.Column(db.String(5), nullable=False)
    country_res = db.Column(db.String(3), nullable=False)
    dept_res = db.Column(db.String(2), nullable=False)
    muni_res = db.Column(db.String(2), nullable=False)
    dist_res = db.Column(db.String(3), nullable=False)
    adress = db.Column(db.String(75))

with app.app_context():
    all_users = session.query(users).all()
print(all_users)