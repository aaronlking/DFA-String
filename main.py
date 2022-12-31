
########################################################
# Problem 1: Calculates the number of accepting
# states when given a user defined integer between
# the numbers 1 and 300
########################################################


def strToINT(incStr):
    # converts an incomming string to a integer

    incStrlength = len(incStr)
    value = 0

    for i in incStr:

        if (i == "a"):
            value = value + (1 * 4 ** (incStrlength - 1))
            incStrlength = incStrlength - 1
            continue
        elif (i == "b"):
            value = value + (2 * 4 ** (incStrlength - 1))
            incStrlength = incStrlength - 1
            continue
        elif (i == "c"):
            value = value + (3 * 4 ** (incStrlength - 1))
            incStrlength = incStrlength - 1
            continue
        elif (i == "d"):
            value = value + (4 * 4 ** (incStrlength - 1))
            incStrlength = incStrlength - 1
            continue
        else:
            print("input string not valid. re-run program and try again")
            exit(1)

    return value


def intToSTR(incInt):
    # converts an incomming integer to a string

    finalStr = ""
    count = 0
    while incInt > 0:
        if (incInt > 340):
            while incInt > 340:
                incInt = incInt - 256
                count += 1
        elif (incInt > 84):
            while incInt > 84:
                incInt = incInt - 64
                count += 1

        elif (incInt > 20):
            while incInt > 20:
                incInt = incInt - 16
                count += 1

        elif (incInt > 4):
            while incInt > 4:
                incInt = incInt - 4
                count += 1
        else:
            count = incInt
            incInt = 0

        if (count == 1):
            newStr = 'a'
        elif (count == 2):
            newStr = 'b'
        elif (count == 3):
            newStr = 'c'
        else:
            newStr = 'd'

        finalStr = finalStr + newStr

        count = 0

    return finalStr


def isStateValid(currState):
    # gets passed a string and returns True if state is valid and false otherwise

    if (len(currState) <= 5):
        return True

    return ((currState.count("a") != 0) & (currState.count("b") != 0) & (currState.count("c") != 0) & (currState.count("d") != 0))


def countFunc(n):
    # given a user defined n value, function counts the total number of accepting states
    prev = [1] * 1366
    next = [1] * 1365

    prev[1365] = 0

    for y in range(0, n):

        for j in range(0, 1365):
            temp = 0
            for x in ['a', 'b', 'c', 'd']:
                temp = temp + prev[transitionFunc(j, x)]
                next[j] = temp

        for i in range(len(next)):
            prev[i] = next[i]

    return prev[0]


def transitionFunc(curState, nextChar):
    # given a state and next input char, this function returns the next state
    if (curState == 1365):
        return 1365
    newState = intToSTR(curState)

    if (len(newState) < 5):
        newState = newState + nextChar
        return strToINT(newState)
    elif (len(newState) == 5):

        if (isStateValid(newState+nextChar)):
            newState = newState[1:] + nextChar
            return strToINT(newState)
        else:
            return 1365


########################################################
# Problem 2:
# Algorithm FindString used to find the minimum possible
# integer comprised of the digits given by the user
# that is a multiple of k
########################################################

class Problem2:
    # initialize a queue of valid digits accepted
    validDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def findString(k, alphabet):

        def delta(current_queue, digit_queue, k):
            value = (10 * current_queue + digit_queue) % k
            return value

        result = []

        Q = []

        final = [None] * k

        visited = [False for i in range(k)]

        parent = [-1] * k

        visited[0] = True

        nextVal = -1

        firstTime = True

        for x in alphabet:
            if x == 0:
                alphabet.remove(0)
                firstTime = False

        for d in alphabet:
            nextVal = delta(0, d, k)

            visited[nextVal] = True

            Q.append(nextVal)

            parent[nextVal] = 0

            final[nextVal] = d

        # while loop continues until the queue is empty
        while len(Q) != 0:
            current = Q.pop(0)
            break_flag = False

            for d in alphabet:

                nextVal = delta(current, d, k)
                if nextVal == 0:
                    parent[nextVal] = current
                    current = 0
                    final[nextVal] = d
                    break_flag = True
                    break

                elif not visited[nextVal]:
                    visited[nextVal] = True
                    parent[nextVal] = current
                    final[nextVal] = d
                    Q.append(nextVal)

            if firstTime == False:
                alphabet.append(0)
                firstTime = True
            if break_flag:
                break
        if nextVal != 0:
            noSolution = "No solution."
            return noSolution
        # traverse backwards of final and push the result to a string
        else:
            tempParentIdx = current
            result.append(final[tempParentIdx])
            tempParentIdx = parent[tempParentIdx]

            while tempParentIdx != 0:
                result.append(final[tempParentIdx])
                tempParentIdx = parent[tempParentIdx]

            result = result[::-1]
            stringResult = ' '.join(str(i) for i in result)

        return stringResult

