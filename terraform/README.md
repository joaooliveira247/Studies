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

  - `-replace`: Esse comando permite marcar um recurso específico para ser recriado, mesmo que não tenha mudado na configuração. O Terraform irá destruí-lo e recriá-lo. Útil para forçar a substituição de um recurso quando necessário. Exemplo:

    ```bash
    terraform plan -replace="aws_instance.example"
    ```

  - `-target`: Esse comando planeja mudanças apenas para um recurso específico ou conjunto de recursos, ignorando o restante da infraestrutura. É útil para focar em uma atualização sem afetar outros recursos. Exemplo:

    ```bash
    terraform plan -target="aws_instance.example"
    ```

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

### [`Remote State`](./remote_state)

O remote state no Terraform, usando o provider azurerm, refere-se ao armazenamento do estado do Terraform em um local remoto, em vez de mantê-lo localmente. Isso é crucial para colaboração em equipe e manter a integridade do estado da infraestrutura, permitindo que múltiplos usuários acessem e modifiquem o mesmo estado de forma segura e simultânea.

No caso do Azure, o estado remoto geralmente é armazenado em uma conta de armazenamento no Azure Blob Storage. Aqui está um resumo de como configurar o remote state usando o provider azurerm:

### Configuração da Conta de Armazenamento:

- Você precisa criar uma conta de armazenamento no Azure.

- Nessa conta, crie um contêiner onde o estado do Terraform será armazenado.

### Configuração no Terraform:

- No arquivo de configuração do Terraform, defina o backend como azurerm e configure os detalhes do armazenamento.

### Exemplo básico de configuração:

```hcl
terraform {
  backend "azurerm" {
    resource_group_name   = "nome-do-grupo-de-recursos"
    storage_account_name  = "nome-da-conta-de-armazenamento"
    container_name        = "nome-do-container"
    key                   = "terraform.tfstate"
  }
}
```

### Autenticação:

- O Terraform precisa de permissões para acessar a conta de armazenamento do Azure. Isso pode ser feito configurando a autenticação via uma conta de serviço ou utilizando as credenciais locais (como az login).

### Benefícios:

- Colaboração: Facilita o trabalho em equipe ao garantir que todos acessem o mesmo estado da infraestrutura.

- Segurança: O estado remoto pode ser protegido usando permissões no Azure e criptografia no Blob Storage.

- Automação: Facilita a automação dos pipelines CI/CD ao fornecer um local centralizado para o estado da infraestrutura.

## Outros Comandos

`terraform show`

O comando terraform show é utilizado para exibir informações detalhadas sobre o estado atual de uma infraestrutura gerenciada pelo Terraform. Ele pode ser utilizado para exibir tanto o arquivo de estado gerado pelo Terraform quanto os planos de execução.

- Arquivo de estado: O `terraform show` exibe as informações sobre os recursos atualmente gerenciados, seus atributos e valores. Isso é útil para entender o estado real da infraestrutura após a aplicação de mudanças.

-Plano de execução: Também pode ser usado para revisar um plano gerado por terraform plan, permitindo uma verificação visual das mudanças que serão feitas na infraestrutura.

Exemplo de uso:

```bash
terraform show terraform.tfstate
```

`terraform state`

O comando `terraform state` é utilizado para interagir diretamente com o arquivo de estado do Terraform. O estado mantém um mapeamento entre os recursos configurados no código Terraform e os recursos reais criados na infraestrutura. Através do comando terraform state, é possível inspecionar e gerenciar esse estado.

Ele oferece várias subcomandos úteis, como:

- `terraform state list`: Lista todos os recursos que estão sendo gerenciados no arquivo de estado.

- `terraform state show <resource>`: Exibe detalhes sobre um recurso específico gerenciado no estado.

- `terraform state mv`: Move um recurso de um lugar para outro no estado, útil em refatorações de código.

`terraform state rm`: Remove um recurso do estado sem destruí-lo fisicamente, usado em casos onde o recurso deve parar de ser gerenciado pelo Terraform, mas continuar existindo na infraestrutura.

Exemplo de uso:

```bash
terraform state list
terraform state show azurerm_public_ip.public_ip
```

`terraform import`

O comando terraform import permite importar recursos que já existem na infraestrutura para serem gerenciados pelo Terraform. Isso é útil quando você tem recursos criados manualmente ou por outros sistemas e deseja começar a gerenciá-los com Terraform sem ter que recriá-los.

