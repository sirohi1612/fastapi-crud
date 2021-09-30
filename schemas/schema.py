def userEntity(item):
    # it will return dict
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
    }

def usersEntity(entity):
    # it will return list
    return [userEntity(item) for item in entity]