# 1. Library imports
from  app.Diabetes_Inputs import user_input
from fastapi import FastAPI, Form
import numpy as np

import pandas as pd
from route.user import user
import uvicorn



app = FastAPI()
app.include_router(user)




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

    
#uvicorn indexapp:app --reload