O comando não gera automaticamente o código Terraform para os recursos importados. Após a importação, você precisa adicionar manualmente a configuração correspondente no arquivo .tf.

Exemplo de uso:

```bash
terraform import aws_s3_bucket.my_bucket my-existing-bucket-name
```

OBS: seria como fazer um `backend` na mão

`terraform refresh`

O comando terraform refresh atualiza o arquivo de estado do Terraform com o estado real dos recursos na infraestrutura. Ele sincroniza o que está no arquivo de estado local com o que realmente existe no provedor de nuvem ou infraestrutura.

Esse comando verifica os recursos existentes e seus atributos no provedor, atualizando o estado do Terraform para refletir qualquer mudança que tenha ocorrido fora do Terraform, como modificações feitas manualmente.

Importante: Este comando não aplica mudanças nem modifica a infraestrutura, ele apenas atualiza o estado interno do Terraform.

Exemplo de uso:

```bash
terraform refresh
```

No Terraform 0.15 e posterior, o terraform apply já inclui automaticamente a etapa de atualização do estado, então o uso do terraform refresh tornou-se menos comum.

`terraform init -flags`

`-reconfigure`

A flag -reconfigure força o Terraform a reconfigurar o backend ao executar o terraform init. Isso é útil quando você deseja alterar a configuração do backend (por exemplo, mudar de um backend local para um backend remoto como o S3 ou Azure Storage), ou se você quer garantir que o backend seja configurado a partir das opções atuais, mesmo que o Terraform já tenha sido inicializado anteriormente.

Exemplo de uso:

```bash
terraform init -reconfigure
```

Neste caso, o Terraform ignora qualquer configuração de backend previamente usada e reconfigura o backend com base nas opções atuais fornecidas no código.

`-migrate-state`

A flag -migrate-state é usada quando você deseja migrar o estado do Terraform de um backend para outro. Quando você altera a configuração do backend (como mover o estado de um backend local para um S3, por exemplo), o Terraform precisa migrar o arquivo de estado antigo para o novo backend.

Ao utilizar essa flag durante a inicialização, o Terraform fará a migração automática do estado existente para o novo backend definido na configuração.

Exemplo de uso:

```bash
terraform init -migrate-state
```

Isso instruirá o Terraform a mover o arquivo de estado existente para o novo backend.

`-backend`

A flag -backend permite habilitar ou desabilitar o uso de backend. Se você passar -backend=false, o Terraform não usará nenhum backend para armazenar o arquivo de estado remotamente, e o estado será mantido localmente.

Exemplo de uso:

```bash
terraform init -backend=false
```

Esse comando inicializa o projeto sem usar um backend remoto, mantendo o estado localmente (geralmente em um arquivo terraform.tfstate na máquina onde o comando foi executado).

Quando usar essas flags:

Use `-reconfigure` se você estiver alterando ou reconfigurando o backend.

Use `-migrate-state` se você estiver mudando de backend e precisar migrar o estado existente.

Use `-backend=false` se você quiser manter o estado localmente e não usar um backend remoto.

`terraform force-unlock`

O comando terraform force-unlock é utilizado para forçar a liberação de um lock em um estado de Terraform que ficou preso, geralmente durante uma operação. O Terraform bloqueia o arquivo de estado para garantir que apenas uma operação possa modificar a infraestrutura por vez, prevenindo mudanças conflitantes.

No entanto, se uma operação for interrompida inesperadamente (por exemplo, devido a um erro de rede ou falha no processo), o lock pode não ser liberado automaticamente. Nesses casos, o comando force-unlock é necessário para liberar manualmente o lock.

Sintaxe:

```bash
terraform force-unlock <LOCK_ID>
```

