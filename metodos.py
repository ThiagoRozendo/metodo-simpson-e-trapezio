import numpy as np
import sympy as sp
from sympy import *
from scipy.optimize import minimize_scalar

def simpsons_rule(f, a, b, n): #funcao que aplica o metodo de Simspson
    h = (b - a) / n
    xs = np.linspace(a, b, n + 1)
    ys = f(xs)
    S = ys[0] + ys[-1] + 4 * np.sum(ys[1:-1:2]) + 2 * np.sum(ys[2:-2:2])
    integral = S * h / 3
    return integral

def max_abs_fourth_derivative(f_expr, a, b):# calcula o valor maximo absoluto da quarta derivada de f_expr no intervalo [a, b]
    x = sp.symbols('x')
    f4_expr = sp.diff(f_expr, x, 4)  # quarta derivada simbolica
    f4 = sp.lambdify(x, f4_expr, 'numpy')  # convertendo para função numerica 

    # busca o maximo absoluto da quarta derivada 
    res = minimize_scalar(lambda t: -abs(f4(t)), bounds=(a, b), method='bounded')
    max_val = abs(f4(res.x))
    return max_val

def simpsons_error(a, b, n, max_f4): # funcao que calcula o erro estimado
    h = (b - a) / n
    erro = ((b - a) * h**4) / 180 * max_f4
    return erro

def trapezio_composto(f, a, b, n): #funcao que aplica o metodo do trapezio composto
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        soma += 2 * f(x)
    integral = (h / 2) * soma
    return integral

def erro_estimado_trapezio(f2_max, a, b, n): #funcao que calcula o erro estimado do metodo
    erro = ((b - a)**3 / (12 * n**2)) * f2_max
    return erro

# main

if __name__ == "__main__":
    x = sp.symbols('x')  #definindo x como uma icognita/simbolo matematico

    #funcao simbolica, nesse caso é x^2 (aqui, pode colocar qualquer funcao a qual deseja aplicar o metodo)
    f_expr = cos(x)
    # cria a funcao numerica para avaliacao com numpy
    f_num = sp.lambdify(x, f_expr, modules=['numpy'])

    print(f"Função escolhida: {f_expr}")

    a = float(input("Digite o limite inferior a: "))
    b = float(input("Digite o limite superior b: "))

    while True:
        try:
            n = int(input("Digite o número de subintervalos (n): "))
            if n > 0:
                break
            else:
                print("Por favor, insira um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    print("\nEscolha o método de integração:")
    print("1 - Método de Simpson (n deve ser par)")
    print("2 - Método do Trapézio composto")
    while True:
        metodo = input("Digite 1 ou 2: ").strip()
        if metodo in ['1', '2']:
            break
        else:
            print("Opção inválida. Digite 1 ou 2.")

    if metodo == '1':
        # verifica se n é par para o metodo de Simpson
        if n % 2 != 0:
            print("Número de subintervalos para Simpson deve ser par. Ajustando n = n + 1.")
            n += 1

        # calcula o maximo absoluto da quarta derivada no intervalo [a,b]
        max_f4 = max_abs_fourth_derivative(f_expr, a, b)

        # calcula a integral aproximada usando o metodo de Simpson
        integral = simpsons_rule(f_num, a, b, n)

        # calcula o erro
        erro_estimado = simpsons_error(a, b, n, max_f4)

        print(f"\nIntegral aproximada ≈ {integral}")
        print(f"Erro estimado ≤ {erro_estimado}")

    else:
        # calcula a segunda derivada da função simbolica
        f2_expr = sp.diff(f_expr, x, 2)
        f2 = sp.lambdify(x, f2_expr, 'numpy')

        # busca o maximo absoluto da segunda derivada
        res_f2 = minimize_scalar(lambda t: -abs(f2(t)), bounds=(a, b), method='bounded')
        f2_max = abs(f2(res_f2.x))
        
        # chama a funcao para aplicar o metodo do trapezio sobre a funcao f, no intervalo de [a, b], e n trapezios
        integral = trapezio_composto(f_num, a, b, n)

        # chama a funcao para verificar o erro
        erro_estimado = erro_estimado_trapezio(f2_max, a, b, n)

        # resultados
        print(f"\nIntegral aproximada ≈ {integral}")
        print(f"Erro estimado ≤ {erro_estimado}")