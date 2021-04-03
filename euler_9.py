num1 = 0
num2 = 0
num3 = 0
ONE = 0
TWO = 0
THREE = 0
tc = 1

for one in range(0,501):
    for two in range(0,501):
        for three in range(0,501):
            num1 = one
            num2 = two
            num3 = three
            if num1 < num2 < num3 and num1**2+num2**2 == num3**2 and num1+num2+num3 == 1000:
                ONE= num1
                TWO = num2 
                THREE = num3
    if tc % 50 == 0:
        print(f"{tc/5}%")
    tc += 1
print(f"{ONE} {TWO} {THREE}")
