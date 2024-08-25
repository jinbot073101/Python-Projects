def evaluate(number):
    valid = False
    divided = list(str(number))
    discarded = divided[::2]
    discarded.reverse()
    sum = 0
    for j in discarded:
        num = int(j) * 2
        if num >= 10:
            num = num%10 + (num%100)//10
        sum += num
    if sum%10 == 0:
        valid = True
    return valid
          
number = input('Credit card number -> ')
if evaluate(number):
    print('\n[ The credit card is valid ]\n')
else:
    print('\n[ The credit card is not valid ]\n')