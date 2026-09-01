---
description: Fecha um encontro de mentoria no MentoringMX a partir da transcrição, decompondo em debrief, conquistas, tasks, jornada, saúde e notas.
---

Feche o encontro de mentoria no MentoringMX.

1. Chame `get_bootstrap()` e resolva a organização. Se ambígua, pergunte antes de qualquer coisa.
2. Carregue `get_playbook("pos-sessao")` e siga.
3. Ache o encontro antes de criar: `list_events(org_id, mentee_id)` e
   `list_events(org_id, only_pending_debrief=true)`. Encontro duplicado credita entrega duas vezes.
4. Fonte da transcrição, nesta ordem: o que o operador anexou ou colou; uma gravação de
   alguma ferramenta de transcrição conectada nesta sessão, perguntando qual antes de puxar;
   se não houver nenhuma das duas, pergunte. Não reconstrua o encontro de memória.
5. Leia a fonte inteira antes de extrair.
6. Extraia com âncora: cada item carrega a citação, o timestamp ou a seção de onde saiu.
   Sem âncora, não entra.
7. Classifique pela tabela do playbook. Três armadilhas: `agreements` é prosa e não substitui
   `create_mentee_task`; toda task precisa de `owner` e `due_date`; e `internal_note` grava
   como briefing, então leitura sensível vai em `add_mentee_note(kind="confidential")` mais
   `link_event_note`.
8. Pergunte pela jornada mesmo que a fonte não diga: algum item de checklist foi concluído?
   A pessoa mudou de estágio? Preencher `stage` no evento não move a trilha.
9. Rode `close_event_debrief(..., dry_run=true)` e leia `ritual_open` antes de montar o plano.
10. Apresente o plano em bloco, agrupado por destino, com as âncoras. Espere aprovação.
11. Execute com o debrief por último e devolva o ledger com os ids.

Se a fonte for call de venda e não encontro de mentorado, pare e confirme com o operador
antes de seguir por `capturar-lead`.

$ARGUMENTS
