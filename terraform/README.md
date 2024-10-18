# <img width="25px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/terraform/terraform-original.svg" /> Terraform

Terraform é uma ferramenta de **infraestrutura como código** (IaC) desenvolvida pela HashiCorp. Ela permite definir e provisionar infraestrutura de forma programática em diversos provedores de nuvem (como AWS, Azure, Google Cloud), além de provedores locais (on-premise) e outros serviços (DNS, bancos de dados, etc.). A infraestrutura é declarada em arquivos de configuração utilizando a linguagem HCL (HashiCorp Configuration Language).

## Principais Conceitos

### Arquivos de configuração
A infraestrutura é descrita em arquivos `.tf`, onde você define recursos como servidores, redes e bancos de dados, além de suas dependências.

### Provedores
Terraform se integra a diversos provedores de serviços. Cada provedor contém recursos específicos que podem ser gerenciados.

### State (estado)
Terraform mantém um arquivo de estado (`terraform.tfstate`) que contém informações sobre os recursos gerenciados, permitindo rastrear mudanças e aplicar apenas as modificações necessárias.

### Comandos principais
- **`terraform init`**: Inicializa o ambiente, baixando provedores e módulos necessários.
- **`terraform plan`**: Gera um plano das mudanças a serem feitas, permitindo revisão antes da aplicação.
- **`terraform apply`**: Aplica as mudanças para provisionar ou atualizar a infraestrutura.
- **`terraform destroy`**: Destrói todos os recursos definidos no código.

### Módulos
Permitem organizar e reutilizar blocos de configuração para padronizar a infraestrutura em múltiplos ambientes.

### Backends remotos
Terraform pode usar backends remotos (como S3 ou o Terraform Cloud) para armazenar o arquivo de estado de forma segura e colaborativa.

## Benefícios
- **Automatização**: Reduz o esforço manual na gestão de infraestrutura.
- **Idempotência**: Garante que a infraestrutura seja aplicada de maneira consistente, independentemente de quantas vezes o código for executado.
- **Colaboração**: Pode ser utilizado por equipes de forma colaborativa, permitindo ajustes na infraestrutura com rastreamento de alterações.

## Casos de Uso
- Provisionamento de infraestrutura em nuvem.
- Gestão de redes, servidores, bancos de dados e outros recursos.
- Automação de pipelines de CI/CD para infraestrutura.

Terraform é uma solução robusta e amplamente utilizada para gerenciar infraestrutura, ajudando a garantir escalabilidade, previsibilidade e consistência no gerenciamento de ambientes complexos.









          