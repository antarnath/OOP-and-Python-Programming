list = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
ans = []
for i in list:
    val = 0
    for j in range(len(i)):
        val += ord(i[j])
        
    if i=='-1':
        continue

    tmp = []
    
    for k in list:
        val1 = 0
        for l in range(len(k)):
            val1 += ord(k[l])
        if val==val1:
            tmp.append(k)
            list[list.index(k)] = '-1'
            
    ans.append(tmp)      

print(ans)
    