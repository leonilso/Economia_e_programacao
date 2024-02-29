import sympy as sp
print("--------------------------------------------------------------------------------------")
print("---------------------Maximização-de-Lucro-em-um-mercado-monopolista-------------------")
print("--------------------------------------------------------------------------------------")
demanda = input("Informe a função da demanda em q: \n(OBS: somente a parte depois do igual) \n")
custo = input("Informe a função do custo em q: \n(OBS: somente a parte depois do igual) \n")

x = sp.symbols('q')

demanda = sp.S(demanda)
custo = sp.S(custo)

receita = demanda*x

receita_marginal = sp.diff(receita, x)
custo_marginal = sp.diff(custo, x)

maximo = (sp.solve(sp.Eq(receita_marginal, custo_marginal), x))[0]

demanda_maxima = demanda.subs(x, maximo)
custo_medio = custo/x
custo_medio = custo_medio.subs(x, maximo)
lucro_medio = demanda_maxima - custo_medio
lucro_total = maximo*lucro_medio

print("--------------------------------------------------------------------------------------")
print("---------------------------------------Respostas--------------------------------------")
print("--------------------------------------------------------------------------------------")

print(f"A quantidade Q em que os lucros são máximizado é: {maximo}")
passos = input('Pressione "e" para exibir o passo-a-passo da resolução do problema: \n')

if passos == "e":
    print(f"Para sabermos nosso Q* vamos utilizar as informações dadas no problema: \nNossa demanda é: {demanda}\nNosso custo é: {custo}")
    print(f"A condição de maximizar lucros é dada pela \u0394\u03C0/\u0394Q = \u0394R/\u0394Q  - \u0394C/\u0394Q = 0\nEm que:")
    print(f"\u0394R/\u0394Q é a receita marginal ou seja a derivada da receita total")
    print(f"\u0394C/\u0394Q é o custo marginal ou seja a derivada da custo total")
    print(f"Ou seja a condição para maximizar os lucros é Receita marginal = Custo Marginal")
    print(f"O nosso custo é informado no problema, fazemos a derivada, então nosso custo marginal é: {custo_marginal}")
    print(f"Para a receita marginal primeiro devemos calcular a receita que é dada por R = P * Q, ou seja, R = {receita} ")
    print(f"A receita marginal é a derivada disso em relação a Q: {receita_marginal}")
    print(f"Igualamos e obtemos o valor de Q que maximiza os lucros: {maximo}")
    print(f"Podemos calcular outras informações como o preço na quantidade Q = {maximo} que é: {demanda_maxima}")
    print(f"Podemos calcular o custo médio que é o custo total dividido pela quantidade: {custo_medio}")
    print(f"O lucro médio que é o preço quando Q é máximo menos o custo médio: {lucro_medio}")
    print(f"E por fim o lucro total que é o custo médio X a quantidade: {lucro_total}")
    input()
