from colorama import *
from os import system
init()
while True:
        try:
	    system('cls')
        except:
            system('clear') 
	print(Fore.MAGENTA)
	print('░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░')
	print('██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗')
	print('██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝')
	print('██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗')
	print('╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║')
	print('░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝ by Endy_Cat')
	print(Fore.WHITE + '██████████████████████████████\n' + Fore.BLUE + '██████████████████████████████\n' + Fore.RED + '██████████████████████████████')
	try:
		print(Fore.GREEN)
		primer = input('Ваш пример: ')
		print(Fore.BLUE)
		print('Ответ: ' + str(eval(primer)))
	except:
		print(Fore.RED)
		print('Вы указали буквы! Допускаются все цифры и знаки: * + - / % .')
	print(Fore.YELLOW)
	input('Жми enter чтобы продолжить или c + ctr чтобы выйти.')
