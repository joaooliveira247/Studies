# Persistent Volumes (PV) e Persistent Volume Claims (PVC)

Em Kubernetes, Persistent Volumes (PV) e Persistent Volume Claims (PVC) são usados para gerenciar o armazenamento persistente de forma eficiente e desacoplada dos pods. Eles são recursos cruciais para garantir que os dados sejam preservados mesmo quando os pods são recriados ou reiniciados.

## Persistent Volume (PV)

O Persistent Volume é um recurso de armazenamento fornecido por um administrador. Ele é uma abstração para o armazenamento físico, seja ele em um disco local, em uma rede, ou em um serviço de nuvem (como AWS EBS, NFS, Google Persistent Disk, etc). 

### Um PV tem as seguintes características:

- Capacidade: Define o tamanho do volume de armazenamento.

- Tipo de Acesso: Especifica o modo de acesso, por exemplo, se pode ser lido e escrito por um único pod ou por múltiplos pods (ReadWriteOnce, ReadOnlyMany, ReadWriteMany).

- Política de Retenção: Define o que deve acontecer com o volume quando o PVC associado é excluído (Retain, Recycle, Delete).

### Exemplo de um PV:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-example
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /mnt/data
```

Neste exemplo, um volume de 10Gi é criado no caminho `/mnt/data` no host.

## Persistent Volume Claim (PVC)

O Persistent Volume Claim é uma requisição feita pelos pods para o armazenamento persistente. O PVC solicita um volume com tamanho e modos de acesso específicos e, quando um PV compatível é encontrado, o PVC é vinculado a ele. O PVC permite que o armazenamento seja gerenciado dinamicamente pelos usuários, sem a necessidade de conhecer detalhes sobre o provedor de armazenamento subjacente.

### Exemplo de um PVC:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-example
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

Neste exemplo, o PVC solicita 10Gi de armazenamento com acesso de leitura e escrita.

## Como PV e PVC funcionam juntos:

1. Provisionamento estático: O administrador do cluster cria manualmente um PV, e os usuários criam um PVC que, se compatível, será vinculado ao PV disponível.

2. Provisionamento dinâmico: Se não houver PVs disponíveis que atendam ao PVC, o Kubernetes pode criar dinamicamente um PV baseado em um StorageClass configurado. Nesse caso, o processo é mais automatizado.


## Exemplo de uso no Pod:

Após a criação de um PV e PVC, você pode anexá-los a um Pod da seguinte maneira:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-example
spec:
  containers:
    - name: container-example
      image: nginx
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: storage
  volumes:
    - name: storage
      persistentVolumeClaim:
        claimName: pvc-example
```

Aqui, o PVC `pvc-example` é montado no contêiner NGINX no diretório `/usr/share/nginx/html`.

### Conclusão

`PV`: Um recurso de armazenamento no cluster gerenciado pelo administrador.

`PVC`: Um pedido de armazenamento feito pelos usuários ou pelos pods.

A combinação de `PV` e `PVC` em Kubernetes permite o armazenamento persistente, essencial para garantir a durabilidade dos dados em aplicativos stateful.