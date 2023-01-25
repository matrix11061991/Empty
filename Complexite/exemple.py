import time
# Algorithme de tri à bulles
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Algorithme de tri rapide (QuickSort)
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Génération de liste aléatoire de taille n
n = 100000
arr = [i for i in range(n)]

# Mesure du temps d'exécution pour chaque algorithme
start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print("Temps d'exécution de l'algorithme de tri à bulles:", end_time - start_time)

start_time = time.time()
quick_sort(arr, 0, n-1)
end_time = time.time()
print("Temps d'exécution de l'algorithme de tri rapide:", end_time - start_time)
