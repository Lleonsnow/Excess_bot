from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


api_router = APIRouter()


class AuthData(BaseModel):
    username: str
    password: str


@api_router.get("/")
async def root():
    print("API is working")


@api_router.post("/webhook")
async def webhook(auth_data: AuthData):
    print(auth_data)
    print("Webhook is working")


app = FastAPI()
app.include_router(api_router)
app.add_middleware(CORSMiddleware)
