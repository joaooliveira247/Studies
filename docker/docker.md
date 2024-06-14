# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" width=20px/> Docker

O Docker é uma plataforma de software livre que permite aos desenvolvedores desenvolver, implementar, executar, atualizar e gerenciar componentes de contêineres executáveis e padronizados que combinam o código-fonte de aplicativos com as bibliotecas e estruturas do sistema operacional (S.O.) necessárias para executar o código em qualquer ambiente.

## Por que usar o Docker?

- Portabilidade de contêiner aprimorada e contínua

- Mais leve e com atualizações mais granulares

- Criação automatizada de contêineres 

- Controle de versões de contêineres

- Reutilização de contêiner

- Bibliotecas compartilhadas de contêineres:

## Basic Commands

|Comando|Descrição|
|:---:|:---:|
|`docker ps`|Lista todos os containers em execução|
|`docker image ls` or `docker images`|Lista todas as imagens na maquina|
|`docker image rm <image_name or image_id>` or `docker rmi <image_name or image_id>`|Remove um ou mais containers|
|`docker image pull <image_name>`|Baixa uma imagem de uma [fonte](https://hub.docker.com/)|

## Executando o primeiro container

[Docker image](https://hub.docker.com/_/hello-world)

```shell
docker run hello-world
```

## [Docker images](./docker_images.md)

# Referências

https://www.redhat.com/pt-br/topics/containers/what-is-docker

https://www.ibm.com/br-pt/topics/docker