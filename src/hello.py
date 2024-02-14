from flask import Flask, request, render_template
import pickle as pickle
from pickle import load
import numpy as np
import numpy as numpy
import joblib as joblib
import os
import pickle

print(os.getcwd())

"""model=joblib.load("iris_model_LR.pkl")
data = [[1.0, 2.0, 3.0, 4.0]]
prediction = model.predict(data)
print(prediction)"""

"""app = Flask(__name__)
app.config['TEMPLATES_FOLDER'] = '/workspaces/ML-WEB-APP-USING-FLASK/src/template/index.html'


#model = load(open("/workspaces/ML-WEB-APP-USING-FLASK/models/iris_model_LR.pkl", "rb"))
model = pickle.load(open("/workspaces/ML-WEB-APP-USING-FLASK/models/decision_tree_classifier_default_42.sav", "rb"))
class_dict = {
    "0": "Iris setosa",
    "1": "Iris versicolor",
    "2": "Iris virginica"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        val1 = float(request.form['val1'])
        val2 = float(request.form['val2'])
        val3 = float(request.form['val3'])
        val4 = float(request.form['val4'])
        
        data = [[val1, val2, val3, val4]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template('index.html', prediction=pred_class)

if __name__ == '__main__':
    app.run(debug=True)
"""