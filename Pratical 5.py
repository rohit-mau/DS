#LINEAR SEARCH
pos = -1

def search(list, n):
    i = 0

    while i< len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1;

    return False

list = [5,8,4,6,9,2]
n = 9

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not Found")
   
  #######################
   
#binary search
pos = -1

def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;

    return False


list = [4,7,8,12,45,99,102,702,10987,56666]
n = 8

if search(list, n):
    print("BINARY SEARCH Found at ",pos+1)
else:
    print("BINARY SEARCH Not Found")
