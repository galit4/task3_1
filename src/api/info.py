from fastapi import APIRouter

router = APIRouter(tags=["Info"])

@router.get("/info1")
def info_print():
    return {"Author": "Yurchyshyn Dmytro", 
            "ProgramDeskriprtion":"Simple FastApi example"}
