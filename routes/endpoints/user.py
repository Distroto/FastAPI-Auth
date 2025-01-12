from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...api.deps import get_current_user, get_db
from ...models.user import User
from ...schemas.user import User as UserSchema

router = APIRouter()

@router.get("/users/me", response_model=UserSchema)
def read_current_user(
    current_user: User = Depends(get_current_user)
) -> Any:
    return current_user

@router.get("/users", response_model=List[UserSchema])
def read_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Any:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    users = db.query(User).all()
    return users