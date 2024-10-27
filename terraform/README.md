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
 
  - `--out <file>.<ext>`: salva a saido do plan em um arquivo.
  
- **`terraform show <file>`**: mostra oq foi gerado de um out. 
  
- **`terraform apply`**: Aplica as mudanças para provisionar ou atualizar a infraestrutura.

  - `-destroy`: Apaga oque foi gerado pelo apply.
  
  - `-auto-approve`: sem necessidade de confirmação
  
  - `<file>`: file é o tipo de gerado pelo `plan out`, não é necessario confirmar usando o plan

- **`terraform destroy`**: Destrói todos os recursos definidos no código.

- **`terraform providers`**: lista os providers usados em um projeto .tf

- **`terraform fmt`**: formata os arquivos `.tf`

  - `--check`: mostra quais arquivos são necessaios as mudanças
  
  - `--diff`: faz as alterações e mostra quais foram realizadas
  
- **`terraform validate`:** verifica se as configurações são validas. só funciona apos usar o `terraform init`



### Módulos
Permitem organizar e reutilizar blocos de configuração para padronizar a infraestrutura em múltiplos ambientes.

### Backends remotos
Terraform pode usar backends remotos (como S3 ou o Terraform Cloud) para armazenar o arquivo de estado de forma segura e colaborativa.

## Benefícios
- **Automatização**: Reduz o esforço manual na gestão de infraestrutura.
- **Idempotência**: Garante que a infraestrutura seja aplicada de maneira consistente, independentemente de quantas vezes o código for executado.
- **Colaboração**: Pode ser utilizado por equipes de forma colaborativa, permitindo ajustes na infraestrutura com rastreamento de alterações.

## `.tfvars`

Seriam arquivos para guardar variáveis de escopo global, funcionariam quase como constantes.

## Casos de Uso
- Provisionamento de infraestrutura em nuvem.
- Gestão de redes, servidores, bancos de dados e outros recursos.
- Automação de pipelines de CI/CD para infraestrutura.

Terraform é uma solução robusta e amplamente utilizada para gerenciar infraestrutura, ajudando a garantir escalabilidade, previsibilidade e consistência no gerenciamento de ambientes complexos.

## Tipos de Blocos

blocos são as unidades básicas de definição de infraestrutura. Cada bloco possui uma sintaxe específica e serve para declarar recursos, variáveis, provedores e outras configurações que o Terraform utiliza para orquestrar e gerenciar infraestruturas.

### 1. Terraform

O bloco terraform configura aspectos gerais sobre como o Terraform deve se comportar ao aplicar a infraestrutura. Ele é usado para definir coisas como a versão do Terraform que será usada, configurações de backend (onde o estado será armazenado), e configurações de provedores.

```hcl
terraform {
  required_version = ">= 1.2.0"

  backend "s3" {
    bucket = "my-terraform-state"
    key    = "terraform.tfstate"
    region = "us-west-2"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}
```

### 2. Providers

O bloco provider especifica o provedor de infraestrutura (como AWS, GCP, Azure) que o Terraform vai usar para criar e gerenciar recursos. Cada provedor permite interagir com a API de um serviço de nuvem ou outra plataforma. Os provedores são o ponto de integração do Terraform com serviços externos.

```hcl
provider "aws" {
  region = "us-west-2"
}
```

### 3. Resource

O bloco resource é onde você define os recursos reais que serão gerenciados pelo Terraform. Recursos podem ser coisas como instâncias de máquinas virtuais, bancos de dados, redes, etc. Cada recurso tem um tipo (por exemplo, aws_instance para instâncias EC2 na AWS) e um nome local.

```hcl
resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
}
```

### 4. Data

O bloco data permite que você recupere dados de recursos existentes ou de informações externas que não são gerenciadas diretamente pelo Terraform, mas que você precisa para construir seus recursos. Ele é geralmente usado para buscar valores ou IDs que serão usados na criação de outros recursos.

