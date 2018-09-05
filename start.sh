#!/usr/bin/env bash

if command -v python3 &>/dev/null; then
    echo Python 3 is installed
else
    echo Python 3 is not installed
    exit
fi

if command -v pip3 &>/dev/null; then
    echo pip3 is installed
else
    echo pip3 is not installed
    exit
fi

if python3 -c "import flask" &> /dev/null; then
    echo 'Flask is had'
else
    echo 'uh oh'
fi

python3 -c "import flask"
if [ $? -eq 1 ] ; then
	echo 'Must pip3 install Flask'
	exit
fi

python3 -c "import flask_sqlalchemy"
if [ $? -eq 1 ] ; then
	echo 'Must pip3 install flask_sqlalchemy'
	exit
fi

if [ ! -f /home/jon/pracwebdev/ToDoList/app.py ]; then
    echo "app.py not found!"
    exit
else
	echo "app.py exists"
fi

if [ ! -f /home/jon/pracwebdev/ToDoList/todo.db ]; then
    echo "todo.db not found"
    exit
else
	echo "todo.db exists"
fi

if [ ! -f /home/jon/pracwebdev/ToDoList/templates/index.html ]; then
    echo "index.html not found!"
    exit
else
	echo "index.html exists"
fi

if [ ! -f /home/jon/pracwebdev/ToDoList/templates/login.html ]; then
    echo "login.html not found!"
    exit
else
	echo "login.html exists"
fi

python3 app.py