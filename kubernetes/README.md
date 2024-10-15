# <img width="25px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kubernetes/kubernetes-original.svg" /> Kubernetes

Kubernetes (K8s) é uma plataforma open-source para automação da implantação, escalonamento e gestão de aplicações containerizadas. Ele foi originalmente desenvolvido pelo Google e é agora mantido pela CNCF (Cloud Native Computing Foundation).

## Principais Conceitos de Kubernetes:

- `Cluster`: É o conjunto de máquinas (nós) que executam as aplicações containerizadas gerenciadas pelo Kubernetes. O cluster consiste em:

- `Master Node`: Controla o cluster, gerencia a distribuição de workloads, monitora a integridade dos nós e aplica políticas. Ele contém componentes como o API server, Scheduler, e Controller Manager.

- `Worker Nodes`: São as máquinas onde os containers são executados. Cada worker node tem componentes como o kubelet, que se comunica com o Master, e o kube-proxy, que gerencia a rede do cluster.

- `Pod`: É a menor unidade de deploy no Kubernetes. Um pod contém um ou mais containers que compartilham o mesmo armazenamento, rede, e especificações de como esses containers devem rodar. Se um container falha, o Kubernetes pode reiniciar o pod, garantindo alta disponibilidade. Os pods podem ser escalados horizontalmente para lidar com mais tráfego ou carga de trabalho.

- `Deployment`: Uma abstração que permite a definição de como os pods devem ser criados, atualizados e gerenciados. Ele garante que o número desejado de pods esteja sempre rodando no cluster e que as atualizações sejam aplicadas de forma controlada.

- `Service`: Define uma forma de expor um conjunto de pods em um cluster, seja para acesso interno ou externo. Isso garante que o tráfego seja roteado corretamente entre os pods, mesmo que eles mudem de IP.

- `Namespaces`: Servem para separar ambientes dentro de um mesmo cluster. Isso é útil para dividir recursos entre diferentes equipes ou aplicações.

Kubernetes é amplamente utilizado devido à sua capacidade de orquestrar containers em escala, automatizando tarefas como balanceamento de carga, resiliência de serviços e escalonamento automático.

## [MiniKube](https://minikube.sigs.k8s.io/docs/)

O Minikube é uma ferramenta que permite rodar um cluster Kubernetes local em uma única máquina, facilitando o desenvolvimento, teste e aprendizado com o Kubernetes sem a necessidade de configurar um cluster completo em servidores remotos. Ele cria uma instância de Kubernetes em uma máquina virtual (VM) ou contêiner no seu computador, oferecendo todos os recursos essenciais do Kubernetes, como gerenciamento de pods, serviços e volumes.

### Minikube é popular entre desenvolvedores porque permite:

- Testar aplicações localmente em um ambiente Kubernetes.

- Simular o comportamento de um cluster real, inclusive com suporte para vários containers.

- Oferecer um ambiente de desenvolvimento Kubernetes leve e de fácil configuração.

### Comandos

`minikube start` - Inicia cluster

`minikube stop` - Para o cluster

`minikube expose` - Expoe um app

Exemplo

kubectl expose deployment app-html-deployment --type=LoadBalancer --name=app-html --port 80


## kubectl

O kubectl é a interface de linha de comando (CLI) para interagir com o Kubernetes. Ele permite que os usuários gerenciem e inspecionem recursos de um cluster Kubernetes, como pods, serviços, deployments, namespaces, e muito mais. Com o kubectl, é possível executar uma variedade de operações, desde criar e deletar recursos até depurar e monitorar o comportamento de aplicações dentro do cluster.

### Principais Comandos do kubectl:

`kubectl get`

Lista os recursos no cluster.

Exemplo: 

```bash
kubectl get pods
```

exibe todos os pods em execução.

flags:

- `-o wide` exibe pods em execução com informações mais detalhadas



`kubectl describe`

Mostra detalhes sobre um recurso específico.

Exemplo: 

```bash
kubectl describe pod <pod_name> 
```

exibe informações detalhadas sobre um pod.


`kubectl apply`

Aplica configurações de um arquivo YAML ou JSON, criando ou atualizando recursos.

Exemplo:

```bash
kubectl apply -f deployment.yaml
```

aplica o deployment especificado no arquivo.

`kubectl create`

Cria recursos diretamente da linha de comando ou a partir de arquivos de definição.

Exemplo

```bash
kubectl create deployment nginx --image=nginx
```

cria um deployment com uma imagem NGINX.


`kubectl delete`

Remove recursos de um cluster.

Exemplo

```bash
kubectl delete pod <pod_name>/<deployment>
```

deleta um pod específico.

`kubectl logs`

Visualiza os logs de um container em execução dentro de um pod.

Exemplo

```bash
kubectl logs <pod_name>
```

exibe os logs do pod.

`kubectl exec`

Executa comandos diretamente em um container dentro de um pod.

Exemplo

```bash
kubectl exec -it <pod_name> -- /bin/bash
```

abre um shell interativo dentro de um container.

`kubectl expose`

Exemplo

```bash
kubectl expose deployment app-html-deployment --type=LoadBalancer --name=app-html --port 80
```

`kubectl port-forward [resource-type]/[resource-name] [local-port]:[pod-port]`

- [resource-type]: Tipo do recurso, como `pod` ou `service`.

- [resource-name]: Nome do Pod ou Serviço ao qual você deseja se conectar.

- [local-port]: A porta na sua máquina local que será mapeada.

- [pod-port]: A porta no Pod que está sendo redirecionada.

Exemplo

```bash
kubectl port-forward pod/go-app-pod 8080:8080
```

## Conteudos

### [Yaml](./yaml.md)

### [NodePort](./NodePort.md)