from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class fieldna(Form):
   name = TextField("Type of Product",[validators.Required("Please enter Product")])
   aname = TextField("Area",[validators.Required("Please enter Area")])
   tpname = TextField("Survey Time Period",[validators.Required("Please enter Time Period")])
   mname= IntegerField("No of males",[validators.Required("Please enter the field")])
   Fname= IntegerField("No of Females",[validators.Required("Please enter Time field")])
   pname= TextField("Type of Product",[validators.Required("Please enter ")])
   submit = SubmitField("Submit")
