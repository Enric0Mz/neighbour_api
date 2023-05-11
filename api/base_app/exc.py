from fastapi import HTTPException, status


def not_found():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


def incorrect_password():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
    )


def not_authenticated():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated"
    )


def invalid_token():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or Expired token"
    )
