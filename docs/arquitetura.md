# Arquitetura

O MentoringMX distribui o comportamento do agente em quatro camadas. Três moram no
servidor e chegam sozinhas; só a quarta exige instalação, e ela é a menos importante.

| Camada | Onde vive | Chega como | Precisa instalar |
|---|---|---|---|
| `instructions` | Servidor MCP | Automático no `initialize` | Não |
| `get_bootstrap` | Servidor MCP | Tool | Não |
| `get_playbook` | Servidor MCP | Tool, sob demanda | Não |
| Skill e comandos | Este repositório | Instalação humana | Sim, opcional |

## O que cada camada carrega

O **`instructions`** é o contrato de operação: regra de organização, modelo canônico de
dados, o que é escrita e o que não é, e o que fazer quando algo fica ambíguo. Ele entra no
contexto do agente no momento em que a conexão é aberta, antes da primeira pergunta.

O **`get_bootstrap`** abre a sessão. Devolve identidade do chamador, organizações com
permissões efetivas, programas, templates de jornada, pipeline, produtos e o índice de
playbooks — de uma vez, para que o agente não precise adivinhar contexto nem montar isso
com uma sequência de leituras.

O **`get_playbook`** entrega a sequência de chamadas de uma operação específica, sob
demanda. É o que impede o agente de reproduzir de memória uma sequência que mudou.

A **skill e os comandos** deste repositório adicionam o que o protocolo não carrega:
formato de conversa, o fechamento de encontro a partir de transcrição e cinco atalhos de
digitação.

## Por que os playbooks não moram aqui

Fonte única, e correção sem redistribuição. Um playbook corrigido no servidor muda o
comportamento de todo mundo na chamada seguinte; um playbook corrigido por pull request
num repositório público não muda nada, porque o agente lê a tabela do servidor. Duas
fontes de verdade, com uma delas inerte, é pior que uma só — alguém abriria o PR, o merge
entraria, e o problema continuaria em produção.

Há um segundo motivo, igualmente decisivo: clientes que não suportam skill — ChatGPT, n8n,
agentes próprios — recebem exatamente o mesmo contrato pelo servidor. Se a regra morasse
na skill, esses clientes operariam sem ela.

## Regra de precedência

**Se a skill ou um comando divergir do playbook do servidor, o playbook vence.** Sempre.

O playbook é versionado e atualizado centralmente. A skill é uma cópia instalada na
máquina de alguém, fixada numa tag, e pode estar velha — inclusive velha o bastante para
citar um tool que já foi descontinuado.

Na prática, isso significa que a skill nunca reproduz uma sequência de chamadas de
memória: ela manda carregar o playbook.
