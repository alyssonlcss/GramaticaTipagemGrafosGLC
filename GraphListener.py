# Generated from Graph.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete listener for a parse tree produced by GraphParser.
class GraphListener(ParseTreeListener):

    # Enter a parse tree produced by GraphParser#program.
    def enterProgram(self, ctx:GraphParser.ProgramContext):
        pass

    # Exit a parse tree produced by GraphParser#program.
    def exitProgram(self, ctx:GraphParser.ProgramContext):
        pass


    # Enter a parse tree produced by GraphParser#graph.
    def enterGraph(self, ctx:GraphParser.GraphContext):
        pass

    # Exit a parse tree produced by GraphParser#graph.
    def exitGraph(self, ctx:GraphParser.GraphContext):
        pass


    # Enter a parse tree produced by GraphParser#type_section.
    def enterType_section(self, ctx:GraphParser.Type_sectionContext):
        pass

    # Exit a parse tree produced by GraphParser#type_section.
    def exitType_section(self, ctx:GraphParser.Type_sectionContext):
        pass


    # Enter a parse tree produced by GraphParser#vertex_type_decl.
    def enterVertex_type_decl(self, ctx:GraphParser.Vertex_type_declContext):
        pass

    # Exit a parse tree produced by GraphParser#vertex_type_decl.
    def exitVertex_type_decl(self, ctx:GraphParser.Vertex_type_declContext):
        pass


    # Enter a parse tree produced by GraphParser#edge_type_decl.
    def enterEdge_type_decl(self, ctx:GraphParser.Edge_type_declContext):
        pass

    # Exit a parse tree produced by GraphParser#edge_type_decl.
    def exitEdge_type_decl(self, ctx:GraphParser.Edge_type_declContext):
        pass


    # Enter a parse tree produced by GraphParser#cardinality.
    def enterCardinality(self, ctx:GraphParser.CardinalityContext):
        pass

    # Exit a parse tree produced by GraphParser#cardinality.
    def exitCardinality(self, ctx:GraphParser.CardinalityContext):
        pass


    # Enter a parse tree produced by GraphParser#attribute_block.
    def enterAttribute_block(self, ctx:GraphParser.Attribute_blockContext):
        pass

    # Exit a parse tree produced by GraphParser#attribute_block.
    def exitAttribute_block(self, ctx:GraphParser.Attribute_blockContext):
        pass


    # Enter a parse tree produced by GraphParser#attribute_decl.
    def enterAttribute_decl(self, ctx:GraphParser.Attribute_declContext):
        pass

    # Exit a parse tree produced by GraphParser#attribute_decl.
    def exitAttribute_decl(self, ctx:GraphParser.Attribute_declContext):
        pass


    # Enter a parse tree produced by GraphParser#vertex_section.
    def enterVertex_section(self, ctx:GraphParser.Vertex_sectionContext):
        pass

    # Exit a parse tree produced by GraphParser#vertex_section.
    def exitVertex_section(self, ctx:GraphParser.Vertex_sectionContext):
        pass


    # Enter a parse tree produced by GraphParser#vertex_instance.
    def enterVertex_instance(self, ctx:GraphParser.Vertex_instanceContext):
        pass

    # Exit a parse tree produced by GraphParser#vertex_instance.
    def exitVertex_instance(self, ctx:GraphParser.Vertex_instanceContext):
        pass


    # Enter a parse tree produced by GraphParser#edge_section.
    def enterEdge_section(self, ctx:GraphParser.Edge_sectionContext):
        pass

    # Exit a parse tree produced by GraphParser#edge_section.
    def exitEdge_section(self, ctx:GraphParser.Edge_sectionContext):
        pass


    # Enter a parse tree produced by GraphParser#edge_instance.
    def enterEdge_instance(self, ctx:GraphParser.Edge_instanceContext):
        pass

    # Exit a parse tree produced by GraphParser#edge_instance.
    def exitEdge_instance(self, ctx:GraphParser.Edge_instanceContext):
        pass


    # Enter a parse tree produced by GraphParser#attribute_assign_block.
    def enterAttribute_assign_block(self, ctx:GraphParser.Attribute_assign_blockContext):
        pass

    # Exit a parse tree produced by GraphParser#attribute_assign_block.
    def exitAttribute_assign_block(self, ctx:GraphParser.Attribute_assign_blockContext):
        pass


    # Enter a parse tree produced by GraphParser#attribute_assignment.
    def enterAttribute_assignment(self, ctx:GraphParser.Attribute_assignmentContext):
        pass

    # Exit a parse tree produced by GraphParser#attribute_assignment.
    def exitAttribute_assignment(self, ctx:GraphParser.Attribute_assignmentContext):
        pass


    # Enter a parse tree produced by GraphParser#value.
    def enterValue(self, ctx:GraphParser.ValueContext):
        pass

    # Exit a parse tree produced by GraphParser#value.
    def exitValue(self, ctx:GraphParser.ValueContext):
        pass


    # Enter a parse tree produced by GraphParser#type.
    def enterType(self, ctx:GraphParser.TypeContext):
        pass

    # Exit a parse tree produced by GraphParser#type.
    def exitType(self, ctx:GraphParser.TypeContext):
        pass



del GraphParser