#from datetime import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)
#bookmarks = []
#app.config['SECRET_KEY'] = '\xc7\xdf\xf9\xb3\xe5\xed\x9b\xaa\xe9\xdbgan\xb9\x197\xc9\xe4\x89JeL|4'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)