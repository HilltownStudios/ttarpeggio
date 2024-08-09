from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Optional
import uuid
import PyPDF2

app = FastAPI()


def get_current_user():
    return None


# Files
class RPGFile(BaseModel):
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


# Records
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


# Configurations
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


# users
class User(BaseModel):
    pass


# List and Search users
@app.get("/users", dependencies=[Depends(get_current_user)])
async def get_users():
    pass


# Create users
@app.post("/users", dependencies=[Depends(get_current_user)])
async def post_users():
    pass


# Read a user
@app.get("/users/{user_id}", dependencies=[Depends(get_current_user)])
async def get_user(user_id: str):
    pass


# Update a user
@app.put("/users/{user_id}", dependencies=[Depends(get_current_user)])
async def put_user(user_id: str):
    pass


# Delete a userj
@app.delete("/users/{user_id}", dependencies=[Depends(get_current_user)])
async def delete_user(user_id: str):
    pass


# roles
class Role(BaseModel):
    pass


# List and Search roles
@app.get("/roles", dependencies=[Depends(get_current_user)])
async def get_roles():
    pass


# Create roles
@app.post("/roles", dependencies=[Depends(get_current_user)])
async def post_roles():
    pass


# Read a user
@app.get("/roles/{role_id}", dependencies=[Depends(get_current_user)])
async def get_role(role_id: str):
    pass


# Update a user
@app.put("/roles/{role_id}", dependencies=[Depends(get_current_user)])
async def put_role(role_id: str):
    pass


# Delete a userj
@app.delete("/roles/{role_id}", dependencies=[Depends(get_current_user)])
async def delete_role(role_id: str):
    pass


# permissions
class Permission(BaseModel):
    pass


# List and Search permissions
@app.get("/permissions", dependencies=[Depends(get_current_user)])
async def get_permissions():
    pass


# Create permissions
@app.post("/permissions", dependencies=[Depends(get_current_user)])
async def post_permissions():
    pass


# Read a user
@app.get("/permissions/{permission_id}", dependencies=[Depends(get_current_user)])
async def get_permission(permission_id: str):
    pass


# Update a user
@app.put("/permissions/{permission_id}", dependencies=[Depends(get_current_user)])
async def put_permission(permission_id: str):
    pass


# Delete a userj
@app.delete("/permissions/{permission_id}", dependencies=[Depends(get_current_user)])
async def delete_permission(permission_id: str):
    pass
