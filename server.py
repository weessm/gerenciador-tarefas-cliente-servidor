import socket
import threading

tasks = []
server_running = True

def handle_client(client_socket, addr):
    while True:
        try:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break

            if request.startswith('ADD'):
                _, task = request.split(':', 1)
                tasks.append(task.strip())
                client_socket.send("Tarefa adicionada.".encode('utf-8'))
            elif request.startswith('REMOVE'):
                _, index = request.split(':', 1)
                index = int(index.strip())
                if 0 <= index < len(tasks):
                    del tasks[index]
                    client_socket.send("Tarefa removida.".encode('utf-8'))
                else:
                    client_socket.send("Índice inválido.".encode('utf-8'))
            elif request.startswith('UPDATE'):
                _, index, new_task = request.split(':', 2)
                index = int(index.strip())
                if 0 <= index < len(tasks):
                    tasks[index] = new_task.strip()
                    client_socket.send("Tarefa atualizada.".encode('utf-8'))
                else:
                    client_socket.send("Índice inválido.".encode('utf-8'))
            elif request.startswith('LIST'):
                task_list = "\n".join(f"{i}. {task}" for i, task in enumerate(tasks))
                client_socket.send(task_list.encode('utf-8'))
            elif request.startswith('EXIT'):
                print(f"Cliente {addr[0]}:{addr[1]} solicitou desconexão.")
                break
            else:
                client_socket.send("Comando inválido.".encode('utf-8'))
        except ConnectionAbortedError:
            print(f"Conexão foi fechada abruptamente pelo cliente {addr[0]}:{addr[1]}")
            break
        except Exception as e:
            print(f"Erro: {e}")
            break

    print(f"Cliente {addr[0]}:{addr[1]} desconectado.\n\n")
    client_socket.close()

def main():
    global server_running

    host = '192.168.XX.XX'  # Substituir pelo endereço IP do servidor na rede (IPV4)
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor de tarefas iniciado em {host}:{port}")

    def server_accept():
        while server_running:
            try:
                server_socket.settimeout(1)
                client_socket, addr = server_socket.accept()
                print(f"Conexão estabelecida com {addr[0]}:{addr[1]}\n\n")
                client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
                client_handler.start()
            except socket.timeout:
                continue
            except Exception as e:
                print(f"Erro ao aceitar conexão: {e}\n\n")
                break

    accept_thread = threading.Thread(target=server_accept)
    accept_thread.start()

    while True:
        cmd = input("Digite 'exit' para encerrar o servidor.\n\n")
        if cmd.strip().lower() == 'exit':
            server_running = False
            break

    accept_thread.join()
    server_socket.close()
    print("Servidor encerrado.")

if __name__ == "__main__":
    main()
