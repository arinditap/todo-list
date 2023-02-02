from flask import render_template, request, redirect, url_for
from app import db
from app import Todo

def home():
    todo_list = Todo.query.all()
    data = transform(todo_list)
    return render_template("base.html", todo_list=todo_list)

def add():
    title = request.form.get("title")
    description = request.form.get("description")
    new_todo = Todo(title=title, description=description, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

def todo_detail(id):
    todo = Todo.query.filter_by(id).first()

def update(id):
    title = request.form.get("title")
    description = request.form.get("description")
    todo = Todo.query.filter_by(id).first()
    todo.title = title
    todo.description = description
    db.session.commit()
    return redirect(url_for("home"))

def delete(id):
    todo = Todo.query.filter_by(id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    data = {
        'id': values.id,
        'title': values.title,
        'description': values.description,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
    }
    return data