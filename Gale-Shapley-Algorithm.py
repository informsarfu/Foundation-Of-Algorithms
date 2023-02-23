def gs(h_rec,s_rec):
    h_pos = {} #Storing the vacancies of each hospital
    h_pref = {} #Storing Preference List of each hospital
    stack = [] 
    
    for h in h_rec:
        stack.append(h)
        h_pos[h] = h_rec[h][0]
        h_pref[h] = h_rec[h][1]
    
    free_s = set(s_rec.keys())    
    matchings = set()
    
    while stack: #Algorithm runs as long as stack is not empty.
        curr_hosp = stack.pop()
        for s in h_pref[curr_hosp]:
            #First hospital tries to match its vacancies with unpaired students.
            if h_pos[curr_hosp]>0 and s in free_s:
                matchings.add((curr_hosp,s))
                free_s.remove(s)
                h_pos[curr_hosp]-=1 
            elif h_pos[curr_hosp]>0 and s not in free_s: #elif student is already paired,
                for old_hosp,stud in matchings:
                    if stud == s:
                        if old_hosp==curr_hosp:
                            break
                        #check student preference list to see if current hospital is prefered over older pair.
                        if s_rec[s].index(curr_hosp)<s_rec[s].index(old_hosp):
                            #If so, add this new pair to the  matchings set and remove the old pair
                            matchings.add((curr_hosp,s))
                            matchings.remove((old_hosp,s))
                            h_pos[old_hosp]+=1
                            h_pos[curr_hosp]-=1
                            #push the removed hospital (from matchings) back into the stack as it is unpaired.
                            stack.append(old_hosp)
                            break
            else:
                break
    return matchings
            
        
#Taking inputs of hospitals and students (preference list)

h_rec = {'H1':(2,['A','C','D','E','F','B']),
         'H2':(3,['C','A','E','F','B','D'])}
s_rec = {'A':['H2','H1'],
         'B':['H2','H1'],
         'C':['H1','H2'],
         'D':['H1','H2'],
         'E':['H2','H1'],
         'F':['H1','H2']}

print(gs(h_rec,s_rec))