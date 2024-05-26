from fastapi import FastAPI, HTTPException
from model.tables import User, Employer, JobApplication, JobPosting, Login
import operations
from Authentication import *
from Authentication.encoding_decoding_jwt import *

app = FastAPI()

"""This is for CRUD Operations for USER Table"""


@app.post("/users/signup")
def create_user(user: User):
    res = operations.create_user(user)
    
    return res

@app.post("/users/login")
def user_login(user:Login):
    if operations.verify_user(user.email, user.password):
        return encode_jwt(user.email, user.password)
    else:
        return "Invalid Login Details! Please try again with correct credentials."

@app.get("/users/get")
def get_user(user_id: int):
    res = operations.get_user(user_id)
    
    return res

@app.put("/users/update")
def update_user(user_id: int, user: User):
    res = operations.update_user(user_id, user)
    
    return res

@app.delete("/users/delete")
def delete_user(user_id: int):
    res = operations.delete_user(user_id)
    
    return res


"""This is for CRUD Operations for Employee Table"""


@app.post("/employers/signup")
def create_employer(employer: Employer):
    res = operations.create_employer(employer)
    
    return res

@app.post("/employers/login")
def employer_login(user:Login):
    if operations.verify_employer(user.email, user.password):
        return encode_jwt(user.email, user.password)
    else:
        return "Invalid Login Details! Please try again with correct credentials."

@app.get("/employers/get")
def get_employeer(emp_id: int):
    res = operations.employer_details(emp_id)
    
    return res

@app.put("/employers/update")
def update_employer(emp_id: int, employer: Employer):
    res = operations.employer_update(emp_id, employer)
    
    return res

@app.delete("/employees/delete")
def delete_employer(emp_id: int):
    res = operations.employer_delete(emp_id)

    return res


"""This is for CRUD Operations for JobPosting"""


@app.post("/job_postings/create")
def create_job_posting(job_posting: JobPosting):
    res = operations.create_job_posting(job_posting)
    
    return res

@app.get("/job_postings/get")
def get_job_posting(job_id: int):
    res = operations.job_posting_details(job_id)
    
    return res

@app.put("/job_postings/update")
def update_job_posting(job_id: int, job_posting: JobPosting):
    res = operations.update_job_posting(job_id, job_posting)
    
    return res

@app.delete("/job_postings/delete")
def delete_job_posting(job_id: int):
    res = operations.delete_job_posting(job_id)
    
    return res


"""This is for CRUD Operations for JobApplication"""


@app.post("/job_applications/create")
def create_job_application(job_application: JobApplication):
    res = operations.create_job_application(job_application)
    
    return res

@app.get("/job_applications/get")
def get_job_application(job_id: int):
    res = operations.get_job_application(job_id)
    
    return res

@app.put("/job_applications/update")
def update_job_application(job_id: int, job_application: JobApplication):
    res = operations.update_job_application(job_id, job_application)
    
    return res

@app.delete("/job_applications/delete")
def delete_job_application(job_id: int):
    res = operations.delete_job_application(job_id)
    
    return res