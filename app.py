from flask import Flask, render_template,url_for,request,flash
from form import ContactForm

#create flask instance
app = Flask(__name__)
app.config['SECRET_KEY']='private_key'



@app.route('/')
def home():
    return "Wecome to WTForms"

#Create name page
@app.route('/contact',methods=['GET','POST'])
def contact():
    name=None
    form=ContactForm()
    #validate
    if request.method=='POST':
        name=form.name.data
        form.name.data=''
        if form.validate()==False:

            flash("All fields are required")
            return render_template('contact.html',form=form,name=name)
        else:
            return render_template('user.html',name=name)
    return render_template('contact.html',form=form)


@app.errorhandler(404)
def error_handler(error):
    return render_template('404.html')

if __name__=='__main__':
    app.run(debug=True)

