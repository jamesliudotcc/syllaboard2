from users import users

import requests

for user in users:
    requests.post("http://localhost:5000/auth/register", json=user)
