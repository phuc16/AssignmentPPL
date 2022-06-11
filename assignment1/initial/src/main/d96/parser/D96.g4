/* Truong Hoang Phuc - 1914720 */

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//PARSER
program: classdecl+ EOF;

classdecl: CLASS ID (COLON ID)? LP classbody* RP;

classbody: attrdecl | methdecl;

attrdecl: (mutable | immutable) SEMI;

mutable: VAR (nonvalue | nonvaluedollar | value | valuedollar);
immutable: VAL (nonvalue | nonvaluedollar | value | valuedollar);

nonvalue: ID (COMMA nonvalue | COLON typ);
nonvaluedollar: DOLLARID (COMMA nonvalue | COLON typ);
value: ID (COMMA value COMMA exp | COLON typ ASSIOP exp);
valuedollar: DOLLARID (COMMA value COMMA exp | COLON typ ASSIOP exp);

methdecl: basicmeth | constructor | destructor;

basicmeth: (ID | DOLLARID) LB paralist? RB blockstmt;
constructor: CONSTRUCTOR LB paralist? RB blockstmt;
destructor: DESTRUCTOR LB RB blockstmt;

paralist: ID (COMMA ID)* COLON typ (SEMI ID (COMMA ID)* COLON typ)*;

methodattrdecl: (VAR | VAL) (nonvalue | value) SEMI;

indexedarray: ARRAY LB arraylist RB;

// arraylist: (INTLIT (COMMA INTLIT)*) | (FLOATLIT (COMMA FLOATLIT)*) | (BOOLLIT (COMMA BOOLLIT)*) | (STRINGLIT (COMMA STRINGLIT)*);
arraylist: exp (COMMA exp)*;

multiarray: ARRAY LB multiarraylist RB;

multiarraylist: indexedarray (COMMA indexedarray)*;


//stmt
blockstmt: LP stmt* RP;

stmt: assignstmt
    | ifstmt
    | forinstmt
    | breakstmt 
    | continuestmt 
    | returnstmt
    | methodinvostmt
    | methodattrdecl
    ;

assignstmt: exp6 ASSIOP exp SEMI;

indexexp: (LSB exp RSB)+;

ifstmt: IF LB exp RB blockstmt (ELSEIF LB exp RB blockstmt)* (ELSE blockstmt)? ;

forinstmt: FOREACH LB (ID | DOLLARID) IN exp DOUDOT exp (BY exp)? RB blockstmt;

breakstmt: BREAK SEMI;

continuestmt: CONTINUE SEMI;

returnstmt: RETURN exp? SEMI;

methodinvostmt: (exp7 DOT ID | ID DOUCOLON DOLLARID) LB explist? RB SEMI;


//expressions
explist: exp (COMMA exp)*;
exp: exp0 (ADDDOTOP | DOUEQUODOTOP) exp0 | exp0;
exp0: exp1 (EQUOP | NEOP | LTOP | GTOP | LTEOP | GTEOP) exp1 | exp1;
exp1: exp1 (ANDOP | OROP) exp2 | exp2;
exp2: exp2 (ADDOP | SUBOP) exp3 | exp3;
exp3: exp3 (MULOP | DIVOP | MODOP) exp4 | exp4;
exp4: NOTOP exp4 | exp5;
exp5: SUBOP exp5 | exp6;  
exp6: exp6 indexexp | exp7; 
exp7: exp7 DOT ID (LB explist? RB)? | exp8;
exp8: ID DOUCOLON DOLLARID (LB explist? RB)? | exp9;
exp9: NEW ID LB explist? RB | operands;

operands: ID | literals | LB exp RB | SELF;

literals: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | indexedarray | multiarray | ARRAYSIZE;

typ: arraytyp | primitivetyp | ID;

arraytyp: ARRAY LSB typ COMMA ARRAYSIZE RSB;
primitivetyp: INT | FLOAT | BOOLEAN | STRING;


//Keywords
BREAK: 'Break';

CONTINUE: 'Continue'; 

IF: 'If'; 

ELSEIF: 'Elseif';

ELSE: 'Else';

FOREACH: 'Foreach';

