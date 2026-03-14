from repository.index import UserRepo


class userServices:
    def register(db,data):
        userdata = UserRepo(db)
        user = userdata.create(
            name=data.name,
            email=data.email,
            password=data.password
        )
        return {
            "success":True,
            "data":user    
        }
    def login(db,data):
        userdata = UserRepo(db)
        user = userdata.getProfilebyEmail(email=data.email)
        print("--------------- ",user)
        # if(user):
        return {
                "success":True,
                "data":user    
        }
        # else:
        #     raise HTTPException(
        #     status_code=400,
        #     detail="User Not Registered"
        #     )