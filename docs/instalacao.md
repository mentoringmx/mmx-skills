# Instalação

**O passo obrigatório não é este.** Antes de qualquer coisa, conecte o servidor MCP do MMX
pela tela do produto: aviso “Opere o MentoringMX conversando com seu agente de IA” → Conectar. Feito isso, seu agente
já opera o MentoringMX com o contrato completo, sem instalar nada.

Instalar a skill e os comandos é opcional e posterior. O que eles adicionam é
conveniência: formato de conversa, fechamento de encontro a partir de transcrição e cinco
atalhos.

## Autenticação

Nenhum comando desta página pede token, senha ou chave. A autenticação do MMX é OAuth,
acontece no navegador no momento em que você conecta o MCP, e o agente herda exatamente as
permissões que você já tem no produto. Se alguma instrução pedir uma credencial colada no
chat, ela não veio daqui.

## Como a versão fica fixada

A versão não vai no comando de instalação. Ela está declarada no manifesto deste
repositório: a entrada do plugin aponta para uma tag específica.

```json
"source": {
  "source": "url",
  "url": "https://github.com/mentoringmx/mmx-skills.git",
  "ref": "v1.1.1"
}
```

O catálogo acompanha o `main`, mas o conteúdo que chega na sua máquina é sempre a árvore
daquela tag, em qualquer cliente. Você só recebe uma versão nova quando o `ref` muda num
release — nunca por um commit que entrou no `main`.

Isso vale igual para Claude Code, Claude Desktop e Cowork, inclusive nos dois últimos,
onde a interface não tem campo para tag.

## Claude Code

Instalar:

```
claude plugin marketplace add https://github.com/mentoringmx/mmx-skills
claude plugin install mmx-operador@mentoringmx
```

Use a URL inteira, não o atalho `mentoringmx/mmx-skills`. O atalho é resolvido por SSH, e
falha em quem não tem chave SSH configurada no GitHub. Com a URL, o acesso é por HTTPS e
não pede nada.

Conferir o que foi instalado:

```
claude plugin list
claude plugin details mmx-operador@mentoringmx
```

O `details` mostra o inventário de componentes — a skill e os cinco comandos — e o custo
de contexto projetado. Espere ver `mmx-operador` na versão `1.0.0`, uma skill e cinco
comandos, e nenhum hook, agente ou servidor MCP: este plugin não traz nenhum dos três.

Remover:

```
claude plugin uninstall mmx-operador@mentoringmx
claude plugin marketplace remove mentoringmx
```

O primeiro comando desinstala o plugin; o segundo tira o catálogo da sua configuração.
Rodar só o primeiro deixa o marketplace registrado, sem nada instalado, o que também é um
estado válido se você pretende reinstalar depois.

## Claude Desktop

1. Abra o menu **Customize**, na barra lateral esquerda.
2. Vá na aba **Plugins**.
3. Em *Personal plugins*, clique no botão **+** e escolha **Add from a repository**.
4. Cole `https://github.com/mentoringmx/mmx-skills` e confirme.
5. Instale o plugin **mmx-operador** na lista que aparecer.

Conferir: o menu Customize lista os plugins instalados. Digitando `/` no chat aparecem os
comandos que vieram com ele.

Remover: na seção Plugins, botão de menu no canto direito do plugin → **Remove**.

## Cowork

Mesmo caminho do Desktop, com um passo a mais no começo: abra a aba **Cowork** antes de
abrir o **Customize**.

1. Aba **Cowork**.
2. Menu **Customize** → aba **Plugins**.
3. Em *Personal plugins*, **+** → **Add from a repository**.
4. Cole `https://github.com/mentoringmx/mmx-skills` e confirme.
5. Instale **mmx-operador**.

Conferir e remover funcionam como no Desktop.

## Se algo não aparecer

Comando que não aparece depois de instalar costuma ser sessão que precisa reiniciar. No
Claude Code, `claude plugin list` diz o que está instalado mesmo que a sessão atual ainda
não tenha carregado.

Se a skill ativar mas o agente disser que não encontra os tools do MMX, o problema não é a
instalação: é a conexão MCP, e ela se resolve na tela do produto, não aqui.
