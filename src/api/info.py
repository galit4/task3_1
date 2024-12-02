from fastapi import APIRouter

#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["Info"])

#вказуєм ендпоінт в декораторі, та ретюрним інфу у функції
@router.get("/info")
def info_print():
    return {"Author": "Yurchyshyn Dmytro", 
            "ProgramDescription":"Simple FastApi example"}
