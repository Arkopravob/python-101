a ="dsgbe#72t8"
char = 0
dig = 0
spChar =0
for i in a:
    if i.isalpha():
        char+=1
    elif i.isdigit():
        dig+=1
    else:
        spChar+=1;
print(f"your digit is {dig} and char is {char} and special character is{spChar}")