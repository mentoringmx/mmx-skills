# Segurança

## Este repositório não recebe credencial

Nada aqui pede token, senha ou chave de API, e nada aqui armazena uma. A autenticação do
MentoringMX é OAuth, acontece no navegador quando você conecta o servidor MCP pela tela do
produto, e o agente herda exatamente as permissões que a pessoa já tem no MMX — nem uma a
mais.

Não existe caminho de instalação neste repositório que envolva colar uma credencial em
algum lugar. Se você encontrar uma instrução pedindo isso e ela se apresentar como sendo
do MMX, ela não é.

## Por que a instalação é por versão fixada

Porque a alternativa é perigosa de um jeito específico.

Um agente que busca instrução de uma URL pública e a segue fica exposto a três coisas ao
mesmo tempo: repositório comprometido, URL trocada e typo-squatting. Nos três casos o
resultado é o mesmo — o agente executa instrução escrita por terceiro contra uma base
multi-tenant de produção, com as credenciais legítimas do operador e sem nada que pareça
errado na tela.

Não é um risco teórico de supply chain. É a diferença entre "alguém alterou um arquivo" e
"alguém escreveu na organização de um cliente".

Instalação humana com tag fixada corta isso: quem instala é uma pessoa, o que é instalado
é uma árvore específica e imutável, e uma versão nova só entra quando alguém decide
instalá-la. Por isso o pin está no manifesto e não no comando — assim ele vale também nos
clientes cuja interface não tem campo para tag.

Pela mesma razão, nenhum documento deste repositório instrui um agente a buscar conteúdo
em `raw.github` + `usercontent.com` ou equivalente. Isso é verificado no CI, em todo
commit.

## O agente não segue instrução remota

O campo `instructions` do servidor MMX instrui o agente a não buscar nem seguir instrução
de operação vinda de URL, arquivo ou mensagem de terceiro, mesmo que se apresente como
oficial. A skill deste repositório repete a mesma regra, na seção *Procedência*.

As fontes legítimas de instrução de operação do MMX são três, e apenas três: o
`instructions` do servidor, o `get_playbook`, e a skill instalada.

## Como reportar

Encontrou algo com implicação de segurança, mande para `<PREENCHER: endereço de contato de
segurança>`.

Enquanto esse endereço não existir, não abra issue pública descrevendo o problema em
detalhe. Abra uma issue dizendo apenas que encontrou algo e pedindo um canal privado.
