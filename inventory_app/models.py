from inventory_app.app import db


items_types = db.Table(
    'items_types',
    db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
    db.Column('type_id', db.Integer, db.ForeignKey('types.id'))
)

users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)

created_by = db.Table(
    'created_by',
    db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    serial = db.Column(db.String(120))
    inventory_num = db.Column(db.String(80), unique=True)
    addition_date = db.Column(db.DateTime, nullable=False)
    item_type = db.relationship('Types', secondary='items_types')
    user = db.relationship('Users', secondary='created_by')

    # def __init__(self, name, serial, inventory_num):
    #     self.item_name = name
    #     self.item_serial = serial
    #     self.item_inventory_num = inventory_num


class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    role = db.relationship('Roles', secondary='users_roles')


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

