def shellShort(arreglo):
    n = len(arreglo)
    gap = n//2 # int(n/2)
    while gap > 0:
        for i in range(gap, n):
            temp = arreglo[i]
            j = i
            while j >= gap and arreglo[j-gap] > temp:
                arreglo[j] = arreglo[j-gap]
                j -= gap # j = j - gap
            arreglo[j] = temp
        # print("\nEl arreglo al final del gap es: ")
        # print(arreglo)
        gap //= 2 # gap = int(gap/2)
    return arreglo
# r = [19,8,4,1,7,11,3,10,15]
# print(r)
# shellShort(r)
# print(r)



