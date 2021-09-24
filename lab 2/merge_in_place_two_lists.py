import math
L=[1,6,12,3,54,21,34,5,8]

end=None

def merge (L, start, center, finish):
    inv_count=0
    i = start
    j = center + 1
    L2 = []
    while (i <= center) and (j <= finish):
        if L[j] < L[i]:
            inv_count += (center - i + 1)
            L2.append(L[j])
            j +=1
        else:
            L2.append(L[i])
            i += 1
        end
    end

    if i <= center:
        while i <= center:
            L2.append(L[i])
            i +=1
        end
    else:
        while j <= finish:
            L2.append(L[j])
            j +=1
        end
    end
    s = finish - start + 1
    i = 0
    while i < s:
        L[start + i] = L2[i]
        i += 1
    end
    return inv_count
end


def merge_sort (L, start, finish):
    inv_count = 0
    if start != finish:
        center = int(math.floor((start + finish) / 2))
        inv_count +=merge_sort(L, start, center)
        inv_count +=merge_sort(L, center + 1, finish)
        inv_count +=merge(L, start, center, finish)
    end
    return inv_count
end
arr = [1, 20, 6, 4, 5]
result=merge_sort(L,0, len(L)-1)
print(result)
			
