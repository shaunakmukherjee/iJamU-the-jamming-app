# returns a dictionary of the paramaters in a request
def parseRequest(req) :
    l = req.split('/')
    plist = l[len(l)-1]
    ps = plist.split(';')
    params = dict()
    for p in ps:
        pss = p.split(":")
        params[pss[0]] = pss[1]
    
    return params

#Example
d = parseRequest("r/jamming/Login/username:example;password:1234")
print d

#Output
#Chis-MacBook-Pro:Desktop chiyoungshin$ python parseRequest.py
#{'username': 'example', 'password': '1234'}