`LOCK_ID: É o ID do bloqueio que você deseja forçar a liberar. O Terraform fornece esse ID quando ocorre o bloqueio, ou você pode encontrá-lo no backend remoto.

## Provisioners

Provisioners são usados para executar comandos ou scripts em recursos provisionados, geralmente após sua criação. Eles permitem configurar detalhes específicos que vão além da configuração principal do recurso. Embora úteis, devem ser usados com cautela, pois introduzem ações imperativas em uma ferramenta declarativa.

### 1\. local-exec Provisioner

O local-exec executa comandos na máquina onde o Terraform é executado (local), não no recurso provisionado. Ele é útil para tarefas como gerar logs ou enviar notificações.

Exemplo:

```hcl
resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  provisioner "local-exec" {
    command = "echo 'Instance created!' > instance_creation.log"
  }
}
```

Neste exemplo, o comando cria um log local (instance_creation.log) na máquina que executa o Terraform após a criação da instância.

### 2\. remote-exec Provisioner

O remote-exec executa comandos diretamente no recurso provisionado, como uma VM ou instância de servidor. Ele é frequentemente usado para configurar ou instalar software.

Exemplo:

```hcl
resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y nginx"
    ]
  }
}
```

Aqui, o remote-exec usa SSH para se conectar à instância AWS e instala o servidor Nginx.

### 3\. file Provisioner

O file provisioner copia arquivos ou diretórios do sistema local para o recurso remoto, útil para mover arquivos de configuração ou scripts.

Exemplo:

```hcl
resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }

  provisioner "file" {
    source      = "app/config.yaml"
    destination = "/etc/myapp/config.yaml"
  }
}
```

Este exemplo copia o arquivo config.yaml do sistema local para o diretório /etc/myapp/ na instância AWS.

### Cuidados ao Usar Provisioners

- Use-os como último recurso: Provisioners são recomendados apenas quando não há outra forma de alcançar a configuração desejada, pois podem tornar a infraestrutura menos reprodutível.

- Ferramentas alternativas: Para configurações complexas, use ferramentas como Ansible ou Chef, que são especializadas em gerenciar configurações de software.

## Modules

Módulos no Terraform são blocos de código reutilizáveis que permitem organizar e compartilhar configurações de infraestrutura. Eles encapsulam um conjunto de recursos e variáveis, facilitando a manutenção e reaproveitamento da configuração em diferentes partes do projeto ou em outros projetos.

Vantagens dos Módulos

- Reutilização: Você pode usar o mesmo módulo em várias partes do projeto, evitando duplicação de código.

- Organização: Ajuda a estruturar a infraestrutura em componentes lógicos, tornando o código mais fácil de entender e modificar.

- Escalabilidade: Permite que equipes padronizem configurações e escalem a infraestrutura de maneira consistente.

Estrutura Básica de um Módulo

Um módulo Terraform geralmente contém:

main.tf: Define os recursos principais.

variables.tf: Declara as variáveis de entrada para personalizar o módulo.

outputs.tf: Declara as saídas que o módulo retorna.

### Local Modules

Exemplo Básico de Módulo

Estrutura de Pastas

```plaintext
.
├── main.tf
├── s3_bucket/
│ └── bucket.tf
│ ├── variables.tf
│ └── outputs.tf
└── variables.tf
```

`s3_bucket/bucket.tf`

```hcl
resource "aws_s3_bucket" "example" {
bucket = var.bucket_name
}
```

`s3_bucket/outputs.tf`

```hcl
output "bucket_id" {
value = aws_s3_bucket.example.id
}
```

Usando o Módulo no `main.tf`

```hcl
module "s3_bucket" {
source = "./modules/s3_bucket"
bucket_name = "my-unique-bucket-name"
}
```

### Remote Module

Para usar um módulo remoto no Terraform, você pode especificar a fonte do módulo como um repositório Git, um bucket no Amazon S3, ou diretamente do Terraform Registry. Usar módulos remotos facilita a centralização de configurações, permitindo que outros projetos ou equipes utilizem o mesmo módulo sem a necessidade de duplicá-lo localmente.

Exemplo Usando um Módulo Remoto do Terraform Registry
O Terraform Registry possui muitos módulos prontos para uso, como configurações de VPC, RDS, e S3. Para usar um módulo do Registry, basta referenciá-lo em seu main.tf com o parâmetro source.

#### Exemplo: Criando uma VPC Usando um Módulo do Terraform Registry

```hcl
provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.19.0"

  name                 = "example-vpc"
  cidr                 = "10.0.0.0/16"
  azs                  = ["us-east-1a", "us-east-1b"]
  public_subnets       = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets      = ["10.0.3.0/24", "10.0.4.0/24"]
  enable_dns_support   = true
  enable_dns_hostnames = true
}
```

Neste exemplo:

O módulo VPC é baixado do Terraform Registry (especificado em source = "terraform-aws-modules/vpc/aws").
A variável version controla a versão do módulo, garantindo consistência.

#### Exemplo Usando um Módulo de um Repositório Git

Também é possível referenciar módulos armazenados em repositórios Git. Para isso, é necessário fornecer a URL do repositório e, opcionalmente, um branch, tag, ou commit específico.

```hcl
module "s3_bucket" {
  source      = "git::https://github.com/user/terraform-s3-bucket-module.git?ref=v1.0"
  bucket_name = "my-remote-bucket"
  acl         = "private"
}
```

### Exemplo Usando um Módulo de um Bucket S3

```hcl
module "example" {
  source = "s3::https://s3.amazonaws.com/mybucket/terraform/modules/example.zip"
}
```

Neste caso, o módulo é buscado em um arquivo .zip armazenado no S3.

- Terraform Registry: source = "terraform-aws-modules/vpc/aws"
- Git: source = "git::https://github.com/user/repo.git?ref=tag"
- S3: source = "s3::https://s3.amazonaws.com/bucket/path.zip"

### `terraform get`

O comando terraform get no Terraform é utilizado para baixar e atualizar os módulos referenciados nas configurações do seu projeto. Módulos no Terraform são conjuntos reutilizáveis de recursos que ajudam a organizar e simplificar a infraestrutura como código. O terraform get garante que todos os módulos necessários estejam disponíveis localmente para que o Terraform possa aplicá-los corretamente.

Principais Funcionalidades do terraform get

- Download de Módulos: Baixa módulos de fontes remotas especificadas nas configurações, como o Terraform Registry, repositórios Git, ou armazenamento em nuvem (por exemplo, Amazon S3).

- Atualização de Módulos: Atualiza os módulos existentes para suas versões mais recentes, conforme definido nas configurações do seu projeto.

- Gerenciamento de Dependências: Garante que todas as dependências de módulos sejam resolvidas e baixadas, mantendo a consistência do ambiente.

Sintaxe Básica

```bash
terraform get [opções] [diretório]
```

`[diretório]`: Opcional. Especifica o diretório onde o Terraform deve procurar as configurações. Se não for especificado, o comando será executado no diretório atual.

Principais Flags

`-update`: Força a atualização de todos os módulos para a versão mais recente disponível, ignorando o cache local.

```bash
terraform get -update
```

`-json`: Retorna a saída no formato JSON, útil para integração com outras ferramentas ou scripts.

```bash
terraform get -json
```

`-lock` e `-lock-timeout`: Controla o bloqueio do estado durante a operação, garantindo que outras operações concorrentes não interfiram.

```bash
terraform get -lock=true -lock-timeout=30s
```

#### Exemplo de Uso

1\. Baixando Módulos Necessários
Suponha que você tenha a seguinte configuração no seu main.tf que utiliza um módulo do Terraform Registry:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.19.0"

  name                 = "example-vpc"
  cidr                 = "10.0.0.0/16"
  azs                  = ["us-east-1a", "us-east-1b"]
  public_subnets       = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets      = ["10.0.3.0/24", "10.0.4.0/24"]
  enable_dns_support   = true
  enable_dns_hostnames = true
}
```

