from flask import Flask

app = Flask('__main__')


#GET METHOD
@app.route('/getmethod', methods=['GET'])
def go_home():
    return 'Este es un metodo GET'

#POST METHOD
# localhost:5000/users
@app.route('/postmethod', methods=['POST'])
def post_data():
    data= request.json
    print(data)
    return data;

#PATCH METHOD
@app.route('/devices', methods=['PATCH'])
def save_device():
    device = request.json
    return device

if __name__ == "__main__":
    app.run(debug=True, port=5000)