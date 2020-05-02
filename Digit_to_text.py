one_digit = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four",
             "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
ten_to_nineteen = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
                   "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
tens = {"0": "", "2": "twenty ", "3": "thirty ", "4": "fourty ", "5": "fifty ",
        "6": "sixty ", "7": "seventy ", "8": "eighty ", "9": "ninety "}


def print_function(text,tbr=[]):
    if len(text)==1:
        tbr.append(text[0])
        del text[text.index(text[0])]
    elif len(text)==2:
        if text[0]!="":
            tbr.append(text[0]+" hundred ")
        text=text[1:]
        print_function(text,tbr)
    elif len(text)==3:
        if text[0]!="":
            tbr.append(text[0]+" thousand ")
        text=text[1:]
        print_function(text,tbr)
    elif len(text)==4:
        if text[0]!="":
            tbr.append(text[0]+" lakhs ")
        text=text[1:]
        print_function(text,tbr)
    elif len(text)>4:
        print_function(text[:-4])
        tbr.append(" crore ")
        print_function(text[-4:],tbr)
    return tbr




def d_to_t(number,text=[]):
    l = len(number)
    if l < 3:
        if l==1:
            number="0"+number
        if number[0]=="1":
            text.append(ten_to_nineteen[number])
        else:
            text.append(tens[number[0]]+one_digit[number[1]])
    elif l==3:
        element=one_digit[number[0]]
        text.append(element)
        number=number[1:]
        d_to_t(number,text)
    elif l>3 and l<=7:
        if l%2==0:
            number="0"+number
        d_to_t(number[:2],text)
        number=number[2:]
        d_to_t(number,text)
    else:
        first=number[:-7]
        d_to_t(first)
        second=number[-7:]
        d_to_t(second,text)
    return text

print("Enter number")
number=input()
returned=d_to_t(number)
ts=print_function(returned)
ps=""
for element in ts:
    ps=ps+element
print(ps)