# Generated from Graph.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO # type: ignore

def serializedATN():
    return [
        4,1,39,177,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,2,
        1,2,1,3,1,3,1,3,1,3,3,3,61,8,3,1,3,3,3,64,8,3,1,3,3,3,67,8,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,79,8,4,1,4,3,4,82,8,4,1,
        4,3,4,85,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,98,
        8,6,10,6,12,6,101,9,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,109,8,7,1,7,1,
        7,3,7,113,8,7,1,7,1,7,1,8,1,8,1,8,5,8,120,8,8,10,8,12,8,123,9,8,
        1,8,1,8,1,9,1,9,1,9,1,9,3,9,131,8,9,1,9,1,9,1,10,1,10,1,10,5,10,
        138,8,10,10,10,12,10,141,9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,154,8,11,1,11,1,11,1,12,1,12,1,12,1,12,
        5,12,162,8,12,10,12,12,12,165,9,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,14,1,14,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,0,5,1,0,12,13,2,0,16,16,34,34,1,0,20,21,2,0,26,27,34,37,
        1,0,28,33,177,0,33,1,0,0,0,2,37,1,0,0,0,4,45,1,0,0,0,6,56,1,0,0,
        0,8,70,1,0,0,0,10,88,1,0,0,0,12,94,1,0,0,0,14,104,1,0,0,0,16,116,
        1,0,0,0,18,126,1,0,0,0,20,134,1,0,0,0,22,144,1,0,0,0,24,157,1,0,
        0,0,26,168,1,0,0,0,28,172,1,0,0,0,30,174,1,0,0,0,32,34,3,2,1,0,33,
        32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,1,1,0,0,
        0,37,38,5,1,0,0,38,39,5,33,0,0,39,40,5,2,0,0,40,41,3,4,2,0,41,42,
        3,16,8,0,42,43,3,20,10,0,43,44,5,3,0,0,44,3,1,0,0,0,45,46,5,4,0,
        0,46,51,5,2,0,0,47,50,3,6,3,0,48,50,3,8,4,0,49,47,1,0,0,0,49,48,
        1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,
        53,51,1,0,0,0,54,55,5,3,0,0,55,5,1,0,0,0,56,57,5,5,0,0,57,60,5,33,
        0,0,58,59,5,6,0,0,59,61,5,33,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,
        63,1,0,0,0,62,64,3,10,5,0,63,62,1,0,0,0,63,64,1,0,0,0,64,66,1,0,
        0,0,65,67,3,12,6,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,
        69,5,7,0,0,69,7,1,0,0,0,70,71,5,8,0,0,71,72,5,33,0,0,72,73,5,9,0,
        0,73,74,5,33,0,0,74,75,5,10,0,0,75,76,5,33,0,0,76,78,5,11,0,0,77,
        79,7,0,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,82,3,10,
        5,0,81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,85,3,12,6,0,84,
        83,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,7,0,0,87,9,1,0,0,
        0,88,89,5,14,0,0,89,90,5,34,0,0,90,91,5,15,0,0,91,92,7,1,0,0,92,
        93,5,17,0,0,93,11,1,0,0,0,94,95,5,18,0,0,95,99,5,2,0,0,96,98,3,14,
        7,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,
        102,1,0,0,0,101,99,1,0,0,0,102,103,5,3,0,0,103,13,1,0,0,0,104,105,
        5,33,0,0,105,106,5,19,0,0,106,108,3,30,15,0,107,109,7,2,0,0,108,
        107,1,0,0,0,108,109,1,0,0,0,109,112,1,0,0,0,110,111,5,22,0,0,111,
        113,3,28,14,0,112,110,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,
        115,5,7,0,0,115,15,1,0,0,0,116,117,5,23,0,0,117,121,5,2,0,0,118,
        120,3,18,9,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,5,3,0,0,125,
        17,1,0,0,0,126,127,5,33,0,0,127,128,5,19,0,0,128,130,5,33,0,0,129,
        131,3,24,12,0,130,129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,
        133,5,7,0,0,133,19,1,0,0,0,134,135,5,24,0,0,135,139,5,2,0,0,136,
        138,3,22,11,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,
        140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,5,3,0,0,143,
        21,1,0,0,0,144,145,5,33,0,0,145,146,5,19,0,0,146,147,5,33,0,0,147,
        148,5,9,0,0,148,149,5,33,0,0,149,150,5,25,0,0,150,151,5,33,0,0,151,
        153,5,11,0,0,152,154,3,24,12,0,153,152,1,0,0,0,153,154,1,0,0,0,154,
        155,1,0,0,0,155,156,5,7,0,0,156,23,1,0,0,0,157,158,5,14,0,0,158,
        163,3,26,13,0,159,160,5,10,0,0,160,162,3,26,13,0,161,159,1,0,0,0,
        162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,
        165,163,1,0,0,0,166,167,5,17,0,0,167,25,1,0,0,0,168,169,5,33,0,0,
        169,170,5,22,0,0,170,171,3,28,14,0,171,27,1,0,0,0,172,173,7,3,0,
        0,173,29,1,0,0,0,174,175,7,4,0,0,175,31,1,0,0,0,17,35,49,51,60,63,
        66,78,81,84,99,108,112,121,130,139,153,163
    ]

