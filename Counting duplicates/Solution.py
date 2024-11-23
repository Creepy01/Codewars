def duplicate_count(text):
    textlow=text.lower()
    visited=[]
    dup=0
    for i in range(len(textlow)):
        if textlow[i] not in visited :
            if textlow.count(textlow[i])>1:
                dup+=1
                visited.append(textlow[i])
    return dup
