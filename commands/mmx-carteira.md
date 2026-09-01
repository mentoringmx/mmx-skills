---
description: Panorama de leitura da carteira no MentoringMX: saúde, ritual pendente, tasks vencidas e funil. Não grava nada.
---

Dê um panorama da carteira no MentoringMX. Este comando não grava nada.

1. `get_bootstrap()`. Organização ambígua pergunta.
2. Leia: `get_health_summary`, `list_mentees`,
   `list_events(only_pending_debrief=true)`,
   `list_mentee_tasks` em aberto e vencidas, por `owner`,
   `get_crm_pipeline_summary`.
3. Responda em no máximo uma tela, nesta ordem:
   - encontros realizados sem debrief fechado, com há quanto tempo
   - mentorados em risco ou atenção, com há quanto tempo estão assim
   - tasks vencidas, separando `owner=mentor` de `owner=mentee`
   - mentorados sem encontro registrado há mais tempo
   - funil: valor por estágio e leads parados sem próxima ação
4. Feche com a pergunta mais útil, não com um resumo do que você acabou de listar.

O primeiro item é o mais acionável: encontro sem debrief significa entrega não creditada e
combinado não registrado. É dívida de registro, e ela cresce em silêncio.

Não grave nada. Se o operador pedir uma ação a partir daqui, use o comando específico.

$ARGUMENTS
