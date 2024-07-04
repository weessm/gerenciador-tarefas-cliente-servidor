import socket
import os

def clear_screen():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para MacOS e Linux
        os.system('clear')

def main():
    host = input("Digite o endereço IP do servidor: ")
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    clear_screen()

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Atualizar tarefa")
        print("4. Listar tarefas")
        print("5. Sair")

        choice = input("\nEscolha uma opção: ")

        if choice == '1':
            task = input("Digite a tarefa a ser adicionada: ")
            client_socket.send(f"ADD:{task}".encode('utf-8'))
            clear_screen()
            print(client_socket.recv(1024).decode('utf-8'))
        elif choice == '2':
            index = input("Digite o índice da tarefa a ser removida: ")
            client_socket.send(f"REMOVE:{index}".encode('utf-8'))
            clear_screen()
            print(client_socket.recv(1024).decode('utf-8'))
        elif choice == '3':
            index = input("Digite o índice da tarefa a ser atualizada: ")
            new_task = input("Digite a nova descrição da tarefa: ")
            client_socket.send(f"UPDATE:{index}:{new_task}".encode('utf-8'))
            clear_screen()
            print(client_socket.recv(1024).decode('utf-8'))
        elif choice == '4':
            client_socket.send("LIST:".encode('utf-8'))
            task_list = client_socket.recv(1024).decode('utf-8')
            clear_screen()
            print("\n== Lista de Tarefas ==")
            print(task_list)
        elif choice == '5':
            client_socket.send("EXIT:".encode('utf-8'))
            break
        else:
            clear_screen()
            print("Opção inválida. Tente novamente.")

    print("\nO cliente foi encerrado.")
    client_socket.close()

if __name__ == "__main__":
    main()
