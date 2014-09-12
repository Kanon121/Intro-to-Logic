
# First we need to declare what all of our sets are, and what they contain. 
univ = [1, 2, 3, 4, 5, 6, 7, 8]
a = [1, 2, 3] 
b = [ 2, 3 ,7 ,8]
c = [4, 6, 8]
d = []
e = [1, 3, 7] 



# For readability, we will print what question we are on each time we complete one.
print "Question 1"
print a + c         # Fairly simple, print out the lists combined

print "Question 2"
print c + d         # Again, print out the two lists put together

print "Question 3"
a_e = []            # We need to define an empty list here, and put in numbers that are in both A, and E
for number in a:        #for each number that is in list A...
        if number in e:         # If that number is in list E...
            a_e.append(number)      # put that number into our new list, a_e
print a_e                                  # Print out that new list! 
            
print "Question 4"
a_b = []                    #First we declare an empty list to hold lists A and B together..
a_b_compliment = []         #Then we'll need this one when we take the compliment of the two
for number in a:                #for each number in a...    
    if number not in a_b:           #if it is NOT in list a_b, our empty list...
        a_b.append(number)          # Add it into it! We check to make sure it's not already there so that we don't have duplicates

for number in b:                        #for each number in b...
    if number not in a_b:               # if the number isn't already in a_b...
        a_b.append(number)              # Throw it on in there!

for number in univ:             #Now we need to take the compliment. So lets see what's inside of the univ(erse) list. For each number in univ...
    if number not in a_b:       # If the number is NOT in a_b (a_b = a + b with no duplicates)...  
        a_b_compliment.append(number)       #then add the number to a_b_compliment. We just did (A+B)^
print a_b_compliment        #Print the result

print "Question 5"          
a_c = []                    # New list to contain the answer 
for number in a:        #Lets see if you can figure out the rest of this problem...
    if number in c:
        a_c.append(number)
print a_c

print "Question 6"
a_e = []            #We'll need a new list for their intersection (A / E)
a_e_c = []          # and a new list for the intersection of a_e and c... (a_e) / C 
for number in a:   #For each number in list a...
    if number in e:         # if the number is in list e...
        a_e.append(number)      #add it to the new list, a_e. This gives us the intersection. 
for number in a_e:          #for each number in a_e...
    if number in c:             #if the number is in list c...
        a_e_c.append(number)        #add it to our new list
print a_e_c                             #print it out!

print "Question 7"
b_e = []            #Again, you should be able to figure this one out using the previous ones. 
b_e_a = []
for number in b:
    if number in e:
        b_e.append(number)
for number in b_e:
    if number in a:
        b_e_a.append(number)

print b_e_a
