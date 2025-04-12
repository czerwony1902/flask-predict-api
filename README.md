readme = """
# Predict API

## Endpoint:
`GET /api/v1.0/predict?num1=1.2&num2=4.7`

## Model:
- Jeśli suma podanych liczb > 5.8 → predykcja = 1
- W przeciwnym razie → predykcja = 0

## Uruchomienie w Dockerze

```bash
docker build -t flask-predict-api .
docker run -p 5000:5000 flask-predict-api
# flask-predict-api
# flask-predict-api
