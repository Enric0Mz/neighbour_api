from fastapi import APIRouter

from . import auth, products, register, transactions, user

router = APIRouter(prefix="/api")


router.include_router(register.router, prefix="/register", tags=["Register"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(user.router, prefix="/user", tags=["User"])
router.include_router(products.router, prefix="/products", tags=["Products"])
router.include_router(
    transactions.router, prefix="/transactions", tags=["Transactions"]
)
