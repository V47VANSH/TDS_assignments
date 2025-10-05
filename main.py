from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import numpy as np
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_methods=["*"],  # allow POST + OPTIONS
    allow_headers=["*"],
)

cwd = os.getcwd()
json_path = os.path.join(cwd, "lat.json")
with open(json_path) as f:
    telemetry_data = json.load(f)

class TelemetryRequest(BaseModel):
    regions: List[str]
    threshold_ms: int

@app.options("/telemetry")
async def preflight(request: Request):
    """
    Explicitly handle OPTIONS requests for CORS preflight
    """
    return {"status": "ok"}

@app.post("/telemetry")
async def telemetry(req: TelemetryRequest):
    response = {}
    for region in req.regions:
        region_records = [r for r in telemetry_data if r['region'] == region]
        if not region_records:
            continue
        latencies = [r['latency_ms'] for r in region_records]
        uptimes = [r['uptime_pct'] for r in region_records]
        response[region] = {
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime": round(float(np.mean(uptimes)), 4),
            "breaches": int(sum(1 for l in latencies if l > req.threshold_ms))
        }
    return response
