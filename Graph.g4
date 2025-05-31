// Arquivo: Graph.g4

grammar Graph;

// Regras principais
program: graph+ ;

graph: 'graph' ID '{' type_section vertex_section edge_section '}' ;

type_section: 'types' '{' (vertex_type_decl | edge_type_decl)* '}' ;

vertex_type_decl: 'vertex' ID ('extends' ID)? cardinality? attribute_block? ';' ;
edge_type_decl: 'edge' ID '(' ID ',' ID ')' ('directed' | 'undirected')? cardinality? attribute_block? ';' ;

cardinality: '[' INT '..' (INT | '*') ']' ;

attribute_block: 'attributes' '{' attribute_decl* '}' ;
attribute_decl: ID ':' type ( 'required' | 'optional' )? ( '=' value )? ';' ;

vertex_section: 'vertices' '{' vertex_instance* '}' ;
vertex_instance: ID ':' ID attribute_assign_block? ';' ;

edge_section: 'edges' '{' edge_instance* '}' ;
edge_instance: ID ':' ID '(' ID '->' ID ')' attribute_assign_block? ';' ;

attribute_assign_block: '[' attribute_assignment (',' attribute_assignment)* ']' ;
attribute_assignment: ID '=' value ;

// Tipos e valores
value: INT | FLOAT | STRING | 'true' | 'false' | DATE ;
type: 'int' | 'float' | 'string' | 'bool' | 'date' | ID ;

// Tokens
ID: [a-zA-Z_] [a-zA-Z_0-9]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
STRING: '"' (~["])* '"' ;
DATE: INT '-' INT '-' INT ;

COMMENT: ('//' ~[\r\n]* | '#' ~[\r\n]*) -> skip ;
WS: [ \t\r\n]+ -> skip ;
