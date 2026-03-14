from sqlalchemy.orm import Session

from repository.index import UserRepo
from services.index import userServices

class Authentication:
    def register(self,data,db:Session): # type: ignore
        return userServices.register(db,data);
        # type: ignore
    def login(self,data,db:Session): # type: ignore
        return userServices.login(db,data) # type: ignore