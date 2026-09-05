---
description: Inclui e matricula um mentorado no MentoringMX, com deduplicação e posicionamento na trilha.
---

Inclua um mentorado no MentoringMX.

1. `get_bootstrap()`. Organização ambígua pergunta, nunca escolhe.
2. `get_playbook("incluir-mentorado")` e siga.
3. Deduplique antes de criar, em pessoas, mentorados e leads. Use
   `find_person_by_contact` para email e telefone: a leitura de pessoa vem mascarada e
   comparar o que você leu nunca bate. Achou parecido mas não idêntico, mostre e pergunte.
4. Se existir lead para essa pessoa, use `convert_lead`. Nunca crie a person à mão para um
   lead ganho.
5. Não esqueça de posicionar na jornada: sem isso o mentorado não aparece no Kanban.
6. Documento pessoal vai no campo próprio da pessoa, nunca em observação. Campo que
   voltou mascarado não está vazio: não o preencha para "completar".
7. Plano em bloco, aprovação, ledger.

Lista com várias pessoas: deduplique todas antes de qualquer escrita, apresente a triagem
(novas, existentes, duvidosas), pergunte só sobre as duvidosas.

$ARGUMENTS
