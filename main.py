#libaries to make the magic happen 
import random
import statistics as st
#variables 
count, below, hi_number = 0,0,0
lower = []
higher = []
c = []
#below where the magic happens. 
try:
  def re():
  #variables are linked by the global() feature, because they are defined outside of the function. 
    global count,below,hi_number,lower,higher
    count +=1
  #random numbers will be run, a 1000 times if needed.
    a= random.randint(0,1000)
    int(a)
    a+10/2*5
  #code will stop as soon 42 has been reached.
    if a == 42:
      print(a)
      print ("It run "+str(count)+" times, to get to 42.") 
    elif a >42:
      #since this ain't 42 and is higher instead, the code will keep running
      hi_number+=1
      higher.append(a)
      a= a-1
      re()
    elif a < 42:
      #since this ain't 42 and is lower instead, the code will keep running
      below+=1
      lower.append(a)
      a = a+1
      re()
except:
  print("Fatal Error")
  
#function to get the higher's numbers average.
def positive_num():
  #print("\nAverage of higher numbers.")
  x = st.mean(higher)
  print("\nthe avareage of higher numbers is "+str(x)+"\n")
#function to get the lower's numbers average.
def negative_num():
  #print("\nAverage of below numbers.")
  x = st.mean(lower)
  print("\nthe avareage of below numbers is "+str(x)+"\n")
#function that tells us the average of times it ran. 
def times_num():
  for x in range(count):
    c.append(x)
  y = st.mean(c)
  print("\nthe average time that this ran was "+str(y)+"\n")
  
re()
times_num()
negative_num()
positive_num()





     


