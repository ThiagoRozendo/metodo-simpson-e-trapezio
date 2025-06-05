# Método de Simpson e Trapézio

Este projeto implementa métodos numéricos de integração: Simpson e Trapézio composto, com cálculo de erro estimado.

## Requisitos

- Python 3.8+
- [NumPy](https://numpy.org/)
- [SymPy](https://www.sympy.org/)
- [SciPy](https://scipy.org/)

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/metodo-simpson-e-trapezio.git
   cd metodo-simpson-e-trapezio
    ```

2. Instale as dependências:
   ```sh
   pip install numpy sympy scipy
   ```


## Como rodar
Execute o script principal:
```sh
python metodos.py
```
O programa irá solicitar:

- Limite inferior a

- Limite superior b

- Número de subintervalos n

- Escolha do método (Simpson ou Trapézio)


## Como passar a função
No início do arquivo metodos.py, edite a linha 48:

```python
f_expr = x ** 2 
```
Altere para a função desejada, por exemplo:

f_expr = x**2 + 3*x + 1
## ou 
```python
f_expr = cos(x)
```
Use funções do SymPy (sin, cos, exp, etc.) e a variável x já definida.

## Exemplo de execução:
```
Função escolhida: cos(x)
Digite o limite inferior a: 0  
Digite o limite superior b: 2  
Digite o número de subintervalos (n): 4


Escolha o método de integração:  
1 - Método de Simpson (n deve ser par)   
2 - Método do Trapézio composto

Digite 1 ou 2: 1

Integral aproximada ≈ 0.9096228049035733
Erro estimado ≤ 0.0006944444444387921
```