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
#First I will be generating keys by first using the Find_Public_Key_e function I created above,then I will use the Find_Private_Key_d function. 
#For this example I will be using p = 41 and q = 37 as they are both prime numbers (necessary for p and q to each be prime).


#First- Find the Public Key e
pub_key = Find_Public_Key_e(41, 37)
print(pub_key) #Prints: (1517, 29) (n, e)

#The above shows (n,e) n being p*q and e being the public key which I found by doing a simple if conditional statement
#where it will be a number (k) between 25 and 40 that is relatively prime to (p-1)*(q-1) 
#which I tested with a simple if conditional statement in a for loop that started at 25 and checked each number going up
#until it found a number that was not equal to p, not equal to q and has a remainder of 1 after dividing ((p-1)*(q-1)) by it. 

#Next I will find the Private Key d which is the inverse of e(public key)mod((p-1)*(q-1)). 
#I used the Extended Euclid Algorithm to build my function.

priv_key = Find_Private_Key_d(29, 41, 37) #(e, p, q)
print(priv_key) #Prints (1517, 149) (n, d)

#The above shows (n,d) n being p * q and d being the inverse of e mod ((p-1)*(q-1)). 
#I used the extended euclidean algorithm to find the inverse value which is ns1 in the main part of the function
#and it is converted to d at the end. d(or ns1) is the bezouts coefficient that gets multiplied by e.

#Encoding a message example- using encoded_message to represent the encoded message.
#I used a combination of the Convert_text function and the FME function to achieve the encoded numbers that correspond to the letters.
encoded_message = Encode(1517, 29, "Life is Great! Seize The Day!")
print(encoded_message) #Prints [1208, 845, 289, 1306, 483, 845, 1020, 483, 1119, 1508, 1306, 304, 997, 1348,
                       #483, 821, 1306, 845, 286, 1306, 483, 840, 580, 1306, 483, 1326, 304, 1210, 1348]

#Below I am showing that everything works by reversing the code with the Private key d found above. 
#The decode function is build as a combination of the Convert_Num function and FME function. 
#The output of the Decode function is a message that can be read by a person with the private key.

decoded_message = Decode(1517, 149, encoded_message)
print(decoded_message) #Prints 'Life is Great! Seize The Day!'


#Below I will show how code exchanging works


#Example 1
#Original Post by Michael Becker:
#Public key n, e = (95839, 47)
#Private key n, d = (95839, 30383)                                
#Encoded Message = [77729, 91101, 35790, 61009, 11263, 72699, 21592, 11263, 67164, 6505, 2134, 16072, 11263, 33897, 35790, 63091, 6505, 16072, 72699, 61009, 8849, 11263, 21592, 36081, 6505, 16072, 61009, 21592, 11263, 61009, 8849, 35790, 78155, 12286]
#I will keep the private key listed to prove my functions work.

#First Step: Factorize 95839 (the n) to get p.
#I will be assigning the values to there respective variables as I go through this so as to simplify things.

e1 = 47
n1 = 95839
p1 = factorize(n1)
print(p1) #Prints 239

q1 = n1//p1
print(q1) #Prints 401

#Now that I have p and q and know that e = 47 I will find the Private Key d
priv_key1 = Find_Private_Key_d(e1, p1, q1)
print(priv_key1) #Prints (95839, 30383) (n, d)

#I now know that d = 30383 so I can move on to decoding the message
d1 = 30383
decode1_1 = Decode(n1,d1,[77729, 91101, 35790, 61009, 11263, 72699, 21592, 11263, 67164, 6505, 2134, 16072, 11263, 33897, 35790, 63091, 6505, 16072, 72699, 61009, 8849, 11263, 21592, 36081, 6505, 16072, 61009, 21592, 11263, 61009, 8849, 35790, 78155, 12286])
print(decode1_1) #Prints 'What is your favorite sports team?'

#Now that I know what Michael's message is, I can move on to encoding my own message back to him
my_message1 = Encode(n, e, "My favorite sports team is the Tampa Bay Buccaneers!")
print(my_message1) #Prints [29528, 67164, 11263, 33897, 35790, 63091, 6505, 16072, 72699, 61009, 8849, 11263, 21592, 36081, 6505, 16072, 61009, 21592, 11263, 61009, 8849, 35790, 78155, 11263, 72699, 21592, 11263, 61009, 91101, 8849, 11263, 44268, 35790, 78155, 36081, 35790, 11263, 29447, 35790, 67164, 11263, 29447, 2134, 44226, 44226, 35790, 70675, 8849, 8849, 16072, 21592, 90455]

#I will now reverse this with the Decode function like Michael would do in order to read it.
decode1_2 = Decode(n1,d1,my_message1)
print(decode1_2) #Prints 'My favorite sports team is the Tampa Bay Buccaneers!'

#Example 2
#Original Post by Emily Carpenter
#Public key n,e = (10403, 523) 
#Private key n,d = (10403, 6787)
#Encoded message = [4427, 7520, 8907, 2139, 5486, 1734, 7114, 480, 8373, 1270, 251, 7114, 102, 8907, 3903, 8373, 251, 6647, 2139, 7979, 7114, 6216, 8373, 8373, 9205, 7114, 8907, 10398, 4443, 7114, 1856, 7520, 480, 6127]
#Again, keeping the Private Key to prove everything works.

#First Step: Factorize 10403 (the n) to get p.
#I will be assigning the values to there respective variables as I go through this so that I can simplify what I am doing.

