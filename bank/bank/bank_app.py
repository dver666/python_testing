import sys
sys.path.append('/home/diver/www_python_testing/bank')
sys.path.append('/home/diver/www_python_testing/bank/test')
sys.path.append('/home/diver/www_python_testing/bank/test/bdd')
sys.path.append('/home/diver/www_python_testing/bank/test/bdd/features')
sys.path.append('/home/diver/www_python_testing/bank/test/bdd/steps')
sys.path.append('/home/diver/www_python_testing/bank/bank')
sys.path.append('/home/diver/www_python_testing/bank/templates')

from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
