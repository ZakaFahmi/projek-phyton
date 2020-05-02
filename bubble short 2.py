def bidirectional_bubble_sort(a):
    left=-1
    right = len(a)
    while left < right:
        swap = False
        left += 1
        right -= 1
        for i in range(left, right):
            if a[i] < a[i + 1]:
                t = a[i]
                a[i] = a[i + 1]
                a[i + 1] = t
                swap = True
        if not swap:
            return a
        else:
            swap = False
        for i in range(right, left, -1):
            if a[i] > a[i - 1]:
                t = a[i]
                a[i] = a[i - 1]
                a[i - 1] = t
                swap = True
        if not swap:
            return a
x = [8,10,12,19,18,7,4,100,7,101,13]
print(bidirectional_bubble_sort(x))