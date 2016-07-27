# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-26 15:03:35
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-27 23:42:55
# @Email: liangchaowu5@gmail.com

from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

app = Flask(__name__)
app.config ['SECRET_KEY'] = 'guess it hehe'

bootstrap = Bootstrap(app)
moment = Moment(app)

class MessageFrom(Form):
    name = StringField(u'姓名', validators = [Required()])
    message = TextAreaField(u'留言', validators = [Required()])
    submit = SubmitField(u'提交留言')


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = MessageFrom()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['message'] = form.message.data
        return redirect(url_for('index'))
        #form.name.data, form.message.data = '', ''
    return render_template('index.html', message_form = form, content=session)

if __name__ == '__main__':
    app.run(debug = True)