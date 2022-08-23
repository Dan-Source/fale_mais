# Fale Mais

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Este projeto foi feito com base no cookiecutter, que facilita o desenvolvimento e prapara o ambiente com a configurações de banco de dados e bibliotecas, e um padrão para organização dos modulos.

## Sobre o que é este projeto:

A empresa de telefonia Telzir, especializada em chamadas de longa distância nacional, formulou um novo produto chamado FaleMais.
O cliente Telzir pode fazer uma chamada de uma cidade para outra pagando uma
tarifa fixa por minuto, com o preço sendo pré-definido em uma lista com os códigos DDDs de
origem e destino.
Preocupada com a transparência junto aos seus clientes, solicitou a disponibilização de uma
página na web onde o cliente pode calcular o valor da ligação.
Onde, o cliente pode escolher os códigos das cidades de origem e destino, o tempo da ligação em minutos e escolher qual o plano FaleMais. O sistema mostra dois valores:

    - (1) o valor da ligação com o plano.
    - (2) sem o plano.

# Prerequisites

Optei por desenvolver o projeto dentro de um container. O que facilita o desenvolvimento.

- [Docker](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

# Local Development

Para construir seu ambiente o desenvolvimento local execute o commando:
```bash
docker-compose -f local.yml build
```

Para levantar o ambiente execute:
```bash
docker-compose -f local.yml up
```

Faça a migrações:
```bash
docker-compose -f local.yml run --rm django python manage.py makemigrations
docker-compose -f local.yml run --rm django python manage.py migrate
```


Depois é necessário criar um superusuario:
```bash
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

Para derrubar o ambiente de desenvolvimiento:
```bash
docker-compose -f local.yml down
```

# Testes

Execute os teste e verifica se o sistema funciona de acordo com esperado:

```bash
docker-compose -f local.yml run --rm django pytest
```

# Links Utéis

Você pode verificar se está certo acessando o link.
- [Ambiente Web Local](http://127.0.0.1:8000/)
