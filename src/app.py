from flask import Flask, redirect, url_for, render_template
from pymongo import MongoClient
import crud
import algo

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017", 27017)
db = client.tododb
col = db.todo_collection


@app.route('/mock')
def mock():
    rand_item = crud.pick_rand()
    item_doc = {
        'id': rand_item['id'],
        'offering': rand_item['offering'],
        'seeking': rand_item['seeking']
    }
    col.insert_one(item_doc)
    return redirect(url_for('index'))


@app.route('/remove')
def remove():
    col.delete_many({})
    return redirect(url_for('index'))


@app.route('/match')
def match():
    algo.match()
    return redirect(url_for('index'))


@app.route('/')
def index():
    _items = col.find()
    items = [item for item in _items]
    return render_template('index.html', items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
