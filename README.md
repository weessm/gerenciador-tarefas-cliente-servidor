# Gerenciador de Tarefas Cliente-Servidor

## Descrição

Este projeto é um gerenciador de tarefas distribuído implementado em um modelo cliente-servidor. Utilizando sockets TCP para comunicação, o cliente envia comandos para adicionar, remover, atualizar e listar tarefas. O servidor processa esses comandos em threads separadas, garantindo uma comunicação confiável e a integridade das operações.

## Funcionamento

- **Servidor:** Espera por conexões de clientes e processa comandos recebidos para manipular tarefas em um armazenamento centralizado.
- **Cliente:** Conecta-se ao servidor, envia comandos específicos e recebe respostas correspondentes às operações realizadas.

## Protocolo de Comunicação

### Comandos do Cliente

- **ADD:** Adiciona uma nova tarefa.

  - **Formato:** `ADD:Descrição da tarefa`
  - **Resposta do Servidor:** `Tarefa adicionada.`

- **REMOVE:** Remove uma tarefa pelo índice.

  - **Formato:** `REMOVE:Índice`
  - **Resposta do Servidor:** `Tarefa removida.` ou `Índice inválido.`

- **UPDATE:** Atualiza a descrição de uma tarefa pelo índice.

  - **Formato:** `UPDATE:Índice:Descrição da nova tarefa`
  - **Resposta do Servidor:** `Tarefa atualizada.` ou `Índice inválido.`

- **LIST:** Lista todas as tarefas.

  - **Formato:** `LIST`
  - **Resposta do Servidor:** Lista de tarefas com índices.

- **EXIT:** Solicita desconexão do servidor.
  - **Formato:** `EXIT`
  - **Resposta do Servidor:** Nenhuma. O servidor encerra a conexão.

### Respostas do Servidor

- Mensagens de confirmação ou erro baseadas nos comandos recebidos.
- Lista de tarefas quando solicitado.

## Requisitos

- **Servidor:** Python 3.x, acesso à rede.
- **Cliente:** Python 3.x, acesso à rede.

## Como Executar

### Servidor

1. Clone o repositório:

   ```bash
   git clone https://github.com/weessm/tarefas-cliente-servidor
   cd tarefas-cliente-servidor
   ```

2. Altere a linha 55 em server.py para o endereço IPv4 da rede

   ```python
   host = '192.168.XX.XX'  # Substituir pelo endereço IP do servidor na rede (IPV4)
   ```

3. Execute o servidor:
   ```bash
   python server.py
   ```

### Cliente

1. Execute o cliente:

   ```bash
   python client.py
   ```

2. Siga as instruções para digitar o endereço IP do servidor.

## Exemplo de Uso

1. **Adicionar uma tarefa:**

   - Comando: `ADD:Comprar leite`
   - Resposta: `Tarefa adicionada.`

2. **Listar tarefas:**

   - Comando: `LIST`
   - Resposta: `0. Comprar leite`

3. **Atualizar uma tarefa:**

   - Comando: `UPDATE:0:Comprar pão`
   - Resposta: `Tarefa atualizada.`

4. **Remover uma tarefa:**

   - Comando: `REMOVE:0`
   - Resposta: `Tarefa removida.`

5. **Sair do cliente:**
   - Comando: `EXIT`
