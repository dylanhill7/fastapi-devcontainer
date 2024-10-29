#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@api.get("/customer/{idx}")
def get_customer(idx: int):
    # Read the data from the CSV file
    df = pd.read_csv("../customers.csv")
    # Filter the data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@api.post("/get_body")
async def get_body(request: Request):
    return await request.json()

@api.post("/mapit")
async def map_request(request: Request):
    response = await request.json()
    geo = response.get("geo")
    url = "https://maps.google.com/?q={geo}".format(geo=geo)
    return {"gmaps_url": url}
