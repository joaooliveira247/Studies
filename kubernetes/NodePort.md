# NodePort

O NodePort é um tipo de serviço no Kubernetes que expõe uma aplicação rodando no cluster para acesso externo. Ele mapeia uma porta de um nó do cluster (host) para o serviço, permitindo que o tráfego externo chegue ao pod. Diferente de outros tipos de serviços (como ClusterIP e LoadBalancer), o NodePort permite o acesso direto através do IP de qualquer nó do cluster.

### Como funciona o NodePort:

1. O Kubernetes aloca automaticamente uma porta no intervalo 30000–32767.

2. Essa porta é exposta em todos os nós do cluster.

3. O tráfego recebido na porta do nó é redirecionado para o serviço e, em seguida, para os pods.

### Exemplo:

1. Definir um Serviço do Tipo `NodePort`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80           # Porta interna do serviço (ClusterIP)
      targetPort: 80      # Porta do pod onde a aplicação Nginx está rodando
      nodePort: 30036     # Porta exposta no nó do cluster (dentro do intervalo 30000-32767)
```

2. Exemplo de Deployment do Nginx

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```

3. Aplicando o Deployment e Serviço no Cluster:

```bash
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-nodeport.yaml
```

4. Acessando a Aplicação Exposta

## Vantagens e Desvantagens do NodePort:

- Vantagens:
    - Simples de configurar.

    - Acesso direto ao serviço sem precisar de balanceadores de carga externos.

- Desvantagens:

    - Depende do IP dos nós, o que pode não ser ideal para um ambiente de produção em larga escala.

    - Exposição limitada às portas no intervalo 30000–32767.