from winrm import Protocol
import os

def run_remote_command(remote_host, username, password, command):
    # Создание соединения с удаленным компьютером
    protocol = Protocol(
        endpoint='http://' + remote_host + ':5985/wsman',
        transport='ntlm',
        username=username,
        password=password,
        server_cert_validation='ignore'
    )

    # Выполнение команды на удаленном компьютере
    shell_id = protocol.open_shell()
    command_id = protocol.run_command(shell_id, command)
    std_out, std_err, status_code = protocol.get_command_output(shell_id, command_id)
    protocol.cleanup_command(shell_id, command_id)
    protocol.close_shell(shell_id)

    return std_out.decode('cp866', errors='replace').strip()


# Параметры удаленного компьютера
remote_host = 'ip_add'
username = 'username'
password = 'password'

# Команда для получения данных о версии ОС
os_version_command = 'wmic os get Caption, Version, OSArchitecture, ServicePackMajorVersion /value'

# Команда для получения списка установленных патчей
installed_patches_command = 'wmic qfe list brief /format:texttablewsys'

# Получение данных о версии ОС
os_version_info = run_remote_command(remote_host, username, password, os_version_command)

# Получение списка установленных патчей
installed_patches_info = run_remote_command(remote_host, username, password, installed_patches_command)

# Вывод результатов
print('Операционная система и версия:')
print(os_version_info)
print('Установленные патчи:')
print(installed_patches_info)

# Создание текстового файла на рабочем столе
file_path = os.path.join(os.path.expanduser("~"), "Desktop", "remote_info.txt")
with open(file_path, 'w') as file:
    file.write('Операционная система и версия:\n')
    file.write(os_version_info + '\n\n')
    file.write('Установленные патчи:\n')
    file.write(installed_patches_info)

print(f'Файл сохранен по пути: {file_path}')