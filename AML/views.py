"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from AML import app
from AML.process import data

@app.route('/')
def home_page():
    return render_template(
        'home/home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/file', methods = ["POST"])
def file():
    #C:\Users\iad7kor\Desktop\sasi\repos\Automate-ML-Modeling\Demo Datasets\Fish-1.csv
    path = request.form
    cols = data.get_cols(path["file"])
    return render_template('home/model_details.html',
                                   title='Home Page',
                                    year=datetime.now().year,
                                    cols = cols,
                                    path = path
                                )

@app.route('/details', methods = ["POST"])
def details():
    data = dict(request.form)
    if(data["type"] == "Classification"):
        metrix = data.classifier(data["label"])
    elif(data["type"] == "Regression"):
        metrix = data.regressor(data["label"])
    return metrix



@app.route('/test_graph')
def chartTest():
    lnprice=np.log(price)
    plt.plot(lnprice)
    return render_template('untitled1.html', name = plt.show())


@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
