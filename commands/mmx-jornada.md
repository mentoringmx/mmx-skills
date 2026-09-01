---
description: Atualiza a trilha de um mentorado no MentoringMX: estágio, checklist e saúde.
---

Atualize a jornada de um mentorado no MentoringMX.

1. `get_bootstrap()` e `get_playbook("atualizar-jornada")`.
2. Carregue o template antes de mover: os stage_id são por trilha, não existe "próximo
   estágio" calculável.
3. Verifique assento compartilhado com `list_seat_group`. Se houver, avise que mover um move
   os dois antes de executar.
4. Movimento para trás confirma com o operador e registra o motivo em nota.
5. Saúde só muda com motivo escrito. Status sem justificativa é número sem evidência.
6. Plano em bloco, aprovação, ledger.

$ARGUMENTS
