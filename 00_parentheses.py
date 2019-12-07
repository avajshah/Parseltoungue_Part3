ask = ("avashah")
odd = 1
empty = ""
for x in ask:
    odd = odd + 1
    if odd%2 ==0:
        empty = empty + ((x.upper()))
    else:
        empty = empty +  ((x.lower()))
print(empty)


ask = ("avashah")
odd = 1
anotherempty = ""
for t in ask:
    odd = odd + 1
    if odd%2 ==0:
        t = t.upper()
        if t =="A" or t == "E" or t == "I" or t == "U" or t == "O":
            anotherempty = anotherempty + ("*")
        else:
            anotherempty  = anotherempty + t
    else:
        anotherempty = anotherempty + (t.lower())
print("asterik: " + anotherempty)


thisway = 0
thatway = 0
ask = ("avashah()(((")
for y in ask:
    if "(" in y:
        thisway = thisway + 1
    elif ")" in y:
        thatway = thatway + 1

if thisway == thatway:
    print("Balanced? True.")
else:
    print("Balanced? False.")


    

