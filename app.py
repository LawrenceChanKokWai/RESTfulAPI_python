#Flask - Web application framework lib
#jsonify - To convert list into JSON Object
#request - part of flask tool, used in sending request from user
from logging import error
from flask import Flask, jsonify, request

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
# * request.get_jason is the request that had was make to the /store endpoint.
# when the browser sends a request to create a new store which is request_data.
# browser will as well send JSON data.
# create a new store of which is a dictionary, with name: of request data name. etc...
# then stores the request and appending on the new_store, 
# * Important in returning jsonify of new_store. As we are wanting to get dictionary, but fail with getting back a string
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')  #By default, methods are GET
def get_store(name):
    #Iterate over stores
    #if store name matches, return it
    #if no match, return error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message': 'store not found'})

    

# GET /store: http://127.0.0.1:5000/store
# jsonify converts the list into a JSON.
# Above stores is defined as a list. JSON requires a dictionary.
#Solution: converting the stores list 'stores' as a key, that holds list of stores {'stores': stores}
@app.route('/store')    #By default, methods are GET
def get_stores():
    return jsonify({'stores': stores})  #

# POST /store/<string:name>/item {name: , price: }
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})        

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    #Iterate over stores
    #if store name matches, return the store items
    #if no match, return error message
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        return jsonify({'message': 'store item not found'})

app.run(port=5000)  #app run the homepage on localport 5000