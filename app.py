from email.mime import image
from flask import Flask,jsonify,request
from classifier import get_prediction
app=Flask(__name__)
@app.route('/')
def index():
    return "Welcome to our homepage for prediction"

@app.route("/predict-digit",methods=["POST"])
def predict_data():
    image=request.files.get("digit")
    prediction=get_prediction(image)
    return jsonify({
        "prediction":prediction  
    }),200

if __name__=="__main__":
    app.run(debug=True,port=8000)
