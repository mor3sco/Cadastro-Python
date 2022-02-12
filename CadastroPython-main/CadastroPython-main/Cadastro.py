#Classe de cores
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    AZUL = '\033[1;34m '
user = "andre"
password = "1234"
CPF = ["xxx.xxx.xxx-xx"]
#Inicio do Programa
en = ("N")
while en == ("N") and en!=("S"):
   print(f'''{bcolors.WARNING}
   +-------------------+
   |Sistema de Cadastro|
   +-------------------+
   {bcolors.RESET}''')
   #OPÇÕES
   print(f'''{bcolors.OK}
   [1] - Iniciar ]
   [2] - Login   ]
   [3] - Sair    ]
   {bcolors.RESET}''')
   cadastro = input('Qual opção: ')
   #Estrutura de Decisão 
   if cadastro == ("1"):
      print('''[Página de Cadastro]''')
      user = input('Qual seu usuário: ')
      #Enquanto usuario for menor que 6 caracteres
      while len(user) < 6:
        print('Nome de Usúario Fraco! ')
        user = input('Qual seu Usúario: ')
      password = input('Criar senha:')
      #Enquanto senha for menor que 6 caracteres
      while len(password) < 6:
        print('Senha Fraca! ')
        password = input('Criar senha: ')
        #Caso maior Sucesso!
      print('Registrado Com Sucesso! ')
   elif cadastro == ("2"):
       print('''
        Login
       --------
       ''')
       logname = input("Digite seu Usúario:")
       logsenha= input("Digite sua Senha:")
       while logname != user or logsenha != password:
           print("Usuário e Senha Invalidos!!!")
           logname = input("Digite seu Usúario:")
           logsenha= input("Digite sua Senha:")
           if logname == ("z"):
               print("Programa Encerrado")
               exit()
       print("Logado com Sucesso!!!")
       print('''
       ---------------
        Seu Cadastro
       ---------------
       Nome Completo:
       CPF: {}
       Usuário: {}
       Senha: {}

       '''.format(CPF,user,password))
       
   elif cadastro == ("3"):
      print("Saindo Do Sistema....")
      print("Programa Encerrado!")
      exit()
      
      #Caso não seja nem S e N retorna invalido
   else:
      print("Opção Invalida!")
   en = input("Deseja Sair[S/N]:")
   #Enquanto for diferente de S e N é opção invalida até ser igual:
   while en != ("S") and en !=("N"):
       print("Opção Invalida")
       en = input("Deseja Sair[S/N]:")
print("Programa Encerrado")
