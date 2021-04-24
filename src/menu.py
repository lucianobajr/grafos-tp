import os  
class bcolors:
    Preto = '\033[1;30m'
    Vermelho = '\033[1;31m'
    Verde = '\033[1;32m'
    Amarelo = '\033[1;33m'
    Azul = '\033[1;34m'
    Magenta = '\033[1;35m'
    Cyan = '\033[1;36m'
    CinzaC = '\033[1;37m'
    CinzaE = '\033[1;90m'
    VermelhoC = '\033[1;91m'
    VerdeC = '\033[1;92m'
    AmareloC = '\033[1;93m'
    AzulC = '\033[1;94m'
    MagentaC = '\033[1;95m'
    CyanC = '\033[1;96m'
    Branco = '\033[1;97m'
    Negrito = '\033[;1m'
    Inverte = '\033[;7m'
    Reset = '\033[0;0m'

#clear terminal
def clearScreen( ):
	os.system('cls' if os.name == 'nt' else 'clear')

#wait for user to press enter
def pause( text = 'Aperte enter para continuar...'):
	input( text )

class simpleMenu( ):
	#default back function that enables loop exit
	def Back( self ):
		self.run = False

	#deletes the first default option and sets the offset to 1
	def delBackAndOffset( self ):
		del self.menuOptions[ '0' ]
		self.currentAutoIndex = 1

	def reset( self, title ):
		#sets default values
		#creates menuOptions used to store the functions related to the menu
		#creates menuNames that stores user readable name
		#with the same index as the function related to it

		self.menuOptions = 	{ '0': [ self.Back, f' {bcolors.Vermelho}SAIR{bcolors.Reset}'] }
		if ( title != '' ):
			self.title = title
		
		#prints afther the menu
		self.description = ''

		#should it still run
		self.run = True

		#for breaking outside the loop
		self.breaking = False

		#for adding space inbetween the option
		self.spacing = []

		#for currect indexing when a str is added as a key
		self.currentAutoIndex = 1

		#currently selected key
		self.selection = ''
	
	def outside_loop_break(self):
		self.run = False
		self.breaking = True

	def change_back_to_outside_loop_break(self, name = 'SAIR'):
		self.menuOptions['0'] = [ self.outside_loop_break, name ]

	def __init__( self, title, defaultFunction = False ):
		#sets title calls reset to set values
		self.title = title
		self.reset( title )
		self.defaultFunction = defaultFunction

	def change_backFunction( self, key, func, name, args=False ):
		func_custom = func
		
		self.menuOptions[ key ] = self.menuOptions['0']
		del self.menuOptions['0']
		self.menuOptions[ key ] = [ func_custom,name ]

	def menu_option_add( self, func, name, customKey=False, args=False ):
		#adds a new function to menuOptions with a int key
		#and stores a user readable name with same index
		
		#checks if args are present
		
		func_custom = func
		
		if( customKey ):
			self.menuOptions.update( { str(customKey) : [ func_custom,name ] } )
		
		else:
			#sets the key value to be the next number in line
			self.menuOptions.update( { str(self.currentAutoIndex) : [ func_custom, name ] } )
			self.currentAutoIndex += 1
	
	def menu_option_remove( self, key ):
		del self.menuOptions[ key ]

	def defaultFunciton_SetTo( self, func, args = False):
		func_custom = func
		self.defaultFunction = func_custom

	def menu_print( self ):
		#prints the title and adds '-' as a seperator
		#with the length as the title
		print( self.title )
		seperator = ''
		for _ in self.title:
			seperator +='-'
		print( seperator )
		#prints all the use readable names
		#in format '[key] name'
		#print(self.menuOptions)
		for key,value in self.menuOptions.items():
			temp= '[' + str(key) + ']'
			print ( temp, value[1] )
			if key in self.spacing:
				print()
		
		print()
		print( self.description )
		self.description = ''
	
	def menu_start( self ):
		while ( True ):
			#if the loop should still run
			if(self.run):
				
				#clears terminal
				clearScreen()

				if(self.defaultFunction):
					self.defaultFunction()
				
				#prints the menu
				self.menu_print()

				#gets user choice
				inp = input(f'{bcolors.Amarelo}Escolha ->{bcolors.Reset} ')
				if(inp != ''):
					menuOption = self.menuOptions.get(inp, False)
					if(menuOption):
						menuOption[0]()
					else:
						print(inp, 'Opção não encontrada!')
						pause()
				
			else:
				break