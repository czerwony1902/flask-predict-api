from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."}), 400

    total = num1 + num2
    prediction = 1 if total > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2,
            "sum": total
        }
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
