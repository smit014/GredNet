from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.functions.user.user import get_current_user
from src.resource.admin.schema import DataEntryRequest
from src.functions.admin.admin import add_data_entry
from database.database import Sessionlocal

# Define the router
data_router = APIRouter()


# Dependency to get database session
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


@data_router.post("/admin/add-data", status_code=201)
def add_data_api(
    data: DataEntryRequest,
    current_user: Annotated[dict, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    """
    API endpoint to add data to the `datasources` table by admin.
    """
    try:
        breakpoint()
        response = add_data_entry(data.model_dump(), current_user, db)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Unexpected error: {str(e)}",
                "data": {},
            },
        )
