import sys
import utils

def main():

	help_message = """
	To (re)build your site, type: python3 manage.py build
	To create a new placeholder page: python3 manage.py new
	To create a new blog placeholder: python3 manage.py blog
			"""
	try:
		command = sys.argv[1]
		if command == 'build':
			utils.re_generate()
		elif command == 'new' or command == 'blog':
			utils.create_placeholder(command)
		else:
			print(help_message)	
	except SyntaxError as e:
			print(help_message)
			print(e)
		
	
if __name__ == "__main__":
	main()