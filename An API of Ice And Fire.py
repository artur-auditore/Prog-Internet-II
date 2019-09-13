import json, requests

def main():

	
	print("An API of Ice And Fire\n")
	print("1. Books\n2. Characters\n3. Houses\n")

	while (True):

		response = requests.get("https://www.anapioficeandfire.com/api") #só permite o método get
		opcao = int(input("Opção: "))	

		if opcao == 1:
			id = input("Digite o id do livro: ")
			nova_url = response.url+"/books/"+str(id)
			response = requests.get(nova_url)
			livro = json.loads(response.content)
			
			print("Livro\n")
			print("Livro: %s" %livro["name"])
			print("Autor: %s" %livro["authors"][0])

		elif opcao == 2:
			id = input("Digite o id do personagem: ")
			nova_url = response.url+"/characters/"+str(id)
			response = requests.get(nova_url)
			personagem = json.loads(response.content)

			#Apenas dados mais relevantes
			print("Personagem:\n")
			print("Nome: %s" %personagem["name"])
			print("Genero: %s" %personagem["gender"])
			print("Pai: %s" %personagem["father"])
			print("Mãe: %s" %personagem["mother"])
			print("Ator: %s" %personagem["playedBy"][0])
			#for dados in personagem:
			#	print(dados, personagem[dados])

		elif opcao == 3:
			id = input("Digite o id da casa: ")
			nova_url = response.url+"/houses/"+str(id)
			response = requests.get(nova_url)
			house =  json.loads(response.content)

			print("%s" %house["name"])
			print("Palavras: %s" %house["words"])

		elif opcao == 0:
			break
		else:
			print ('Opcao Invalida!')
	print ('Finalizado!')

if __name__ == '__main__':
	main()