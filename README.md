# admissions_predictor

A data science project to predict admission probability of a student based on 7 factors : 
1. GRE score (out of 340)
2. TOEFL score (out of 120)
3. University rating (out of 5)
4. Statement of Purpose score (out of 5)
5. Letter of Recommendation score (out of 5)
6. CGPA (out of 10)
7. Researce experience (0 for NO, 1 for YES)

Linear Regression, Decision Tree, Random Forest and Neural Network were some of the tested models after data cleaning and extensive graphic analysis to extract insights out of the data. Random Forest gave the best overall accuracy, hence was the deployment choice. Check "admissions_predict.ipynb" for more details.

## To serve the model as a REST webservice locally
1. Run `pip install -r requirements.txt` to install dependencies.
2. Run `python local_flask.py` to wrap the inference logic in a flask server to serve the model as a REST webservice.
3. Run the below sample command in terminal to query the server to get 77% as output:
```
curl -X POST localhost:6969 -H 'Content-Type: application/json' -d '[323,107,4.3,4,3.9,8.8,1]'
```

## To use the REST API deployed on heroku
NOTE: Code used for heroku deployment can be found in "heroku-app" directory.
1. Run the below sample command in terminal to query the heroku-app to get 77% as output:
```
curl -X POST http://admission-predict-app.herokuapp.com/ -H 'Content-Type: application/json' -d '[323,107,4.3,4,3.9,8.8,1]'
```
