# Docker volumes

Docker volumes são uma maneira de persistir dados gerados e usados por contêineres Docker. Por padrão, os dados dentro de um contêiner são armazenados no sistema de arquivos do contêiner e são perdidos quando o contêiner é removido. Volumes permitem que você armazene dados de forma independente do ciclo de vida do contêiner, facilitando a persistência e o compartilhamento de dados entre diferentes contêineres.

Existem diferentes tipos de volumes em Docker:

1. Volumes gerenciados pelo Docker: Docker cria e gerencia esses volumes. Eles são armazenados em um local padrão no host e são ideais para a maioria dos casos de uso, pois Docker lida com a gestão dos dados.

2. Volumes bind mounts: Esses volumes são criados diretamente em um caminho especificado do sistema de arquivos do host. Eles oferecem mais controle sobre onde os dados são armazenados no host, mas também são mais propensos a problemas de segurança e permissões.

3. Volumes tmpfs: São armazenados na memória do sistema e não no sistema de arquivos do host. Eles são úteis para dados temporários que não precisam ser preservados após o término do contêiner.