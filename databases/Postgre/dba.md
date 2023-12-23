# 👩‍💼 `DBA` - Administrador de Banco de Dados

é o profissional responsável por realizar o gerenciamento, a configuração, a instalação, a atualização e o monitoramento de bancos de dados.

Além disso, esse profissional também desenvolve melhorias para o sistema de banco de dados. Dependendo do tipo de dados que cada empresa utiliza, tipos de banco terão que ser definidos. Por exemplo, dependendo da informação o banco de dados deve ser relacional ou não relacional. O DBA deve escolher as ferramentas e como esse banco de dados deve ser construído, pois cada caso específico necessita de um tratamento.

---

## [Clusters](https://www.postgresql.org/docs/current/creating-cluster.html)

Na sua forma mais básica, um cluster é um sistema que compreende dois ou mais computadores ou sistemas (denominados nós) onde trabalham em conjunto para executar aplicações ou realizar outras tarefas de tal forma que os usuários que os utilizam tenham a impressão que somente um único sistema responde para eles (computador virtual). Este conceito é denominado transparência do sistema. Como características fundamentais para a construção destas plataformas incluem-se elevação da confiança, distribuição de carga e performance.

PGCluster é um sistema síncrono de replicação de composição multi-master para PostgreSQL. Devido ao fato do sistema de replicação ser um sistema síncrono, atrasos não irão ocorrer na duplicação de dados entre os servidores de armazenamento. Em um servidor de composição multi-master, dois ou mais servidores de armazenamento podem ser acessados simultaneamente por um usuário.

- Iniciando um cluster

    - o local onde o PostgreSQl vai armazenar os arquivos necessários para representar o esquema e seus dados.

```bash
initdb -D /usr/local/pgsql/data
```

- [Iniciando um servidor](https://www.postgresql.org/docs/current/server-start.html)

```bash
pg_ctl start -l logfile
```

> **__Note:__**
>
>O utilitário pg_ctl é um dos melhores amigos do DBA PostgreSQL. Ele facilita (e muito) a gestão do serviço postgres que fica rodando para receber conexões no servidor.
>
>Através desse utilitários nós podemos fazer muita coisa com menos conhecimento sobre o sistema operacional, já que esse utilitário abstrai diversas complexidades para nós.
>
>Mas é válido dizer que via de regra, tudo que pode ser feito com o pg_ctl pode ser feito sem ele através do serviço postgres e com conhecimentos de gestão de sistemas operacionais.

> **__Lembrete:__**
>
> Rodar os comandos com usuário postgres
>
> `su postgres`

## [Configurando o postgres](https://www.postgresql.org/docs/current/config-setting.html)

