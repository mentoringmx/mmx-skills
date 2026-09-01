# Changelog

Todas as mudanças relevantes deste projeto são registradas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e o
versionamento segue [SemVer](https://semver.org/lang/pt-BR/).

## [Não publicado]

## [1.0.1] - 2026-09-01

### Corrigido

- A instalação não exige mais chave SSH. A entrada do plugin usava o source type
  `github`, que faz o Claude Code clonar por `git@github.com`; quem não tem chave
  configurada recebia `Permission denied (publickey)` e não conseguia instalar. Agora
  o source é um git URL HTTPS explícito, com o mesmo mecanismo de pin por tag.
- Os comandos da documentação usam a URL inteira do repositório em
  `claude plugin marketplace add`. O atalho `owner/repo` também é resolvido por SSH.

A `1.0.0` está publicada mas não é instalável em máquina sem chave SSH. Use a `1.0.1`.

## [1.0.0] - 2026-09-01

Primeira versão pública.

### Adicionado

- Skill `mmx-operador`: camada de conversa para operar o MentoringMX via MCP. Cobre o
  formato do plano de escrita e do ledger, o fechamento de encontro a partir de
  transcrição e o que fazer quando o servidor MCP não está conectado.
- Comando `/mmx-carteira`: panorama de leitura da carteira — saúde, encontros sem debrief
  fechado, tasks vencidas e funil. Não grava nada.
- Comando `/mmx-fechar-sessao`: fecha um encontro a partir da transcrição, decompondo em
  debrief, conquistas, tasks, jornada, saúde e notas.
- Comando `/mmx-incluir`: inclui e matricula mentorado, com deduplicação e posicionamento
  na trilha.
- Comando `/mmx-jornada`: atualiza a trilha de um mentorado — estágio, checklist e saúde.
- Comando `/mmx-lead`: registra ou movimenta lead no CRM, incluindo atividade, objeção e
  conversão.
- Documentação de instalação por versão fixada, arquitetura das camadas e segurança.

### Notas de instalação

- No Claude Code, use a URL inteira do repositório em `claude plugin marketplace add`. O
  atalho `owner/repo` é resolvido por SSH e falha em quem não tem chave configurada no
  GitHub.

### Requisitos

- Exige um servidor MMX que exponha `get_bootstrap` e `get_playbook`. Sem eles a skill
  opera em modo degradado, avisando o operador e confirmando cada entidade antes de
  gravar.

### Notas

- O modelo de encontro é **evento**, não sessão. `create_session` e `update_session` estão
  descontinuados e retornam erro sem gravar. Um encontro é fechado por
  `close_event_debrief`, que credita a entrega de forma idempotente.
- O contrato de operação não mora aqui: ele chega pelo campo `instructions` do servidor e
  por `get_playbook`. Divergiu, o playbook do servidor vence.

[Não publicado]: https://github.com/mentoringmx/mmx-skills/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/mentoringmx/mmx-skills/releases/tag/v1.0.1
[1.0.0]: https://github.com/mentoringmx/mmx-skills/releases/tag/v1.0.0
