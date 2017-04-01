'''
Created on Apr 1, 2017

@author: williamkhaine
'''

import data_parse 
import url_build

class Representative: 
    def __init__(self, district, state):
        self._url = url_build.Representative(district, state).construct_url()
        self._r = data_parse.CongresspersonImport(self._url) 
        
        self._district = district
        self._state = state
        self.set_name()
        self.set_party()
        self.set_twitter_handle()
        self.set_district()
        
    def get_base_data(self):
        self._r.conduct_call()
        
    def set_name(self):
        self._name = self._r.get_name() 
    
    def get_name(self):
        return self._name
    
    def set_party(self):
        self._party = self._r.get_party() 
    
    def get_party(self):
        return self._party

    def set_district(self):
        self._district = self._r.get_dist() 
    
    def get_district(self):
        return self._district
    
    def set_twitter_handle(self):
        self._twitter_handle = self._r.get_twitter() 
        
    def get_twitter_handle(self):
        return self._twitter_handle

if __name__ == "__main__":
    sd = "47"
    ss = "CA"
    
    r = Representative(sd, ss)
    
    print(r.get_name())
    print(r.get_district())
    print(r.get_party())
    print(r.get_twitter_handle())
