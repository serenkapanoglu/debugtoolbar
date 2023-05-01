from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension



app=Flask(__name__)
app.config['SECRET_KEY']='abc123'
app.debug=True


toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    session['count'] = session.get('count',0)+1
    
    return render_template("index.html")

@app.route('/fav-color', methods=['GET', 'POST'])
def fav_color():
    fav_color = request.form.get('color')
    return render_template("color.html", fav_color=fav_color)

@app.route('/redirect-me')
def redirect_me():
    return redirect('/')
    