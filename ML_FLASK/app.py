import flask
from flask import render_template
import tensorflow as tf
from tensorflow import keras
import sklearn
import keras

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def main():
    temp = 1
    param_lst = []

    if flask.request.method == 'GET':
        return render_template('mn.html' )
        
    if flask.request.method == 'POST':
        loaded_model = keras.models.load_model("model_mn")
        for i in range(1,13,1): 
			
            
            
            experience = flask.request.form.get(f'experience{i}')
            
            param_lst.append(float(experience))
        
        temp = loaded_model.predict([param_lst])
        return render_template('mn.html', message = temp)

if __name__ == '__main__':
    app.run()