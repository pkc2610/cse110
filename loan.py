loansize=input("How large is the loan?")
credhis=input("How good is your credit history?")
income=input("How high is your income?")
downpay=input("How large is your down payment?")

loandecision= False

if loansize>=5: 
    if credhis>=7 and income>=7:
        loandecision= True 
    elif credhis>=7 or income>=7:
        if downpay>=5:
            loandecision=True
        else: loandecision=False
