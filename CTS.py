import requests
import os
import random
import string
import json

while True:
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))

        url = '# PUT YOUR LINK HERE'

        names = json.loads(open('names.json').read())
        for name in names:
                name_extra = ''.join(random.choice(string.digits))
                email = name.lower() + name_extra + '@EMAILADDRESS.com'
                name = ''.join(random.choice(chars) for i in range(8))
                message = ''.join(random.choice(chars) for i in range(8))
                requestz = requests.post(url, allow_redirects=False, data={
                        'loginName': email,
                        'password': email,
                        'Login': 'Login',
                        })
                print("Sent Email", email, "and password , to servers with status code", requestz.status_code)

