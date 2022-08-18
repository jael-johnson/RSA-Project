def Convert_Text(_string):
    integer_list = []
    for i in _string:
        integer_list.append(ord(i))  
        #This loop looks at each letter in the string that is inputed and converts it into the ASCII numberical value
        #Then it takes the ASCII numerical value and adds it as an item to the integer_list list. 
        #The loop repeats for every letter in the string input
    
    return integer_list
