# import routeros_api


# try:
#   connection = routeros_api.RouterOsApiPool('10.10.10.1', username='', password='', plaintext_login=True)
#   api = connection.get_api()
#   list = api.get_resource('/ip/hotspot/user')
#   list.edit()
#   connection.disconnect()
# except Exception as e:
#   print(e)

from app import run
