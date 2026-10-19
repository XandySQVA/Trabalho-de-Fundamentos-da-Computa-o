import random
listaDeRespostas = ["É certo", "É decididamente assim", "Sem dúvida", "Sim, definitivamente", "Você pode contar com isso", "É promissor", "As perspectivas são boas", "Sim", "Sinais apontam que sim", "Provavelmente", "Responda mais tarde", "Melhor não te dizer agora", "Não posso prever agora", "Concentre-se e pergunte novamente", "É difícil dizer agora", "Não conte com isso", "Minha resposta é não", "Minhas fontes dizem que não", "Perspectiva não muito boa", "Muito duvidoso"]

while True:
  print("--------------------------- \n\tBola 8 Mágica \n---------------------------")
  pergunta = input("Faça sua pergunta: \n\n")
  print(random.choice(listaDeRespostas))
