# Práctica 2 - UTPL APEB1: Predicción de Esperanza de Vida con MLFlow + Flask

Este proyecto consiste en el desarrollo de un modelo de aprendizaje automático para predecir la esperanza de vida a partir de datos de salud y desarrollo. Se hace uso de **MLflow** para gestionar el ciclo de vida del modelo, y **Flask** para exponer el modelo como una API REST lista.

## Contenido del repositorio

- `Life Expectancy Data.csv`: Dataset de esperanza de vida.
- `life_expectancy_mlflow.ipynb`: Notebook con el preprocesamiento, entrenamiento, experimentación y log de modelos usando MLflow.
- `app.py`: API Flask que carga el mejor modelo entrenado y expone un endpoint de predicción.
- `requirements.txt`: Lista de dependencias necesarias para correr el proyecto.
- `model_life_expectancy.pkl`: Modelo final guardado tras evaluar múltiples ejecuciones.

---

## Requisitos

- Python 3.8 o superior
- Entorno virtual (recomendado con conda o venv)
- MLflow ejecutándose en `http://localhost:9090`

---

## Instalación del entorno

```bash
pip install -r requirements.txt
```

---

## Ejecución del entrenamiento y registro con MLflow

1. Inicia el servidor de MLflow (desde otra terminal):

```bash
mlflow ui --port 9090
```

2. Abre y ejecuta el notebook:

```bash
jupyter notebook life_expectancy_mlflow.ipynb
```

3. El notebook entrenará 5 modelos con hiperparámetros aleatorios, registrará métricas en MLflow y guardará el mejor modelo en `model_life_expectancy.pkl`.

---

## Ejecución del servidor Flask

```bash
python app.py
```

## Pruebas

### Prueba con `curl`

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"input\": [0.5, 2000, 0.1, 80.0, 500.0, 60.0, 80.0, 1.5, 80.0, 85.0, 90.0, 0.2, 65.0, 5.5, 70.0, 90.0, 0.5, 85.0, 60.0, 65.0]}"
```

### Prueba con Postman

- Método: `POST`  
- URL: `http://localhost:5000/predict`  
- Headers:  
  - `Content-Type: application/json`  
- Body (raw JSON):

```json
{
  "input": [0.5, 2000, 0.1, 80.0, 500.0, 60.0, 80.0, 1.5, 80.0, 85.0, 90.0, 0.2, 65.0, 5.5, 70.0, 90.0, 0.5, 85.0, 60.0, 65.0]
}
```

---

## Resultados esperados

- RMSE promedio de ~1.6
- R² cercano a 0.97
- Modelo cargado y funcionando correctamente

---

## Autor

Carlos Condor  
Maestría en Inteligencia Artificial  
Universidad Técnica Particular de Loja