Para baixar esse módulo, você executaria:

```bash
terraform get
```

Este comando irá:

Conectar-se ao Terraform Registry.
Baixar o módulo terraform-aws-modules/vpc/aws na versão 3.19.0.
Armazenar o módulo no diretório .terraform/modules dentro do seu projeto.

2\. Atualizando Módulos para a Versão Mais Recente
Se você deseja atualizar todos os módulos para suas versões mais recentes conforme especificado nas configurações, utilize a flag -update:

```bash
terraform get -update
```

Isso forçará o Terraform a verificar e baixar as versões mais recentes dos módulos, substituindo quaisquer versões antigas no cache local.

Considerações Importantes
Automatização com terraform init: A partir das versões mais recentes do Terraform (0.13 e posteriores), o comando terraform init já incorpora as funcionalidades do terraform get. Portanto, geralmente, você não precisa executar terraform get separadamente, a menos que tenha necessidades específicas de gerenciamento de módulos.

### Resumo

Módulos: Permitem organizar e reaproveitar configurações de infraestrutura.
Estrutura: Inclui main.tf, variables.tf, e outputs.tf.
Uso: Facilitam a padronização, escalabilidade e manutenção da infraestrutura em Terraform.

## Meta-arguments

meta-argumentos são utilizados dentro de blocos para controlar o comportamento dos recursos, módulos e outros blocos. Eles permitem modificar a execução e a configuração dos recursos sem alterar diretamente os parâmetros principais. Aqui estão os meta-argumentos principais usados no Terraform e onde você pode aplicá-los:

