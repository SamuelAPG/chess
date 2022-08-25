from colorama import Fore, Back 

# remove extra spaces
def clear_tab(draw, information):

    if (information[0] == 'tab'):
        space_num = 4

    elif (information[0] == 'space'):
        space_num = 1
        pass

    else:
        print(Fore.RED + """It have been an error:
            data 1 of the information
            list is not valid""")

        exit(-1)
    
    space_num *= information[1]
    
    for num in range(4):
        for i in range(space_num):
            draw[num].pop(0)
    
    return(draw)

# convert normal drawing to list of lists
def drawing_in_list_fuction(draw):
    
    drawing_in_list = [[]]

    for i in draw:
        if (i == '\n'):
            drawing_in_list.append([])
        
        else:
            drawing_in_list[-1].append(i)
        
    return(drawing_in_list)

# returing the corresponding drawings of each token
def tokens_drawing_function(token_type):

    if (token_type == 'pawns'):
        return("""\
                    
               pp   
              pppp  
                    """)

    elif (token_type == 'bischops'):
        return("""\
               bb
             bb  bb 
            b      b
            bbb  bbb""")

    elif (token_type == 'towers'):
        return("""\
            TT TT TT
            TT TT TT
             TTTTTT 
              TTTT  """)

    elif (token_type == 'horses'):
        return("""\
            L       
            L       
            L       
            LLLL    """)
    
    elif (token_type == "queens"):
        return("""\
            Q  QQ  Q
            QQ QQ QQ
            QQQ  QQQ
            QQQQQQQQ""")
    
    elif (token_type == "king"):
        return("""\
               KK   
              KKKK  
             KKKKKK 
            KKKKKKKK""")

    else:
        print(Fore.RED + """It have been and error:
            the token type that have put
            doesn't exist, check the progam code""")
        
        exit(-1)

    
# print token on the screan
def print_tokens(token_drawing, token_color):
    if (token_color == 'red'):
        print(Fore.RED + '', end="")

    elif (token_color == 'blue'):
        print(Fore.BLUE + '', end="")

    else:
        print(Fore.RED + """It have been and erro:
            The token color is incorrect, 
            check the program code""")

        exit(-1)

    for line in token_drawing:
        for i in line:
            print(i, end="")
        
        print()

if __name__ == '__main__':

    pass