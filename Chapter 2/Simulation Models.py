''' Johnson Bui '''
# Importing modules
import numpy as np
import numpy.linalg as la
import random as ra

''' Ex 1 ''' 
print('Exercise 1:')
# Simple function to create a random num between 0 and 1
def randGen():
    randNum = ra.random()
    return randNum

# Function to get two heads in a row and return count the num of tries
def aRandGen(probOfHeads):
    aRand = np.array([])
    twoHeads = 0
    # Loop through while keeping track of how many heads in order and adding the value to array.
    while twoHeads < 2:
        randNum = randGen()
        # Empty add a random number
        if aRand.size == 0:
            aRand = np.append(aRand, randNum)
            # If heads, increment twoHeads
            if randNum < probOfHeads:
                twoHeads += 1
        # If heads, increment twoHeads
        elif randNum < probOfHeads:
            aRand = np.append(aRand, randNum)
            twoHeads += 1
        elif randNum > probOfHeads:
            aRand = np.append(aRand, randNum)
            twoHeads = 0
    # Count num of iterations it takes to get two heads            
    iCount = len(aRand)
    
    return(iCount, aRand)    

# Function to loop through aRandGen iMax total times
def randLooper(probOfHeads, iMax):
    iTries = 0
    # Loop random generator for iMax times
    for i in range(0,iMax):
        iTries += aRandGen(probOfHeads)[0]
    # Divide the total amount of tries by the max amount of iterations
    avgTries = iTries / iMax
    print('\nWith a PR[h] = {}, the avg amount of tries to get two heads in a row after {} iterations is {}.'.format(probOfHeads, iMax, avgTries)) 

# Passthrough function to write repetitive text.
def randDescript(probOfHeads):
    (iCount, aRand) = aRandGen(probOfHeads)
    print('For one iteration, it took {} tries. \nThe set is: \n{}'.format(iCount, aRand))

# Run it once!
#tries = aRandGen(1/2)
#print('\nIt took {} tries to get two heads.'.format(tries))
randDescript(1/2)
# Run it iMax times! And find the avg num of tries!
randLooper(1/2, 10)



''' Ex 3a '''
print('\nExercise 3a:')
randDescript(1/3)
randLooper(1/3, 10)


''' Ex 7a '''
print('\nExercise 7:')

def randToken(maxSet):
    rand = np.array([])
    token = np.array([])
    iC = 0
    iA = 0
    iT = 0
    iS = 0
    noSet = True
    # maxSet = maxCollect * 4 Previous model was to simulate for collection of 10 sets in one run which is around 60 tries
    
    # Loop through while keeping track of how many heads in order and adding the value to array.
    while noSet:
        randNum = randGen()
        # If less than .3, C token
        if randNum < .3:
            #tRand = np.append((rand, token), (randNum, 'C'))
            rand = np.append(rand, randNum)
            token = np.append(token, 'C')
            iC += 1
        # Check for A
        elif randNum > .3 and randNum < .4:
            #tRand = np.append((rand, token), (randNum, 'A'))
            rand = np.append(rand, randNum)
            token = np.append(token, 'A')
            iA += 1
        # Check for T
        elif randNum > .4 and randNum < .7:
            #tRand = np.append((rand, token), (randNum, 'T'))
            rand = np.append(rand, randNum)
            token = np.append(token, 'T')
            iT += 1
        # S token
        else:
            #tRand = np.append((rand, token), (randNum, 'S'))
            rand = np.append(rand, randNum)
            token = np.append(token, 'S')
            iS += 1
        # Check for full collection
        # if iC >= maxSet and iA >= maxSet and iT >= maxSet and iS >= maxSet:
        if iC >= maxSet and iA >= maxSet and iT >= maxSet and iS >= maxSet:
            noSet = False
                
    # Count num of iterations it takes to get a full set            
    iCount = len(rand)
    
    return(iCount, rand, token)

def collectTokens(maxCollect):
    iTries = 0
    # Loop through for maxCollect times
    for i in range(0, maxCollect):
        iTries += randToken(4)[0]
    print('The avg number of collected tokens is {}.'.format(iTries))

# Run for collection of 10 sets
collectTokens(10)

''' Ex 10a ''' 
print('\nExercise 10a:')

# Function to get two heads in a row and return count the num of tries
def aShot(numShots):
    aRand = np.array([])
    points = 0 
    shots = 0
    # Loop through while keeping track of how many heads in order and adding the value to array.
    while shots < numShots:
        randNum = randGen()
        # Empty add a random number
        if aRand.size == 0:
            if randNum < .4:
                points += 1
            aRand = np.append(aRand, randNum)
        # Made first shot
        elif aRand[0] < .4:
            # To make next shot
            if randNum < .5:
                points += 1
        # Missed first shot
        else:
            # Make next shot
            if randNum < .3:
                points += 1
        shots += 1      
    return(points, numShots, aRand) 
    
def shotLooper(games):
    points = 0
    for i in range(0, games):
        points += aShot(25)[0]
    print('\nFor {} game(s), Hack scores an average of {} points.'.format(games, points))
    
shotLooper(1)

''' Ex 10b ''' 
print('\nExercise 10b:')
# Loop the Hack sim for 10 games
shotLooper(10)