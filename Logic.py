# Define our variables x and y so we can reference them later
x = 1    
y = 1

# Declare a stop variable so we know when to stop
stop = False

# This is just so when we know it starts the flow chart 
print "FLOW TWO" 


while not stop:     # While stop = False, this will keep looping the indented code below! 
    if x%2 == 0:     # If x is even, then print y. If not, it will pass and continue working down
        print y          # print y
    x += 1              # x = x + 1
    y = x + 3          # y = x + 3
    if x > 7:           # if x > 7, then we have gotten to our stop point, if not, continue looping 
        stop = True  # Now that stop is True, our loop will stop! 

# Again, this is so we know it is now working on the second loop
print "FLOW ONE"

#This flow chart uses 3 as x, and 1 as y, so re-define them here
x = 3
y = 1

#Reset stop to False, so this new code will loop 
stop = False

while not stop:                     # While stop = False, loop through this code below    
    if y > x:                            # If y > x, then it will set stop to True, ending the loop, and print our final x and y
        stop = True
        print "x = %i" % x          # Fancy formatting for our print statement. %i is a place holder for an integer that we define
        print "y = %i" % y          # after the final quote, by putting % then the variable we want to take the place holder
    x += 3                               # x = x + 3
    y += 1                               # y = y + 1
    if x > 10:                           # if x > 10
        x -= 10                          # x = x - 10
                                            # After this line, the code will loop again if stop has not been set to True
    


