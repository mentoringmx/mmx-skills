#!/usr/bin/env python3
"""Cinco checagens mecanicas. Nenhuma delas olha o conteudo do texto.

Os arquivos sao quebrados em ~90 colunas, entao regra por proximidade de palavra
reprovaria pela quebra de linha, nao pelo conteudo. Esse controle pertence ao
repositorio do servidor, onde ficam as descricoes dos tools.

Sobre o parser de frontmatter: o SKILL.md e conferido com YAML estrito. Os
comandos sao conferidos com o mesmo criterio do runtime, que aceita um valor com
dois-pontos sem aspas ("... no MentoringMX: saude ..."). Reprovar um arquivo que o
Claude Code carrega sem reclamar seria travar PR legitimo por ruido de CI.
"""

import json
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
falhas = []


def erro(msg):
    falhas.append(msg)


def corpo_frontmatter(path):
    """Devolve o texto entre os delimitadores '---'. Levanta ValueError se nao houver."""
    texto = path.read_text(encoding="utf-8")
    if not texto.startswith("---\n"):
        raise ValueError("nao comeca com '---'")
    fim = texto.find("\n---", 3)
    if fim == -1:
        raise ValueError("frontmatter nao fechado")
    return texto[4:fim]


def frontmatter_yaml(path):
    """Frontmatter como YAML estrito."""
    dados = yaml.safe_load(corpo_frontmatter(path))
    if not isinstance(dados, dict):
        raise ValueError("frontmatter nao e um mapeamento YAML")
    return dados


def frontmatter_chaves(path):
    """Frontmatter como o runtime le: chave ate o primeiro dois-pontos, valor no resto."""
    dados = {}
    for linha in corpo_frontmatter(path).splitlines():
        if not linha.strip() or linha.startswith("#") or ":" not in linha:
            continue
        if linha[0].isspace():  # continuacao de valor
            continue
        chave, _, valor = linha.partition(":")
        dados[chave.strip()] = valor.strip().strip("'\"")
    return dados


# 1 e 2. SKILL.md tem frontmatter YAML valido com name/description, e o name bate
#        com o nome da pasta.
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    erro("[1] nenhum SKILL.md encontrado em skills/")

for skill_md in skills:
    rel = skill_md.relative_to(ROOT)
    try:
        fm = frontmatter_yaml(skill_md)
    except (ValueError, yaml.YAMLError) as exc:
        erro(f"[1] {rel}: frontmatter YAML invalido ({str(exc).splitlines()[0]})")
        continue
    for campo in ("name", "description"):
        if not str(fm.get(campo, "")).strip():
            erro(f"[1] {rel}: campo '{campo}' ausente ou vazio")
    pasta = skill_md.parent.name
    if fm.get("name") != pasta:
        erro(f"[2] {rel}: name '{fm.get('name')}' != nome da pasta '{pasta}'")

# 3. Todo arquivo em commands/ tem frontmatter com description nao vazio.
comandos = sorted((ROOT / "commands").glob("*.md"))
if not comandos:
    erro("[3] nenhum comando encontrado em commands/")

for cmd in comandos:
    rel = cmd.relative_to(ROOT)
    try:
        fm = frontmatter_chaves(cmd)
    except ValueError as exc:
        erro(f"[3] {rel}: frontmatter invalido ({exc})")
        continue
    if not fm.get("description", "").strip():
        erro(f"[3] {rel}: 'description' ausente ou vazio")

# 4. marketplace.json e JSON valido, todo caminho local que ele cita existe, e o name
#    da entrada bate com o name do plugin.json.
mkt_path = ROOT / ".claude-plugin" / "marketplace.json"
plugin_path = ROOT / ".claude-plugin" / "plugin.json"
try:
    mkt = json.loads(mkt_path.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    erro(f"[4] marketplace.json ilegivel ou invalido: {exc}")
    mkt = None


def conferir_caminho(valor, origem):
    if isinstance(valor, str) and valor.startswith("./"):
        if not (ROOT / valor[2:]).exists():
            erro(f"[4] {origem}: caminho '{valor}' nao existe")
    elif isinstance(valor, list):
        for item in valor:
            conferir_caminho(item, origem)


CAMPOS_DE_CAMINHO = ("skills", "commands", "agents", "hooks", "mcpServers", "lspServers")

if mkt is not None:
    entradas = mkt.get("plugins", [])
    if not entradas:
        erro("[4] marketplace.json nao declara nenhum plugin")

    for entrada in entradas:
        nome = entrada.get("name", "<sem name>")
        conferir_caminho(entrada.get("source"), f"plugin '{nome}' source")
        for campo in CAMPOS_DE_CAMINHO:
            conferir_caminho(entrada.get(campo), f"plugin '{nome}' {campo}")

    try:
        plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        erro(f"[4] plugin.json ilegivel ou invalido: {exc}")
    else:
        nomes = sorted(n for n in (e.get("name") for e in entradas) if n)
        if plugin.get("name") not in nomes:
            erro(
                f"[4] plugin.json name '{plugin.get('name')}' nao aparece em "
                f"marketplace.json {nomes}"
            )
        for campo in CAMPOS_DE_CAMINHO:
            conferir_caminho(plugin.get(campo), f"plugin.json {campo}")

# 5. Nenhum arquivo contem URL de fetch nem string parecida com credencial.
#    As agulhas sao montadas por concatenacao, com o corte fora do termo buscado,
#    para que este arquivo nao se reprove e para que um grep pelo termo nao o
#    encontre aqui. A varredura cobre o repositorio inteiro, sem excecao.
AGULHAS = ["raw.github" + "usercontent.com", "gh" + "p_", "s" + "k-"]

for caminho in sorted(ROOT.rglob("*")):
    if not caminho.is_file() or ".git" in caminho.parts:
        continue
    try:
        conteudo = caminho.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    for agulha in AGULHAS:
        if agulha in conteudo:
            erro(f"[5] {caminho.relative_to(ROOT)}: contem '{agulha}'")

if falhas:
    print(f"{len(falhas)} falha(s):\n")
    for f in falhas:
        print(f"  {f}")
    sys.exit(1)

print("As cinco checagens passaram.")
