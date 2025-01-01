from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from src.resource.user.model import User
from src.resource.admin.model import Data
from datetime import datetime
import json


def add_data_entry(data_details: dict, cur_user: dict, db: Session):
    """
    Function to add a new entry to the `datasources` table.
    Args:
        data_details (dict): Contains `spid_no`, `name`, `phone_no`, `email`.
        db (Session): Database session object.
    Returns:
        JSONResponse: Success or failure response.
    """
    try:
        # parsed_data = json.loads(user.body.decode("utf-8"))
        data = cur_user.get("data")
        user = data.get("user")
        user_id = user.get("id")
        user_role = user.get("role")
        admin = (
            db.query(User).filter(User.id == user_id, User.role == user_role).first()
        )

        if not admin:
            return JSONResponse(
                status_code=403,
                content={
                    "status": False,
                    "code": 403,
                    "message": "you are not allowed to create a new entry.",
                    "data": {},
                },
            )

        # Check if SPID or email already exists
        existing_data = (
            db.query(Data)
            .filter(
                (Data.spid_no == data_details["spid_no"])
                | (Data.email == data_details["email"])
            )
            .first()
        )

        if existing_data:
            return JSONResponse(
                status_code=400,
                content={
                    "status": False,
                    "code": 400,
                    "message": "SPID number or email already exists in the database.",
                    "data": {},
                },
            )

        # Add the new data entry
        new_data = Data(
            spid_no=data_details["spid_no"],
            name=data_details["name"],
            phone_no=data_details["phone_no"],
            email=data_details["email"],
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        db.add(new_data)
        db.commit()

        return JSONResponse(
            status_code=201,
            content={
                "status": True,
                "code": 201,
                "message": "Data entry added successfully.",
                "data": {
                    "user": {
                        "spid_no": data_details["spid_no"],
                        "name": data_details["name"],
                        "email": data_details["email"],
                        "phone_no": data_details["phone_no"],
                    }
                },
            },
        )

    except SQLAlchemyError as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Database error: {str(e)}",
                "data": {},
            },
        )
