from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import joblib
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Subscription_Length_Months = int(request.form['Subscription_Length_Months'])
        Monthly_Bill = float(request.form['Monthly_Bill'])
        #NumOfProducts = int(request.form['NumOfProducts'])
        Total_Usage_GB = int(request.form['Total_Usage_GB'])
#         Location_Chicago = request.form['Location_Chicago']
#         if(Location_Chicago == 'Chicago'):
#             Location_Chicago = 1
#             Location_Houston= 0
#             Location_New York = 0
#             Location_Miami = 0
#             Location_Los Angeles = 0
                
#         elif(Location_Chicago == 'Houston'):
#             Location_Chicago = 0
#             Location_Houston= 1
#             Location_New York = 0
#             Location_Miami = 0
#             Location_Los Angeles = 0
            
#         elif(Location_Chicago == 'New York'):
#             Location_Chicago = 0
#             Location_Houston= 0
#             Location_New York = 1
#             Location_Miami = 0
#             Location_Los Angeles = 0
            
#         elif(Location_Chicago == 'Miami'):
#             Location_Chicago = 0
#             Location_Houston= 0
#             Location_New York = 0
#             Location_Miami = 1
#             Location_Los Angeles = 0
            
#         else:
#             Location_Chicago = 0
#             Location_Houston= 0
#             Location_New York = 0
#             Location_Miami = 0
#             Location_Los Angeles = 1
            
#         Gender_Male = request.form['Gender_Male']
#         if(Gender_Male == 'Male'):
#             Gender_Male = 1
#             Gender_Female = 0
#         else:
#             Gender_Male = 0
#             Gender_Female = 1
        prediction = model.predict([[ Age, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]])
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will leave the bank")
        else:
             return render_template('index.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True)
