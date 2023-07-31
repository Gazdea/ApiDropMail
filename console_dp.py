import sys
from Dropmail import *

args = sys.argv[1:]

# Определяем доступные команды
commands = {
    'get_domains': get_domains,
    'get_session': get_session,
    'list_sessions': list_sessions,
    'list_mails': list_mails,
    'get_mail': get_mail,
    'generate_mail': generate_mail

    # Добавьте другие функции сюда
}

# Проверяем, была ли указана команда
if len(args) < 1 or args[0] not in commands:
    print("Доступные команды:")
    for command in commands:
        print(command)
    sys.exit(1)

# Вызываем выбранную команду
command = args[0]
result = commands[command]()

# Выводим результат
print(result)