1\. `depends_on`

Onde usar: Dentro de blocos de recursos e módulos.

O que faz: Define dependências explícitas, garantindo que um recurso ou módulo só seja criado ou atualizado após outro recurso ou módulo estar pronto.

Exemplo:

```hcl
resource "aws_instance" "example" {
ami = "ami-123456"
instance_type = "t2.micro"

depends_on = [aws_security_group.example]
}
```

2\. `count`

Onde usar: Em blocos de recursos e módulos.

O que faz: Cria múltiplas instâncias de um recurso ou módulo com base no valor definido. Um valor maior que 1 cria várias instâncias, enquanto 0 impede a criação.

Exemplo:

```hcl
resource "aws_instance" "example" {
ami = "ami-123456"
instance_type = "t2.micro"

count = 3
}
```

3\. `for_each`

Onde usar: Em blocos de recursos e módulos.

O que faz: Itera sobre uma coleção (lista, mapa ou set) e cria uma instância para cada item. Diferente do count, ele usa chaves específicas para cada instância.

Exemplo:

```hcl
resource "aws_instance" "example" {
ami = "ami-123456"
instance_type = "t2.micro"

for_each = toset(["web", "db", "cache"])

tags = {
  Name = each.key
}
}
```

4\. `provider`

Onde usar: Em blocos de recursos e módulos.

O que faz: Define qual provedor usar para um recurso específico, útil quando há várias instâncias de um mesmo provedor (por exemplo, múltiplas contas AWS).

Exemplo:

```hcl
resource "aws_instance" "example" {
ami = "ami-123456"
instance_type = "t2.micro"

provider = aws.eu_west_1
}
```

5. `lifecycle`

Onde usar: Em blocos de recursos.

O que faz: Controla como o Terraform gerencia o ciclo de vida de um recurso, com atributos como create_before_destroy, prevent_destroy, e ignore_changes.

Exemplo:

```hcl
resource "aws_instance" "example" {
ami = "ami-123456"
instance_type = "t2.micro"

lifecycle {
create_before_destroy = true
prevent_destroy = true
ignore_changes = [tags]
}
}
```

6. `provider_meta`

Onde usar: Em blocos de recursos e módulos.

O que faz: Permite a passagem de informações adicionais para o provedor, principalmente para provedores que precisam de configurações adicionais em certos contextos. Este meta-argumento é menos usado e depende do suporte do provedor.

### Resumo

Blocos de recurso podem ter: `depends_on`, `count`, `for_each`, `provider`, e `lifecycle`.
Blocos de módulo podem ter: `depends_on`, `count`, `for_each`, e `provider`.

## Funções e Expressões

### 1\. Conditional Expressions

As expressões condicionais em Terraform seguem uma estrutura condition ? true_value : false_value, permitindo definir valores condicionalmente. É útil para aplicar lógica baseada em condições, sem a necessidade de estruturas complexas de controle. Exemplo:

```hcl
instance_type = var.environment == "production" ? "t3.large" : "t3.micro"
```

Aqui, o tipo de instância depende do valor da variável `environment`.

### 2\. For Expressions

for expressions permitem iterar sobre listas ou mapas para transformar dados ou filtrá-los. Podem ser aplicados em arrays e mapas para criar novas estruturas de dados. Exemplo:

```hcl
instance_names = [for i in range(3) : "instance-${i}"]
```

Nesse exemplo, é criada uma lista com nomes de instância numerados.

Também é possível usar uma condição para filtrar elementos:

```hcl
instance_ids = [for instance in aws_instance.example : instance.id if instance.tags["env"] == "prod"]
```

### 3\. Splat Expressions

Splat expressions (`*`) são usadas para acessar propriedades de todos os elementos em uma lista ou conjunto de objetos. É útil para simplificar expressões que acessam múltiplos itens. Exemplo:

```hcl
instance_ids = aws_instance.example[*].id
```

Esse exemplo coleta todos os IDs de instância do recurso aws_instance.example. As splat expressions são equivalentes a for expressions mais simples e são frequentemente mais concisas.

## Dynamic Blocks

