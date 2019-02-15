
# prints a staircase that is right aligned that is n stairs high.
def staircase(n):
    spaces = n-1
    stairs = 1

    for i in range(n):
        stair_string = ""
        for j in range(spaces):
            stair_string+= " "
        for k in range(stairs):
            stair_string+= "#"
        
        print(stair_string)
        spaces-=1
        stairs+=1