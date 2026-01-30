
from fastapi import FastAPI
from app.api import health, finance, auth
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.api import upload,gst, banking
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Financial Health Assessment Tool", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(finance.router, prefix="/finance", tags=["Finance"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(gst.router)
app.include_router(banking.router)
