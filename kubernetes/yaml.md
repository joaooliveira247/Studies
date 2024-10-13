# Kubernetes YAML

um arquivo YAML (Yet Another Markup Language) é usado para definir configurações de recursos que serão gerenciados dentro do cluster. Esses arquivos são escritos em um formato legível por humanos e são amplamente utilizados para declarar a infraestrutura e o estado desejado das aplicações no Kubernetes.

Os arquivos YAML no Kubernetes descrevem recursos como pods, deployments, services, configmaps, entre outros. Cada recurso tem uma especificação (spec) que define como ele deve se comportar, incluindo o número de réplicas, imagens de containers, portas expostas e volumes montados.

## Estrutura Básica de um Arquivo YAML no Kubernetes:

Um arquivo YAML típico para Kubernetes contém várias seções chave:

1. apiVersion: Define a versão da API Kubernetes usada para o recurso.

2. kind: Especifica o tipo de recurso (ex: Pod, Deployment, Service).

3. metadata: Contém informações como o nome do recurso e labels associadas.

4. spec: A seção que descreve a especificação, ou seja, os detalhes de como o recurso deve se comportar.

### Exemplo

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app-container
          image: nginx:1.21
          ports:
            - containerPort: 80
```

#### Descrição do Exemplo:

`apiVersion: apps/v1`: Define que estamos utilizando a versão v1 da API de aplicativos (apps) do Kubernetes.

`kind: Deployment`: Especifica que o recurso é um Deployment, que gerencia a criação e a atualização de pods.

`metadata`: Inclui o nome do recurso, my-app, e um rótulo app: my-app para identificar os recursos associados.

`spec:`

`replicas: 3`: Define que o deployment deve criar e manter 3 réplicas (ou instâncias) do pod.

`selector:` Indica quais pods este deployment gerenciará, usando rótulos (no caso, app: my-app).

`template:` Define o template do pod, contendo metadata e a especificação dos containers.

`containers:` Lista os containers que farão parte do pod.

`name: my-app-container`: Nome do container.

`image: nginx:1.21`: Especifica a imagem do container (neste caso, uma imagem do NGINX na versão 1.21).

`ports:` Define a porta 80 como a porta onde o container estará ouvindo.

### Utilização

Este arquivo pode ser aplicado ao Kubernetes com o comando:

```bash
kubectl apply -f deployment.yaml
```