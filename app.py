from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
import sys

pathway = sys.argv[1]

app = Flask(__name__)

print('sqlite:///'+ pathway + '/todo.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ pathway + '/todo.db' 



db = SQLAlchemy(app) 

usern = ""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	use = db.Column(db.String(200))
	text = db.Column(db.String(200))
	complete = db.Column(db.String(200))

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def login():
	global usern
	usern = ""
	return render_template('login.html')

@app.route('/logout', methods=['GET','POST'])
def logout():
	global usern
	usern = ""
	return render_template('login.html')

@app.route('/checkusername', methods=['GET', 'POST'])
def checkusername():
	global usern
	usern = request.form['username']
	exists = db.session.query(User).filter(User.username == usern).all()
	if exists:
		return index()
	else:
		return render_template('login.html')

@app.route('/makeusername', methods=['GET', 'POST'])
def makeusername():
	global usern
	usern = request.form['newname']
	newacc = User(username=usern)
	db.session.add(newacc)
	db.session.commit()
	return index()


@app.route('/index', methods=['GET', 'POST'])
def index():
	todos = db.session.query(Todo).filter(Todo.use == usern).all()
	return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
	todo = Todo(use=usern, text=request.form['todoitem'], complete='TODO')
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
	todo.complete = 'DONE'
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/MarkAsIncomplete/<id>', methods=['GET','POST'])
def MarkAsIncomplete(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	todo.complete = 'TODO'
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
