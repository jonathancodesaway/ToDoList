from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/jon/pracwebdev/project1/todo.db' 

db = SQLAlchemy(app) 

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200))
	complete = db.Column(db.Boolean)

@app.route('/')
def index():
	todos = Todo.query.all()
	return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
	todo = Todo(text=request.form['todoitem'], complete=False)
	db.session.add(todo)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['GET'])
def delete(id):
	todo = Todo.query.filter_by(id=int(id)).delete()
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/MarkAsComplete/<id>', methods=['GET','POST'])
def MarkAsComplete(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	todo.complete = True
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/MarkAsIncomplete/<id>', methods=['GET','POST'])
def MarkAsIncomplete(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	todo.complete = False
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/status/<id>', methods=['GET','POST'])
def status(id):
	print('hi')
	todo = Todo.query.filter_by(id=int(id)).first()
	if todo.complete:
		return 'Completed'
	else:
		return 'Not Completed'


if __name__ == '__main__':
	app.run(debug=True)
