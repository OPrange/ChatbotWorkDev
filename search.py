import wikipedia
while True:
	wikipedia.set_lang('pt')
	busca = str(input('O que deseja buscar?'))
	l = wikipedia.search(str(busca))
	print (wikipedia.summary(busca, sentences = 1))
