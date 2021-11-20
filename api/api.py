from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        'name':'OH, not you again...'
    }



if __name__=='__name__':
    app.run(debug=True)