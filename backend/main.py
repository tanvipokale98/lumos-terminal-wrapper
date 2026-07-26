import fastapi
import uvicorn
from app.api.response_api import router
app=fastapi.FastAPI()

app.include_router(router,prefix="/api/v1")

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)