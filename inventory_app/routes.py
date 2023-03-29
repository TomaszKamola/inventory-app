from flask import (
    render_template, 
    request, 
    flash, 
    redirect, 
    url_for
)
from sqlalchemy import desc
from inventory_app.app import app, db
from inventory_app.models import Items, Types
from datetime import datetime


@app.route("/")
@app.route("/items", methods=['GET', 'POST'])
def items():
    items = Items.query.order_by(Items.id).all()
    types = Types.query.order_by(Types.name).all()

    return render_template('items.html', items=items, types=types)

@app.route("/new_item", methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        if not request.form['add_name'] \
        or not request.form['add_serial'] \
        or not request.form['add_inventory_num']:
            flash("If you want add item, you have to enter each field.", 'warning')
        else:
            date = datetime.now()
            item_type = Types.query.filter_by(id=request.form['add_type']).all()

            item = Items(
                name=request.form['add_name'], 
                serial=request.form['add_serial'], 
                inventory_num=request.form['add_inventory_num'],
                addition_date=date,
                item_type=item_type
            )

            db.session.add(item)
            db.session.commit()
            flash('Record added succefully.', 'success')
            
    return redirect(url_for('items'))

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        delete_checks = request.form.getlist('delete_check')
        if delete_checks:
            for checkid in delete_checks:
                item = Items.query.get(checkid)

                db.session.delete(item)
                db.session.commit()
            flash('Items deleted succefully.', 'success')
        else:
            flash('You must check at least one item in table below.', 'warning')
    
    return redirect(url_for('items'))

@app.route("/", methods=['GET', 'POST'])
def modify():
    pass

@app.route("/about")
def about():
    return render_template('about.html')