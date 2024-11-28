import requests
import time
from colorama import Fore, Style, init


init(autoreset=True)


def send_discord_message(webhook_url, message, count=100, delay=1):

    for i in range(count):
        data = {
            "content": message
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"{Fore.GREEN}Сообщение {i + 1}/{count} успешно отправлено!")
        else:
            print(f"{Fore.RED}Ошибка при отправке сообщения {i + 1}/{count}: {response.status_code}")



def gradient_text(text, colors):

    gradient_message = ""
    length = len(text)
    color_step = len(colors) / length
    for i, char in enumerate(text):
        color_index = int(i * color_step)
        gradient_message += colors[color_index] + char
    return gradient_message + Style.RESET_ALL


def main():
    print(f"{Fore.CYAN}=== Отправка сообщения в Discord через вебхук ===")


    webhook_url = input("Введите URL вебхука: ")
    message = input("Введите сообщение для отправки: ")


    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    gradient_message = gradient_text(message, colors)

    print(f"{Fore.WHITE}Сообщение с градиентом: ")
    print(gradient_message)


    if input(f"{Fore.CYAN}Отправить сообщение на сервер Discord 100 раз? (y/n): ").lower() == 'y':
        send_discord_message(webhook_url, message, count=100, delay=1)
    else:
        print(f"{Fore.YELLOW}Отправка отменена.")


if __name__ == "__main__":
    main()
