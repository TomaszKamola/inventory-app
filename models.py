from inventory import db


items_types = db.Table(
    'items_types',
    db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
    db.Column('type_id', db.Integer, db.ForeignKey('types.id'))
)

# users_roles = db.Table(
#     ''
# )

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    item_type = db.Column(db.Integer)
    serial = db.Column(db.String(120))
    inventory_num = db.Column(db.String(80), unique=True)
    types = db.relationship('Types', secondary='items_types', back_populates='items')


class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    items = db.relationship('Items', secondary='items_types', back_populates='types')


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
