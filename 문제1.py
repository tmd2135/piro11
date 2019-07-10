qusetion1 = ['apple','apps','ape']
qusetion2 = ['hawaii','happy']
qusetion3 = ['dog','dogs','dogs']

all = [qusetion1,qusetion2,qusetion3]

result=[]

result1='';  result2=''; result3=''

maxlen=6; minlen=3

for i in range(maxlen):
    if qusetion1[0][i] == qusetion1[1][i] == qusetion1[2][i]:
        result1 += qusetion1[i][i]
    else:
        result.append(result1)
        break

for i in range(maxlen):
    if qusetion2[0][i] == qusetion2[1][i]:
        result2 += qusetion2[i][i]
    else:
        result.append(result2)
        break

for i in range(minlen):
    if qusetion3[0][i] == qusetion3[1][i] == qusetion3[2][i]:
        result3 += qusetion3[i][i]
result.append(result3)

print(result)
for i in range(0,3):
    print("입력 : ", end='')
    print(all[i])
    print('출력 : ',end='')
    print(result[i])