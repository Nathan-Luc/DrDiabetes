def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "blood_pressure": item["blood_pressure"],
        "gender": item["gender"],
        "glucose": item["glucose"],
        "height": item["height"],
        "insulin": item["insulin"],
        "name": item["name"],
        "pedigree": item["pedigree"],
        "pregancies": item["pregancies"],
        "skin_thickness": item["skin_thickness"],
        "weight": item["weight"]
    }

def usersEntity(entitiy) -> list:
    return [userEntity(item) for item in entitiy]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a)for a in entity]