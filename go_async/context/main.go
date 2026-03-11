package main

// Max time to exec something, cancel or timeout
// args: parent context.Context, t time.Time
// Return: ctx context.Context, cancel context.CancelFunc
func WithDeadLine() {

}

// Same thing o WithDeadLine but u pass a duration not end time
// args: parent context.Context, timeout time.Duration
// Return: ctx context.Context, cancel context.CancelFunc
func WithTimeOut() {
	
}

// send signal to all process that uses context to cancel or igone exec task
// args: parent context.Context
// Return: ctx context.Context, cancel context.CancelFunc
func WithCancel() {
	
}

// define values in memory, with immutable key-value in assync flux (like a map)
// args: parent context.Context, key interface{}, value interface{}
// Return: context.Context
func WithValue() {
	
}

/*
usada para gerenciar o ciclo de vida, cancelamento, deadlines (prazos) e compartilhamento de valores entre goroutines e APIs, especialmente em operações de rede ou banco de dados. Ele previne desperdício de recursos ao cancelar tarefas desnecessárias.

# Principais Funcionalidades e Tipos:

- Gerenciamento de Ciclo de Vida: Permite cancelar operações em cascata, onde o cancelamento de um pai cancela todos os seus filhos.

- Timeouts e Deadlines: Define um limite de tempo (WithTimeout) ou um horário específico (WithDeadline) para uma operação terminar.

- Propagação de Valores: Passa dados essenciais, como IDs de requisição ou tokens de autenticação, entre camadas da aplicação (WithValue).

- Contextos Raiz: context.Background() é usado na main/inicialização, e context.TODO() quando o contexto ainda não foi definido.
*/
func main() {

}
