from matplotlib import pyplot as plt

def main():
    '''
    grafico de dispersao eh bom para visualizar o relacionamento entre dois pares
    de conjuntos de dados
    '''
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
            xy=(friend_count, minute_count),
            xytext=(5, -5),
            textcoords='offset points')

    plt.title("Minutos Diarios vs Numero de Amigos")
    plt.xlabel("# de amigos")
    plt.ylabel("minutos diarios passados no site")
    plt.show()

if __name__ == "__main__":
    main()