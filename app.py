from flask import Flask
from flask import jsonfiy
app = Flask(__name__)

def append(something)
    res = something + ' new'
    return res
    
@app.route('/')
    def hello():
        print("I can make something new")
        return 'I can make something new. Type something at routh: /new'
    
@app.route('/new/<typed>')
    def makeNew
        print(f"Make it new")
        result = append(typed)
        return jsonify(result)
