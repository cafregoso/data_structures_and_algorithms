def mover(n, origen, destino, aux):
    if n > 0:
        mover(n-1, origen, aux, destino)
        print(n, origen, aux, destino)
        destino.append(origen.pop())
        mover(n-1, aux, destino, origen)
        print(n, origen, aux, destino)


if __name__ == "__main__":
    n = 7
    A = [i for i in range(n, 0, -1)]
    B = []
    C = []

    print(A, B, C)
    mover(n, A, B, C)
