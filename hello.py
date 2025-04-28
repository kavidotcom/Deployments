import numpy as np
import pandas as pd
import pickle
from flask import Flask, request


with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

print(model.intercept_)

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to prediction of Loan !!!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                color: #343a40;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #007bff;
            }
            p {
                font-size: 18px;
            }
            .button {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 16px;
                color: #fff;
                background-color: #28a745;
                border: none;
                border-radius: 5px;
                text-decoration: none;
            }
            .button:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to prediction of Loan !!!</h1>
        <p>Your one-stop shop for the world class predictions.</p>
        <a href="#" class="button">Explore Our Products</a>
    </body>
    </html>
    """

@app.route('/predict', methods = ['POST'])
def predict():
    loan_req = request.get_json()
	
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    if loan_req['Credit_History'] == "Uncleared Debts":
        Credit_History = 0	
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']

    LoanAmount = loan_req['LoanAmount']

    x = [[Gender, Married, LoanAmount, ApplicantIncome, Credit_History]]

    clf = model.predict(x)
    if clf[0] == 1:
        prediction = "Loan Approved"
    else:
        prediction = "Loan Not Approved"

    return {'prediction of the model': prediction}

