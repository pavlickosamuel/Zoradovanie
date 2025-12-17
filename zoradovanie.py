import random


#generate list
def generuj(n: int) -> list:
    zoznam1 = []
    for i in range(n):
        zoznam1.append(random.randint(1, 100))
    return zoznam1


#bubble sort
def bubble_sort(zoznam: list, dlzka: int):
    for j in range(len(zoznam), 1 , -1):
        for i in range(0 , j - 1):
            if zoznam[i] > zoznam[i+1]:
                zoznam[i], zoznam[i+1] = zoznam[i+1], zoznam[i] #python swap


#sort by maximum
def sort_by_max(zoznam: list, dlzka: int):
     for j in range(len(zoznam), 1 , -1):
        max_index = 0
        for i in range(1 , j):
            if zoznam[i] > zoznam[max_index]:
                 max_index = i
            zoznam[max_index], zoznam[j-1] = zoznam[j-1], zoznam[max_index] #python swap


#





#test
test_list = generuj(10)
print(test_list)
bubble_sort(test_list, len(test_list))
print(test_list)

test_list2 = generuj(10)
print(test_list2)
sort_by_max(test_list2, len(test_list2))
print(test_list2)
     