from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10))
    status = db.Column(db.Integer)

    def __init__(self, title, status):
        self.title = title
        self.status = status

class TodoSchema(ma.Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    status = fields.Integer(equired=True)
