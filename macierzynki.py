import numpy as np

aa = int(input("Podaj liczbe wierszy macierzy 1: \n"))
ab = int(input("Podaj liczbe kolumn macierzy 1: \n"))
ba = int(input("Podaj liczbe wierszy macierzy 2: \n"))
bb = int(input("Podaj liczbe kolumn macierzy 2: \n"))

if ab != ba:
    print("ILOCZYN A*B JEST NIEMOŻLIWY, PONIEWAZ ILOSC KOLUMN MACIERZY 1 JEST ROZNA OD LICZBY WIERSZY MACIERZY 2")
    pass
else:
    mac1 = np.random.randint(1000, size = (aa, ab))
    mac2 = np.random.randint(1000, size = (ba, bb))

    print("MACIERZ 1:")
    print(mac1)
    print("MACIERZ 2:")
    print(mac2)
    print("Dodawanie macierzy:")
    print(mac1 + mac2)
    print("Mnozenie macierzy")
    print(mac1 * mac2)
