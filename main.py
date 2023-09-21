from flask import Flask


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return '200'


@app.route('/user',methods=['GET'])
def user():
    return {'user': 'testuser','email': 'test@gmail.com'}


if __name__ == '__main__':
    app.run(debug=True)