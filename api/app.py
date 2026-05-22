import joblib as jb
import pandas as pd
from fastapi import FastAPI
from typing import Annotated, Literal
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

with open('artifact/model_building/model.pkl', 'rb') as f:
    model = jb.load(f)
    
with open("artifact/data_transformation/preprocessor.pkl", 'rb') as f:
    processor = jb.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'message': 'Hello'}

@app.get("/health")
def health():
    return {"status": "OK"}


class UserInput(BaseModel):
    time_spent_alone: Annotated[float, Field(..., gt=0, description='time spent alone')]
    stage_fear: Annotated[Literal['yes', 'no'], Field(..., description='You have stage fear or not')]
    social_event_attendance: Annotated[float, Field(..., gt=0, description='Social event attendance')]
    going_outside: Annotated[float, Field(..., gt=0, description='Going outside')]
    drained_after_socializing: Annotated[Literal['yes', 'no'], Field(..., description='Have you ever drained after socializing')]
    friends_circle_size: Annotated[float, Field(..., gt=0, description='Friend circle size')]
    post_frequency: Annotated[float, Field(..., gt=0, description='Post Frequency')]


@app.post('/predict')
def prediction(user_data: UserInput):

    input = pd.DataFrame([{
        'time_spent_alone': user_data.time_spent_alone,
        'stage_fear': user_data.stage_fear,
        'social_event_attendance': user_data.social_event_attendance,
        'going_outside': user_data.going_outside,
        'drained_after_socializing': user_data.drained_after_socializing,
        'friends_circle_size': user_data.friends_circle_size,
        'post_frequency': user_data.post_frequency
    }])

    input_transforms = processor.transform(input)
    prediction = model.predict(input_transforms)
    return JSONResponse(content={'prediction': prediction.tolist()}, status_code=200)