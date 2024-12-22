import boto3
import os
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, HTTPException
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

load_dotenv()

# AWS S3 Configuration
s3_bucket_name = "myawsalumnibucket"
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_default_region = os.getenv("AWS_DEFAULT_REGION")

# Initialize S3 Resource
s3 = boto3.resource(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_default_region,
)

# FastAPI App
app = FastAPI(debug=True)

@app.get("/status")
def get_status():
    return {"message": "Hello World!"}


@app.post("/addphotos", status_code=201)
async def add_photos(file: UploadFile):
    try:
        # Upload file to S3
        bucket = s3.Bucket(s3_bucket_name)
        bucket.upload_fileobj(file.file, file.filename)

        # Generate public URL for the uploaded file
        upload_file_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{file.filename}"
        return {"message": "File uploaded successfully", "url": upload_file_url}

    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="AWS credentials not found")
    except PartialCredentialsError:
        raise HTTPException(status_code=500, detail="Incomplete AWS credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")


