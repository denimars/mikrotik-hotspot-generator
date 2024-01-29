import routeros_api
from dotenv import load_dotenv
import os

load_dotenv()
class MikrotikConnection():
    def __init__(self):
        self.mikrotik_connection = routeros_api.RouterOsApiPool(os.getenv['HOTSPOT_MIKROTIK_IP'], username=os.getenv['HOTSPOT_MIKROTIK_USER'], password=os.getenv['password'], plaintext_login=True)
        self.mikrotik_api = self.mikrotik_connection.get_api()
    
    def mikrotik_api(self):
        return self.mikrotik_connection, self.mikrotik_api
    
    