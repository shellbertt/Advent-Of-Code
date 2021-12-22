from aocd import lines

def moreCommon(lis, pos):
    count = 0
    for l in lis:
        if l[pos] == '1':
            count += 1
    if count > len(lis) / 2: return '1'
    elif count < len(lis) / 2: return '0'
    else: return 't'

O2 = lines.copy()
CO2 = lines.copy()

for i in range(12):
    commonO2 = moreCommon(O2, i)
    if commonO2 == '1' or commonO2 == 't': O2 = list(filter(lambda l: l[i] != '0' or len(O2) == 1, O2))
    else: O2 = list(filter(lambda l: l[i] != '1' or len(O2) == 1, O2))
    
    commonCO2 = moreCommon(CO2, i)
    if commonCO2 == '1' or commonCO2 == 't':
        CO2 = list(filter(lambda l: l[i] != '1' or len(CO2) == 1, CO2))

    else:
        CO2 = list(filter(lambda l: l[i] != '0' or len(CO2) == 1, CO2))

print(int(O2[0], 2) * int(CO2[0], 2))