```hcl
data "aws_ami" "latest" {
  most_recent = true
  owners      = ["amazon"]
}
```

### 5. Module

O bloco module permite reutilizar código do Terraform para diferentes projetos ou partes de um projeto. Um módulo é um conjunto de recursos agrupados, e permite que você estruture seu código de forma mais modular e reutilizável.

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "3.0.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"
}
```

### 6. Variable

O bloco variable é usado para definir variáveis de entrada no Terraform, permitindo que você torne sua configuração mais flexível e parametrizada. Você pode definir um valor padrão ou torná-la obrigatória, onde os valores devem ser fornecidos no momento da execução.

```hcl
variable "instance_type" {
  description = "Type of instance to create"
  default     = "t2.micro"
}
```

### 7. Output

O bloco output é utilizado para exibir valores depois que o Terraform executa o plano. Isso pode ser usado para retornar informações úteis, como o endereço IP de uma instância ou o ID de um recurso criado.

```hcl
output "instance_ip" {
  value = aws_instance.example.public_ip
}
```

### 8. Local

O bloco local permite definir variáveis locais dentro de uma configuração Terraform. Isso é útil para definir valores temporários ou intermediários que não precisam ser variáveis de entrada. Ele é útil para reduzir repetição ou computar valores intermediários.

```hcl
locals {
  instance_name = "my-instance"
}

resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  tags = {
    Name = local.instance_name
  }
}
```

## [`TERRAFORM`](https://developer.hashicorp.com/terraform/language/terraform)

### 1. `required_version`

Especifica a versão mínima do Terraform necessária para executar o código. Isso ajuda a garantir que todos os usuários estejam usando uma versão compatível do Terraform.

```hcl
terraform {
  required_version = ">= 1.2.0"
}
```

### 2. `required_providers`

Usado para declarar explicitamente os provedores que serão usados no projeto, suas fontes (como o registro oficial do Terraform ou um registro privado) e suas versões mínimas. Isso garante que a versão correta do provedor seja utilizada.

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
    google = {
      source  = "hashicorp/google"
      version = ">= 3.0"
    }
  }
}
```

### 3. `backend`

Define onde o estado do Terraform será armazenado. Isso é especialmente importante em ambientes de colaboração, onde o estado precisa ser compartilhado entre várias pessoas ou ambientes.

Exemplo de configuração de backend no S3:

```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "path/to/my/key"
    region = "us-west-2"
  }
}
```

### [EXEMPLO](./terraform_example.tf)

## Variaveris

As variáveis em Terraform são usadas para parametrizar e reutilizar configurações, permitindo que você crie módulos e scripts mais flexíveis. Elas permitem definir valores que podem ser modificados sem precisar alterar diretamente o código de infraestrutura.

### Tipos de Variáveis

Em Terraform, as variáveis podem ser definidas de três formas:

- Entrada (`input variables`): Definidas pelo usuário e usadas para passar dados para as configurações. São declaradas usando o bloco variable.

- Locais (`locals`): Usadas para criar valores temporários dentro de um módulo.

- Saída (`output variables`): Exibem informações de um módulo ou script, retornando valores ao final da execução.
Declaração de Variáveis de Entrada

Para definir uma variável de entrada, usa-se a sintaxe:

```hcl
variable "nome_da_variavel" {
  description = "Descrição da variável"
  type        = string
  default     = "valor padrão"
}
```

`description`: Descreve a variável (opcional).

`type`: Define o tipo da variável, que pode ser string, number, bool, list, map, entre outros.

`default`: Define um valor padrão para a variável (opcional).

### Atribuição de Valores

Os valores das variáveis podem ser passados de várias formas:

1\. Arquivo `.tfvars`: Você pode criar um arquivo chamado terraform.tfvars (ou outro nome com a extensão .tfvars) para definir valores de variáveis.

Exemplo de terraform.tfvars:

```hcl
nome_da_variavel = "valor"
```

Ao executar o Terraform, ele automaticamente lê o arquivo terraform.tfvars.

