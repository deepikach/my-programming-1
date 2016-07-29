from flask import Flask, render_template, request, flash
from fna import *

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/fieldna', methods = ['GET', 'POST'])
def fieldnonadmin():
   form = fieldna()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('task.html', form = form)
      else:
         return render_template('success.html')
      
   return render_template('task.html', form = form)

#@app.route('/contact/user', methods=['GET','POST'])
#@app.route('/user', methods = ['GET', 'POST'])




if __name__ == '__main__':
   app.run(debug = True)