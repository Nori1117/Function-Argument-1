#write a python function to find all the strong numbers in a given list of numbers

def factorial(number): 
    if(number == 0 or number == 1): 
        fact = 1
    else: 
        fact = number * factorial(number - 1) 
    return fact 
  
def find_strong_number(num_list): 
    num_list =[] 
  
    for x in num_list: 
        temp = x 
        sum = 0
        while(temp): 
            rem = temp % 10
            sum += factorial(rem) 
            temp = temp // 10
        if(sum == x): 
            num_list.append(x) 
        else: 
            pass  
              
    return num_list 
          
# Driver Code 
num_list = [1, 2, 5, 145, 654, 34] 
strong_num_list = strong_number(num_list) 
print(strong_num_list) 
