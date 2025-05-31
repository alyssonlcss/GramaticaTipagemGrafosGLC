from antlr4 import *
from GraphLexer import GraphLexer
from GraphParser import GraphParser
from GraphValidator import GraphValidator
from anytree import Node, RenderTree
import os

def gerar_arvore_txt(tree, parser, nome_arquivo):
    def to_node(ctx, parent=None):
        name = parser.ruleNames[ctx.getRuleIndex()] if hasattr(ctx, 'getRuleIndex') else str(ctx)
        node = Node(name, parent=parent)
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, ParserRuleContext):
                to_node(child, parent=node)
            else:
                Node(str(child), parent=node)
        return node

    raiz = to_node(tree)
    with open(f"tree_tests/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
        for pre, _, node in RenderTree(raiz):
            f.write("%s%s\n" % (pre, node.name))

def testar_arquivo(caminho):
    print(f"\n🧪 Testando: {caminho}")
    input_stream = FileStream(caminho, encoding="utf-8")
    lexer = GraphLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GraphParser(token_stream)
    tree = parser.graph()

    # Geração da árvore sintática
    nome = os.path.splitext(os.path.basename(caminho))[0]
    os.makedirs("tree_tests", exist_ok=True)
    gerar_arvore_txt(tree, parser, nome)

    # Validação semântica
    validator = GraphValidator()
    validator.visit(tree)
    validator.report()

def rodar_todos():
    for arquivo in sorted(os.listdir("tests")):
        if arquivo.endswith(".txt"):
            testar_arquivo(os.path.join("tests", arquivo))

if __name__ == "__main__":
    rodar_todos()
