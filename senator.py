'''
Created on Apr 1, 2017

@author: williamkhaine
'''

import url_build
import data_parse 


class Senator: 
    def __init__(self, state, index_num):
        self._url = url_build.Senator(state).construct_url()
        self._r = data_parse.CongresspersonImport(self._url) 
        self._index_num = index_num

        
        self._state = state
        self.set_name()
        self.set_party()
        self.set_twitter_handle()
        
        
    def get_base_data(self):
        self._r.conduct_call()
        
    def set_name(self):
        self._name = self._r.get_name(self._index_num) 
     
    def get_name(self):
        return self._name
     
    def set_party(self):
        self._party = self._r.get_party(self._index_num) 
     
    def get_party(self):
        return self._party
    
    def set_twitter_handle(self):
        self._twitter_handle = self._r.get_twitter(self._index_num) 
        
    def get_twitter_handle(self):
        return self._twitter_handle


if __name__ == "__main__":
    ss = "CA"
    r = Senator(ss, 0)
    print(r.get_name())
    print(r.get_party())
    print(r.get_twitter_handle())
    
    r = Senator(ss, 1)
    print(r.get_name())
    print(r.get_party())
    print(r.get_twitter_handle())
