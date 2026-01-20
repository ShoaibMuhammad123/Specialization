## PUT and DELETE-->HTTP VERB
## Working with api-->json

from flask import Flask,jsonify,request

app = Flask(__name__)

## Initial data in my to do list

# Here the data can come from any data bases mysql,mongodb etc as example we taking only key value pairs
items = [
    {'id':1,'name':'Item 1 shoaib','description':'This is item 1'},
    {'id':2,'name':'Item 2','description':'This is item 2'},
    {'id':2,'name':'Item 2','description':'This is item 2'},
]

@app.route('/')
def home():
    return 'Welcome to the sample to Do list APP'


## To retrieve all the information we use GET method
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## GET request: --> get item based on some id
@app.route('/items/<int:item_id>',methods=['GET'])      # variable rule
def get_item(item_id):
    # return items[item_id]
    item = next((item for item in items if item['id']==item_id),None) # it becomes an iterable
    if item is None:
        return jsonify({'error':'Item not found'})
    return jsonify(item)

## Post request --> Create a new tasks
@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'name is required'}), 400

    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }

    items.append(new_item)
    return jsonify(new_item)

## PUT : Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

## DELETE
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items 
    items = [item for item in items if item['id'] !=item_id]
    return jsonify({'result':'Item deleted'})


if __name__ == '__main__':
    app.run(debug=True)