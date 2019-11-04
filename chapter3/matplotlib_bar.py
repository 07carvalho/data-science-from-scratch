from matplotlib import pyplot as plt

def main():
    '''
    grafico de barra eh uma boa escolha para mostrar como quantidades variam
    entre um conjunto particular de itens
    '''
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    xs = [i + 0.1 for i, _ in enumerate(movies)]

    plt.bar(xs, num_oscars)

    plt.ylabel("# de Premiacoes")
    plt.title("Meus Filmes Favoritos")

    # nomeia o eixo x com nomes de filmes na barra central
    plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
    plt.show()

if __name__ == "__main__":
    main()