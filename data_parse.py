'''
Created on Apr 1, 2017

@author: williamkhaine
'''

import requests 
import pprint 
import json 
from geocodio import GeocodioClient


class LegislationImport: 
    def __init__(self, leg: str):
        self._leg = leg
        self._data = ""
        
    def conduct_call(self):
        headers = {
            'X-API-Key': '',
            }

        print(self._leg)
        r = requests.get(self._leg, headers=headers)
        self._data = r.json()
        r.close()
        
    def get_data(self):
        return self._data 
    

class CongresspersonImport: 
    def __init__(self, c: str):
        self._c = c
        self._data = ""
        
    def conduct_call(self):
        headers = {
            'X-API-Key': '4jVRBAKrhn4nniRoSo5Gf4AWuM8DaA9G3GUC9pqN',
            }

        print("TESTING REQUEST: " + self._c)
        r = requests.get(self._c, headers=headers)
        self._data = r.json()
        r.close()
        
    def get_data(self):
        return self._data 
    
    def get_name(self, num=0):
        if self._data == "":
            self.conduct_call()
        dick = self.get_data()
        dick1 = json.dumps(dick)
        dick2 = json.loads(dick1)
        return dick2['results'][num]['name']

    def get_twitter(self, num=0):
        if self._data == "":
            self.conduct_call()
        dick = self.get_data()
        dick1 = json.dumps(dick)
        dick2 = json.loads(dick1)
        return dick2['results'][num]['twitter_id']

    def get_dist(self, num=0):
        if self._data == "":
            self.conduct_call()
        dick = self.get_data()
        dick1 = json.dumps(dick)
        dick2 = json.loads(dick1)
        return dick2['results'][num]['district'] + "th District"

    def get_party(self, num=0):
        if self._data == "":
            self.conduct_call()
        dick = self.get_data()
        dick1 = json.dumps(dick)
        dick2 = json.loads(dick1)
        return dick2['results'][num]['party']
    
    
class DistrictImport:
    def __init__(self, address):
        self._address = address
        self._key = 'aee4500582f41015b15885e534ea55f28af5f82'
        client = GeocodioClient(self._key) 
        print("RUNNING TEST FOR ADDRESS: " + self._address)
        self._location = client.geocode(address, fields=["cd"])

    
    def get_location(self):
        return self._location

    
    # Parse location for the current congresisonal district 
    def get_district_number(self):
        d = json.dumps(self._location)
        l = json.loads(d)
        return l["results"][0]["fields"]["congressional_district"]["district_number"]
    

if __name__ == "__main__": 
    import url_build
    
#     # Example: ISP Bill
#     leg = url_build.Legislation(115, "sjres34") 
#     leg_url = leg.construct_url()
#     d = LegislationImport(leg_url)
#     d.conduct_call() 
#     pprint.pprint(d.get_data())    
# 
#     # Cypress Representative
#     rep = url_build.Representative("47", "CA")
#     rep_url = rep.construct_url()
#     ci = CongresspersonImport(rep_url)
#     ci.conduct_call()
#     ci.get_data()
#          
#     # California Senators
#     sen = url_build.Senator("CA")
#     sen_url = sen.construct_url()
#     ci = CongresspersonImport(sen_url)
#     ci.conduct_call()
#     pprint.pprint(ci.get_data())    
#  
#   
#     # San Gabriel Representative    
#     rep = url_build.Representative("27", "CA")
#     rep_url = rep.construct_url()
#     url_build = CongresspersonImport(rep_url)
#     url_build.conduct_call()
#     pprint.pprint(url_build.get_data())     
    a = "1109 N Highland St, Arlington, VA 22201"
    di = DistrictImport(a)
    print(di.get_district_number())
