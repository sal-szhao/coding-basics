from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_admin():
    return {"admin": "admin user"}