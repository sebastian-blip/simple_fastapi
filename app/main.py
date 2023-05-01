# External libraries
import uvicorn

from fastapi import Depends
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Own libraries
from config import Settings, get_settings
from routers.datasets_info.info_dataset import data_info_router


app = FastAPI(
    title='Director Aeolos',
    version='0.1.0',
    docs_url='/docs',
    redoc_url=None)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


app.include_router(data_info_router)


@app.get('/info')
async def info(settings: Settings = Depends(get_settings)):
    return dict(settings)


if __name__ == '__main__':
    uvicorn.run(app)
