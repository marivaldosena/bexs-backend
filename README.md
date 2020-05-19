# Bexs | Backend

Teste de desenvolvimento Full Stack que visa criar uma API e uma interface web para consumir perguntas.

## Tópicos

- [Instalação](#instalação)
  - [Docker](#docker)
  - [Python](#python)
  - [Flask](#flask)
  - [PostgreSQL](#postgresql)
  - [Visual Studio Code](#visual-studio-code)
- [Configuração e Execução](#configuração-e-execução)
  - [Configuração do ambiente](#configuração-do-ambiente)
    - [Criação de imagem do Docker](#criação-de-imagem-do-docker)
    - [Criação do ambiente virtual em Python](#criação-do-ambiente-virtual-em-python)
    - [Configuração das variáveis de ambiente](#configuração-das-variáveis-de-ambiente)
  - [Execução da solução](#execução-da-solução)
- [Estrutura de arquivos](#estrutura-de-arquivos)
  - [app](#app)
    - [models](#models)
    - [routes](#routes)
    - [tests](#tests)
  - [config](#config)
  - [migrations](#migrations)
    - [versions](#versions)
  - [venv](#venv)

---

## Instalação

Para utilizar a solução é necessário a instalação dos seguintes componentes:

- Docker
- Python
- Flask
- SQLAlchemy
- Gunicorn
- Pytest

### Docker

Docker é uma ferramenta de virtualização que padroniza a experiência de desenvolvimento independentemente da plataforma. Dessa forma, uma equipe de desenvolvedores pode utilizar as mesmas ferramentas, dependências e versões de forma padronizada.

Para tanto, o Docker utiliza o conceito de contêineres, que são abstrações de uma plataforma computacional, de forma que podemos acoplar diversos contêineres com responsabilidades específicas. Por exemplo: um contêiner fica responsável pela persistência dos dados, outro pela execução enquanto outro pode ser responsável pelo sistema de filas de entrega, etc.

A vantangem em utilizá-lo é poder padronizar como toda a equipe trabalha e efetuam mudanças. A desvantagem é que aumenta a complexidade das ferramentas utilizadas.

Para instalar o Docker é necessário acessar o site oficial na seguinte página web [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/) ou clique em [Docker](https://docs.docker.com/docker-for-windows/install/).

[Voltar ao menu](#tópicos)

### Python

Python é uma linguagem de programação interpretada, fortemente tipada e orientada a objetos. Para baixá-la, clique em [Python](https://www.python.org/downloads/) ou digite [https://www.python.org/downloads/](https://www.python.org/downloads/) na barra de endereços do navegador de sua preferência.

Python é uma linguagem simples de utilizar para criação de protótipos e permite que o desenvolvedor possa refatorar rapidamente e adaptar a solução de acordo com as demandas que surgirem.

As vantagens em utilizá-la são relacionadas a rapidez com que um desenvolvedor menos experiente consegue fazer entregas consistentes, não precisar especificar tipos de dados, as alterações serem imediatas e possuem diversas bibliotecas inclusas por padrão e outras instaláveis através do repositório [PyPI](https://pypi.org/).

A desvantagem é que Python é uma linguagem lenta em comparação às linguagens compiladas, ser single-thread e não possuir exigir a especificação dos tipos de dados.

[Voltar ao menu](#tópicos)

### Flask

É uma micro-framework utilizada para a criação de sites e/ou outras APIs Webs.

Flask permite que você esboce protótipos de forma simples e rápida. Além disso, permite a integração com outras bibliotecas para execução atividades específicas, tais como: integração com bancos de dados relacionais e não-relacionais, gerenciamento de filas e outros tipos de jobs, websockets, encriptação de dados, etc.

Esta framework permite que você utilize tanto o paradigma de programação orientada a objetos quanto o procedimental. Dessa forma, o desenvolvedor pode utilizar o padrão que achar melhor para aquela funcionalidade específica desde que não haja detrimento à legibilidade e boas práticas de software.

Para maiores informações, acesse o site no endereço eletrônico [https://palletsprojects.com/p/flask/](https://palletsprojects.com/p/flask/) ou clique no seguinte link [Flask](https://palletsprojects.com/p/flask/).

[Voltar ao menu](#tópicos)

### PostgreSQL

É um banco de dados relacional de código livre de alto desempenho, resiliente, e com forte tolerância a falhas e disponibilidade de serviço. É uma solução de porte empresarial que permite alta escalabilidade.

Uma das vantangens em utilizá-lo é o suporte aos padrões mais recentes de SQL, utilização de JSON, extensibilidade através de PL/SQL, Python e outros.

Para baixá-lo é necessário ir ao site oficial em [https://www.postgresql.org/download/](https://www.postgresql.org/download/) ou clicando no seguinte link [PostgreSQL](https://www.postgresql.org/download/).

[Voltar ao menu](#tópicos)

### Visual Studio Code

É um editor de textos de código livre otimizado para o desenvolvimento. Permite a utilização de extensões para finalidades específicas.

Entre as vantagens, podemos citar: variedade de extensões para linguagens e funcionalidades específicas, leve e multiplataforma, suprir as necessidades mais triviais de desenvolvimento, fácil configuração e extensibilidade, etc.

Por não ser uma IDE, ele não possui recursos de análise estática e de sintaxe integrada incluídos nativamente e, em alguns casos, não há extensões disponíveis.

Para baixá-lo digite o seguinte endereço na barra de navegação de seu navegador [https://code.visualstudio.com/](https://code.visualstudio.com/) ou clique no seguinte link [Visual Studio Code](https://code.visualstudio.com/).

[Voltar ao menu](#tópicos)

---

## Configuração e Execução

Para executar a aplicação é necessária a instalação do [Docker](#docker) e [Python](#python). Quando terminar a instalação e configuração dos componentes supra-citados, proceda conforme as instruções subsequentes.

[Voltar ao menu](#tópicos)

### Configuração do ambiente

Para configurar o ambiente de desenvolvimento serão necessários seguir os passos descritos nos sub-tópicos dessa seção.

[Voltar ao menu](#tópicos)

#### Criação de imagem do Docker

No diretório raiz da solução há um arquivo chamado **docker.env.example**. Copie-o e renomeie-o como **docker.env**. Altere as variáveis conforme sua preferência.

Para a execução dos contêineres, vá ao terminal e digite:

```bash
mv .env.example .env
mv docker.example docker.env
docker-compose up --build -d
```

[Voltar ao menu](#tópicos)

#### Criação do ambiente virtual em Python

É aconselhável abrir outra aba em seu terminal, ir ao diretório da solução e digitar o seguinte:

```bash
virtualenv --python=python3 venv
source ./venv/bin/activate
```

Esse passo serve para que você possa utilizar os recursos do editor de textos ou IDE de sua preferência.

Após ter feito isso, o seu terminal acrescentará (venv) antes do diretório atual, sinalizando que você está no ambiente de desenvolvimento específico. Digite:

```bash
pip install -r requirements.txt
```

[Voltar ao menu](#tópicos)

#### Configuração das variáveis de ambiente

Se você seguiu as instruções da seção [Criação do ambiente virtual em Python](#criação-do-ambiente-virtual-em-python) e está trabalhando com a versão de sua máquina local à parte, será necessário configurar as variáveis de ambiente conforme o que foi definido no arquivo **docker.env** para que a aplicação possa saber exatamente quais são suas configurações.

Senão, pode utilizar o próprio Docker e digitar os seguintes comandos:

```bash
docker-compose exec web flask migrate
docker-compose exec web flask seed
```

**Observação:**

*O procedimento citado acima deve ser executado apenas uma vez quando for configurar o banco de dados. Feito isso, não será mais necessário esta etapa.*

### Execução da solução

Para execução diária da aplicação é realizada por meio do seguinte comando:

```bash
docker-compose exec web flask run
```

Ou, se preferir, pode utilizar o servidor de aplicação Gunicorn:

```bash
gunicorn -b 0.0.0.0:PORT --workers=4 --reload --access-logfile - "app:create_app()"
```

[Voltar ao menu](#tópicos)

---

## Estrutura de arquivos

Os arquivos estão estruturados de acordo com a função lógica deles dentro da aplicação.

### app

É o diretório onde estão todos os detalhes da aplicação. É esse diretório que você trabalhará a maior parte do tempo.

#### models

Este diretório possui todos os modelos lógicos da aplicação.

#### routes

Todos os endpoints devem ser especificados dentro deste diretório. É aconselhável criar um único arquivo para os endpoints relacionados.

#### tests

É aconselhável criar todos os testes unitários e de integração neste diretório. A biblioteca de teste utiliza é o Pytest.

### config

Neste diretório estão contidos todas as variáveis necessárias para a execução da aplicação.

### migrations

As configurações e migrações criadas pela biblioteca Alembic estão localizadas neste diretório.

#### versions

Todas as migrações estão dentro deste diretório e residem em arquivos específicos. É interessante criá-los e editá-los manualmente, já que a biblioteca Alembic possui padrões gerais que podem não ser apropriadas para casos específicos.

### venv

Este diretório foi criado pela ferramenta virtualenv para conter a plataforma de execução com uma versão específica do Python.

Dessa forma, o ambiente de desenvolvimento fica padronizada para a equipe.

Geralmente, não é necessário alterar os arquivos contidos neste diretório.

[Voltar ao menu](#tópicos)