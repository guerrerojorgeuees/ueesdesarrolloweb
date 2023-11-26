from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import Uees, db
contacts = Blueprint('contacts', __name__, template_folder='app/templates')

@contacts.route('/')
def index():
    contacts_data = Uees.query.all()
    return render_template('index.html', contacts=contacts_data)

@contacts.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        try:
            new_contact = Uees(fullname=fullname, phone=phone, email=email)
            db.session.add(new_contact)
            db.session.commit()
            flash('Contact Added successfully')
            return redirect(url_for('contacts.index'))
        except Exception as e:
            flash(str(e))
            return redirect(url_for('contacts.index'))

@contacts.route('/edit/<int:id>', methods=['POST', 'GET'])
def get_contact(id):
    contact = Uees.query.get(id)
    return render_template('edit-contact.html', contact=contact)

@contacts.route('/update/<int:id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        contact = Uees.query.get(id)
        contact.fullname = fullname
        contact.phone = phone
        contact.email = email
        db.session.commit()
        flash('Contact Updated Successfully')
        return redirect(url_for('contacts.index'))

@contacts.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_contact(id):
    contact = Uees.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('contacts.index'))
