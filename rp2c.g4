grammar rp2c;

//---------------------------------------------
program : program_head program_body'.';
program_head : 'program' ID '(' identifier_list ')' ';';
identifier_list : identifier_list','ID | ID;
program_body: declarations subprogram_declarations compound_statement;
declarations: 'var' declaration ';' | ;
declaration: declaration ';' identifier_list ':'  type_
    | identifier_list ':' type_;
type_ : standard_type
    | 'array[' DIGITS '..' DIGITS ']' 'of' standard_type
    | 'record' declaration 'end';
standard_type : 'integer' | 'real' | 'Boolean' | DIGITS '..' DIGITS;

subprogram_declarations : subprogram_declarations subprogram_declaration ';' | ;
subprogram_declaration : subprogram_head declarations compound_statement;
subprogram_head : 'function' ID arguments ':' standard_type ';'
                    | 'procedure' ID arguments ';' ;
arguments : '(' parameter_lists ')' | ;
parameter_lists : parameter_lists ';' parameter_list | parameter_list;
parameter_list : 'var' identifier_list ':' type_ |  identifier_list ':' type_;

compound_statement : 'begin' optional_statements 'end';
optional_statements: statement_list | ;
statement_list : statement_list ';' statement | statement;
statement: variable ASSIGNOP expression
            |procedure_call_statement
            |compound_statement
            |'if' expression 'then' statement ('else' statement)
            |'while' expression 'do' statement
            |'read(' identifier_list ')'
            |'write(' expr_list ')';
variable : ID | ID'['expression']';
procedure_call_statement: ID | ID'('expr_list')';
expr_list : expr_list ',' expression | expression;
expression : simple_expr RELOP simple_expr | simple_expr;
simple_expr: simple_expr ADDOP term | term | sign term;
term: term MULOP factor | factor;
factor : ID
        | ID'(' expr_list ')'
        | ID'[' expression ']'
        | NUM
        |'('expression')'
        |'not' factor
        |'true'
        |'false';
sign : '+' | '-';

//--------------------------------------------------------------------------------
fragment DIGIT : [0-9];
fragment LETTER : [a-zA-Z];
ID : LETTER(LETTER|DIGIT)*;
DIGITS : [0-9]+;
fragment OPTIONAL_FRACTION: '.'DIGITS| ;
fragment OPTIONAL_EXPONENT : ( 'E' ('+'|'-'|) DIGITS) | ;
NUM : DIGITS OPTIONAL_FRACTION OPTIONAL_EXPONENT;
RELOP : '=' | '<>' | '<' | '<=' | '>' | '>=';
ADDOP : '+' | '-' | 'or';
MULOP:'*' | '/' | 'DIV' | 'MOD' | 'AND';
ASSIGNOP : ':=';
WS : [ \t\r\n]+ -> skip;
COMMENT : '{'.* '}'->skip;
COMMENT_LINE: '//' ~[\r\n]* '\r'? '\n' -> skip;