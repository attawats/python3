# == , <> , != , > , < ,>= , <= , not , and , or

# score = 62
# if  score > 70:
#    print('good')
# else:
#    print('tyr harder')

#Check string

def greeting(lang):
    if lang == "th":
        return print('sawadee')
    elif lang == "jp":
        print('Konichiwa')
    else:
        print('hello')

def meet_req(eng,interview):
    if (eng > 70 and interview > 80):
        return True
    else:
        return False

def meet_req2(eng,interview,math):
    if (eng > 70 and interview > 80 and math > 50): #can add operation 
        return True
    else:
        return False

#greeting('th')
#print(meet_req(80,90))
print(meet_req2(80,90,60))