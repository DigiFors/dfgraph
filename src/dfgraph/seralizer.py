
def has_all(json, keys):
    for k in keys:
        if not k in json.keys():
            return False
    return True


class SerializerInterface:
    def to_dict(self) -> dict:
        pass
