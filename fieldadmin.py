from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class fielda(Form):
   name = TextField("Assigned task to non admin",[validators.Required("Please enter name")])
   aname = TextField("Field To be survey",[validators.Required("Please enter assingedfield")])
   tpname = TextField("Id's of non admin'",[validators.Required("Please enter id")])
   mname= IntegerField("Total surveys by non admin",[validators.Required("Please enter the survey")])
   
   submit = SubmitField("Submit")

class taskgiven(Form):
     name = IntegerField("Employee id",[validators.Required("Please enter employee id")])
     aname = TextField("Tasks to be done",[validators.Required("Please enter task")])
     tpname = TextField("Area to be visited",[validators.Required("Please enter Area")])
     
   
     submit = SubmitField("Submit")