TRUE: 'True' ;

FALSE: 'False';

ARRAY: 'Array'; 

IN: 'In';

INT: 'Int'; 

FLOAT: 'Float'; 

BOOLEAN: 'Boolean'; 

STRING: 'String'; 

RETURN: 'Return';

NULL: 'Null'; 

CLASS: 'Class'; 

VAL: 'Val'; 

VAR: 'Var';

SELF: 'Self';

CONSTRUCTOR: 'Constructor';

DESTRUCTOR: 'Destructor'; 

NEW: 'New'; 

BY: 'By';


//Identifiers
ID: [_a-zA-Z][_a-zA-Z0-9]*;

DOLLARID: '$' [_a-zA-Z0-9]+;


//Comment
COMMENT: '##' .*? '##' -> skip;


//Operators
ADDOP: '+';

SUBOP: '-';

MULOP: '*';

DIVOP: '/';

MODOP: '%';

NOTOP: '!';

ANDOP: '&&';

OROP: '||';

EQUOP: '==';

ASSIOP: '=';

NEOP: '!=';

LTOP: '<';

LTEOP: '<=';

GTOP: '>';

GTEOP: '>=';

DOUEQUODOTOP: '==.';

ADDDOTOP: '+.';

DOUCOLON: '::';


// Separators
LB: '(' ;

RB: ')' ;

LSB: '[';

RSB: ']';

DOT: '.';

DOUDOT: '..';

COLON: ':';

COMMA: ',';

SEMI: ';';

LP: '{';

RP: '}';


//Literals
fragment HEXADECIMAL: '0' [Xx] ([1-9A-F][0-9A-F]* ([_]?[0-9A-F]+)* | '0');
fragment HEXNOTNULL: '0' [Xx] [1-9A-F][0-9A-F]* ([_]?[0-9A-F]+)*;

fragment OCTAL: '0' ([1-7][0-7]* ([_]?[0-7]+)* | '0');
fragment OCTNOTNULL: '0' [1-7][0-7]* ([_]?[0-7]+)*;

fragment BINARY: '0' [Bb] ('1' [0-1]* ([_]?[0-1]+)* | '0');
fragment BINNOTNULL: '0' [Bb] '1' [0-1]* ([_]?[0-1]+)*;

fragment DECIMAL: ([1-9][0-9]* ([_]?[0-9]+)* | '0');
fragment DECNOTNULL: [1-9][0-9]* ([_]?[0-9]+)*;

ARRAYSIZE: (HEXNOTNULL | OCTNOTNULL | BINNOTNULL | DECNOTNULL)  {self.text = self.text.replace('_', '')};

INTLIT: (HEXADECIMAL | OCTAL | BINARY | DECIMAL)    {self.text = self.text.replace('_', '')};

fragment INTPART: ([1-9][0-9]* ([_]?[0-9]+)* | '0');

fragment DECPART: DOT [0-9]*;

fragment EXPPART: [Ee] [-+]? ([1-9][0-9]* | '0');

FLOATLIT: (INTPART DECPART EXPPART? | DECPART EXPPART | INTPART EXPPART)  {self.text = self.text.replace('_', '')};

BOOLLIT: TRUE | FALSE;

STRINGLIT
    : '"' (~[\r\n"\\] | '\\' ['bfrnt\\] | [']["])* '"' 
        {
            self.text = self.text[1:-1]
        }
    ;


WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR
    : .
        {
            raise ErrorToken(self.text) 
        }
    ;

ILLEGAL_ESCAPE
    : '"' (~[\r\n"\\] | '\\' ['bfrnt\\] | [']["])* ('\\' ~[bfnrt'"\\] | '\\')
        {
            raise IllegalEscape(self.text[1:])
        }
    ;

UNCLOSE_STRING
    :  '"' (~[\r\n"\\] | '\\' ['bfrnt\\] | [']["])* ([\n\r] | [\\]? EOF | [']["] ([\r\n"\\] | EOF))
        {
            if self.text[-1] in ['\n', '\r']:
                raise UncloseString(self.text[1:-1])
            raise UncloseString(self.text[1:])
        }
    ;