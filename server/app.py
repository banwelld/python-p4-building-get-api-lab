#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

import ipdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakery_lst = [b.to_dict() for b in Bakery.query.all()]
    return make_response(bakery_lst, 200)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter_by(id=id).first()
    return make_response(bakery.to_dict(), 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bg_lst = [b.to_dict() for b in BakedGood.query.all()]
    sorted_bg_lst = sorted(bg_lst, key=lambda item: item["price"], reverse=True)
    return make_response(sorted_bg_lst, 200)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    bg_lst = [b.to_dict() for b in BakedGood.query.all()]
    max_price_bg = max(bg_lst, key=lambda item: item["price"])
    return make_response(max_price_bg, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
