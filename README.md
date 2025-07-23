# GramaticaTipagemGrafosGLC
Teste de gramatica GLC - Tipagem de Grafos

## Descrição

Este projeto implementa uma gramática livre de contexto (GLC) para definição e validação de grafos tipados, utilizando [ANTLR4](https://www.antlr.org/) para geração do parser em Python. O sistema permite definir tipos de vértices e arestas, atributos obrigatórios e opcionais, herança de tipos, além de validar instâncias de grafos quanto à conformidade semântica.

---

## Estrutura do Projeto

```
GramaticaTipagemGrafosGLC/
│
├── Graph.g4                # Gramática ANTLR para grafos tipados
├── main.py                 # Script principal: executa parsing, validação e geração de árvore sintática
├── GraphLexer.py           # Gerado pelo ANTLR (lexer)
├── GraphParser.py          # Gerado pelo ANTLR (parser)
├── GraphVisitor.py         # Gerado pelo ANTLR (visitor)
├── GraphListener.py        # Gerado pelo ANTLR (listener)
├── GraphValidator.py       # Validador semântico customizado
├── TreePrinter.py          # Impressão de árvores sintáticas (opcional)
├── tests/                  # Casos de teste (válidos e inválidos)
├── tree_tests/             # Saídas das árvores sintáticas dos testes
├── .gitignore              # Arquivos e pastas ignorados pelo git
└── README.md               # Este arquivo
```

---

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repo>
   cd GramaticaTipagemGrafosGLC
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   # Ative no Windows:
   .venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install antlr4-python3-runtime anytree
   ```

4. **Baixe o ANTLR4 (caso queira regenerar os arquivos):**
   - [antlr-4.13.1-complete.jar](https://www.antlr.org/download/antlr-4.13.1-complete.jar)

5. **Gere os arquivos Python do ANTLR (se necessário):**
   ```bash
   java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 Graph.g4
   ```

---

## Como Executar

Execute todos os testes e veja a validação semântica:

```bash
python main.py
```

O script irá:
- Ler todos os arquivos em `tests/`
- Gerar a árvore sintática de cada teste em `tree_tests/`
- Validar semanticamente cada grafo e exibir os erros encontrados ou sucesso

---

## Resultados dos Testes (/tests)

```
🧪 Testando: tests\invalido_atributo_ausente.txt
❌ Erros semânticos encontrados:
  - Vértice 'u1' falta atributo obrigatório 'name'.

🧪 Testando: tests\invalido_ciclo_nao_permitido.txt
❌ Erros semânticos encontrados:
  - Aresta 'c1' forma ciclo (self-loop) não permitido.

🧪 Testando: tests\invalido_duplicata_vertice.txt
❌ Erros semânticos encontrados:
  - Identificador duplicado: 'n1'.

🧪 Testando: tests\invalido_multiplo_erro.txt
❌ Erros semânticos encontrados:
  - Vértice 'x1' falta atributo obrigatório 'val'.
  - Identificador duplicado: 'x1'.
  - Vértice 'x2' usa tipo indefinido 'Y'.
  - Aresta 'e1' espera conexão (X -> X), recebeu (X -> Y).
  - Aresta 'e2' usa tipo indefinido 'Z'.

🧪 Testando: tests\invalido_tipo_aresta.txt
❌ Erros semânticos encontrados:
  - Aresta 'e1' espera conexão (B -> A), recebeu (A -> B).

🧪 Testando: tests\invalido_vertice_tipo_nao_declarado.txt
❌ Erros semânticos encontrados:
  - Vértice 'p1' usa tipo indefinido 'Human'.

🧪 Testando: tests\valido01.txt
✔️  Nenhum erro semântico encontrado.

🧪 Testando: tests\valido02_undirected.txt
✔️  Nenhum erro semântico encontrado.

🧪 Testando: tests\valido03_multigrafo.txt
✔️  Nenhum erro semântico encontrado.

🧪 Testando: tests\valido04_heranca_profunda.txt
❌ Erros semânticos encontrados:
  - Aresta 'l1' espera conexão (A -> A), recebeu (C -> A).

🧪 Testando: tests\valido05_atributos_opcionais.txt
✔️  Nenhum erro semântico encontrado.
```

---

## Funcionalidades

- **Definição de tipos de vértices e arestas** com atributos obrigatórios e opcionais
- **Herança de tipos** de vértices
- **Validação semântica**:
  - Tipos não declarados
  - Atributos obrigatórios ausentes
  - Identificadores duplicados
  - Ciclos não permitidos (self-loop)
  - Conexão de tipos incompatíveis em arestas
- **Geração de árvore sintática** dos testes

---

## Como adicionar novos testes

Basta criar arquivos `.txt` na pasta `tests/` seguindo a sintaxe da gramática definida em `Graph.g4`. O sistema irá processar automaticamente todos os arquivos da pasta.

---

## .gitignore

O projeto já inclui um `.gitignore` para evitar versionar arquivos temporários, ambientes virtuais, caches e saídas de testes.

---

## Créditos

- ANTLR4: https://www.antlr.org/
- anytree: https://anytree.readthedocs.io/

---

## Licença

Este projeto é apenas para fins acadêmicos e de estudo.
