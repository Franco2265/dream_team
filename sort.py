def bubble_sort(lista):
    n = len(lista)
    scambi = True  # Ottimizzazione: verifica se ci sono stati scambi
    while scambi:
        scambi = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                # Scambia gli elementi se non sono nell'ordine corretto
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                scambi = True
        n -= 1 #Ottimizzazione: ogni volta che si itera un numero finisce nella posizione giusta
    return lista

# Esempio di utilizzo:
lista_non_ordinata = [5, 1, 4, 2, 8]
lista_ordinata = bubble_sort(lista_non_ordinata)
print("Lista ordinata:", lista_ordinata)  # Output: Lista ordinata: [1, 2, 4, 5, 8]
