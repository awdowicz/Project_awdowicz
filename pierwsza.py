def czy_pierwsza(liczba):
    if liczba > 9223372036854775807:
        return 'Podałeś za dużą liczbę'
    if liczba < 1:
        return 'Podana liczba nie jest liczbą pierwszą'
    if liczba == 2:
        return 'Podana liczba jest liczbą pierwszą'
    for i in range(2, liczba):
        if (liczba % i) == 0:
            return 'Podana liczba nie jest liczbą pierwszą'
    return 'Podana liczba jest liczbą pierwszą'

