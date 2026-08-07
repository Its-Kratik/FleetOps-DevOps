from fastapi import FastAPI
from app.models.vehicle import Vehicle

app = FastAPI(title="FleetOps API", description="FleetOps DevOps API", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Welcome to FleetOps - CI/CD Success 🚀 And Hinal is pootty"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}    

@app.get("/status")
def status():
    return {"status": "FleetOps API is running smoothly"}


vehicles = [
    {
        "vehicle_id": "RJ14AB1234",
        "driver": "Kratik",
        "speed": 62,
        "status": "Running"
    },
    {
        "vehicle_id": "RJ14CD5678",
        "driver": "Rahul",
        "speed": 0,
        "status": "Stopped"
    }
]

@app.get("/vehicles")
def get_vehicles():
    return vehicles

@app.post("/vehicles")
def create_vehicle(vehicle: Vehicle):
    # Placeholder for creating a new vehicle
    vehicles.append(vehicle.model_dump())
    return {"message": "Vehicle created successfully", "vehicle": vehicle}