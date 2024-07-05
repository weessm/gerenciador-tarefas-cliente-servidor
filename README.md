# Gerenciador de Tarefas Cliente-Servidor

# Autores

Weslei Miranda, Thiago de Freitas, Leonam Rabelo, Eduardo Takeshi

## Descrição

Este projeto é um gerenciador de tarefas distribuído implementado em um modelo cliente-servidor. Utilizando sockets TCP para comunicação, o cliente envia comandos para adicionar, remover, atualizar e listar tarefas. O servidor processa esses comandos em threads separadas, garantindo uma comunicação confiável e a integridade das operações.

## Propósito do Software

O gerenciador de tarefas permite aos usuários adicionar, remover, atualizar e listar tarefas. O cliente envia comandos ao servidor, que processa as solicitações e retorna as respostas adequadas.

## Motivação da Escolha do Protocolo de Transporte

TCP foi escolhido como protocolo de transporte porque ele oferece uma conexão confiável, garantindo que todas as mensagens sejam entregues na ordem correta e sem perda de dados. Isso é crucial para um gerenciador de tarefas onde a integridade dos dados é importante.

## Funcionamento

- **Servidor:** Espera por conexões de clientes e processa comandos recebidos para manipular tarefas em um armazenamento centralizado.
- **Cliente:** Conecta-se ao servidor, envia comandos específicos e recebe respostas correspondentes às operações realizadas.

## Protocolo de Aplicação

### Eventos e Estados

#### Estados do Cliente

- **Conectado:** Cliente está conectado ao servidor e pronto para enviar comandos.
- **Desconectado:** Cliente está desconectado do servidor.

#### Estados do Servidor

- **Aguardando Conexão:** Servidor está esperando por novos clientes.
- **Processando Solicitação:** Servidor está processando a solicitação de um cliente.
- **Conexão Encerrada:** Servidor encerra a conexão com o cliente.

### Mensagens

A comunicação é baseada em mensagens enviadas através de sockets TCP. Cada mensagem segue um formato específico descrito abaixo.

### Formato das Mensagens

As mensagens são strings de texto simples, codificadas em UTF-8, com comandos e dados separados por dois pontos (:) quando necessário. Exemplo: `COMANDO:ARGUMENTO1:ARGUMENTO2`.

### Comandos

Servidor é iniciado.

- **Estado do Servidor:** `Aguardando Conexão`

Cliente se conecta ao servidor.

- **Estado do Cliente:** `Conectado`
- **Estado do Servidor:** `Processando Solicitação`

Cliente envia comando **ADD.**

- **Mensagem:** `ADD:Descrição`
- **Resposta do Servidor:** `Tarefa adicionada.`

Cliente envia comando **LIST.**

- **Mensagem:** `LIST`
- **Resposta do Servidor:** Lista de tarefas no formato `Índice. Descrição -- (Endereço do cliente)`

Cliente envia comando **UPDATE.**

- **Mensagem:** `UPDATE:Índice:Descrição`
- **Resposta do Servidor:** `Tarefa atualizada.` ou `Índice inválido.`

Cliente envia comando **REMOVE.**

- **Mensagem:** `REMOVE:Índice`
- **Resposta do Servidor:** `Tarefa removida.` ou `Índice inválido.`

Cliente envia comando **EXIT.**

- **Mensagem:** Nenhuma. O servidor encerra a conexão.
- **Estado do Cliente:** `Desconectado`
- **Estado do Servidor:** `Conexão Encerrada`

### Respostas do Servidor

- Mensagens de confirmação ou erro baseadas nos comandos recebidos.
- Lista de tarefas quando solicitado.

## Requisitos

- **Servidor:** Python 3.x, acesso à rede.
- **Cliente:** Python 3.x, acesso à rede.
- **Rede:** Cliente e servidor devem estar na mesma rede ou acessíveis através da internet.

## Como Executar

### Servidor

1. Clone o repositório:

   ```bash
   git clone https://github.com/weessm/tarefas-cliente-servidor
   cd tarefas-cliente-servidor
   ```

2. Altere a linha 55 em server.py para o endereço IPv4 da rede

   ```python
   host = '192.168.XX.XX'  # Substituir pelo endereço IP do servidor na rede (IPv4)
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

Todo o uso é facilidado por um menu, evitando erros ao digitar os comandos ou formatação.

```bash
=== Menu ===
1. Adicionar tarefa
2. Remover tarefa
3. Atualizar tarefa
4. Listar tarefas
5. Sair
```

1. **Adicionar uma tarefa:**

   - Comando: `1`
   - Entrada: `Limpar a casa`
   - Resposta: `Tarefa adicionada.`

2. **Listar tarefas:**

   - Comando: `4`
   - Resposta: `0. Limpar a casa -- (192.168.XX.XX)`

3. **Atualizar uma tarefa:**

   - Comando: `3`
   - Entrada: `0`
   - Entrada: `Alterando`
   - Resposta: `Tarefa atualizada.`

4. **Remover uma tarefa:**

   - Comando: `2`
   - Entrada: `0`
   - Resposta: `Tarefa removida.`

5. **Sair do cliente:**

   - Comando: `5`

6. **Encerrar servidor (comando dado no servidor)**
   - Comando: `exit`
