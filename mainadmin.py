from flask import Flask, render_template, request, flash
from fieldadmin import *

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/fielda', methods = ['GET', 'POST'])
def fieldadmin():
   form = fielda()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('hfieldadmin.html', form = form)
      else:
         return render_template('success.html')
      
   return render_template('hfieldadmin.html', form = form)

#@app.route('/contact/user', methods=['GET','POST'])
#@app.route('/user', methods = ['GET', 'POST'])

@app.route('/fielda/fieldtask', methods = ['GET', 'POST'])
def fieldtask():
   form = taskgiven()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('hfieldtask.html', form = form)
      else:
         return render_template('success.html')
      
   return render_template('hfieldtask.html', form = form)


if __name__ == '__main__':
   app.run(debug = True)