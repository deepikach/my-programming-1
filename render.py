from flask import Flask
app = Flask(__name__)
@app.route('/')
def h():
    return render_template("index.html)
app.run()    
