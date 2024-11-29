from fastapi import APIRouter
import json
from datetime import datetime, timedelta

router = APIRouter(tags=["Get new cve"])

@router.get("/get/")
def getting(key: str):
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        output = []
        value = content.get("vulnerabilities")
        for cve in value:
            if key in str(cve):
                output.append(cve)
        return output