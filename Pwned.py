import sys,os,requests
from colorama import Fore


print(Fore.MAGENTA+"""
╭━━━╮╱╱╱╱╱╱╭╮╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱╭╯╰╮╱┃╭━━╯
┃┃╱┃┣━━┳┳━╋╮╭╯╱┃╰━━┳╮╱╭┳━━╮
┃┃╱┃┃━━╋┫╭╮┫┣━━┫╭━━┫┃╱┃┃┃━┫
┃╰━╯┣━━┃┃┃┃┃╰┳━┫╰━━┫╰━╯┃┃━┫
╰━━━┻━━┻┻╯╰┻━╯╱╰━━━┻━╮╭┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯ """)
print(Fore.RED+"""                        -BY: HXCKYR""")

def display_menu():
    print(Fore.GREEN + """
    1: EMAILs & IT'S PASSWORDs Search
    2:PHONE NUMBERs Search""")


def execute_command(command):
    if command == '1':
        os.system('cmd /k "python3 Osint-Eye/Url.py"' if os.name == 'nt' else 'python3 Url.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break
