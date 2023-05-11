import uvicorn
from fastapi import FastAPI

from . import router

app = FastAPI(title="Neighbour Api", version="0.1.0", debug=True)

app.include_router(router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
