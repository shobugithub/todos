from services import login, register
from utils import ResponseData
from colorama import Fore


def print_response(response: ResponseData):
    color = Fore.GREEN if response.status else Fore.RED
    print(color + str(response.data) + Fore.RESET)


def menu():
    print('Login => 1')
    print('Register => 2')
    print('Logout => 3')
    print('Quit => q')
    return input('?: ')


def authentication():
    username = input('Username: ')
    password = input('Password: ')
    response: ResponseData = login(username, password)
    print_response(response)


# Inside your main script:

def logout():
    # Perform any necessary actions to clear user authentication state
    print("Logged out successfully")

if __name__ == '__main__':
    logged_in = False  # Track user authentication state
    while True:
        choice = menu()
        if choice == '1':
            authentication()
            logged_in = True
        elif choice == '2':
            register()
        elif choice == '3':
            if logged_in:
                logout()
                logged_in = False
            else:
                print("You are not logged in.")
        elif choice == 'q':
            break