class GraphParser ( Parser ):

    grammarFileName = "Graph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'graph'", "'{'", "'}'", "'types'", "'vertex'", 
                     "'extends'", "';'", "'edge'", "'('", "','", "')'", 
                     "'directed'", "'undirected'", "'['", "'..'", "'*'", 
                     "']'", "'attributes'", "':'", "'required'", "'optional'", 
                     "'='", "'vertices'", "'edges'", "'->'", "'true'", "'false'", 
                     "'int'", "'float'", "'string'", "'bool'", "'date'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "DATE", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_graph = 1
    RULE_type_section = 2
    RULE_vertex_type_decl = 3
    RULE_edge_type_decl = 4
    RULE_cardinality = 5
    RULE_attribute_block = 6
    RULE_attribute_decl = 7
    RULE_vertex_section = 8
    RULE_vertex_instance = 9
    RULE_edge_section = 10
    RULE_edge_instance = 11
    RULE_attribute_assign_block = 12
    RULE_attribute_assignment = 13
    RULE_value = 14
    RULE_type = 15

    ruleNames =  [ "program", "graph", "type_section", "vertex_type_decl", 
                   "edge_type_decl", "cardinality", "attribute_block", "attribute_decl", 
                   "vertex_section", "vertex_instance", "edge_section", 
                   "edge_instance", "attribute_assign_block", "attribute_assignment", 
                   "value", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    ID=33
    INT=34
    FLOAT=35
    STRING=36
    DATE=37
    COMMENT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.GraphContext)
            else:
                return self.getTypedRuleContext(GraphParser.GraphContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GraphParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.graph()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphParser.ID, 0)

        def type_section(self):
            return self.getTypedRuleContext(GraphParser.Type_sectionContext,0)


        def vertex_section(self):
            return self.getTypedRuleContext(GraphParser.Vertex_sectionContext,0)


        def edge_section(self):
            return self.getTypedRuleContext(GraphParser.Edge_sectionContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_graph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph" ):
                listener.enterGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph" ):
                listener.exitGraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraph" ):
                return visitor.visitGraph(self)
            else:
                return visitor.visitChildren(self)




    def graph(self):

        localctx = GraphParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_graph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(GraphParser.T__0)
            self.state = 38
            self.match(GraphParser.ID)
            self.state = 39
            self.match(GraphParser.T__1)
            self.state = 40
            self.type_section()
            self.state = 41
            self.vertex_section()
            self.state = 42
            self.edge_section()
            self.state = 43
            self.match(GraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex_type_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.Vertex_type_declContext)
            else:
                return self.getTypedRuleContext(GraphParser.Vertex_type_declContext,i)


        def edge_type_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.Edge_type_declContext)
            else:
                return self.getTypedRuleContext(GraphParser.Edge_type_declContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_type_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_section" ):
                listener.enterType_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_section" ):
                listener.exitType_section(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_section" ):
                return visitor.visitType_section(self)
            else:
                return visitor.visitChildren(self)




    def type_section(self):

        localctx = GraphParser.Type_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(GraphParser.T__3)
            self.state = 46
            self.match(GraphParser.T__1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==8:
                self.state = 49
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 47
                    self.vertex_type_decl()
                    pass
                elif token in [8]:
                    self.state = 48
                    self.edge_type_decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(GraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vertex_type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.ID)
            else:
                return self.getToken(GraphParser.ID, i)

        def cardinality(self):
            return self.getTypedRuleContext(GraphParser.CardinalityContext,0)


        def attribute_block(self):
            return self.getTypedRuleContext(GraphParser.Attribute_blockContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_vertex_type_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertex_type_decl" ):
                listener.enterVertex_type_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertex_type_decl" ):
                listener.exitVertex_type_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertex_type_decl" ):
                return visitor.visitVertex_type_decl(self)
            else:
                return visitor.visitChildren(self)




    def vertex_type_decl(self):

        localctx = GraphParser.Vertex_type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vertex_type_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(GraphParser.T__4)
            self.state = 57
            self.match(GraphParser.ID)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 58
                self.match(GraphParser.T__5)
                self.state = 59
                self.match(GraphParser.ID)


            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 62
                self.cardinality()


            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 65
                self.attribute_block()


            self.state = 68
            self.match(GraphParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Edge_type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.ID)
            else:
                return self.getToken(GraphParser.ID, i)

        def cardinality(self):
            return self.getTypedRuleContext(GraphParser.CardinalityContext,0)


        def attribute_block(self):
            return self.getTypedRuleContext(GraphParser.Attribute_blockContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_edge_type_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge_type_decl" ):
                listener.enterEdge_type_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge_type_decl" ):
                listener.exitEdge_type_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdge_type_decl" ):
                return visitor.visitEdge_type_decl(self)
            else:
                return visitor.visitChildren(self)




    def edge_type_decl(self):

        localctx = GraphParser.Edge_type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_edge_type_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(GraphParser.T__7)
            self.state = 71
            self.match(GraphParser.ID)
            self.state = 72
            self.match(GraphParser.T__8)
            self.state = 73
            self.match(GraphParser.ID)
            self.state = 74
            self.match(GraphParser.T__9)
            self.state = 75
            self.match(GraphParser.ID)
            self.state = 76
            self.match(GraphParser.T__10)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==13:
                self.state = 77
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 80
                self.cardinality()


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 83
                self.attribute_block()


            self.state = 86
            self.match(GraphParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CardinalityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.INT)
            else:
                return self.getToken(GraphParser.INT, i)

        def getRuleIndex(self):
            return GraphParser.RULE_cardinality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCardinality" ):
                listener.enterCardinality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCardinality" ):
                listener.exitCardinality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCardinality" ):
                return visitor.visitCardinality(self)
            else:
                return visitor.visitChildren(self)




    def cardinality(self):

        localctx = GraphParser.CardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cardinality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(GraphParser.T__13)
            self.state = 89
            self.match(GraphParser.INT)
            self.state = 90
            self.match(GraphParser.T__14)
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==16 or _la==34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 92
            self.match(GraphParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.Attribute_declContext)
            else:
                return self.getTypedRuleContext(GraphParser.Attribute_declContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_attribute_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_block" ):
                listener.enterAttribute_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_block" ):
                listener.exitAttribute_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_block" ):
                return visitor.visitAttribute_block(self)
            else:
                return visitor.visitChildren(self)




    def attribute_block(self):

        localctx = GraphParser.Attribute_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GraphParser.T__17)
            self.state = 95
            self.match(GraphParser.T__1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 96
                self.attribute_decl()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(GraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(GraphParser.TypeContext,0)


        def value(self):
            return self.getTypedRuleContext(GraphParser.ValueContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_attribute_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_decl" ):
                listener.enterAttribute_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_decl" ):
                listener.exitAttribute_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = GraphParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GraphParser.ID)
            self.state = 105
            self.match(GraphParser.T__18)
            self.state = 106
            self.type_()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==21:
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 110
                self.match(GraphParser.T__21)
                self.state = 111
                self.value()


            self.state = 114
            self.match(GraphParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vertex_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex_instance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.Vertex_instanceContext)
            else:
                return self.getTypedRuleContext(GraphParser.Vertex_instanceContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_vertex_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertex_section" ):
                listener.enterVertex_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertex_section" ):
                listener.exitVertex_section(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertex_section" ):
                return visitor.visitVertex_section(self)
            else:
                return visitor.visitChildren(self)




    def vertex_section(self):

        localctx = GraphParser.Vertex_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vertex_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(GraphParser.T__22)
            self.state = 117
            self.match(GraphParser.T__1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 118
                self.vertex_instance()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(GraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vertex_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.ID)
            else:
                return self.getToken(GraphParser.ID, i)

        def attribute_assign_block(self):
            return self.getTypedRuleContext(GraphParser.Attribute_assign_blockContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_vertex_instance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertex_instance" ):
                listener.enterVertex_instance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertex_instance" ):
                listener.exitVertex_instance(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertex_instance" ):
                return visitor.visitVertex_instance(self)
            else:
                return visitor.visitChildren(self)




    def vertex_instance(self):

        localctx = GraphParser.Vertex_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vertex_instance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(GraphParser.ID)
            self.state = 127
            self.match(GraphParser.T__18)
            self.state = 128
            self.match(GraphParser.ID)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 129
                self.attribute_assign_block()


            self.state = 132
            self.match(GraphParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Edge_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edge_instance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.Edge_instanceContext)
            else:
                return self.getTypedRuleContext(GraphParser.Edge_instanceContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_edge_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge_section" ):
                listener.enterEdge_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge_section" ):
                listener.exitEdge_section(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdge_section" ):
                return visitor.visitEdge_section(self)
            else:
                return visitor.visitChildren(self)




    def edge_section(self):

        localctx = GraphParser.Edge_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_edge_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(GraphParser.T__23)
            self.state = 135
            self.match(GraphParser.T__1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 136
                self.edge_instance()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(GraphParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Edge_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.ID)
            else:
                return self.getToken(GraphParser.ID, i)

        def attribute_assign_block(self):
            return self.getTypedRuleContext(GraphParser.Attribute_assign_blockContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_edge_instance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge_instance" ):
                listener.enterEdge_instance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge_instance" ):
                listener.exitEdge_instance(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdge_instance" ):
                return visitor.visitEdge_instance(self)
            else:
                return visitor.visitChildren(self)




    def edge_instance(self):

        localctx = GraphParser.Edge_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_edge_instance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(GraphParser.ID)
            self.state = 145
            self.match(GraphParser.T__18)
            self.state = 146
            self.match(GraphParser.ID)
            self.state = 147
            self.match(GraphParser.T__8)
            self.state = 148
            self.match(GraphParser.ID)
            self.state = 149
            self.match(GraphParser.T__24)
            self.state = 150
            self.match(GraphParser.ID)
            self.state = 151
            self.match(GraphParser.T__10)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 152
                self.attribute_assign_block()


            self.state = 155
            self.match(GraphParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_assign_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.Attribute_assignmentContext)
            else:
                return self.getTypedRuleContext(GraphParser.Attribute_assignmentContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_attribute_assign_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_assign_block" ):
                listener.enterAttribute_assign_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_assign_block" ):
                listener.exitAttribute_assign_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_assign_block" ):
                return visitor.visitAttribute_assign_block(self)
            else:
                return visitor.visitChildren(self)




    def attribute_assign_block(self):

        localctx = GraphParser.Attribute_assign_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attribute_assign_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(GraphParser.T__13)
            self.state = 158
            self.attribute_assignment()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 159
                self.match(GraphParser.T__9)
                self.state = 160
                self.attribute_assignment()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(GraphParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(GraphParser.ValueContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_attribute_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_assignment" ):
                listener.enterAttribute_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_assignment" ):
                listener.exitAttribute_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_assignment" ):
                return visitor.visitAttribute_assignment(self)
            else:
                return visitor.visitChildren(self)




    def attribute_assignment(self):

        localctx = GraphParser.Attribute_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_attribute_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(GraphParser.ID)
            self.state = 169
            self.match(GraphParser.T__21)
            self.state = 170
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GraphParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GraphParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(GraphParser.STRING, 0)

        def DATE(self):
            return self.getToken(GraphParser.DATE, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = GraphParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 257899364352) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GraphParser.ID, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = GraphParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





