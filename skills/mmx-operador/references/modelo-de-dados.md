# Modelo de dados MMX: o mínimo para não errar

Carregue quando precisar decidir onde um registro pendura.

## Hierarquia

```
organization  (5 orgs, isolamento por RLS)
  └─ person            pessoa física, única dentro da org
       └─ mentee       = enrollment: matrícula da person em um program
            ├─ journey_progress        estágio atual no journey_template
            ├─ journey_checklist_progress
            ├─ mentee_achievements
            ├─ event_participants     encontros de que participa
            ├─ mentee_tasks
            ├─ mentor_notes            internas
            └─ mentee_related_people   sócio, cônjuge, indicante

  └─ crm_lead          pré-matrícula. convert_lead cria/reaproveita a person
       ├─ crm_activities
       ├─ crm_tasks
       ├─ crm_objections
       └─ crm_call_envelope

  └─ program
       └─ journey_template
            └─ journey_stages
                 └─ journey_checklist_items
```

## As seis confusões que geram dado errado

**1. `person` não é `mentee`.**
Conquista, task, nota e participação em encontro penduram em `mentee_id`. Uma person com duas matrículas tem
dois `mentee_id`, e lançar na matrícula errada joga o registro no relatório do programa errado.

**2. `create_mentee` e `create_enrollment` gravam na mesma tabela.**
`create_enrollment` exige `program_id` e carrega termos comerciais (`ticket_value`,
`sessions_total`). É o que você quer em 95% dos casos. `create_mentee` existe para matrícula
sem programa definido.

**3. `seat_group_id` amarra pessoas diferentes na mesma vaga comercial.**
Sócios, casal, dupla da mesma empresa. `move_mentee_journey_stage` move o grupo inteiro por
padrão (`apply_to_seat_group = true`). `null` significa assento simples.

**4. `stage_id` é por template, não global.**
Não existe "próximo estágio" calculável. Carregue `get_journey_template` antes de mover.

**5. Encontro é evento, não sessão.**
`create_session` e `update_session` estão descontinuados e retornam erro sem gravar;
`list_sessions` e `get_session` leem apenas legado. Um encontro é um `event`, que é ao mesmo
tempo compromisso de agenda e entregável contratual (`counts_as_delivery`), e fechá-lo é
`close_event_debrief`, idempotente no crédito da entrega.

**6. Lead ganho vira mentorado por `convert_lead`, nunca por `create_person`.**
`convert_lead` cria ou reaproveita a person, marca a conversão e grava a atividade. Criar a
person à mão e marcar o lead como ganho perde o vínculo, e não há como refazer.

## Tools que escrevem em mais de uma tabela

Confira o retorno antes de criar registro complementar, para não duplicar.

| Tool | Escreve também em |
|---|---|
| `move_lead_stage` | `crm_activities` |
| `convert_lead` | `crm_conversions`, `crm_activities` |
| `record_call_envelope` | `crm_leads`, `crm_tasks` |
| `record_mentee_health` | `mentor_notes` |
| `close_event_debrief` | `events`, `event_participants`, `mentees` (contador de entregas), `mentor_notes`, `event_notes` |
| `convert_outreach_prospect` | `crm_leads`, `crm_outreach_touches` |
| `add_crm_activity` | `crm_leads` |

## Permissões por domínio

`forbidden` aponta para uma destas, não para erro de argumento:

```
people.view / people.manage
mentees.view / mentees.manage
programs.view / programs.manage
sessions.view / sessions.manage   (legado)
events.view / events.manage
tasks.view / tasks.manage
achievements.view / achievements.manage
crm.view / crm.manage
outreach.view / outreach.manage
health.view
```

Admin-only: convites, grupos de acesso, `get_audit_events`, seed e cleanup de demo.

## Códigos de erro

```
not_authenticated   sessão inválida
forbidden           falta permissão granular
validation_error    argumento fora do schema
not_found           id inexistente na org
org_mismatch        id pertence a outra org: pare, é sinal de contexto trocado
rate_limited        30 chamadas mutantes por minuto por usuário
internal_error      reporte ao operador, não repita cegamente
```

`org_mismatch` merece tratamento especial: significa que você misturou ids de organizações
diferentes na mesma sequência. Pare tudo, recarregue o contexto com `get_bootstrap` e
reporte ao operador antes de continuar.
