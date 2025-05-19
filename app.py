from flask import Flask, request, jsonify
import joblib
import numpy as np
import traceback

# Cargar el mejor modelo entrenado
model = joblib.load("model_life_expectancy.pkl")

# Inicializar la app Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "API de Predicción de Esperanza de Vida funcionando"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Verificar que la entrada tenga la clave correcta
        if "input" not in data:
            return jsonify({"error": "Falta la clave 'input' en el JSON"}), 400

        input_data = np.array(data["input"]).reshape(1, -1)
        prediction = model.predict(input_data)

        return jsonify({
            "input": data["input"],
            "prediction": float(prediction[0]),
            "modelo": "RandomForestRegressor",
            "estado": "Correcto"
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
