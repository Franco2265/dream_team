import random

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogosort(arr):
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    print(f"Ordinato dopo {attempts} tentativi.")
    return arr

# Esempio di utilizzo
if __name__ == "__main__":
    arr = [3, 2, 5, 1, 4]
    print("Array originale:", arr)
    sorted_arr = bogosort(arr)
    print("Array ordinato:", sorted_arr)
