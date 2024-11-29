from fastapi import APIRouter
import json
from datetime import datetime, timedelta



router = APIRouter(tags=["getting all cves from last 5 in records"])

@router.get("/get/all")
def getting():
    with open("/home/dmytro/Desktop/Code/under/task3/src/api/known_exploited_vulnerabilities.json", "r") as file:
        content = json.load(file)
        
        startdate = datetime.now()-timedelta(days=5)
        output = []
        for cve in content["vulnerabilities"]:
            if (cve["dateAdded"] >= str(startdate)):
                output.append(cve)
                if len(output) == 40:
                    break
        return output
    
