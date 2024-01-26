loansize=int(input("How large is the loan?"))
credhis=int(input("How good is your credit history?"))
income=int(input("How high is your income?"))
downpay=int(input("How large is your down payment?"))

loandecision= False

if loansize >= 5: 
    if credhis >= 7 and income >= 7:
        loandecision= True 
    elif credhis >= 7 or income >= 7:
        if downpay >= 5:
            loandecision = True
        else: loandecision = False
    else: loandecision = False
else:
    if credhis < 4:
        loandecision = False
    else: 
        if income >= 7 or downpay >= 7:
            loandecision = True
        if income >= 4 and downpay >= 4:
            loandecision = True
        else:
            loandecision = False