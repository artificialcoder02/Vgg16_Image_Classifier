import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Load the pre-trained model
model = tf.keras.models.load_model(app.config['cats_and_dogs\cats_and_dogs\model_vgg16.h5'])

# Define a helper function to check if file extensions are allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the predict route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Check if the request contains a file
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # Check if the file is allowed
        if not allowed_file(file.filename):
            return redirect(request.url)

        # Save the file to disk
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))

        # Load the saved file as a TensorFlow image tensor
        img = tf.keras.preprocessing.image.load_img(
            os.path.join('uploads', filename),
            target_size=(150, 150)
        )
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Add batch dimension

        # Make a prediction using the loaded model
        prediction = model.predict(img_array)
        if prediction[0][0] > 0.5:
            result = 'cat'
        else:
            result = 'dog'

        # Return the prediction result
        return render_template('result.html', result=result)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