dynamic blocks são estruturas que permitem gerar blocos repetidos dentro de um recurso ou módulo de maneira programática, tornando o código mais dinâmico e reutilizável. Em vez de definir manualmente cada bloco, você pode usar um for_each ou for para iterar sobre uma lista ou mapa de dados, criando blocos com base nessas informações. Isso é especialmente útil para configurações complexas onde o número de blocos pode variar ou depende de variáveis de entrada, como configurar múltiplos ingress ou egress em recursos de segurança.

Aqui está um exemplo básico de como um dynamic block pode ser usado:

```hcl
resource "aws_security_group" "example" {
 name = "example"

 dynamic "ingress" {
   for_each = var.ingress_rules
   content {
     from_port   = ingress.value.from_port
     to_port     = ingress.value.to_port
     protocol    = ingress.value.protocol
     cidr_blocks = ingress.value.cidr_blocks
   }
 }
}
```

Nesse exemplo, um bloco ingress é gerado para cada item na variável ingress_rules, o que facilita a manutenção e evita repetição no código.

## Terraform console

O terraform console é uma ferramenta interativa de linha de comando no Terraform que permite avaliar expressões, explorar variáveis, recursos e outputs em tempo real. É especialmente útil para testar e depurar expressões Terraform sem precisar aplicar mudanças na infraestrutura.

Ao iniciar o terraform console dentro de um diretório de configuração, você pode executar comandos para visualizar valores e interagir com o estado atual. Por exemplo:

```bash
terraform console
```

### Dentro do console, você pode:

#### Visualizar variáveis:

```bash
> var.my_variable
```

#### Consultar recursos e outputs:

```bash
> aws_instance.example.id
```

#### Avaliar expressões complexas:

```bash
> length(var.list_of_items)
> [for i in var.list_of_items : upper(i)]
```

#### Manipular dados (listas, mapas, strings, etc.):

```bash
> { for k, v in var.map_variable : k => upper(v) }
```

O terraform console permite assim testar transformações e entender o comportamento das configurações antes de aplicar as mudanças, facilitando a verificação de dados e o uso de expressões complexas.

## Built-in functions

O Terraform oferece uma variedade de funções _built-in_ para manipulação de dados e ajudar na criação de configurações mais dinâmicas. Essas funções estão organizadas em categorias como strings, números, listas, mapas, lógica e outros tipos. Aqui estão algumas das principais:

### 1. Funções de String

- `join(separator, list)`: Junta elementos de uma lista em uma única string com um separador especificado.

- `split(separator, string)`: Divide uma string em uma lista com base em um separador.

- `replace(string, substring, replacement)`: Substitui todas as ocorrências de uma substring em uma string por outra substring.

- `upper(string)`, `lower(string)`: Converte a string para maiúsculas ou minúsculas.

### 2. Funções de Número

- `abs(number)`: Retorna o valor absoluto de um número.

- `min(number1, number2, ...)`, `max(number1, number2, ...)`: Retorna o menor ou maior valor de uma lista de números.

### 3. Funções de Lista

- `length(list)`: Retorna o número de elementos em uma lista.

- `contains(list, element)`: Verifica se um elemento está presente em uma lista.

- `element(list, index)`: Retorna o elemento no índice especificado.

- `flatten(list)`: Converte uma lista de listas em uma lista plana.

### 4. Funções de Mapas

- `lookup(map, key, default)`: Procura uma chave em um mapa e retorna o valor associado ou um valor padrão.

- `merge(map1, map2, ...)`: Combina múltiplos mapas em um único mapa.

- `keys(map)`, `values(map)`: Retorna uma lista com as chaves ou valores de um mapa.

### 5. Funções de Lógica

- `coalesce(val1, val2, ...)`: Retorna o primeiro valor não nulo de uma lista.

- `alltrue(list)`, `anytrue(list)`: Retorna verdadeiro se todos ou qualquer elemento da lista for verdadeiro.

### 6. Funções de Manipulação de Path

- `basename(path)`: Extrai o nome do arquivo de um caminho.

- `dirname(path)`: Extrai o caminho do diretório de um caminho de arquivo.

### 7. Funções de Tempo

- `timestamp()`: Retorna a data e hora atual no formato UTC.

- `timeadd(timestamp, duration)`: Adiciona uma duração de tempo a um timestamp e retorna a nova data.

### 8. Funções de Criptografia

- `md5(input)`, `sha1(input)`, `sha256(input)`: Gera hashes de uma string de entrada.

