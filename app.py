from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        liczba1 = float(request.args.get('liczba1', 0))
        liczba2 = float(request.args.get('liczba2', 0))
    except ValueError:
        return jsonify({"Błąd": "Źle wprowadzona liczba."}), 400

    suma = liczba1 + liczba2
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "liczba1": liczba1,
            "liczba2": liczba2,
            "suma": suma
        }
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
