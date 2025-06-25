money = False
if money:
    moveMethod = "택시타고 가라"
else:
    moveMethod = "걸어가라"
#print(moveMethod)

x=3
y=2
#if x>y:
#    print("빙고")

money = 3000
taxiTax = 3000
if money>taxiTax:
    moveMethod = "택시타고 갈란다"
else:
    if money==taxiTax:
 #       print("------------")
        moveMethod='고민한다'
    else:
        moveMethod = "걸어 갈란다"
#print(moveMethod)
#--------------------------------------------------------
if money>taxiTax:
    moveMethod='taxi'
elif money==taxiTax:
    moveMethod='thinking'
else:
    moveMethod='walking'
#print(moveMethod)

#---------------------------------------------------------

pocket = ['paper','cellphone']
card = True
if "paper" in pocket:
    print('택시타고 가라')
elif card:
    print('택시타고 카드로 내라')
else:
    print('걸어가라')

#--------------------------------------------    
score =50
message = "success" if score >= 60 else "failure"

print(message)
