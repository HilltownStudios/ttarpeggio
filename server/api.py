from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Optional
import uuid, PyPDF2

app = FastAPI()

def get_current_user():
    return None

class File(BaseModel):
    pass

# List files
@app.get("/files", dependencies=[Depends(get_current_user)])
async def get_files():
    pass

# Upload one or more files
@app.post("/files", dependencies=[Depends(get_current_user)])
async def post_files():
    pass

# Get file by ID
@app.get("/files/{file_id}", dependencies=[Depends(get_current_user)])
async def get_file(file_id: str):
    pass

# Update a file by ID
@app.put("/files/{file_id}", dependencies=[Depends(get_current_user)])
async def put_file(file_id: str):
    pass

# Delete a file by ID
@app.delete("/files/{file_id}", dependencies=[Depends(get_current_user)])
async def delete_file(file_id: str):
    pass

