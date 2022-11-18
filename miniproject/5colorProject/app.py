from flask import Flask, jsonify, render_template, request, url_for, redirect
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash,check_password_hash
from bson.json_util import dumps

app = Flask(__name__)

import certifi
from pymongo import MongoClient

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.zi0ui9l.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/color5", methods=["POST"])
def web_color5_post():

    comment_list = list(db.color5.find({}, {'_id': False}))
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    count = len(comment_list) + 1

    doc = {
        'num' : count,
        'name' : name_receive,
        'comment' : comment_receive,
    }
    db.color5.insert_one(doc)

    return jsonify({'msg': '게시글이 등록되었어요'})


@app.route("/color5", methods=["GET"])
def web_color5_get():
    order_list = list(db.color5.find({}, {'_id': False}))

    return jsonify({'orders': order_list})


@app.route("/color5/delete", methods=["DELETE"])
def web_color5_delete():
    num_receive = request.form['num_give']
    db.color5.delete_one({'num':int(num_receive)})
    return jsonify({'msg': '삭제가 완료되었어요'})


@app.route("/color5/deleteAll", methods=["DELETE"])
def web_color5_deleteAll():
    db.color5.delete_many({})
    return jsonify({'msg': '삭제가 완료되었어요'})


@app.route("/color5/edit", methods=["POST"])
def comment_edit():
    num_receive = request.form['num_give']




if __name__ == '__main__':
    app.run('0.0.0.0', port=5050, debug=True)
