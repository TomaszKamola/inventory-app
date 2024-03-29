from flask import (
    render_template, 
    request, 
    flash, 
    redirect, 
    url_for
)
from inventory_app.app import app, db
from inventory_app.models import Items, Types
from datetime import datetime


with app.app_context():
    types = Types.query.order_by(Types.name).all()

@app.route("/")
@app.route("/items", methods=['GET', 'POST'])
def items():
    items = Items.query.order_by(Items.id).all()

    return render_template('items.html', items=items, types=types)

@app.route("/new_item", methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        if not request.form['name'] \
        or not request.form['serial'] \
        or not request.form['inventory_num']:
            flash("If you wan't add item, you have to enter each field.", 'warning')
        else:
            date = datetime.now()
            item_type = Types.query.filter_by(id=request.form['type']).all()

            item = Items(
                name=request.form['name'], 
                serial=request.form['serial'], 
                inventory_num=request.form['inventory_num'],
                addition_date=date,
                item_type=item_type
            )

            db.session.add(item)
            db.session.commit()
            flash('Item added succefully.', 'success')
            
        return redirect(url_for('items'))
        
    return render_template('new_item.html', types=types)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == 'POST' and request.form['submit_button'] == 'Delete':
        checks = request.form.getlist('check')
        if checks:
            for checkid in checks:
                item = Items.query.get(checkid)

                db.session.delete(item)
                db.session.commit()
            flash('Items deleted succefully.', 'success')
        else:
            flash('You must check at least one item in table below.', 'warning')
    
    return redirect(url_for('items'))

@app.route("/modify", methods=['GET', 'POST'])
def modify():
    if request.method == 'POST' and request.form['submit_button'] == 'Save':
        if not request.form['edit_name'] \
        or not request.form['edit_serial'] \
        or not request.form['edit_inv_num']:
            flash("If you wan't edit item, each field must be filled.", 'warning')
        else:
            item = Items.query.filter_by(id=request.form['edit_id']).all()

            item.item_type = request.form['edit_type']
            item.name = request.form['edit_name']
            item.serial = request.form['edit_serial']
            item.inventory_num = request.form['edit_inv_num']

            # db.session.commit()
            flash('Item edited succefully.', 'success')

    return redirect(url_for('items'))

@app.route("/about")
def about():
    return render_template('about.html')

