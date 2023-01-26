# Les différents types de tri
Il existe plusieurs algorithmes de tri différents, chacun ayant des avantages et des inconvénients en termes de complexité algorithmique, de mémoire utilisée et de facilité de mise en œuvre. Voici quelques exemples courants d'algorithmes de tri :

* Tri à bulles (Bubble Sort) : c'est un algorithme de tri simple qui fonctionne en comparant chaque élément consécutif de la liste et en échangeant leurs positions si nécessaire. Il a une complexité temporelle de `O(n^2)` dans le pire des cas, ce qui le rend peu efficace pour des listes de grande taille.

* Tri par insertion (Insertion Sort) : cet algorithme de tri fonctionne en divisant la liste en deux parties : une partie triée et une partie non triée. Il insère chaque élément de la partie non triée dans la partie triée en utilisant des comparaisons et des échanges. Il a une complexité temporelle de `O(n^2)` dans le pire des cas, mais est plus efficace que le tri à bulles pour des listes de petite taille ou presque triées.

* Tri rapide (QuickSort) : c'est un algorithme de tri rapide qui utilise une technique de partitionnement pour diviser la liste en deux sous-listes, puis trie récursivement ces sous-listes. Il a une complexité temporelle de `O(n log(n))` en moyenne, mais peut être de `O(n^2)` dans le pire des cas. Il est généralement considéré comme l'un des algorithmes de tri les plus efficaces pour des listes de grande taille.

* Tri fusion (Merge Sort) : c'est un algorithme de tri stable qui utilise une technique de partitionnement pour diviser la liste en sous-listes, puis fusionne ces sous-listes triées pour créer la liste triée finale. Il a une complexité temporelle de `O(n log(n))` dans tous les cas.

* Tri par comptage (Counting Sort) : cet algorithme de tri est efficace pour des listes d'entiers avec des valeurs limitées. Il utilise une technique de comptage pour compter le nombre d'occurrences de chaque valeur dans la liste, puis génère la liste triée en utilisant ces informations de comptage. Il a une complexité temporelle de `O(n+k)` où `k` est la valeur maximale de la liste.

* Tri par sélection (Selection Sort) : c'est un algorithme de tri simple qui fonctionne en sélectionnant le plus petit élément de la liste non triée et en le déplaçant à la fin de la liste triée. Il a une complexité temporelle de `O(n^2)` dans le pire des cas, c'est un algorithest un algorithme peu efficace pour des listes de grande taille.

* Tri par tas (Heap Sort) : c'est un algorithme de tri basé sur l'utilisation d'un tas binaire pour organiser les éléments de la liste. Il a une complexité temporelle de O(n log(n)) dans tous les cas.

* Tri radix (Radix Sort) : cet algorithme de tri est efficace pour des listes d'entiers avec des valeurs de grande taille. Il trie les éléments en utilisant les chiffres individuels (ou "radix") des nombres, en commençant par le chiffre des unités et en finissant par le chiffre des unités de puissance supérieure. Il a une complexité temporelle de `O(nk)` où `k` est le nombre de chiffres dans la valeur la plus grande.

## Tri à bulles (Bubble Sort) :
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
### Tri par insertion (Insertion Sort) :
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```
## Tri rapide (QuickSort) :
```python
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)
    return arr
```
## Tri fusion (Merge Sort) :
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] =L[i]
                i += 1
                else:
                arr[k] = R[j]
                j += 1
                k += 1
            while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
```
## Tri par comptage (Counting Sort) :
## Tri par sélection (Selection Sort) :
## Tri par tas (Heap Sort) :
```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
 
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
 
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```
