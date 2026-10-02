---
description: Importa a ficha consolidada de um mentorado (PDF de onboarding, diagnóstico, objetivos e evolução) para o MentoringMX, decompondo em pessoa, negócio, diagnóstico, objetivo, métrica, encontro, trilha e notas.
---

Importe a ficha consolidada do mentorado para o MentoringMX.

1. Chame `get_bootstrap()` e resolva a organização. Se ambígua, pergunte antes de qualquer coisa.
2. Carregue `get_playbook("importar-ficha")` e siga. Cada encontro da evolução fecha por
   `pos-sessao`, um por vez.
3. Fonte: o PDF ou o texto que o operador anexou. Sem anexo, pergunte. Não reconstrua a
   ficha de memória.
4. Leia o estado atual da matrícula antes de ler o documento: o plano é um diff contra o que
   existe, não uma carga do zero.
5. Leia o documento inteiro antes de extrair, compare páginas vizinhas (página repetida
   conta uma vez) e ancore cada item em `[seção, página]`.
6. Apresente o plano em bloco, agrupado por destino, com as perguntas abertas no fim.
   Espere aprovação. Nada é gravado antes do ok.
7. Execute na ordem do playbook e devolva o ledger com os ids.

Uma ficha, uma rodada: se falhar no meio, pare e entregue o ledger do que já foi gravado.
Relançar duplica registros.

$ARGUMENTS
