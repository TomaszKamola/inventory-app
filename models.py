from inventory import db


items_types = db.Table(
    'items_types',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
    db.Column('type_id', db.Integer, db.ForeignKey('type.id'))
)

users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

created_by = db.Table(
    'created_by',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    serial = db.Column(db.String(120))
    inventory_num = db.Column(db.String(80), unique=True)
    addition_date = db.Column(db.DateTime, nullable=False)
    types = db.relationship('Type', secondary='items_types')
    users = db.relationship('User', secondary='created_by')


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    roles = db.relationship('Role', secondary='users_roles')


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
