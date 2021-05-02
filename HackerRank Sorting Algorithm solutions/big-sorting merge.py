def big_sorting(L):
    size = len(L)
    if size > 1:
        mid = size//2
        left = L[:mid]
        len_left = len(left)
        right = L[mid:]
        len_right = len(right)

        big_sorting(left)
        big_sorting(right)

        i=j=k=0
        while i<len_left and j<len_right:
            if left[i]<right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1

        while i<len_left:
            L[k] = left[i]
            i += 1
            k += 1
        while j<len_right:
            L[k] = right[j]
            j += 1
            k += 1
    return L

if __name__ == "__main__":
    L = [int(input()) for i in range(int(input()))]
    big = big_sorting(L)
    for i in big:
        print(i)