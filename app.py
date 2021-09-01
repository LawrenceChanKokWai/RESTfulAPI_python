from os import name
from typing import ItemsView
from flask import Flask, jsonify

app = Flask(__name__)   #created Flask using a unique name

# @app.route('/') # create the route 'HOME'

#created a function home, and returns a string to the browser
# def home():
#     return "Hello, Lawrence"

# We as the server
# POST - receive data
# GET - send data back

#Create a JSON, dictionary
stores = [
    {
        'name': 'SingTel',
        'items': [
            {
                'name': 'IPhone X',
                'price': 560.65
            }
        ]
    }
]

# TODO: creating application end points
# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')  #By default, methods are GET
def get_store(name):
    pass

# GET /store: http://127.0.0.1:5000/store
# jsonify converts the list into a JSON.
# Above stores is defined as a list. JSON requires a dictionary.
#Solution: converting the stores list 'stores' as a key, that holds list of stores {'stores': stores}
@app.route('/store')    #By default, methods are GET
def get_stores():
    return jsonify({'stores': stores})  #

# POST /store/<string:name>/item {name: , price: }
@app.route('/store/<string:name>/item', methods=['POST'])
def post_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(port=5000)  #app run the homepage on localport 5000