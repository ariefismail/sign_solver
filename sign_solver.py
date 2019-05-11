import itertools

# ref : https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
# Python function to print permutations of a given list 
def permutation_no_repeat(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation_no_repeat(remLst): 
           l.append([m] + p) 
    return l 
	
# ref : https://stackoverflow.com/questions/3099987/generating-permutations-with-repetitions-in-python
def permutation_with_repeat(lst,rpt): 
	return [p for p in itertools.product(lst, repeat=rpt)]

def sign_solver(lst1,ans1,lst2,ans2):
	if(len(lst1) != len(lst2)):
		print 'lists size don\'t match'
		return
	
	# get the list of all possible math process
	# pmp = possible math process
	sign_length=len(lst1)-1
	pmp = permutation_with_repeat(['+','-','*','/'],sign_length)
	# get the list of all possible number order
	# possible num order
	pno1=permutation_no_repeat(lst1)
	pno2=permutation_no_repeat(lst2)

	# i loop is for looping trough the possible number order
	for i in range(len(pno1)): 
		processed_list=pno1[i]
		# j loop is for looping trough the possible math process to be operated on the current number order
		for j in range(len(pmp)):
			math_process = pmp[j]
			ans=processed_list[0]
			# k loop is for mathematic operation on the current number order
			for k in range(sign_length):
				if(math_process[k]=='+'):
					ans+=processed_list[k+1]
				elif(math_process[k]=='-'):
					ans-=processed_list[k+1]
				elif(math_process[k]=='*'):
					ans*=processed_list[k+1]
				elif(math_process[k]=='/'):
					if(ans%processed_list[k+1] != 0):
						continue
					else:
						ans/=processed_list[k+1]
			#if the answer is correct, then check wether the math process can be use on next list
			if(ans==ans1):
				other_processed_list=pno2[i]
				other_ans=other_processed_list[0]
				for l in range(sign_length):
					if(math_process[l]=='+'):
						other_ans+=other_processed_list[l+1]
					elif(math_process[l]=='-'):
						other_ans-=other_processed_list[l+1]
					elif(math_process[l]=='*'):
						other_ans*=other_processed_list[l+1]
					elif(math_process[l]=='/'):
						if(other_ans%other_processed_list[l+1] != 0):
							continue
					else:
						other_ans/=processed_list[l+1]
				#if the next list is also correct
				if(other_ans==ans2):
					#print the answer
					print 'found :'
					print 'num order 1 :',processed_list,'ans :',ans
					print 'num order 2: ',other_processed_list,'ans :',other_ans
					print 'math process:',math_process
					return
	# no solution found
	print 'solution not found'			
	
if __name__ == '__main__':
	#example variaable
	a=[1,2,-2,3] 
	ans_a=-1
	b=[-2,-1,2,1]
	ans_b=-5	
	sign_solver(a,ans_a,b,ans_b)