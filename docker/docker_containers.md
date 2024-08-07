# Containers 

Containers são uma tecnologia de virtualização que permite empacotar e isolar aplicações junto com todas as suas dependências (como bibliotecas, binários e arquivos de configuração) de maneira eficiente e portátil. Eles compartilham o mesmo sistema operacional do host, mas operam em ambientes isolados. Isso os torna mais leves e rápidos de iniciar em comparação com as máquinas virtuais tradicionais.

## Execução

 é usado para criar e iniciar um novo container a partir de uma imagem. 


```bash
docker run <options> image <options>
```

#### Options

`--name` nomeia um container

`-d` detach deixa o terminal livre

`--rm` remove o container quando ele parar de ser executado

`--cpus` capacidade de threads disponiveis para o container

`-m` ou `--memory` capacidade de memoria disponivel para o container

`--gpus` habilita o uso de gpu

`-it` interactive terminal (bash/sh/zsh) não esqueça de verificar qual a imagem usada disponibiliza

`-p` ou `--publish` bind de porta host:container

`-P` bind de porta no `EXPOSE` no host é definida a que estiver disponivel

`-e` ou `--env` define variavel de ambiente sobreescreve a do dockerfile(KEY=VALUE)

`--env-file` pode pegar .env de um arquivo

`-w` ou `--workdir` define WORKDIR no docker run sovreescreve o do dockerfile

#### bind mount no run

```bash
docker run -v <host_path>:<container_path>
```

```bash
docker run --mount type=bind,src=<host_path>,target=<container_path>
```

## Parada

```bash
docker stop <options> image <options>
```

## Iniciando

é usado para iniciar um ou mais containers que foram previamente criados ou parados.

```bash
docker start <options> image <options>
```

## Reiniciando

```bash
docker restart <options> image <options>
```

## Logs

mostra os ultimos logs

```bash
docker logs <options> <container>
```

#### Options

`-n` ou `--tail` o número de linhas nos logs

`-f` ou `--follow` trava o termina mostrando os logs

## Stats

```bash
docker stats <options> <container>
```

#### Options

`-a` ou `--all` mostra todas as estatisticas

## Update

```bash
docker update <options> <container>
```

#### Options

`--cpus` capacidade de threads disponiveis para o container

`-n` ou `--memory` capacidade de memoria disponivel para o container

## Exec

Executa comandos dentro do container onde o WORKDIR está definido

```bash
docker exec <options> <container> <command> <args>
```

#### Options

`-it` interactive terminal (bash/sh/zsh) não esqueça de verificar qual a imagem usada disponibiliza

`-e` ou `--env` define variavel de ambiente sobreescreve a do dockerfile(KEY=VALUE) OBS: disponivel só no terminal interativo

`--env-file` pode pegar .env de um arquivo OBS: disponivel só no terminal interativo

## Copy

copia arquivos para o container

```bash
docker cp <host_path> <container>:<container_path>
```

copia arquivos para o host

```bash
docker cp <container>:<container_path> <host_path>
```

## Diff

Mostra as diferenças entre a base(`FROM`) e o container

```bash
docker diff <container>
```

