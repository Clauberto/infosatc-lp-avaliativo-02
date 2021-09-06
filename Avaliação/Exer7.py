filmes = []
jogos = []
livros = []
esporte = []
#a. Adicione no mínimo 2 itens em cada lista.
filmes.append("Homem de Ferro")
filmes.append("Vingadores: Guerra Infinita")
jogos.append("The Witcher 3")
jogos.append("Minecraft")
livros.append("O Diário de Anne Frank")
livros.append("A Sutil Arte De Ligar O F*da-Se")
esporte.append("Futebol")
esporte.append("Voleibol")
print(filmes)
print(livros)
print(jogos)
print(esporte)
#b. Crie uma lista das 4 listas criadas acima.
lista_geral = [filmes,jogos,livros,esporte]
#c. Acesse (mostrar) algum item da lista de livros.
print(livros[1])
#d. Remova um item da lista esporte. 
del esporte[1]
print(esporte)
#e. Adicione uma lista chamada "disciplinas", no item b.
disciplina = ["Portugues","Matematica"]
lista_geral.append(disciplina)
print(lista_geral)