from jose import jwt

token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')

jwt.decode(token, 'secret', algorithms=['HS256'])
{u'key': u'value'}