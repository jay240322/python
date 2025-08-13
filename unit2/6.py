def remove(duplicate):
    final = []
    for num in duplicate:
        if num not in final:
            final.append(num)
    return final
duplicate = [1,1,2,3,4,3,0,0]
print(remove(duplicate))