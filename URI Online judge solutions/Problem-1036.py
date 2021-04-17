while True:
    F = float(input())
    if F> 100 or F<0:
        print("Fora de intervalo")
    elif F>= 0 and F<= 25.0000:
        print("Intervalo [0,25]")
    elif F>= 25.00001 and F<=50.0000000:
        print("Intervalo (25,50]")
    elif F>= 50.0000001 and F<= 75.000000:
        print("Intervalo (50,75]")
    elif F>=75.0000001 and F<=100.0000000:
        print("Intervalo (75,100]")
