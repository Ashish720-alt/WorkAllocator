from graderConfigs import graderNames, graderWeights
from workParameters import  Ns, qNames, specialQuestions, workWeights 
from math import floor

def getQuestions( a  , b, Qs, Qwtcf):
    def binarySearchCf(A, p, q , key):
        if q < p:
            return -1
        r = (p + q)// 2
        if (A[r-1] < key and key <= A[r] ):
            return r
        elif ( key > A[r] ):
            return binarySearchCf(A, r+1, q, key)
        else:
            return binarySearchCf(A, p, r -1, key)

    if b < a:
        return []
    
    aQ = binarySearchCf(Qwtcf, 1, len(Qwtcf) - 1, a)
    bQ = binarySearchCf(Qwtcf, 1, len(Qwtcf) - 1, b)

    
    rv = []
    for i in range(aQ, bQ+1):
        qwt = (Qwtcf[i] - Qwtcf[i-1]) // Ns
        startQ = max(1, ((a - Qwtcf[aQ - 1]) // qwt) ) if (i == aQ) else 1
        if (i == bQ):
            endQ = (((b + 1 - Qwtcf[bQ - 1]) // qwt) - 1) if (b < Qwtcf[bQ]) else ((b - Qwtcf[bQ - 1]) // qwt) 
        else:
            endQ = Ns
        rv.append( ( Qs[i-1], ( startQ, endQ )) ) 
    
    return rv

def print_grading_schedule(schedule, qNames):
    for grader, assignments in schedule.items():
        output = f"{grader}: "  # Start with the grader's name
        tasks = []
        for question, (start, end) in assignments:
            tasks.append(f"Q{qNames[question - 1]}: {start}-{end}")
        output += " , ".join(tasks)  # Join all tasks with a comma and space
        print(output)
    return output

def workAssignment (Sq = []):    
    #Sanitize Input
    Nq = len(qNames)
    if (Ns <= 0):
        raise Exception("Unsanitary Input Ns")
    elif (Nq <= 0):
        raise Exception("Unsanitary Input Nq")
    
    

    totalWeight = sum(graderWeights)
    totalGraders = len(graderNames)
    work = {}
    for grader in graderNames:
        work[grader] = []
    
    #Divide special questions Sq; here the relative weight of that question doesnt matter as all graders are assigned each question in Sq equally
    if (len(Sq) > 0):
        Sq = list(set(Sq))
        for sq in Sq:
            startIndex = 1
            for (i,grader) in enumerate(graderNames):
                qs =  floor ( (graderWeights[i] * Ns ) / totalWeight )
                endIndex = startIndex + qs - 1 if (i < totalGraders - 1) else Ns
                work[grader] = work[grader] + [ (sq, (startIndex, endIndex)) ]  
                startIndex = startIndex + qs
    
    # print(work)
    
    commonQ = []
    commonQwtcf = [0]
    Sqhash = set(Sq)
    for q in range(0, Nq):
        if q not in Sqhash:
            commonQ.append(qNames[q])
            commonQwtcf.append( commonQwtcf[-1] + Ns * workWeights[q])
    totalCommonWork = commonQwtcf[-1]
    
    startIndex = 1
    for (i,grader) in enumerate(graderNames):
        qs =  floor ( (graderWeights[i] * totalCommonWork ) / totalWeight ) 
        endIndex = startIndex + qs - 1 if (i < totalGraders - 1) else totalCommonWork   
        questions = getQuestions( startIndex  , endIndex, commonQ, commonQwtcf)
        work[grader] = work[grader] + questions
        startIndex = endIndex + 1
        
    for grader in graderNames:
        work[grader].sort(key = lambda x: x[0])
        
    return print_grading_schedule(work, qNames)


workAssignment(Sq = specialQuestions) 