import sys,os,time
from colorama import Fore  #Using colorama for colored text


print(Fore.MAGENTA+"""
╭━━━╮╱╱╱╱╱╱╭╮╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱╭╯╰╮╱┃╭━━╯
┃┃╱┃┣━━┳┳━╋╮╭╯╱┃╰━━┳╮╱╭┳━━╮
┃┃╱┃┃━━╋┫╭╮┫┣━━┫╭━━┫┃╱┃┃┃━┫
┃╰━╯┣━━┃┃┃┃┃╰┳━┫╰━━┫╰━╯┃┃━┫
╰━━━┻━━┻┻╯╰┻━╯╱╰━━━┻━╮╭┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯ """)
print(Fore.RED+"""                        -by: HXCKYR""")
print(Fore.BLUE+ """                        -V: 1.2""")


def display_menu():
  """Displays the menu options."""
  print(Fore.GREEN + """
  1: NUMBER | TRUECALLER ( in development 😓)
  2: BREACHED EMAIL ID Search
  3: WEBSITE Scraper
  4: INSTAGRAM Profile id Scraper
  5: LINKEDIN Profile Scraper
  6: Exit the program""")
  print(Fore.RED + """
  select the option (i.e 4)_👆""")
  print(Fore.WHITE)


def execute_command(command):

  if command == '1':
    print(u"\u001b[31m                    'TRUECALLER 👀'")
    print(Fore.WHITE+""" """)
    os.system('cmd /k "python bin/mobile_number/number-scraper.py"' if os.name == 'nt' else 'python3 bin/mobile_number/number-scraper.py')


  elif command == '2':
    print(u"\u001b[31m			  'EMAIL pwend 👀'")
    print(Fore.WHITE+""" """)
    os.system('cmd /k "python bin/email/data_breach_checker.py"' if os.name == 'nt' else 'python3 bin/email/data_breach_checker.py')

  elif command == '3':
    print(u"\u001b[31m                     'DOMAIN INFORMATION [emails|social handels|etc 👀'")
    print(Fore.WHITE+""" """)
    os.system('cmd /k "python bin/sites/site-scraper.py"' if os.name == 'nt' else 'python3 bin/sites/site-scraper.py')

  elif command == '4':
    print(u"\u001b[31m                     'INSTA I-D 👀'")
    print(Fore.WHITE+""" """)
    os.system('cmd /k "python bin/instagram/instagram-scraper.py"' if os.name == 'nt' else 'python3 bin/instagram/instagram-scraper.py')

  elif command =='5':
    print(u"\u001b[31m                      'LINKEDIN PROFILE 👀'")
    print(Fore.WHITE+""" """)
    os.system('cmd /k "python bin/linkedin/linkedin-scraper.py"' if os.name == 'nt' else 'python3 bin/linkedin/linkedin-scraper.py')

  elif command.lower() == '6':
    print(u"\u001b[31m                     'See u Soon 🥲'")
    print(Fore.CYAN + "Exiting the program...")
    exit()  # Use exit() to terminate the program gracefully
    
  else:
    print(Fore.RED + 'Invalid option! Please choose a number between 1 and 6.')


while True:
  display_menu()
  print(Fore.YELLOW+""" """)
  command = input('🕵🏻_> ')
  print(Fore.WHITE+""" """)
  execute_command(command)
 
