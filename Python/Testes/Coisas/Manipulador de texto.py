#.upper() = Passa o texto para maíusculo.
#.lower() = Passa o texto para minusculo.
#.count = conta todas as letras selecionadas no texto.
#len() = conta quantas letras tem no texto.
#.strip = remove os espaços da 'direita e esquerda' do texto.
#.replace = troca uma frase escolhida do texto por outra.
#.find = localiza a frase dentro do texto.
#.split = Divide toda a frase.
text = """John Von Neumann foi um matemático húngaro de origem
judaica, que foi naturalizado americano nos anos 30 
do século XX. Nasceu em 28 de dezembro de 1903.
Desenvolveu contribuições importantes em Mecânica
Quântica, Teoria dos conjuntos, Ciência da Computação,
Economia, Teoria dos Jogos e praticamente todas 
as áreas da Matemática. Faleceu no dia 8 de Fevereiro de 1957
, vítima de um tumor no cérebro. Foi também professor na 
Universidade de Princeton e um dos construtores do ENIAC
(o primeiro computador eletrônico)."""
print(text.split())

print("A frase john Von Neumann tem: {} vezes e localiza-se ná posição {} no texto".format(text.count("John Von Neumann"), text.find("John Von Neumann")))