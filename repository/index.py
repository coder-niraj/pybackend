import uuid

import bcrypt

from models.user.index import User
class UserRepo:
    def __init__(self, db):
        self.db = db
    
    def create(self,name: str,email: str,password: str):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        id = uuid.uuid4() 
        user = User(
            id=id,
            name=name,
            email=email,
            password=hashed
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user # type: ignore
    
    def updateUsingEmail(self,email:str,data:dict):
        return ""
    
    def delete(self,email:str):
        return ""
    
    def getProfilebyEmail(self,email:str):
        user = self.db.query(User).filter(User.email==email).first()
        print("==============",user)
        return user