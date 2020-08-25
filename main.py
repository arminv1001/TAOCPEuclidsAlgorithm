# pair (m,n)
def pairs_input():
    m = input("m ?")
    n = input("n ?")
    print("Input: ( " + m + " , " + n + " ) = ",end=" ")
    return int(m), int(n)


# singleton (n)
def getSingleton(m, n):
    r = 0
    while True:
        step = 1
        print("( " + str(m) + " , " + str(n) + " , " + str(r) + " , " + str(step) + " )")
        r = m % n
        step += 1
        print("( " + str(m) + " , " + str(n) + " , " + str(r) + " , " + str(step) + " )")
        if (r == 0):
            print("Finish: " + "( " + str(m) + " , " + str(n) + " , " + str(r) + " , " + str(step) + " )")
            return "(" + str(n) + ")"
        else:
            step += 1
            print("( " + str(m) + " , " + str(n) + " , " + str(r) + " , " + str(step) + " ) = " , end=" ")
            m = n
            n = r
            r = 0



result = pairs_input()
print("Result: " + getSingleton(result[0], result[1]))
