
from flask import Flask,render_template,url_for,request, json
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

app = Flask(__name__)


@app.route('/predict',methods=['POST'])
def predict():
    clf = pickle.load(open('classification.model', 'rb'))
    cv = pickle.load(open('vectorizer.pickle', 'rb'))
    data = request.json['data']
    print (data)
    vect = cv.transform([data]).toarray()
    my_prediction = clf.predict(vect)
    print (my_prediction)
    return json.jsonify(
        predicted_results=str(my_prediction[0])
        )


if __name__ == '__main__':
    app.run(debug=True)