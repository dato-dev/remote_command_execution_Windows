# remote_command_execution_Windows
# Удаленное выполнение команды на компьютере Windows

Этот скрипт позволяет выполнить команду на удаленном компьютере с операционной системой Windows с использованием протокола WinRM. Он устанавливает соединение с удаленным хостом, выполняет команду и возвращает результат.

## Использование

1. Установите Python 3, если он еще не установлен.

2. Установите модуль `winrm`, если он еще не установлен, с помощью следующей команды:

```shell
pip install pywinrm
```

3. Загрузите скрипт `remote_execution.py` в свою рабочую директорию.

4. Укажите параметры удаленного компьютера в следующих переменных:
   - `remote_host`: IP-адрес или имя удаленного компьютера.
   - `username`: Имя пользователя для удаленного входа.
   - `password`: Пароль пользователя для удаленного входа.

5. Укажите команду, которую нужно выполнить на удаленном компьютере, в переменной `command`.

6. Запустите скрипт следующей командой:

```shell
python remote_execution.py
```

7. Скрипт установит соединение с удаленным компьютером и выполнит указанную команду.

8. Результат выполнения команды будет выведен в консоль и сохранен в текстовом файле `remote_info.txt`, который будет создан на рабочем столе.

## Зависимости

Скрипт зависит от следующих зависимостей:

- `winrm` - модуль Python для взаимодействия с удаленными компьютерами по протоколу WinRM. Он может быть установлен с помощью команды `pip install pywinrm`.

## Важно

- Перед использованием скрипта убедитесь, что на удаленном компьютере включен протокол WinRM и настроены соответствующие права доступа для удаленного входа.

- Убедитесь, что указанные учетные данные (имя пользователя и пароль) для удаленного входа верны и имеют необходимые привилегии на удаленном компьютере.

- Проверьте соединение с удаленным компьютером, чтобы убедиться, что он доступен и может быть достигнут из вашей сети.

- Рекомендуется внимательно изучить код скрипта и проверить его на соответствие требованиям и безопасности вашей системы перед использованием в боевом окружении.