e2 = 523
n2 = 10403
p2 = factorize(n2)
print(p2) #Prints 101

#Next I will divide n2 by p2 to get q2
q2 = n2//p2
print(q2) #Prints 103

#Now that I have p and q and know that e = 523 I will find the Private Key d
priv_key2 = Find_Private_Key_d(e2, p2, q2)
print(priv_key2) #Prints (10403, 6787) (n, d)

#I now know that d = 6787 so I can move on to decoding the message
d2 = 6787
decode2_1 = Decode(n2,d2, [4427, 7520, 8907, 2139, 5486, 1734, 7114, 480, 8373, 1270, 251, 7114, 102, 8907, 3903, 8373, 251, 6647, 2139, 7979, 7114, 6216, 8373, 8373, 9205, 7114, 8907, 10398, 4443, 7114, 1856, 7520, 480, 6127])
print(decode2_1) #Prints "What's your favorite book and why?"

#Now that I know what Emily's message is, I can move on to encoding my own message back to her
#I will be sending back: "My favorite book is Harry Potter, I absolutely love and magic and wizardry"

my_message2 = Encode(n2,e2,"My favorite book is Harry Potter, I absolutely love and magic and wizardry")
print(my_message2) #[9457, 480, 7114, 102, 8907, 3903, 8373, 251, 6647, 2139, 7979, 7114, 6216, 8373, 8373, 9205, 7114, 6647, 1734, 7114, 9176, 8907, 251, 251, 480, 7114, 2091, 8373, 2139, 2139, 7979, 251, 4182, 7114, 6270, 7114, 8907, 6216, 1734, 8373, 8410, 1270, 2139, 7979, 8410, 480, 7114, 8410, 8373, 3903, 7979, 7114, 8907, 10398, 4443, 7114, 2629, 8907, 7931, 6647, 4391, 7114, 8907, 10398, 4443, 7114, 1856, 6647, 636, 8907, 251, 4443, 251, 480]

#I will now reverse this with the Decode function like Emily would do in order to read it.
decode2_2 = Decode(n2,d2,my_message2)
print(decode2_2) #Prints 'My favorite book is Harry Potter, I absolutely love and magic and wizardry'

#Example 3
#Originally Posted by Nathan Palmer
#Public Key n,e = (3497,1583)
#Private Key n,d = (3497,3023)
#Encoded Message = [2564, 2028, 1298, 181, 1909, 3251, 2294, 1909, 2376, 1978, 1638, 3267, 1909, 1501, 1298, 3290, 1978, 3267, 3251, 181, 797, 1909, 2028, 3251, 2258, 797, 1909, 3251, 1467, 1909, 1853, 1978, 1206, 1978, 3267, 1298, 2694, 1978, 1059]
#I will keep the private key listed to prove my functions work.

#First Step: Factorize 3497 (the n) to get p.
#I will be assigning the values to there respective variables as I go through this so that I can simplify what I am doing.

e3 = 1583
n3 = 3497
p3 = factorize(n3)
print(p3) #Prints 13

#Next I will divide n by p to get q
q3 = n3//p3
print(q3) #Prints 269

#Now that I have p and q and know that e = 1583 I will find the Private Key d
priv_key3 = Find_Private_Key_d(e3,p3,q3)
print(priv_key3) = (3497, 3023) #(n, d)
d3 = 3023

#I now know that d = 3023 so I can move on to decoding the message
decode3_1 = Decode(n3,d3,[2564, 2028, 1298, 181, 1909, 3251, 2294, 1909, 2376, 1978, 1638, 3267, 1909, 1501, 1298, 3290, 1978, 3267, 3251, 181, 797, 1909, 2028, 3251, 2258, 797, 1909, 3251, 1467, 1909, 1853, 1978, 1206, 1978, 3267, 1298, 2694, 1978, 1059])
print(decode3_1) #Prints 'What is your favorite hike in Colorado?'

#Now that I know what Nathan's message is, I can move on to encoding my own message back to him
#I will be sending back: "I love the Blodgett Peak Hike in Colorado Springs, the views are incredible!"

my_message3 = Encode(n3,e3,"I love the Blodgett Peak Hike in Colorado Springs, the views are incredible!")
print(my_message3) #Prints [1279, 1909, 1206, 1978, 3290, 797, 1909, 181, 2028, 797, 1909, 2939, 1206, 1978, 2694, 1429, 797, 181, 181, 1909, 592, 797, 1298, 2258, 1909, 3434, 3251, 2258, 797, 1909, 3251, 1467, 1909, 1853, 1978, 1206, 1978, 3267, 1298, 2694, 1978, 1909, 1373, 3099, 3267, 3251, 1467, 1429, 2294, 1334, 1909, 181, 2028, 797, 1909, 3290, 3251, 797, 384, 2294, 1909, 1298, 3267, 797, 1909, 3251, 1467, 2189, 3267, 797, 2694, 3251, 1861, 1206, 797, 2069]

#I will come full circle again and now reverse this with the Decode function like Nathan would do in order to read it.
decode3_2 = Decode(n3,d3,my_message3)
print(decode3_2) #Prints 'I love the Blodgett Peak Hike in Colorado Springs, the views are incredible!'

#Overall Finding: This method of implementing RSA is not very secure because there are not enough steps in the decode/encode process
#and the numbers are far too small that any computer could crack these messages very quickly.

