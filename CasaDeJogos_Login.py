#Classes e Funções
import random
import csv
import os
import logging


logging.basicConfig(level=logging.INFO, filename="programa.log",format="%(asctime)s - %(levelname)s - %(message)s ") 
log = logging.getLogger("my-logger")
log.info("")
log.debug("")
log.error("")
log.warning("")

#C:\Users\geova\Desktop\Python\src\Parte1\Tarefa5LoginRegistros\baseDados.csv


p=[]
verifica = True 
#C:\Users\geova\Desktop\Python\src\Parte1\Tarefa5LoginRegistros\Login.csv
path = 'src'
check_file = os.path.isfile(path)
cont = True 
with open('src/Parte1/Tarefa5LoginRegistros/Login.csv',mode = 'r') as file: 
   csvFile = csv.reader(file)
   
   for lines in csvFile:
      p.append(lines) # p recebe linhas do ficheiro e ler
file.close()




def veriLogin(email,senha):#verifica se email e senha esta o ficheiro
  
   continua = True
   for linha in p:
         if email in linha and senha in linha:
            log.info("Acessou o sistema " + email)
            print ("BEM VINDO(A)")
            print( email)
            continua = False
            return continua
   log.warning("Falha no login")   
   return continua



def registrarEmailSenha(email,senha): #adiciona no ficheiro
   log.info("Novo Registro email com sucesso: " + email)
   with open('src/Parte1/Tarefa5LoginRegistros/Login.csv','a',newline='') as file:
      csvFile = csv.writer(file)
      csvFile.writerow([email,senha])
      p.append([email,senha])
      print("\nlogin registrado com sucesso.")
      print("Seu novo acesso é email:",email,"\n")   
      file.close()
      return

            
def VerificaçãoEmail(email): #verifica se email existe
       
   for lines in p:
      if email in lines:
         verifica  = False
         return verifica

            
def VerificacaoCriacaoSenha(senha):     #verifica senha e condições 
         erros = []
         contLetra = 0
         contNumero = 0
         contEspaço = 0
         for i in senha:
            if i.isalpha():
               contLetra += 1
            elif i.isdigit():
               contNumero += 1
            elif i.isspace():
               contEspaço += 1
                     
         if len(senha) < 8:
            erros.append("Senha deve conter pelo menos 8 caracteres!")

         if len(senha) > 12:
            erros.append("Senha deve conter no maximo 12 caracteres!")

         if not contLetra:
            erros.append("Senha deve conter letras!")

         if not contNumero:
            erros.append("Senha deve conter números!")
         
         if contEspaço > 0:
            erros.append("Senha não deve conter espaços!")

         # conclusão
         if erros:
            print("Erros de senha:")
            log.error("Criação de senha invalido")
            verifica  = False
            for e in erros:
               print("-", e)
            return verifica
               
   
def displayMenu(): #menu
   print("     MENU    ")
   print("Escolha uma das opções: ")
   print("1- Ja tenho cadastro ")
   print("2- Sou novo por aqui, desejo fazer um cadastro ") 
   print("3- Sair")
   opcao = input("Opção -> ")   
   return opcao     

def displayBoasVindas(): #mensagem de boas vindas
   mensagem = ["***Bem Vindos!***", "***Bom Dia***","***Good Morning***", "***Seja Bem Vindo***","***Olá, Como esta?***"]
   msg = int (random.randrange(0,len(mensagem)))
   print(mensagem[msg])
    
def displayDespedida():#despedidadas
   mensagem = ["Até mais!", "Adeus","XAU", "Volte sempre"]
   msg =int (random.randrange(0,len(mensagem)))
   print(mensagem[msg])
   
   


def msgJogo():
    print("***VAMOS JOGAR PAR OU IMPAR***")
    aposta= input("Adivinhe o numero aleatório! \n Escolha PAR ou IMPAR?\n")
    aposta = aposta.upper() 
    return aposta
    
def JogoParImpar(escolha):
    NumAleatorio = random.randrange(1,21)
    if(NumAleatorio%2 == 0 ):
       res =  "PAR"
    else:
        res = "IMPAR"
        
    if (res == escolha ):
        print("Numero gerado foi: ",NumAleatorio)
        print("VOCÊ ACERTOU!")
    else:
        print("Numero gerado foi: ",NumAleatorio)
        print("ERROU!")
     
    return res

def JogoPedraPapelTesoura():
    PedraPTesouraM = ["PEDRA","PAPEL","TESOURA"]
    #num = random.randrange(0,4)
    num = 0
    print("PEDRA, PAPEL E TESOURA")
    #print("Computador escolheu ", PedraPTesouraM[num])
    nome = input ("Digite seu nome: ")
    
    cont = "S"
    while cont == "S" or cont == "s":
        
        escolhaJogador = input("ESCOLHA: PEDRA | PAPEL | TESOURA\n")
        escolhaJogador = escolhaJogador.upper()
            
        if (escolhaJogador == PedraPTesouraM[num]):
            print("O computador escolheu ",PedraPTesouraM[num] )
            print ("EMPATE")
        elif (escolhaJogador == "PEDRA" and PedraPTesouraM[num] == "TESOURA"):
            print("O computador escolheu ",PedraPTesouraM[num] )
            print ("Parabéns ",nome," você ganhou!")
        elif (escolhaJogador == "TESOURA"  and PedraPTesouraM[num] == "PEDRA"):
            print("O computador escolheu ",PedraPTesouraM[num] )
            print ("Você Perdeu! ")
        elif (escolhaJogador == "PAPEL" and PedraPTesouraM[num] == "PEDRA"):
            print("O computador escolheu ",PedraPTesouraM[num] )
            print ("Parabéns ",nome," você ganhou!")
        elif (escolhaJogador == "PEDRA" and PedraPTesouraM[num] == "PAPEL"):
            print("O computador escolheu ",PedraPTesouraM[num] )
            print ("Você Perdeu! ")
        elif (escolhaJogador == "TESOURA" and PedraPTesouraM[num] == "PAPEL"):
            print("O computador escolheu ",PedraPTesouraM[num] )
            print ("Parabéns ",nome," você ganhou!")
        elif (escolhaJogador == "PAPEL"  and PedraPTesouraM[num] == "TESOURA"):
            print("O computador escolheu ",PedraPTesouraM[num] )
            print ("Você Perdeu! ")
       
        cont = input ("Deseja continuar? [S/N]")

