from fastapi import FastAPI

from . import router


app = FastAPI(title="Neighbour Api", version="0.1.0", debug=True)

app.include_router(router.router)
