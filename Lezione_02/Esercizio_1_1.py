'''
Esercizio 1.1
Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare 1.0/x memorizzare il risultato nella variabile y.
    Visualizzare il valore di x, y e il prodotto tra x e y.
    Sottrarre x dal prodotto tra x e y e mostrarne il risultato.

'''

x:float = 15.25
print(f"x vale {x}")
y:float = 1.0 / x
print(f"y vale {y:.2f}")

z:float = x * y
print(f"x*y vale {z:.2f}")

print(f"(x*y)-x vale {z-x:.2f}")
     
