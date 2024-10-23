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




          