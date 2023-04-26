from flask import Flask,request

database = {'antar': '100', 'kona' : '141'}

# initialize flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to my cute web API'

@app.route('/getdata/', methods=['GET'])
def get_data():
    return database

#api/adddata?user = id
@app.route('/adddata/', methods=['PUT'])
def add_data():
    key, value = list(request.args.items())[0]
    database[key] = value
    return f'{key} added'

# api/deletedata?user = name
@app.route('/deletedata/', methods=['DELETE'])
def delete_data():
    key, value = list(request.args.items())[0]
    if value in database:
        database.pop(value)
        return f'{value} Deleted'
    else:
        return f'this value is not define'



if __name__ == '__main__':
    app.run()