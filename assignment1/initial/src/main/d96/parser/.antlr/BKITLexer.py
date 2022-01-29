# Generated from c:\Users\USER PC\Desktop\ass1\ass1\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("D\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\6\2\25\n\2\r\2\16\2\26\3\3\6\3\32")
        buf.write("\n\3\r\3\16\3\33\3\3\3\3\3\4\3\4\3\4\3\5\3\5\7\5%\n\5")
        buf.write("\f\5\16\5(\13\5\3\5\5\5+\n\5\3\5\3\5\3\6\3\6\7\6\61\n")
        buf.write("\6\f\6\16\6\64\13\6\3\6\3\6\3\6\3\7\3\7\5\7;\n\7\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\5\tC\n\t\2\2\n\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\2\17\2\21\2\3\2\b\3\2c|\5\2\13\f\17\17\"\"\7\3\n\f")
        buf.write("\16\17$$))^^\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3")
        buf.write("\2^^\2F\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\3\24\3\2\2\2\5\31\3\2\2\2\7\37\3\2\2\2")
        buf.write("\t\"\3\2\2\2\13.\3\2\2\2\r:\3\2\2\2\17<\3\2\2\2\21B\3")
        buf.write("\2\2\2\23\25\t\2\2\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24")
        buf.write("\3\2\2\2\26\27\3\2\2\2\27\4\3\2\2\2\30\32\t\3\2\2\31\30")
        buf.write("\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\36\b\3\2\2\36\6\3\2\2\2\37 \13\2\2\2 !")
        buf.write("\b\4\3\2!\b\3\2\2\2\"&\7$\2\2#%\5\r\7\2$#\3\2\2\2%(\3")
        buf.write("\2\2\2&$\3\2\2\2&\'\3\2\2\2\'*\3\2\2\2(&\3\2\2\2)+\t\4")
        buf.write("\2\2*)\3\2\2\2+,\3\2\2\2,-\b\5\4\2-\n\3\2\2\2.\62\7$\2")
        buf.write("\2/\61\5\r\7\2\60/\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2")
        buf.write("\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65\66\5\21")
        buf.write("\t\2\66\67\b\6\5\2\67\f\3\2\2\28;\n\5\2\29;\5\17\b\2:")
        buf.write("8\3\2\2\2:9\3\2\2\2;\16\3\2\2\2<=\7^\2\2=>\t\6\2\2>\20")
        buf.write("\3\2\2\2?@\7^\2\2@C\n\6\2\2AC\n\7\2\2B?\3\2\2\2BA\3\2")
        buf.write("\2\2C\22\3\2\2\2\n\2\26\33&*\62:B\6\b\2\2\3\4\2\3\5\3")
        buf.write("\3\6\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR", "ESC_SEQ", "ESC_ILLEGAL" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.ERROR_CHAR_action 
            actions[3] = self.UNCLOSE_STRING_action 
            actions[4] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