########################################################
# Problem 3:
# Algorithm FindString used to find the minimum possible
# integer comprised of the digits given by the user
# that is a multiple of k. 
########################################################

class Problem3:
    
    # initialize a queue of valid digits accepted
    validDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



    def findString(k, alphabet):
        
        reverseString = ""
        finalResultString = ""
        result = []

        def delta(current_queue, digit_queue, k):
            value = (10 * current_queue + digit_queue) % k
            return value
        
        # Function checks the reverse of the string result to see if it is a palindrome and multiple of k
        def checkReverse(current, final, parent, result, reverseString):
            tempParentIdx = current

            result.append(final[tempParentIdx])
            tempParentIdx = parent[tempParentIdx]

            while tempParentIdx != 0:
                result.append(final[tempParentIdx])
                tempParentIdx = parent[tempParentIdx]

            result = result[::-1]
            stringResult = ' '.join(str(i) for i in result)

            for char in reversed(stringResult):
                reverseString = reverseString + char

            if int(''.join(reverseString.split())) % k == 0 and int(''.join(stringResult.split())) % k == 0:
                return stringResult
            else:
                return False


        Q = []

        final = [None] * k

        visited = [False for i in range(k)]

        parent = [-1] * k

        visited[0] = True

        nextVal = -1

        firstTime = True

        for x in alphabet:
            if x == 0:
                alphabet.remove(0)
                firstTime = False

        for d in alphabet:
            nextVal = delta(0, d, k)

            visited[nextVal] = True

            Q.append(nextVal)

            parent[nextVal] = 0

            final[nextVal] = d

        # while loop continues until the queue is empty
        while len(Q) != 0:
            current = Q.pop(0)
            break_flag = False

            for d in alphabet:

                nextVal = delta(current, d, k)
                if nextVal == 0:
                    parent[nextVal] = current
                    current = 0
                    final[nextVal] = d
                    finalResultString = checkReverse(current, final, parent, result, reverseString)
                    if finalResultString is False:
                        continue
                    else:
                        return finalResultString
                    break_flag = True
                    break

                elif not visited[nextVal]:
                    visited[nextVal] = True
                    parent[nextVal] = current
                    final[nextVal] = d
                    Q.append(nextVal)

            if firstTime == False:
                alphabet.append(0)
                firstTime = True
            if break_flag:
                break
        if nextVal != 0:
            noSolution = "No solution."
            return noSolution


while True:
    print()
    print('Project #1 Test Options:')
    print('\t[1] Problem #1 - Count Function')
    print('\t[2] Problem #2 - FindString Function')
    print('\t[3] Problem #3 - Variation of Problem #2')
    print('\t[4] Quit\n')

    selection = input("\tChoose an problem to test: ")
    print(selection)


    if selection in ['1', '2', '3', '4']:
        selection = int(selection)
    else:
        selection = -1

    if selection == 1:

        # Begin Problem #1 testing

        userInput = input("\t Enter a number between 1 and 300: ")
        print('\tProblem #1 Solution')
        print(userInput)

        n = int(userInput)

        if (n < 1 | n > 300):
            print("Input number must be between 1 and 300, try again")
            exit(-1)

        print("\tn =", n, "   Answer:", countFunc(n))

        # End Problem #1 testing

    elif selection == 2:
        # Begin Problem #2 testing

        print('\t Problem #2 Solution')
        valid_digits = Problem2.validDigits
        k = input("\tEnter K value: ")
        k = int(k)
        if k <= 0:
            print("\tERROR: Must enter a value greater than 0\n")
            break
        q = []
        q = [int(i) for i in input("\tEnter valid digits for the queue: ").split()]
        for i in q:
            if i >= 10:
                print("\tERROR: invalid input, must be a digit between 0-9\n")
                break
        print("\tOUTPUT FOR PROBLEM 2: ", Problem2.findString(k, q))

        # End Problem #2 testing

    elif selection == 3:
        # Problem #3
        print('Problem #3')
        valid_digits = Problem3.validDigits
        k = input("\tEnter K value: ")
        k = int(k)
        if k <= 0:
            print("\tERROR: Must enter a value greater than 0\n")
            break
        q = []
        q = [int(i) for i in input("\tEnter valid digits for the queue: ").split()]
        for i in q:
            if i >= 10:
                print("\tERROR: invalid input, must be a digit between 0-9\n")
                break
        print("\tOUTPUT FOR PROBLEM 3: ", Problem3.findString(k, q))

        # End Problem #3 testing
    elif selection == 4:
        # Quit
        print('\tGoodbye!')
        exit(0)
    else:
        # Invalid selection
        print('\tInvalid selection!')