from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Default route
def read_root():
    return {"message": "Weather Assistant API is running"}

@app.get("/weather/{city}")  # Weather route
def get_weather(city: str):
    return {"city": city, "weather": "Sunny"}



