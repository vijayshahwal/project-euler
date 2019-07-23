#problem 24
from itertools import permutations
i=0
res=0
def allPermutations(str): 
          global s
          # Get all permutations of string 'ABC' 
          permList = permutations(str) 

          # print all permutations 
          for perm in list(permList): 
                    s+=1
                    print(s)
                    if(s==1000000):
                        break
                    
# Driver program 
if __name__ == "__main__": 
          str = '2013456789'
          allPermutations(str) 
print(s)
