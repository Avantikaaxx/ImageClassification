from flask import Flask, render_template, request
from predict_main import pred_image


import os 

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def upload_f():
    return render_template('home_page.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        
        return str(pred_image(f.filename))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host= '0.0.0.0', port = port)
