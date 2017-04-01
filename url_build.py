'''
Created on Apr 1, 2017

@author: williamkhaine
'''
# LAHack data parsing  
# CONGRESSPERSON TRACKER 
import urllib.parse

class Summary: 
    def __init__(self, url_to_parse, keyword_count, summary_length): 
        self.PROTOCOL     = "http://"
        self.HOST         = "api.smmry.com/"
        self.KEY          = "F03936BE6D"
        
        self.url_to_parse   = url_to_parse 
        self.keyword_count  = keyword_count 
        self.summary_length = min(summary_length, 40) # maximum is 40 

        self._url = None

    def construct_url(self, avoid, sm_with_break): 
        """Returns a URL that meets SMMRY API Specifications
        """ 
        result = self.PROTOCOL + self.HOST
        parameters = [("SM_LENGTH", self.summary_length),
            ("SM_KEYWORD_COUNT", self.keyword_count)]
        result += "&SM_API_KEY="+ self.KEY + "&SM_URL=" + self.url_to_parse + "&" + urllib.parse.urlencode(parameters)
        if avoid: 
            result += "&SM_QUOTE_AVOID" 
        if sm_with_break: 
            result += "&SM_WITH_BREAK"
        return result 


class Legislation: 
    def __init__(self, congress_session, leg_id): 
        self.PROTOCOL = "https://"
        self.HOST = "api.propublica.org"

        self.DIRECTORIES     = "congress/v1/"
        self.congress_num    = str(congress_session) if type(congress_session) == int else congress_session # must be between 105 and 115
        self.bill_id         = leg_id

    def construct_url(self):
        """Returns a URL that meets ProRepublica API Specifications
        """ 
        return self.PROTOCOL + self.HOST + "/" + \
            self.DIRECTORIES + self.congress_num +  "/bills/" + \
            self.bill_id + ".json"


# CONGRESSPERSON
class Congressperson:
    def __init__(self, chamber, state):
        self.PROTOCOL           = "https://"
        self.HOST               = "api.propublica.org/"
        self.DIRECTORIES        = "congress/v1/members/"
        self.END                = "/current.json"
        self._chamber           = chamber 
        self._state             = state

    
    def construct_url(self):
        return self.PROTOCOL + self.HOST + self.DIRECTORIES + self._chamber + "/" + self._state + self.END  


class Representative(Congressperson): 
    def __init__(self, district, state):
        Congressperson.__init__(self, "house", state)
        self._district = district
    
        
    def construct_url(self):
        return self.PROTOCOL + self.HOST + self.DIRECTORIES + \
            self._chamber + "/" + self._state +"/" + self._district + self.END  


class Senator(Congressperson):
    def __init__(self, state):
        Congressperson.__init__(self, "senate", state)
        self._chamber = "senate"
        
    def construct_url(self):
        return Congressperson.construct_url(self)


if __name__ == "__main__": 
#     a = Legislation(115, "sjres34").construct_url()
#     print(a)
#     example_url = 'https://www.congress.gov/bill/115th-congress/house-bill/1628/text?format=txt'
#     b = Summary(example_url, 10, 20).construct_url(True, True)
#     print(b)
    s = Senator("CA")
    print(s.construct_url())
#     r = Representative() 

