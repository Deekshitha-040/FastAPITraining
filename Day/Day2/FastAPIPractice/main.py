from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"page": "Home!"}
@app.get("/about")
def about():
    return {"page": "About!","author": "Dexter"}
@app.get("/health")   
def health():
    return {"status": "Healthy!"}  
#POST request
@app.post("/create")
def create_something():
    return {"message": "Something created!"}
#path parameter
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","USN":usn} 
      
#path parameter with type hint
@app.get("/candidate/{rollno}")
def get_candidate(rollno: int):
    return {"Result":"Distinction","Roll No":rollno, "Type": type(rollno)}

#Pydantic model
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool=True
@app.post("/item")
def create_item(item: Item):
    return {"received": item, "price": item.price*1.18} 
       
