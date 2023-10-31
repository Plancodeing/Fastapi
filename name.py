from fastapi import FastAPI, HTTPException


app = FastAPI()

# Connect to MongoDB


@app.get("/name")
def name():
   return "hi"
    
6379121215
9444488370
    


    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.199.65", port=8000)