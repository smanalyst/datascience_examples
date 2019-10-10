#using a loop
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str


#using recursion
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 



#using the stack
def createStack(): 
    stack=[] 
    return stack 
   
def size(stack): 
    return len(stack) 
    
def isEmpty(stack): 
    if size(stack) == 0: 
        return true 
       
def push(stack,item): 
    stack.append(item) 
   
 
def pop(stack): 
    if isEmpty(stack): 
        return
    return stack.pop() 
   
def reverse(string): 
    n = len(string) 
 
    stack = createStack() 
   
    for i in range(0,n,1): 
        push(stack,string[i]) 
       
    string="" 

    for i in range(0,n,1): 
        string+=pop(stack)      
    return string 