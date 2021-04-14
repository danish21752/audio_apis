import uuid


class CommonService:
    @classmethod
    def generate_id(cls):
        return uuid.uuid4()
