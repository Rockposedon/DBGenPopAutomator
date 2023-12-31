import mysql.connector
from faker import Faker
import random

def create_car_model(db):

    cursor = db.cursor()

    # List of predefined vehicle models
    vehicle_models = [
        "Toyota Corolla", "Honda Civic", "Ford Mustang", "Chevrolet Camaro", "Volkswagen Golf",
        "BMW 3 Series", "Nissan Altima", "Mercedes-Benz C-Class", "Jeep Wrangler", "Subaru Outback",
        "Tesla Model S", "Kia Sportage", "Hyundai Elantra", "Mazda CX-5", "Audi A4"
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarModel (
            ModelID INT AUTO_INCREMENT PRIMARY KEY,
            ModelName VARCHAR(100),
            CategoryID INT,
            EngineID INT,
            ModelSpecifications TEXT,
            FOREIGN KEY (CategoryID) REFERENCES CarCategory(CategoryID),
            FOREIGN KEY (EngineID) REFERENCES CarEngine(EngineID)
        )
    """)

    car_models = []
    fake = Faker()
    for model_name in vehicle_models:
        car_models.append((None, model_name, random.randint(1, 5), random.randint(1, 4), fake.paragraph()))

    insert_query = "INSERT INTO CarModel (ModelID, ModelName, CategoryID, EngineID, ModelSpecifications) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, car_models)

    db.commit()
    cursor.close()
    

    print("CarModel table created and populated successfully.")