2\. Linha de Comando (CLI): É possível passar variáveis diretamente pelo CLI usando a opção `-var`.

Exemplo:

```bash
terraform apply -var="nome_da_variavel=valor"
```

Isso substitui o valor da variável sem a necessidade de um arquivo `.tfvars`.

3\. Variáveis de Ambiente: Você pode definir variáveis de ambiente com o prefixo `TF_VAR_` seguido do nome da variável.

Exemplo:

```bash
export TF_VAR_nome_da_variavel="valor"
terraform apply
```

### Exemplo Completo

Aqui está um exemplo completo usando variáveis:

Arquivo `variables.tf`:

```hcl
variable "instance_type" {
  description = "O tipo da instância EC2"
  type        = string
  default     = "t2.micro"
}
```

Arquivo `main.tf`:

```hcl
resource "aws_instance" "example" {
  ami           = "ami-12345678"
  instance_type = var.instance_type
}
```

Você pode passar o valor da variável pela CLI assim:

```bash
terraform apply -var="instance_type=t3.medium"
```

## Terraform State

O Terraform State é um componente essencial no uso do Terraform, pois armazena o mapeamento entre os recursos gerenciados pela configuração e os recursos reais no ambiente de infraestrutura. Aqui estão os principais pontos:

- `Armazenamento do Estado`: O estado do Terraform contém metadados sobre os recursos provisionados, incluindo IDs, dependências e outros atributos. O Terraform usa essas informações para saber o que já foi criado e para gerenciar o ciclo de vida dos recursos.

- `Gerenciamento de Mudanças`: O estado permite que o Terraform calcule de forma eficiente as diferenças entre o que está no código de configuração e o que está efetivamente provisionado. Isso possibilita o uso de comandos como terraform plan para prever mudanças.

- `Backends de Estado`: O estado pode ser armazenado localmente ou em backends remotos, como S3, GCS, Azure Blob Storage, etc. Usar um backend remoto é recomendado em equipes, pois facilita a colaboração e garante que o estado seja compartilhado corretamente entre os membros.

`Bloqueio de Estado`: Quando armazenado remotamente, o Terraform pode usar mecanismos de bloqueio (locking) para garantir que dois processos não alterem o estado ao mesmo tempo, evitando condições de corrida.

`Segurança e Sensibilidade`: O estado pode conter informações sensíveis, como chaves e senhas. Por isso, é importante protegê-lo adequadamente, usando criptografia e acessos restritos.

`Manipulação do Estado`: É possível usar comandos como terraform state list, terraform state show, e terraform state rm para inspecionar e modificar manualmente o estado, se necessário.

### [`Local State`](./local_state)

O Local State no Terraform refere-se ao estado que é armazenado localmente no sistema de arquivos, em vez de em um backend remoto. Aqui estão os pontos principais sobre o Local State:

- `Arquivo de Estado`: Quando você usa o estado local, o Terraform salva as informações sobre os recursos provisionados em um arquivo chamado terraform.tfstate. Este arquivo é criado na pasta onde você executa os comandos Terraform, e contém todo o estado da infraestrutura gerenciada.

- `Uso Individual`: O local state é mais adequado para projetos individuais ou ambientes de desenvolvimento, onde apenas uma pessoa está modificando a infraestrutura. Como o estado está armazenado localmente, ele não é compartilhado entre diferentes membros de uma equipe.

- `Risco de Corrupção`: Em casos onde múltiplos usuários estão trabalhando no mesmo projeto, o uso do estado local pode levar a problemas de sincronização e corrupção do estado, já que não há um mecanismo de controle de acesso ou bloqueio, como há em backends remotos.

- `Backups`: O estado local é mais suscetível a perdas de dados, por exemplo, se o arquivo for acidentalmente excluído ou o sistema tiver algum problema. Embora o Terraform faça backup automático do arquivo terraform.tfstate (geralmente nomeado como terraform.tfstate.backup), a perda de ambos os arquivos pode resultar em perda de controle sobre os recursos provisionados.
