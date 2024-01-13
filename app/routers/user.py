from .. import schema,models,database,util
from fastapi import Depends,status,HTTPException,APIRouter
from sqlalchemy.orm  import Session


router = APIRouter(
    prefix="/users",
    tags=["users"]
) 


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.User_Response)
def Create_user(user:schema.User,db : Session = Depends(database.get_db),):
    user.password = util.hash(user.password)  #hashing the password


    new_user = models.User(**(user.dict()))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}",response_model=schema.User_Response)
def get_User(id:int,db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="user not found")
    return user