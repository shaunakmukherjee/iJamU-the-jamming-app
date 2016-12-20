from Profile.models import Userdetail
from django.contrib.auth.models import User
import operator

# m number of endorsements to be taken in to account in calculation
m = 20

# the algo function returns a technical level and rating 
# according to a list of endorsements
# temp structure prior to back-end implementation
# end = [e_1, e_2, ...]
# e = [t_r, o-r]
# returns a list [Technical Level, Overall Rating, Beginner(T/F) might not]
def rating(end):
    
    # boolean variable indicating whether user is a beginner
    #beg = False
    
    # get the number of endorsements
    n_e = len(end)
    
    t_r = []
    o_r = []
    
    # retrieve the most current m ratings from endorsement list
    # if n_e is less than m take into account the whole list
    if n_e < m:
        beg = True
        for e in end:
            t_r.append(e.Techlevel)
            o_r.append(e.Rating)
    else:
        for i in range(n_e - m, n_e):
            e = end[i]
            t_r.append(e.Techlevel)
            o_r.append(e.Rating)
    
    # add the ratings for sum
    tlevel = 0
    for t in t_r:
        tlevel = tlevel + t
    ovr = 0
    for o in o_r:
        ovr = ovr + o
    
    # divide the sum by m (beginners will receive ratings lower than average)
    if n_e < m:
        tlevel = tlevel / m
        ovr = ovr / m
    
    return [tlevel, ovr]

# given a list of userdetails, the function gives a ranking to each user and 
# returns a sorted tuple (according to ranking)
def ranking(udlist):
    
    # number of years to reach proficient skill
    yrs_prof = 5
    
    # factors (weights for the technical level: ft, rating: fo)
    ft = 1;
    fo = 2;
    # factors that determine weight (out of) for yrs_exp and endorsements
    fy = 2;
    fe = 2;
    
    ratedlist = dict()
    
    for ud in udlist:
        n_e = len(udlist)
        # Retrieve required variables (technical level, years experience, rating)
        yrs_exp = ud.Year
        tl = ud.Techlevel
        rating = ud.Rating
        
        # if user has greater than m endorsements, 
        # additional endorsements are weighted down
        if n_e > m:
            ef = m + (n_e - m)*.25
        else:
            ef = n_e
        
        # if user has longer years of experience than the minimum required proficiency,
        # additional endorsements are weighted down
        if yrs_exp > yrs_prof:
            yf = yr_prof + (yrs_exp - yrs_prof)*.5
        else:
            yf = yrs_exp
        
        # Rating calculation
        # tl and fo are out of 5
        # yf = 1 if yrs_exp = yrs_prof, additional yr adds .5/yrs_prof (.1 for yrs_prof=5)
        # the years experience factor is out of fy
        # ef = 1 if n_e = m, additional endorsement adds .25/m (.0125 for m=20)
        # the number of endorsement factor is out of fe
        R1 = (tl*ft + rating*fo + yf*fy + ef*fe)
        R2 = (ft + fo + m + yrs_prof)
        R = R1/R2
        
        
        # Add user to dictionary as key with value R
        ratedlist[ud] = R
       
    # return a sorted tuple according to the value (R) of rated list
    return sorted(ratedlist.items(), key=operator.itemgetter(1))









