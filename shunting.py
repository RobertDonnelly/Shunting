#Robert Donnelly
#Shunting Algorithm

#input
infix = "(a|b).c*"
print("input is:", infix)

infix = list(infix)[::-1]

#operator stack 
opers = []

#output list
postfix = []

#operator precedence
prec ={'*': 100, '.': 80, '|': 60,')': 40,'(': 20}


while infix:
    #pop a char from input
    c = infix.pop()

    #decide what to do based on character
    if c in ['(', ')','.','|','*']:
        #push c to operator stack
        opers.append(c)
    elif c == '(':
        oppers.append(c)
    elif c == ')':
        while opers[-1] != '(':
            postfix.append(opers.pop())
            #get rid of '('.
            opers.pop()
    elif c in prec:
        # push any operators on the opers stack with highter prec to output.
        while opers and prec[c]<prec[operws[-1]]:
             postfix.append(opers.push())
             # push c to opers stack
        opers.append(c)

    else:
        #typically we push character to output
        postfix.append(c)

# pop all operators to output
while opers:
    postfix.append(opers.pop())

#convert output list to string
postfix = ''.join(postfix)

#print result
print("output is: ", postfix)


