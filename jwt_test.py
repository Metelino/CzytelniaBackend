from datetime import datetime

from jose import jwt


key = 'secret'

data = dict()
data['user'] = 'Metelino'
data['id'] = 15
data['iat'] = datetime.now()
token = jwt.encode(data, key, algorithm='HS256')


out = jwt.decode(token, key)
print(out)