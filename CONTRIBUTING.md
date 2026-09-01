# Contribuindo

Este repositório distribui a skill `mmx-operador` e cinco comandos. É uma camada de
conveniência — o contrato de operação do MMX vive no servidor. Vale ler
[`docs/arquitetura.md`](docs/arquitetura.md) antes de abrir qualquer coisa aqui, porque
boa parte das contribuições que chegam pertence a outro lugar.

## Playbook não se altera aqui

É a confusão que aparece primeiro, então ela vem antes de tudo.

Os playbooks — as sequências de chamada de cada operação — vivem no servidor MCP e são
servidos por `get_playbook`. Não existe cópia deles neste repositório, de propósito.

Se você viu o agente chamar os tools na ordem errada, pular uma etapa, usar um tool
descontinuado ou gravar em campo errado, **isso é playbook, e a issue vai para o time do
produto**, não para cá. Um pull request corrigindo um playbook aqui não teria nada para
corrigir, e se tivesse, o merge não mudaria o comportamento de agente nenhum.

O que pertence a este repositório: o agente entendeu o pedido errado, respondeu num
formato ruim, ativou a skill quando não devia, não ativou quando devia, ou um comando
pediu a coisa errada.

## A lógica não mora no comando

Um comando resolve a organização com `get_bootstrap`, carrega o playbook certo e segue.
Ele é atalho de digitação, não segunda fonte de verdade.

Um pull request que move regra de negócio para dentro de um arquivo de `commands/` — a
sequência de chamadas, os campos obrigatórios, a tabela de classificação — não vai ser
aceito, mesmo que funcione. Ele cria exatamente a divergência que a arquitetura existe
para evitar.

## Melhoria de skill ou comando

Abra uma issue com o template **melhoria**, descrevendo duas coisas:

- **o comportamento observado** do agente, com o que você pediu e o que ele fez;
- **o comportamento esperado**, com o que ele deveria ter feito.

"Descreva sua sugestão" não é o que estamos pedindo. A diferença entre os dois é o que
permite verificar se a mudança resolveu.

## Pull requests

Todo PR que mexe em `skills/` ou `commands/` **diz na descrição qual comportamento de
agente muda**. Não o que o arquivo passou a dizer — o que o agente passa a fazer
diferente, e em que situação.

O CI roda cinco checagens mecânicas: frontmatter da skill, nome batendo com a pasta,
`description` em todo comando, manifesto válido com os caminhos existindo, e ausência de
credencial ou URL de fetch. Elas são mecânicas de propósito. Se você achar que falta uma
checagem de conteúdo, provavelmente ela pertence ao repositório do servidor, onde ficam as
descrições dos tools.

## Versionamento

SemVer, e o [`CHANGELOG.md`](CHANGELOG.md) atualizado em todo release.

- **MAJOR** — o operador precisa mudar como fala com o agente, ou um comando saiu.
- **MINOR** — comando ou capacidade nova, compatível com o que já existia.
- **PATCH** — correção de texto, gatilho de ativação ou formato.

## Checklist de release

A versão instalada é fixada no manifesto, então a ordem importa:

1. Atualizar `version` em `.claude-plugin/plugin.json` e na entrada do plugin em
   `.claude-plugin/marketplace.json`.
2. Atualizar `source.ref` em `.claude-plugin/marketplace.json` para a tag que está
   prestes a existir.
3. Atualizar o `CHANGELOG.md`.
4. Merge no `main`.
5. **Depois** criar a tag `vX.Y.Z` nesse commit e publicar a release.

Inverter os passos 4 e 5 publica um manifesto apontando para uma tag que ainda não existe,
e a instalação quebra até a tag ser criada.
