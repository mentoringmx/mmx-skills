# MentoringMX Skills

Skill e comandos para operar o MentoringMX conversando com um agente de IA. Você descreve
o que aconteceu — "cadastra a Marina no Acelera", "fecha o encontro de ontem", "entrou um
lead pelo Instagram" — e o agente monta o plano de escrita, pede sua aprovação e executa
no MMX.

**[Como funciona e como instalar, em uma página →](https://mentoringmx.github.io/mmx-skills/)**
Feita para quem vai usar, não para quem vai ler código.

## Você provavelmente não precisa disto

O servidor MCP do MentoringMX já entrega o contrato de operação completo a qualquer
cliente conectado, sem instalação nenhuma. As regras de organização, o modelo de dados e
as sequências de chamada chegam sozinhas: pelo campo `instructions` da conexão e pelo tool
`get_playbook`.

Quem só quer operar o MMX conecta o MCP e pronto. Um agente sem nada deste repositório
opera com a mesma segurança e segue exatamente as mesmas regras.

O que está aqui é conveniência opcional: o formato de conversa, o fechamento de encontro a
partir de transcrição e cinco atalhos de digitação. Se você usa ChatGPT, n8n ou um agente
próprio, nada disto se aplica a você e você não está perdendo nada.

## Comece pelo produto

O passo obrigatório é dentro do MMX: **aviso “Opere o MentoringMX conversando com seu agente de IA” → Conectar**. É
lá que você conecta o servidor. A autenticação é OAuth, pelo navegador, e o agente herda
exatamente as permissões que você já tem.

Instalar a skill vem depois, e só se você quiser.

## Instalação

Sempre por versão fixada. A versão instalada é determinada pelo manifesto deste
repositório, não pelo comando — ver [`docs/instalacao.md`](docs/instalacao.md) para o
passo a passo de cada cliente, como conferir o que foi instalado e como remover.

Claude Code:

```
claude plugin marketplace add https://github.com/mentoringmx/mmx-skills
claude plugin install mmx-operador@mentoringmx
```

Claude Desktop e Cowork instalam pela interface, colando a URL do repositório. O
`docs/instalacao.md` tem o caminho de menu exato, e a
[página de instalação](https://mentoringmx.github.io/mmx-skills/) tem o mesmo passo a
passo com telas.

## O que tem aqui

| Item | O que faz | Equivalente em português |
|---|---|---|
| Skill `mmx-operador` | Camada de conversa: formato do plano e do ledger, fechamento por transcrição, cuidado com dado pessoal mascarado, o que fazer sem o MCP conectado | Ativa sozinha, você não chama |
| `/mmx-carteira` | Panorama de leitura: saúde, encontros sem debrief, tasks vencidas, funil. Não grava nada | "como está minha carteira" |
| `/mmx-fechar-sessao` | Decompõe a transcrição em debrief, conquistas, tasks, jornada, saúde e notas | "fecha a sessão que acabei de dar" |
| `/mmx-incluir` | Inclui e matricula mentorado, com deduplicação e posição na trilha | "cadastra o Rafael no Acelera" |
| `/mmx-jornada` | Move estágio, marca checklist, lança saúde | "põe a Marina na próxima etapa" |
| `/mmx-lead` | Registra ou movimenta lead no CRM, com atividade, objeção e conversão | "entrou um lead novo" |

## Compatibilidade

Exige um servidor MMX que exponha `get_bootstrap` e `get_playbook`. Sem eles a skill ainda
funciona, mas em modo degradado: ela avisa e passa a confirmar cada entidade com você
antes de gravar.

Para conferir, peça ao agente conectado:

> chama `get_server_info` e me diz se `get_bootstrap` e `get_playbook` estão na lista

A resposta traz `version`, `instructions_version` e o catálogo de tools. Os dois precisam
aparecer.

## Segurança

Nada aqui pede token, senha ou chave, e nada aqui é escrito para um agente buscar sozinho
em tempo de execução. A instalação é ação humana, com versão fixada, justamente para que
instrução de operação não entre por URL. Ver [`docs/seguranca.md`](docs/seguranca.md).

## Licença

Apache License 2.0. Ver [`LICENSE`](LICENSE) e [`NOTICE`](NOTICE).
