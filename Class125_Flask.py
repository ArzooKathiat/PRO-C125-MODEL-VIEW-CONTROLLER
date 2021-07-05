from flask import Flask,jsonify,request
from Class125_Prediction import get_prediction

app = Flask(__name__)

@app.route("/")
def home():
    print("This is a home page!")

@app.route("/pred-digit",methods=['POST'])
def predict_data():
    image = request.files.get("digit")
    prediction = get_prediction(image)
    return jsonify({
        "prediction":prediction
    }),200

if __name__ =='__main__':
    app.run(debug=True)


