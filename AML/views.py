"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from AML import app
from AML.process import data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
                                   title='Selection',
                                    year=datetime.now().year,
                                    cols = cols,
                                )

@app.route('/details', methods = ["POST"])
def details():
    values = dict(request.form)
    metrix = ""
    if(values["model"] == "Classification"):
        col_names = ["train_accuracy", "test_accuracy"]
        if(values["type"] == "Default"):
            metrix = data.default_classifier_models(values["label"])
            metrix.sort(key=lambda x: x[2])
            metrix.reverse()
        elif(values["type"] == "All_Models"):
            metrix = data.all_classifier_models(values["label"])
            metrix.sort(key=lambda x: x[2])
            metrix.reverse()
    elif(values["model"] == "Regression"):
        col_names = ["R_SQUARE", "RMSE"]
        if(values["type"] == "Default"):
            metrix = data.default_regressor_models(values["label"])
            metrix.sort(key=lambda x: x[1])
            metrix.reverse()
        elif(values["type"] == "All_Models"):
            metrix = data.all_regressor_models(values["label"])
            metrix.sort(key=lambda x: x[1])
            metrix.reverse()
    else:
        error = "error"
    return render_template("home/display_results.html",
                           title='Model results',
                            year=datetime.now().year,
                            metrix = metrix,
                            col_names = col_names
                           )

@app.route('/graph')
def graph():
    fig = Figure()
    df = pd.read_csv("C:/Users/iad7kor/Desktop/sasi/repos/Automate-ML-Modeling/Demo Datasets/Fish-1.csv")
    sns.countplot('Species',data=df)
    sns.savefig('./static/images/new_plot.png')
    return render_template('graphs/g1.html', 
                           name = 'new_plot', 
                           url ='/static/images/new_plot.png')
#render_template('graphs/g1.html', name = plt.show())


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
