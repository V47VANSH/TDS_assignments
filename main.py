from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import numpy as np

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Load telemetry data from cwd
# cwd = os.getcwd()
# json_path = os.path.join(cwd, "lat.json")
# with open(json_path) as f:
telemetry_data = [
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 161.94,
    "uptime_pct": 98.435,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 189.55,
    "uptime_pct": 97.935,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 155.29,
    "uptime_pct": 97.315,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 222.39,
    "uptime_pct": 97.565,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 181.13,
    "uptime_pct": 97.442,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 129.58,
    "uptime_pct": 99.367,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 199.46,
    "uptime_pct": 98.368,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 134.47,
    "uptime_pct": 98.193,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 196.75,
    "uptime_pct": 98.109,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 214.05,
    "uptime_pct": 97.752,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 158.36,
    "uptime_pct": 97.152,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 118.71,
    "uptime_pct": 97.557,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 167.97,
    "uptime_pct": 99.312,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 172.38,
    "uptime_pct": 98.331,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 184.1,
    "uptime_pct": 97.134,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 106.86,
    "uptime_pct": 99.117,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 132.37,
    "uptime_pct": 97.316,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 220.84,
    "uptime_pct": 97.919,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 160.15,
    "uptime_pct": 97.724,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 154.43,
    "uptime_pct": 98.978,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 116.08,
    "uptime_pct": 98.191,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 159.52,
    "uptime_pct": 97.254,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 151.33,
    "uptime_pct": 98.638,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 110.26,
    "uptime_pct": 98.631,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 154.89,
    "uptime_pct": 98.048,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 146.79,
    "uptime_pct": 98.028,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 200.38,
    "uptime_pct": 97.257,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 223.45,
    "uptime_pct": 98.645,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 178.04,
    "uptime_pct": 98.568,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 164.11,
    "uptime_pct": 98.687,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 147.14,
    "uptime_pct": 99.252,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 178.45,
    "uptime_pct": 98.406,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 155.9,
    "uptime_pct": 97.619,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 158.98,
    "uptime_pct": 98.815,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 174.34,
    "uptime_pct": 97.553,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 155.84,
    "uptime_pct": 97.304,
    "timestamp": 20250312
  }
]

# Request body schema
class TelemetryRequest(BaseModel):
    regions: List[str]
    threshold_ms: int

@app.post("/api/telemetry")
async def telemetry(req: TelemetryRequest):
    response = {}
    
    for region in req.regions:
        region_records = [r for r in telemetry_data if r['region'] == region]
        if not region_records:
            continue
        
        latencies = [r['latency_ms'] for r in region_records]
        uptimes = [r['uptime_pct'] for r in region_records]  # updated field name
        
        response[region] = {
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime": round(float(np.mean(uptimes)), 4),
            "breaches": int(sum(1 for l in latencies if l > req.threshold_ms))
        }
    
    return response
