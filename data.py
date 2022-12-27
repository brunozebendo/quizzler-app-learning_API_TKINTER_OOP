import requests
"""a intenção do código é buscar dez questões no site abaixo através de um API e então gerar um sistema de trivia,
 para isso, primeiramente, importou a biblioteca request, que é a que trabalha com API, depois, no site da trivia,
onde estão armazenadas as questões, foi na opção API, selecionou os parâmetros que quer importar, no caso, a
 quantidade de dez questões por vez e o tipo booleano, e gerou o link abaixo. O link é passado para a variável
 response, assim como os parâmetros. A função do raise_for_status é lidar com erros no requerimento da API, depois,
 o data guarda o variável response em um data, no formato json, então, por fim, o question data guarda o campo
  results. Esse código já havia sido parcialmente criado em uma aula anterior, mas sem a parte visual
"""
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
