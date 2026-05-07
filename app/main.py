from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from . import models, schemas, crud, database, utils

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

logging.basicConfig(level=logging.INFO)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses", response_model=schemas.AddressResponse)
def create(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logging.info("Creating address")
    return crud.create_address(db, address)


@app.get("/addresses", response_model=list[schemas.AddressResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_addresses(db)


@app.put("/addresses/{address_id}")
def update(address_id: int, updated: schemas.AddressUpdate, db: Session = Depends(get_db)):
    result = crud.update_address(db, address_id, updated)
    if not result:
        raise HTTPException(status_code=404, detail="Address not found")
    return result


@app.delete("/addresses/{address_id}")
def delete(address_id: int, db: Session = Depends(get_db)):
    result = crud.delete_address(db, address_id)
    if not result:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Deleted successfully"}


@app.get("/addresses/nearby")
def get_nearby(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db)

    result = []
    for addr in addresses:
        dist = utils.calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if dist <= distance:
            result.append(addr)

    return result