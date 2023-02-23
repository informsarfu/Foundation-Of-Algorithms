def gs(h_rec,s_rec):
    h_pos = {} #('H1': 2,'H2': 3)
    h_pref = {} #('H1' : ['D','A','C','F','B','E'], 'H2' : ['A','C','D','F','E','B'])
    total = 0 #5
    stack = []
    
    for h in h_rec:
        stack.append(h)
        total += h_rec[h][0]
        h_pos[h] = h_rec[h][0]
        h_pref[h] = h_rec[h][1]
    
    free_s = set(s_rec.keys())    
    matchings = set()
    
    while stack:
        curr_hosp = stack.pop()
        for s in h_pref[curr_hosp]:
            if h_pos[curr_hosp]>0 and s in free_s:
                matchings.add((curr_hosp,s))
                free_s.remove(s)
                h_pos[curr_hosp]-=1
            elif h_pos[curr_hosp]>0 and s not in free_s:
                for old_hosp,stud in matchings:
                    if stud == s:
                        if old_hosp==curr_hosp:
                            break
                        if s_rec[s].index(curr_hosp)<s_rec[s].index(old_hosp):
                            matchings.add((curr_hosp,s))
                            matchings.remove((old_hosp,s))
                            h_pos[old_hosp]+=1
                            h_pos[curr_hosp]-=1
                            stack.append(old_hosp)
                            break
            else:
                break
    return matchings
            
        

h_rec = {'H1':(2,['A','C','D','E','F','B']),
         'H2':(3,['C','A','E','F','B','D'])}
s_rec = {'A':['H2','H1'],
         'B':['H2','H1'],
         'C':['H1','H2'],
         'D':['H1','H2'],
         'E':['H2','H1'],
         'F':['H1','H2']}

print(gs(h_rec,s_rec))