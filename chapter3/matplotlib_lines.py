from matplotlib import pyplot as plt

def main():
    '''
    grafico de linhas pode ser usado para indicar tendencias
    '''
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    # podemos chamar o plt.plot varias vezes para
    # multiplas linhas em um grafico
    plt.plot(xs, variance, 'g-', label='variance')       # linha verde solida
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')     # tracejado vermelho
    plt.plot(xs, total_error, 'b:', label='total error') # pontilhado azul

    plt.legend(loc=9)
    plt.xlabel("complexidade do modelo")
    plt.title("Compromisso entre Polarizacao e Variancia")

    plt.show()

if __name__ == "__main__":
    main()