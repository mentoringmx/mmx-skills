---
description: Registra ou movimenta um lead no CRM do MentoringMX, incluindo atividade, objeção e conversão.
---

Opere um lead no CRM do MentoringMX.

1. `get_bootstrap()` e `get_playbook("capturar-lead")`.
2. Deduplique em leads e em pessoas, com `find_person_by_contact` para email e telefone,
   que vêm mascarados na leitura. Ex-mentorado voltando é lead legítimo, mas o operador
   precisa saber do histórico antes de tratar como frio.
3. Campos de diagnóstico (ponto B, custo de inação, histórico, ganchos) vêm do que a pessoa
   disse, com as palavras dela. Não invente. Vazio é honesto.
4. Objeção registra a frase da pessoa, não o rótulo que você deu a ela.
5. Motivo de perda vem da lista existente. Criar um novo precisa de aprovação do operador.
6. Plano em bloco, aprovação, ledger.

Se o operador anexou transcrição de call de venda, extraia com âncora antes de classificar,
do mesmo jeito que em `pos-sessao`.

$ARGUMENTS
