# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-26 15:03:35
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-29 17:03:51
# @Email: liangchaowu5@gmail.com

import os
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import  SQLAlchemy

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

app = Flask(__name__)
# prevent CSRF
app.config ['SECRET_KEY'] = 'guess it hehe'

# set database
base_dir = os.path.abspath(os.path.dirname(__file__))
database_file = os.path.join(base_dir,'data.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ database_file
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


# form of the page
class MessageFrom(Form):
    name = StringField(u'姓名', validators = [Required()])
    message = TextAreaField(u'留言', validators = [Required()])
    submit = SubmitField(u'提交留言')


# table of database
class Message(db.Model):
    __tablename__ = "user_message"
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Unicode)
    message = db.Column(db.UnicodeText)
    time = db.Column(db.String)

def write_record(message):
    db.session.add(message)
    db.session.commit()

def delete_record(user_name):
    Message.query.filter_by(user = user_name).delete()
    db.session.commit()

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = MessageFrom()
    if form.validate_on_submit():
        if form.name.data and form.message.data:
            current_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            message = Message(user = form.name.data, message = form.message.data, time = current_time)
            form.name.data, form.message.data = '', ''
            write_record(message)
        return redirect(url_for('index'))
    try:
        history_messages = reversed(Message.query.all())
    except Exception:
        history_messages = None
    return render_template('index.html', message_form = form, messages=history_messages)


if __name__ == '__main__':
    if not os.path.exists(database_file):
        db.create_all()
        print 'Initialize database %s successfully' %database_file
    app.run(debug = True)
