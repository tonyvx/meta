def sub_array(arr, k):
    sub = []

    for idx, val in enumerate(arr):
        # initialize
        temp = int(val)
        i = idx
        new_arr = [temp]

        # loop backwards if current value not equal to k and exit once its equal or greater
        while ((temp < k) & (i > 0)):
            i = i-1
            temp = temp + int(arr[i])
            new_arr.append(int(arr[i]))

        # if sub arr sum is equal to k add to valid sub arrays
        if (temp == k):
            sub.append(new_arr)

    # publish sub arrays for k
    print("\n\nOutput:\nFor k = ", k, " found ", len(sub),
          " sub arrays \n\n Sub Array Details: \n", sub)


print('Enter array separated by space: ')
arr = input().split(" ")
print('Enter k: ')
k = input()
sub_array(arr, int(k))
