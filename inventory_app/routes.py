from flask import (
    render_template, 
    request, 
    flash, 
    redirect, 
    url_for
)
from inventory_app.app import app, db
from inventory_app.models import Items
from datetime import datetime


@app.route("/")
@app.route("/items", methods=['GET', 'POST'])
def items():
    items = Items.query.order_by(Items.id).all()

    return render_template(
        'items.html',
        items=items
    )

@app.route("/new_item", methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        if not request.form['name'] \
        or not request.form['serial'] \
        or not request.form['inventory_num']:
            flash("If you wan't add item, you have to enter each field.", 'warning')
        else:
            date = datetime.now()
            item = Items(
                name=request.form['name'], 
                serial=request.form['serial'], 
                inventory_num=request.form['inventory_num'],
                addition_date=date
            )

            db.session.add(item)
            db.session.commit()
            flash('Record added succefully.', 'success')
            
            return redirect(url_for('items'))
        
    return render_template('new_item.html')

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        for checkid in request.form.getlist('delete_check'):
            item = Items.query.get(checkid)

            db.session.delete(item)
            db.session.commit()
        flash('Items deleted succefully.', 'success')
    
    return redirect(url_for('items'))

@app.route("/about")
def about():
    return render_template('about.html')