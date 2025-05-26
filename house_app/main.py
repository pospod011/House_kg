import fastapi
import uvicorn
from starlette.middleware.sessions import SessionMiddleware

from house_app.admin.setup import setup_admin
from house_app.api.endpoints import houses, auth


house_app = fastapi.FastAPI(title='House site')
house_app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")
setup_admin(house_app)

house_app.include_router(auth.auth_router, tags=["Auth"])
house_app.include_router(houses.house_router)



if __name__ == "__main__":
    uvicorn.run(house_app, host="127.0.0.1", port=8000)

