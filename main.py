def Convert_Text(_string):
    integer_list = []
    for i in _string:
        integer_list.append(ord(i))  
        #This loop looks at each letter in the string that is inputed and converts it into the ASCII numberical value
        #Then it takes the ASCII numerical value and adds it as an item to the integer_list list. 
        #The loop repeats for every letter in the string input
    
    return integer_list
#Overall this function gives you a list of all the characters in there respecive ASCII numerical value as integers
#Each character value is a unique list item

def Convert_Num(_list):
    _string = ''
    for i in _list:
        _string += chr(i)
        #This loop looks at each item in the list _list and converts it to the letter that the ASCII number represents
        #Each time it loops, the character is added on to the end of the string _string
    
    return(_string)
    #The result of this function is a string with all of the items in the list converted back to there characters
    #returns the message that the ASCII characters represent
    
    
def Convert_Binary_String(_int):
    bits_l = []
    if _int == 0:
        bits_l = str(0)
    #The first part looks to see if the number is 0, if so, the string returns as just 0
    else: 
    #The else statement executes if the number is greater than or equal to 1
    
        while _int > 0:
            k = _int % 2 
            bits_l.insert(0,str(k))
            _int = _int//2
        #Turns the number into binary form
        
    bits = "".join(bits_l)
    #Joins all of the individual string numbers in the bits_l list together to create a string, getting rid of the list
    #Want the number to be a string so that it can be iterated over and so that each number can be looked at individually
    
    return(bits)

def FME(b,n,m): 
    binary = Convert_Binary_String(n)
    #calling the Convert_Binary_String function for the value n
    #saves this function as binary
    reverse_binary = binary[::-1]
    #reverses the order of the binary number (important that it is still a string for this to work)
    bin_list = []
    start_val = 0
    #initializing a start value for the loop
    #the first round of the loop
    a = 0
    
    for i in reverse_binary:
        if i == "1":
            a = 2**start_val
            bin_list.append(a)
            start_val += 1
        #adds the exponent value of 2 in the loop number to the list bin_list
        #These numbers are what each of the 1's represent in the binary number
        
        else:
            start_val += 1
        #just continues to count the loop number when there is a 0 in the binary number
        #binary numbers that are 0 are number positions that are not used to get the binary number
    
    sum_value = 1
    
    for i in bin_list:
        x = (b**i)%m
        sum_value *= x
        #This is where the FME takes place
        #Multiples sum value by each of the FME calculations
   
    z = sum_value%m
    #Takes the sum value calculated above and finds the remainder of it
   
    return z


def Euclidean_Alg(a, b):
    while b > 0: #loop that will find the GCD
        k = a%b #Calculating the remainder in each loop
        q = a//b #Calculating the quotient in each loop
        a = b #updating the value of a
        b = k #updating the value of b
   
    x = a
    #setting x to a as a is the GCD
    
    return(x)

def Find_Public_Key_e(p, q):
    n = p*q
    k = (p-1) * (q-1)
    
    for i in range(25, 40):
        m = Euclidean_Alg(k, i)
        if i != q and i != p and m == 1:
        #Checking to make sure that e isn't set as value that equals q or p
        #also making sure the remainder of k ((p-1)*(q-1)) divided by i is 1
            e = i
    #loop for establishing a value of e that is relatively prime to k ((p-1)*(q-1))
    #function as a whole also sets n as p*q
            return(n, e)
    

def Find_Private_Key_d(e, p, q):
    number = p*q
    g = (p-1)*(q-1)
    n = (p-1)*(q-1)
    k = 0 #Defining the remainder to be 0 before loop starts
    q = 0 #Defining the quotient to be 0 before loop starts
    s1 = 1 #Defining s1 value for first loop
    t1 = 0 #Defining t1 value for first loop
    s2 = 0 #Defining s2 value for first loop
    t2 = 1 #Defining t2 value for first loop
    ns1 = s1 #Defining the s1 value so it doesn't update in the 6th line of the loop when I still need the original s1
    nt1 = t1 #Defining the t1 value so it doesn't update in the 6th line of the loop when I still need the original t1
    
    while n > 0: #loop that will find the GCD
        k = e%n #Calculating the remainder in each loop
        q = e//n #Calculating the quotient in each loop
        e = n #updating the value of e
        n = k #updating the value of n
        ns1,nt1 = s2,t2 #using the values of s1 and t1 to now equal s2 and t2
        s2,t2 = s1-(q*s2),t1-(q*t2) #using the same values of s1 and t1 as were used in the line above to get the new s2 and t2 values
        s1,t1 = ns1,nt1 #updating s1 and t1 to be the new s1 and new t1 values for next loop
        
    #This loop finds the Bezout Coefficient needed, which is the private key
    
    d = ns1
    
    while d < 0:
        d = d + g
    #ensures that d is a positive number
    
    return(number,d) 


def Encode(n, e, message):
    cipher_text = []
    m = Convert_Text(message)
    #Takes the message you want to send and converts each letter into its ASCII numerical equivalent
    
    for i in m:
        cipher_text.append(FME(i, e, n))
    #This loop uses FME function to further encode each item in the list (numerical values of the letters)
    #Each time the loop iterates the result of the FME of the item in the list is added to the list cipher_text
    
    return cipher_text


def Decode(n, d, cipher_text):
    m_list = []
    message = ""
    for i in cipher_text:
        m = FME(i,d,n)
        m_list.append(m)
    #loop uses the FME function to undo the encryption done in encoding by using the inverse of e mod (p-1)*(q-1) 
    #The inverse is the private key d
    #The result is the list m_list which contains all of the characters, each character seperated as an item in ASCII numerical value
    
    message += Convert_Num(m_list)
    #Converts the ASCII numerical value to the letter it represents
    
    return message

def factorize(n):
    a = n-1
    for i in range(2, a):
        if n%i==0:
            return i
    #Loop checks to see if the remainder of the number n is evenly divisible by the number that is i in the loop
    #Setting a, the end of the loop range to n-1 as counting starts at 0
    
    return False


#Demo below:
p = 41
q = 37

Find_Public_Key_e(p, q)
#This returns (1517, 29)

n = p*q #The first number above, 1517

e = 29 
#Found by doing a for loop that starts at 25 and checks each number going up until it finds a
#number that is not equal to p, not equal to q and has a remainder of 1 after dividing ((p-1)*(q-1)) by it

Find_Private_Key_d(e, p, q)
#This returns (1517, 149)
#1517 remains the same as above as n is always p*q
n = 1517
d = 149

#149 found by using the extended euclidean algorithm to find the inverse value which is ns1
#in the main part of the function and it is converted to d at the end


#Encoding a message example- using a to represent the encoded message.
#I used a combination of the Convert_text function and the FME function to achieve the encoded numbers that correspond to the letters.

a = Encode(n, e, "Life is Great! Seize The Day!")
print(a)

#Below I am showing that everything works by reversing the code with the Private key d found above. 
#The decode function is built as a combination of the Convert_Num function and FME function. 
#The output of the Decode function is a message that can be read by a person with the private key.

#Setting the result of Decode to b

b = Decode(n, d, a)
print(b)



