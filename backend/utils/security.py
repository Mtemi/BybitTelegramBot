import uuid

def generate_auth_token():
    code = uuid.uuid4().hex
    auth_token = str(code)
    return auth_token 