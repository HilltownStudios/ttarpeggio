from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Optional
import uuid, PyPDF2

app = FastAPI()

def get_current_user():
    return None

### Files

class File(BaseModel):
    pass

# List and Search Files
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

### Records

class Record(BaseModel):
    pass

# List and Search Records
@app.get("/records", dependencies=[Depends(get_current_user)])
async def get_records():
    pass

# Create Record
@app.post("/records", dependencies=[Depends(get_current_user)])
async def post_records():
    pass

# Read Record
@app.get("/records/{record_id}", dependencies=[Depends(get_current_user)])
async def get_record(record_id: str):
    pass

# Update Record
@app.put("/records/{record_id}", dependencies=[Depends(get_current_user)])
async def put_record(record_id: str):
    pass

# Delete Record
@app.delete("/records/{record_id}", dependencies=[Depends(get_current_user)])
async def delete_record(record_id: str):
    pass

## Configurations

class Configuration(BaseModel):
    pass

# List and Search Configurations
@app.get("/configurations", dependencies=[Depends(get_current_user)])
async def get_configurations():
    pass

# Create Configurations
@app.post("/configurations", dependencies=[Depends(get_current_user)])
async def post_configurations():
    pass

# Read a configuration
@app.get("/configurations/{configuration_id}", dependencies=[Depends(get_current_user)])
async def get_configuration(configuration_id: str):
    pass

# Update a configuration
@app.put("/configurations/{configuration_id}", dependencies=[Depends(get_current_user)])
async def put_configuration(configuration_id: str):
    pass

# Delete a configurationj
@app.delete("/configurations/{configuration_id}", dependencies=[Depends(get_current_user)])
async def delete_configuration(configuration_id: str):
    pass
