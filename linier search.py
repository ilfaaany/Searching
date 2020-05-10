def liniersearch(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return False


arr = [1 , 3 , 6 , 7 , 10 , 90]
yangdicari = 90
hasil = liniersearch(arr, len(arr), yangdicari)
if hasil:
    print("Elemen di temukan di index ke", hasil)
else:
    print("Elemen yang dicari tidak ada dalam array")