- `bcrypt(input, cost)`: Gera um hash bcrypt da string de entrada (com custo especificado).

### Exemplo de uso:

```hcl
variable "names" {
  type = list(string)
  default = ["alice", "bob", "charlie"]
}

output "upper_names" {
  value = [for name in var.names : upper(name)]
}
```

## Workspaces

O conceito de workspaces no Terraform é uma funcionalidade que permite criar e gerenciar diferentes estados independentes para o mesmo conjunto de configurações. Isso é especialmente útil quando você quer usar a mesma infraestrutura em ambientes diferentes, como dev, staging e production, sem duplicar o código de configuração.

Cada workspace tem seu próprio estado, ou seja, as alterações feitas em um workspace não afetam o estado dos outros. O workspace padrão é chamado de default, mas é possível criar outros usando o comando:

```bash
Copy code
terraform workspace new <nome-do-workspace>
```

Depois de criar um workspace, você pode alternar entre eles com:

```bash
terraform workspace select <nome-do-workspace>
```

E listar todos os workspaces com:

```bash
terraform workspace list
```

### Exemplo

exemplo básico para configurar dois workspaces em Terraform, um para dev (desenvolvimento) e outro para prod (produção). Vamos considerar uma configuração simples que cria uma instância EC2 na AWS.

1. Arquivo de configuração: `main.tf`

Este é um arquivo de configuração Terraform para criar uma instância EC2. Ele também usa variáveis para configurar recursos específicos para cada workspace.

```hcl
provider "aws" {
  region = "us-east-1"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI ID
  instance_type = var.instance_type
  tags = {
    Name = "${terraform.workspace}-instance"
  }
}
```

2. Definindo variáveis específicas para dev e prod

Você pode configurar variáveis para cada workspace diretamente no código usando o terraform.workspace. Nesse caso, vamos alterar o tipo de instância com base no workspace.

```hcl
variable "instance_type" {
  type    = string
  default = terraform.workspace == "prod" ? "t2.large" : "t2.micro"
}
```

3. Criando e alternando entre os workspaces

Para configurar e usar workspaces, siga estes passos no terminal:

1. Inicializar o Terraform:

```bash
terraform init
```

2. Criar o workspace de dev:

```bash
terraform workspace new dev
```

3. Criar o workspace de prod:

```bash
terraform workspace new prod
```

4. Selecionar um workspace:

Para alternar entre os ambientes, você pode selecionar o workspace desejado:

```bash
terraform workspace select dev
```

5. Aplicar a configuração:

Após selecionar o workspace, aplique as configurações:

```bash
terraform apply
```

## Data Source

um data source é um bloco de configuração que permite obter informações de recursos que já existem fora do gerenciamento direto do Terraform ou que são gerados em tempo de execução. Ele é útil para consultar e reutilizar dados de infraestrutura existentes ou externos, sem necessidade de recriar esses recursos.

Os data sources são frequentemente usados para:

Obter informações sobre recursos já existentes, como IPs de sub-redes, IDs de instâncias, ou dados de configuração de VPCs.
Utilizar esses dados em outras configurações do Terraform, permitindo a integração e automação sem duplicação de informações.
Exemplo de data source

Suponha que você queira obter o ID de uma VPC existente e usá-lo para criar uma nova sub-rede. O data source aws_vpc permite buscar a VPC por um filtro:

```hcl
provider "aws" {
  region = "us-east-1"
}

data "aws_vpc" "example" {
  filter {
    name   = "tag:Name"
    values = ["my-vpc"]
  }
}

resource "aws_subnet" "example_subnet" {
  vpc_id            = data.aws_vpc.example.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}
```

### [Exemplo 2](./azure_project/vm/main.tf)

## Time Sleep

você pode usar o recurso time_sleep para inserir uma pausa ou atraso durante a aplicação da infraestrutura. Isso pode ser útil em cenários onde você precisa esperar um tempo específico antes de realizar outra operação, como após a criação de um recurso que pode demorar a estar completamente disponível.

Exemplo de time_sleep

```hcl
resource "time_sleep" "wait_30_seconds" {
  depends_on = [aws_instance.example]
  create_duration = "30s"
}
```

Neste exemplo, o recurso time_sleep aguarda 30 segundos após a criação de aws_instance.example antes de continuar com os próximos recursos ou operações. Isso ajuda a garantir que o próximo recurso ou ação só seja executado após o tempo determinado.
