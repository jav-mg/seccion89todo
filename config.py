from flask import *
from flask_sqlalchemy import *
from sqlalchemy import Integer, String, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import sys                                                                          # utilizado para redirigir la salida a la consola

app = Flask(__name__)                                                               # instanciar servidor
# ---------------------------- DATABASE --------------------------------------------

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"                         # ruta a la base de datos, se construye en: \var\config-instance\

class Base(DeclarativeBase):
  pass
  
db = SQLAlchemy(model_class=Base)                                                   # se crea el objeto db
db.init_app(app)
# ----------------------------- TABLAS ---------------------------------------------

class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    status = db.Column(db.Boolean, unique=False, nullable=False)
# -------------------------- CONSTRUYE TABLAS --------------------------------------

with app.app_context():
    db.create_all()    
# ----------------------------- CONSULTAS ------------------------------------------

def QUERY_selectAll()->[]:    
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
    return result.scalars()   

