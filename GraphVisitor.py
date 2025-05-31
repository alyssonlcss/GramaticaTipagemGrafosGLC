# Generated from Graph.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete generic visitor for a parse tree produced by GraphParser.

class GraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphParser#program.
    def visitProgram(self, ctx:GraphParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#graph.
    def visitGraph(self, ctx:GraphParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#type_section.
    def visitType_section(self, ctx:GraphParser.Type_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#vertex_type_decl.
    def visitVertex_type_decl(self, ctx:GraphParser.Vertex_type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#edge_type_decl.
    def visitEdge_type_decl(self, ctx:GraphParser.Edge_type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#cardinality.
    def visitCardinality(self, ctx:GraphParser.CardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#attribute_block.
    def visitAttribute_block(self, ctx:GraphParser.Attribute_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#attribute_decl.
    def visitAttribute_decl(self, ctx:GraphParser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#vertex_section.
    def visitVertex_section(self, ctx:GraphParser.Vertex_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#vertex_instance.
    def visitVertex_instance(self, ctx:GraphParser.Vertex_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#edge_section.
    def visitEdge_section(self, ctx:GraphParser.Edge_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#edge_instance.
    def visitEdge_instance(self, ctx:GraphParser.Edge_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#attribute_assign_block.
    def visitAttribute_assign_block(self, ctx:GraphParser.Attribute_assign_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#attribute_assignment.
    def visitAttribute_assignment(self, ctx:GraphParser.Attribute_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#value.
    def visitValue(self, ctx:GraphParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#type.
    def visitType(self, ctx:GraphParser.TypeContext):
        return self.visitChildren(ctx)



del GraphParser