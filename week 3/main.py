from fastapi import FastAPI
from models.user import UserData
app = FastAPI()
userData =[]

@app.post("/save_date_of_birth")
def save_data(data: UserData):
    print(data)
    userData.append(data)
    print(userData)
    return {"user_data":userData}