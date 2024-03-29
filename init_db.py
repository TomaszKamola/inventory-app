from inventory_app.app import app, db
from inventory_app.models import Items, Types, Users, Roles
from datetime import datetime


date = datetime.now()

with app.app_context():
    db.drop_all()
    db.create_all()

    item1 = Items(
        name='Dell Optiplex XYZ123', 
        serial='S/N 224466135', 
        inventory_num='XY100111',
        addition_date=date
    )

    item2 = Items(
        name='Dell SH1T1488', 
        serial='S/N 21371488', 
        inventory_num='XY100222',
        addition_date=date
    )

    item3 = Items(
        name='Mysz Logitech M2137', 
        serial='S/N 11111111', 
        inventory_num='XY100333',
        addition_date=date
    )

    item4 = Items(
        name='Klawiatura Logitech K2137', 
        serial='S/N 101010101010', 
        inventory_num='XY100444',
        addition_date=date
    )

    type1 = Types(name='Komputer')
    type2 = Types(name='Monitor')
    type3 = Types(name='Mysz')
    type4 = Types(name='Klawiatura')

    user1 = Users(name='Janusz Maj')
    user2 = Users(name='Andrzej Bęc')

    role1 = Roles(name='Admin')

    item1.item_type.append(type1)
    item2.item_type.append(type2)
    item3.item_type.append(type3)
    item4.item_type.append(type4)

    item1.user.append(user1)
    item2.user.append(user1)
    item3.user.append(user2)
    item4.user.append(user1)

    user1.role.append(role1)
    user2.role.append(role1)

    db.session.add_all([item1, item2, item3, item4])
    db.session.add_all([type1, type2, type3, type4])
    db.session.add_all([user1, user2])
    db.session.add_all([role1])

    db.session.commit()

