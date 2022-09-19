#from fastapi import FastAPI 
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database


app = FastAPI()

#@app.get("/")
#async def root():
#    return {"message":"Hello SYKE!"}

database = Database("sqlite:///tiha.db")


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get("/test/{id}")
async def fetch_data(id):
    print(id)
    query = "SELECT * FROM tiha WHERE id={}".format(str(id))
    results = await database.fetch_all(query=query)

    return  results

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}