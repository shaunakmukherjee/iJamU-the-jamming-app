# the algo function returns a technical level and rating according to a list of endorsements
# temp structure prior to back-end implementation
# end = [e_1, e_2, ...]
# e = [t_r, o-r]
# returns a list [Technical Level, Overall Rating, Beginner(T/F)]
def algo(end):
    
    # m number of endorsements to be taken in to account in calculation
    m = 20
    
    # boolean variable indicating whether user is a beginner
    beg = False
    
    # get the number of endorsements
    n_e = len(end)
    
    t_r = []
    o_r = []
    
    # retrieve the most current m ratings from endorsement list
    # if n_e is less than m take into account the whole list
    if n_e < m:
        beg = True
        for e in end:
            t_r.append(e[0])
            o_r.append(e[1])
    else:
        for i in range(n_e - m, n_e)
            e = end[i]
            t_r.append(e[0])
            o_r.append(e[1])
    
    # add the ratings for sum
    TL = 0
    for t in t_r:
        TL = TL + t
    OvR = 0
    for o in o_r:
        OvR = OvR + o
    
    # divide the sum by m (beginners will receive ratings lower than average)
    if n_e < m:
        TL = TL / m
        OvR = OvR / m
    
    return [TL, OvR, beg]