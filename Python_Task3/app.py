from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('energy_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Route to display the input form
@app.route('/')
def home():
    return render_template('index.html')

# Route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    square_footage = float(request.form['square_footage'])
    num_occupants = int(request.form['num_occupants'])
    appliances_used = int(request.form['appliances_used'])
    avg_temp = float(request.form['avg_temp'])
    building_type = int(request.form['building_type'])  # Encoded value for Building Type
    day_of_week = int(request.form['day_of_week'])  # Encoded value for Day of Week
    
    # Prepare the input array (same order as training data)
    input_data = np.array([[square_footage, num_occupants, appliances_used, avg_temp, building_type, day_of_week]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the result to the user
    return render_template('index.html', prediction_text=f'Predicted Energy Consumption: {prediction[0]:.2f} kWh')

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)
