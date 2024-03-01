
def main():

    grafo = []
    N, L = map(int, input().split())
    for i in range(L):
        line = list(map(int, input().split()[1:]))
        grafo.append(line)


if __name__  == '__main__':
    main()
