from graderConfigs import graderNames, graderWeights
from workParameters import  Ns, Nq 

def getQuestions( a, b, Qlist ):
    if b < a:
        return []

    rv = []
    qi =  a // Ns if (a % Ns  == 0) else 1 + (a // Ns)
    startQ = 1 + ((a - 1) % Ns) #According to numbering 1 ... Ns for a given question which a belongs to
    endQ = 1 + ((b - 1) % Ns)
    currQEnd = qi * Ns  # Accoring to numbering 1 ... Ns .. 2Ns ... NqNs
    while(1):
        if (b <= currQEnd ):
            rv.append( (Qlist[qi-1], (startQ, endQ) )  )
            return rv
        else:
            rv.append( (Qlist[qi-1], (startQ, Ns)  ) )
            qi = qi + 1
            startQ = 1
            currQEnd = currQEnd + Ns

    return rv #Control never reaches here!    

def print_grading_schedule(schedule):
    for grader, assignments in schedule.items():
        output = f"{grader}: "  # Start with the grader's name
        tasks = []
        for question, (start, end) in assignments:
            tasks.append(f"Q{question}: {start}-{end}")
        output += " , ".join(tasks)  # Join all tasks with a comma and space
        print(output)
    return output

def workAssignment (Sq = []):    
    #Sanitize Input
    if (Ns <= 0):
        raise Exception("Unsanitary Input Ns")
    elif (Nq <= 0):
        raise Exception("Unsanitary Input Nq")
    
    

    totalWeight = sum(graderWeights)
    totalGraders = len(graderNames)
    work = {}
    for grader in graderNames:
        work[grader] = []
    
    
    if (len(Sq) > 0):
        Sq = list(set(Sq))
        for sq in Sq:
            startIndex = 1
            for (i,grader) in enumerate(graderNames):
                qs =  (graderWeights[i] * Ns ) // totalWeight
                endIndex = startIndex + qs - 1 if (i < totalGraders - 1) else Ns
                work[grader] = work[grader] + [ (sq, (startIndex, endIndex)) ]  
                startIndex = startIndex + qs
    
    commonQ = []
    Sqhash = set(Sq)
    for q in range(1, Nq + 1):
        if q not in Sqhash:
            commonQ.append(q)
    totalCommonWork = Ns * len(commonQ)
    
    startIndex = 1
    for (i,grader) in enumerate(graderNames):
        qs =  (graderWeights[i] * totalCommonWork ) // totalWeight
        endIndex = startIndex + qs - 1 if (i < totalGraders - 1) else totalCommonWork
        work[grader] = work[grader] + getQuestions( startIndex, endIndex, commonQ )
        startIndex = startIndex + qs    
        
    for grader in graderNames:
        work[grader].sort(key = lambda x: x[0])
        
    return print_grading_schedule(work)



workAssignment(Sq = [1])