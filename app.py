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

@app.route('/complete/<id>', methods=['GET'])
def complete(id):

	todo = Todo.query.filter_by(id=int(id)).delete()
#	todo.complete = True
	db.session.commit()

	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
