#I linearly scan through the dictionary assessing each entry in it for inclusion of the target string
#On finding the first match I add the first ten anagrams of this match to anagram_list by generating them in sorted order one at a time.
#(I generate anagrams one at a time because I don't need the whole list at once; I have to return only the lexicographically smallest ten anagrams.)
#Then I move onto identifying the next match. Once I have identified it, I again start generating the anagrams in sorted order 
#(I have not formally used the concept of generators with the keyword "yield" but I have used a similar idea of generating anagrams on the fly).
#As each anagram is identified, I find out where it can be fitted into the pre-existing anagram_list while preserving the sorted order. 
#If it can be fit somewhere in between, I fit it and move onto generating the next anagram, and then see where this next anagram can be fit. 
#If it cannot be fit or can be fit only in the 10th position 
#in anagram_list, I move onto identifying the next match since lexicographically later anagrams for the current match cannot be fitted into the list.
#I finally swap the first and second characters of each of the entries in anagram_list because the ordering is by second letter
#Since there is a one-one mapping between the list so obtained and anagram_list we obtain a sorted list with the priority of sorting on the second letter
#

#Concerns and how to address them:  
#If the dictionary becomes very large, it could be stored in a database or be broken up into chunks for reading it.

#Alternative implementations
#I could have formally used Python's generator feature with the yield keyword (I have used the same design pattern)

#If the dictionary were a living document I would keep note (in a table(array)) of the target strings and of the latest timestamps of generation of the lists 
#corresponding to these target strings. I would also keep note (in a list) of the timestamps for the dictionary updates. If a new request 
#came in for a target string that exists in the table and if its timestamp is less than the timestamp for the latest dictionary update, 
#I would take the set difference between the latest version of the 
#dictionary and the latest version of the dictionary whose timestamp is less than the timestamp of list generation 
#of the list corresponding to the target string, and run my program only for this difference to get the updated list of anagrams for the target string.
#The reason why this will work is that the order in which words from the dictionary are processed does not matter - the ten smallest anagrams
#from the matches will be identified through generation of the anagrams and fitting them into the right position into the pre-existing list of the current
#ten smallest anagrams.

#Personal opinions about best practices in coding and other thoughts
#Write a function/procedure for every sub-task that achieves exactly what it purports to do
#Egoless programming - Have a conservative mindset while programming. If things can go wrong they sooner or later will.
#Pay attention to boundary cases
#Try to make variable names suggestive
#Have empathy for the next person who will handle your project and also for a future yourself, and so comment the code properly
#Strike a balance between efficiency and expediency
#Premature optimization is the root cause of all evil - Donald Knuth
#Focus on writing the application correctly before trying to optimize or beautify it.
#Be open to tips and feedback from more experienced people. Don't reinvent the wheel.

#flip first and second characters of string; single responsibility principle design pattern
def flip_first_and_second(x):
  return x[1]+x[0]+ x[2:]

#push the contents of list one position to the right starting at the ith index; single responsibility principle design pattern
def push_to_right(l,i):
    for j in range(len(l)-1,i,-1):
        l[j]=l[j-1]

#iterator pattern; generating the next permutation from the current permutation
def next_permutation(s):
    sl=list(s)
     
    for i in range(len(sl)-1,0,-1):
      if sl[i-1]>=sl[i]:
           continue
      else:
           for j in range(i,len(sl)):
               if (sl[j]>sl[i-1]):
                continue
               else:
                break
           if sl[j]>sl[i-1]:
            tmp=sl[i-1]
            sl[i-1]=sl[j]
            sl[j]=tmp
           else:
            tmp=sl[i-1]
            sl[i-1]=sl[j-1]
            sl[j-1]=tmp

            
           k=sl[i:]
           k.sort()
           sl=sl[:i]+k
           return ''.join(sl)

#can code the matching criterion here (palindrome, etc.) dependency injection design pattern
def criterion(x,target):
  if target in x:
      return True
  else:
      return False

anagram_list=[] #list containing anagrams of matches
target=input("string?") #take the input string
dictionary=input("dictionary?")#pick the dictionary
f=open(dictionary,"r") #open the file containing strings
move_on_to_next_match=0
for x in f:
    if criterion(x,target):
     #generate anagrams of matched string in sorted order after dropping newline character and add to anagram_list         
     #l=list(itertools.permutations(x.rstrip()))
     x=list(x.rstrip())
     x.sort()
     first_anagram=''.join(x)
     

     if anagram_list==[]:
       anagram_list.append(first_anagram)
       tmp=first_anagram
       for i in range(2,11):
           next_anagram=next_permutation(tmp)
           anagram_list.append(next_anagram)
           tmp=next_anagram
     else:
       tmp=first_anagram
       while True:
        for i in range(0,10):
           if tmp<anagram_list[i]:
               push_to_right(anagram_list,i)
               anagram_list[i]=tmp
               break
        if i==9:
            move_on_to_next_match=1
        if move_on_to_next_match==0:
           tmp=next_permutation(tmp)
        else: 
           move_on_to_next_match=0
           break
           

        
      
#since the sorting is to be by the second character flip the first and the second characters
#there is a one-one correspondence between the new set and the old set and since
#the first character is now in the second position and the sorting in other positions
# is undisturbed we have the desired sorting constraint met.
for i in range(0,len(anagram_list)-1):
    anagram_list[i]=flip_first_and_second(anagram_list[i])


if anagram_list:
    for i in range(0,10):
      print(anagram_list[i])
else:
    print("None")
  
  
   
  
