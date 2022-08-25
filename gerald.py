nombreASaisir = input("Saisir un nombre : ");
resultat = 0;

def factorielle(nombre=1):
    resultatFactorielle = 1;
    # Produits
    for nombreDeBoucle in range(1, nombre+1):
        resultatFactorielle = resultatFactorielle * nombreDeBoucle;
    return resultatFactorielle;

# Somme finale des factorielles du nombre saisi
for i in nombreASaisir:
    resultat += factorielle(int(i));

if (resultat == int(nombreASaisir)):
    print("super nombre");
else:
    print("naze");
