from GraphVisitor import GraphVisitor
from GraphParser import *

class GraphValidator(GraphVisitor):
    def __init__(self):
        self.types = {}
        self.edges = {}
        self.vertices = {}
        self.errors = []
        self.declared_ids = set()

    def visitGraph(self, ctx):
        self.visitChildren(ctx)

    def visitVertex_type_decl(self, ctx):
        name = ctx.ID(0).getText()
        parent = ctx.ID(1).getText() if ctx.ID(1) else None
        attrs = self._parse_attributes(ctx.attribute_block())

        # Herdar atributos se houver extends
        if parent:
            if parent not in self.types:
                self.errors.append(f"Tipo pai '{parent}' não declarado para '{name}'.")
            else:
                parent_attrs = self.types[parent]['attrs']
                # Merge: atributos do pai + sobrescritas locais
                for k, v in parent_attrs.items():
                    if k not in attrs:
                        attrs[k] = v

        self.types[name] = {
            'type': 'vertex',
            'parent': parent,
            'attrs': attrs
        }

    def visitEdge_type_decl(self, ctx):
        name = ctx.ID(0).getText()
        source_type = ctx.ID(1).getText()
        target_type = ctx.ID(2).getText()
        directed = ctx.getChild(7).getText() if ctx.getChildCount() > 7 and ctx.getChild(7).getText() in ['directed', 'undirected'] else 'directed'
        self.edges[name] = {
            'type': 'edge',
            'from': source_type,
            'to': target_type,
            'directed': directed,
            'attrs': self._parse_attributes(ctx.attribute_block())
        }

    def visitVertex_instance(self, ctx):
        id_ = ctx.ID(0).getText()
        typ = ctx.ID(1).getText()

        if id_ in self.declared_ids:
            self.errors.append(f"Identificador duplicado: '{id_}'.")
        else:
            self.declared_ids.add(id_)

        attrs = self._parse_assignments(ctx.attribute_assign_block())
        if typ not in self.types:
            self.errors.append(f"Vértice '{id_}' usa tipo indefinido '{typ}'.")
        else:
            declared = self.types[typ]['attrs']
            for k, meta in declared.items():
                if meta['required'] and k not in attrs:
                    self.errors.append(f"Vértice '{id_}' falta atributo obrigatório '{k}'.")
        self.vertices[id_] = typ

    def visitEdge_instance(self, ctx):
        eid = ctx.ID(0).getText()
        etyp = ctx.ID(1).getText()
        src = ctx.ID(2).getText()
        dst = ctx.ID(3).getText()

        if eid in self.declared_ids:
            self.errors.append(f"Identificador duplicado: '{eid}'.")
        else:
            self.declared_ids.add(eid)

        if etyp not in self.edges:
            self.errors.append(f"Aresta '{eid}' usa tipo indefinido '{etyp}'.")
            return

        if src not in self.vertices or dst not in self.vertices:
            self.errors.append(f"Aresta '{eid}' conecta vértices inexistentes '{src}' ou '{dst}'.")
            return

        src_typ = self.vertices[src]
        dst_typ = self.vertices[dst]
        expected = self.edges[etyp]

        if src == dst:
            self.errors.append(f"Aresta '{eid}' forma ciclo (self-loop) não permitido.")

        if src_typ != expected['from'] or dst_typ != expected['to']:
            self.errors.append(f"Aresta '{eid}' espera conexão ({expected['from']} -> {expected['to']}), recebeu ({src_typ} -> {dst_typ}).")

    def _parse_attributes(self, ctx):
        if ctx is None: return {}
        attrs = {}
        for decl in ctx.attribute_decl():
            name = decl.ID().getText()
            typ = decl.type_().getText()
            required = decl.getText().find("required") != -1
            attrs[name] = { 'type': typ, 'required': required }
        return attrs

    def _parse_assignments(self, ctx):
        if ctx is None: return {}
        assigns = {}
        for pair in ctx.attribute_assignment():
            key = pair.ID().getText()
            assigns[key] = True  # valor irrelevante para validação de presença
        return assigns

    def report(self):
        if self.errors:
            print("❌ Erros semânticos encontrados:")
            for e in self.errors:
                print("  -", e)
        else:
            print("✔️  Nenhum erro semântico encontrado.")