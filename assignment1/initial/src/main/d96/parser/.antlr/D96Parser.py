# Generated from c:\Users\USER PC\Documents\HCMUT\212\PPL\Assignment\assignment1\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u01fe\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\6\2b\n\2\r\2\16\2c\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3l\n\3\3\3\3\3\7\3p\n\3\f\3\16\3s\13\3\3\3")
        buf.write("\3\3\3\4\3\4\5\4y\n\4\3\5\3\5\5\5}\n\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0086\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u008d")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u0094\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u009b\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13\u00b5\n\13\3\f\3\f\3\f\5")
        buf.write("\f\u00ba\n\f\3\r\3\r\3\r\5\r\u00bf\n\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\5\16\u00c7\n\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\7\20\u00d4\n\20\f\20\16\20")
        buf.write("\u00d7\13\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00df")
        buf.write("\n\20\f\20\16\20\u00e2\13\20\3\20\3\20\7\20\u00e6\n\20")
        buf.write("\f\20\16\20\u00e9\13\20\3\21\3\21\3\21\5\21\u00ee\n\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\7\23")
        buf.write("\u00fa\n\23\f\23\16\23\u00fd\13\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\7\25\u0107\n\25\f\25\16\25\u010a")
        buf.write("\13\25\3\26\3\26\7\26\u010e\n\26\f\26\16\26\u0111\13\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u011d\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\31\6\31\u0128\n\31\r\31\16\31\u0129\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0137\n\32")
        buf.write("\f\32\16\32\u013a\13\32\3\32\3\32\5\32\u013e\n\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0149\n")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\5\36\u0156\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0161\n\37\3\37\3\37\5\37\u0165\n\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \7 \u016d\n \f \16 \u0170\13 ")
        buf.write("\3!\3!\3!\3!\3!\5!\u0177\n!\3\"\3\"\3\"\3\"\3\"\5\"\u017e")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\7#\u0186\n#\f#\16#\u0189\13#\3")
        buf.write("$\3$\3$\3$\3$\3$\7$\u0191\n$\f$\16$\u0194\13$\3%\3%\3")
        buf.write("%\3%\3%\3%\7%\u019c\n%\f%\16%\u019f\13%\3&\3&\3&\5&\u01a4")
        buf.write("\n&\3\'\3\'\3\'\5\'\u01a9\n\'\3(\3(\3(\3(\3(\7(\u01b0")
        buf.write("\n(\f(\16(\u01b3\13(\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01bd")
        buf.write("\n)\3)\5)\u01c0\n)\7)\u01c2\n)\f)\16)\u01c5\13)\3*\3*")
        buf.write("\3*\3*\3*\5*\u01cc\n*\3*\5*\u01cf\n*\3*\5*\u01d2\n*\3")
        buf.write("+\3+\3+\3+\5+\u01d8\n+\3+\3+\5+\u01dc\n+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\5,\u01e5\n,\3-\3-\3-\3-\3-\3-\3-\5-\u01ee\n-\3")
        buf.write(".\3.\3.\5.\u01f3\n.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\2\7DFHNP\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\n\3\2\33\34")
        buf.write("\3\2\24\25\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"\3\2\r")
        buf.write("\20\2\u0212\2a\3\2\2\2\4g\3\2\2\2\6x\3\2\2\2\b|\3\2\2")
        buf.write("\2\n\u0080\3\2\2\2\f\u0087\3\2\2\2\16\u008e\3\2\2\2\20")
        buf.write("\u0095\3\2\2\2\22\u009c\3\2\2\2\24\u00a9\3\2\2\2\26\u00b9")
        buf.write("\3\2\2\2\30\u00bb\3\2\2\2\32\u00c3\3\2\2\2\34\u00cb\3")
        buf.write("\2\2\2\36\u00d0\3\2\2\2 \u00ea\3\2\2\2\"\u00f1\3\2\2\2")
        buf.write("$\u00f6\3\2\2\2&\u00fe\3\2\2\2(\u0103\3\2\2\2*\u010b\3")
        buf.write("\2\2\2,\u011c\3\2\2\2.\u011e\3\2\2\2\60\u0127\3\2\2\2")
        buf.write("\62\u012b\3\2\2\2\64\u013f\3\2\2\2\66\u014d\3\2\2\28\u0150")
        buf.write("\3\2\2\2:\u0153\3\2\2\2<\u0160\3\2\2\2>\u0169\3\2\2\2")
        buf.write("@\u0176\3\2\2\2B\u017d\3\2\2\2D\u017f\3\2\2\2F\u018a\3")
        buf.write("\2\2\2H\u0195\3\2\2\2J\u01a3\3\2\2\2L\u01a8\3\2\2\2N\u01aa")
        buf.write("\3\2\2\2P\u01b4\3\2\2\2R\u01d1\3\2\2\2T\u01db\3\2\2\2")
        buf.write("V\u01e4\3\2\2\2X\u01ed\3\2\2\2Z\u01f2\3\2\2\2\\\u01f4")
        buf.write("\3\2\2\2^\u01fb\3\2\2\2`b\5\4\3\2a`\3\2\2\2bc\3\2\2\2")
        buf.write("ca\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\7\2\2\3f\3\3\2\2\2gh")
        buf.write("\7\23\2\2hk\7\33\2\2ij\7\66\2\2jl\7\33\2\2ki\3\2\2\2k")
        buf.write("l\3\2\2\2lm\3\2\2\2mq\79\2\2np\5\6\4\2on\3\2\2\2ps\3\2")
        buf.write("\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sq\3\2\2\2tu\7:\2\2")
        buf.write("u\5\3\2\2\2vy\5\b\5\2wy\5\26\f\2xv\3\2\2\2xw\3\2\2\2y")
        buf.write("\7\3\2\2\2z}\5\n\6\2{}\5\f\7\2|z\3\2\2\2|{\3\2\2\2}~\3")
        buf.write("\2\2\2~\177\78\2\2\177\t\3\2\2\2\u0080\u0085\7\25\2\2")
        buf.write("\u0081\u0086\5\16\b\2\u0082\u0086\5\20\t\2\u0083\u0086")
        buf.write("\5\22\n\2\u0084\u0086\5\24\13\2\u0085\u0081\3\2\2\2\u0085")
        buf.write("\u0082\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2")
        buf.write("\u0086\13\3\2\2\2\u0087\u008c\7\24\2\2\u0088\u008d\5\16")
        buf.write("\b\2\u0089\u008d\5\20\t\2\u008a\u008d\5\22\n\2\u008b\u008d")
        buf.write("\5\24\13\2\u008c\u0088\3\2\2\2\u008c\u0089\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\r\3\2\2\2\u008e")
        buf.write("\u0093\7\33\2\2\u008f\u0090\7\67\2\2\u0090\u0094\5\16")
        buf.write("\b\2\u0091\u0092\7\66\2\2\u0092\u0094\5Z.\2\u0093\u008f")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\17\3\2\2\2\u0095\u009a")
        buf.write("\7\34\2\2\u0096\u0097\7\67\2\2\u0097\u009b\5\16\b\2\u0098")
        buf.write("\u0099\7\66\2\2\u0099\u009b\5Z.\2\u009a\u0096\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009b\21\3\2\2\2\u009c\u00a7\7\33")
        buf.write("\2\2\u009d\u009e\7\67\2\2\u009e\u009f\5\22\n\2\u009f\u00a0")
        buf.write("\7\67\2\2\u00a0\u00a1\5@!\2\u00a1\u00a8\3\2\2\2\u00a2")
        buf.write("\u00a3\7\66\2\2\u00a3\u00a4\5Z.\2\u00a4\u00a5\7\'\2\2")
        buf.write("\u00a5\u00a6\5@!\2\u00a6\u00a8\3\2\2\2\u00a7\u009d\3\2")
        buf.write("\2\2\u00a7\u00a2\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00b4")
        buf.write("\7\34\2\2\u00aa\u00ab\7\67\2\2\u00ab\u00ac\5\22\n\2\u00ac")
        buf.write("\u00ad\7\67\2\2\u00ad\u00ae\5@!\2\u00ae\u00b5\3\2\2\2")
        buf.write("\u00af\u00b0\7\66\2\2\u00b0\u00b1\5Z.\2\u00b1\u00b2\7")
        buf.write("\'\2\2\u00b2\u00b3\5@!\2\u00b3\u00b5\3\2\2\2\u00b4\u00aa")
        buf.write("\3\2\2\2\u00b4\u00af\3\2\2\2\u00b5\25\3\2\2\2\u00b6\u00ba")
        buf.write("\5\30\r\2\u00b7\u00ba\5\32\16\2\u00b8\u00ba\5\34\17\2")
        buf.write("\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3")
        buf.write("\2\2\2\u00ba\27\3\2\2\2\u00bb\u00bc\t\2\2\2\u00bc\u00be")
        buf.write("\7\60\2\2\u00bd\u00bf\5\36\20\2\u00be\u00bd\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\7\61\2")
        buf.write("\2\u00c1\u00c2\5*\26\2\u00c2\31\3\2\2\2\u00c3\u00c4\7")
        buf.write("\27\2\2\u00c4\u00c6\7\60\2\2\u00c5\u00c7\5\36\20\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c9\7\61\2\2\u00c9\u00ca\5*\26\2\u00ca\33\3\2")
        buf.write("\2\2\u00cb\u00cc\7\30\2\2\u00cc\u00cd\7\60\2\2\u00cd\u00ce")
        buf.write("\7\61\2\2\u00ce\u00cf\5*\26\2\u00cf\35\3\2\2\2\u00d0\u00d5")
        buf.write("\7\33\2\2\u00d1\u00d2\7\67\2\2\u00d2\u00d4\7\33\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3")
        buf.write("\2\2\2\u00d8\u00d9\7\66\2\2\u00d9\u00e7\5Z.\2\u00da\u00db")
        buf.write("\78\2\2\u00db\u00e0\7\33\2\2\u00dc\u00dd\7\67\2\2\u00dd")
        buf.write("\u00df\7\33\2\2\u00de\u00dc\3\2\2\2\u00df\u00e2\3\2\2")
        buf.write("\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7\66\2\2\u00e4")
        buf.write("\u00e6\5Z.\2\u00e5\u00da\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\37\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00ea\u00ed\t\3\2\2\u00eb\u00ee\5\16\b")
        buf.write("\2\u00ec\u00ee\5\22\n\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\78\2\2\u00f0")
        buf.write("!\3\2\2\2\u00f1\u00f2\7\13\2\2\u00f2\u00f3\7\60\2\2\u00f3")
        buf.write("\u00f4\5$\23\2\u00f4\u00f5\7\61\2\2\u00f5#\3\2\2\2\u00f6")
        buf.write("\u00fb\5@!\2\u00f7\u00f8\7\67\2\2\u00f8\u00fa\5@!\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fc\3\2\2\2\u00fc%\3\2\2\2\u00fd\u00fb\3\2\2")
        buf.write("\2\u00fe\u00ff\7\13\2\2\u00ff\u0100\7\60\2\2\u0100\u0101")
        buf.write("\5(\25\2\u0101\u0102\7\61\2\2\u0102\'\3\2\2\2\u0103\u0108")
        buf.write("\5\"\22\2\u0104\u0105\7\67\2\2\u0105\u0107\5\"\22\2\u0106")
        buf.write("\u0104\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109)\3\2\2\2\u010a\u0108\3\2\2")
        buf.write("\2\u010b\u010f\79\2\2\u010c\u010e\5,\27\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0112\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0112\u0113\7:\2\2\u0113+\3\2\2\2\u0114\u011d\5.\30\2")
        buf.write("\u0115\u011d\5\62\32\2\u0116\u011d\5\64\33\2\u0117\u011d")
        buf.write("\5\66\34\2\u0118\u011d\58\35\2\u0119\u011d\5:\36\2\u011a")
        buf.write("\u011d\5<\37\2\u011b\u011d\5 \21\2\u011c\u0114\3\2\2\2")
        buf.write("\u011c\u0115\3\2\2\2\u011c\u0116\3\2\2\2\u011c\u0117\3")
        buf.write("\2\2\2\u011c\u0118\3\2\2\2\u011c\u0119\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011b\3\2\2\2\u011d-\3\2\2\2\u011e\u011f")
        buf.write("\5N(\2\u011f\u0120\7\'\2\2\u0120\u0121\5@!\2\u0121\u0122")
        buf.write("\78\2\2\u0122/\3\2\2\2\u0123\u0124\7\62\2\2\u0124\u0125")
        buf.write("\5@!\2\u0125\u0126\7\63\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0123\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\61\3\2\2\2\u012b\u012c\7\5")
        buf.write("\2\2\u012c\u012d\7\60\2\2\u012d\u012e\5@!\2\u012e\u012f")
        buf.write("\7\61\2\2\u012f\u0138\5*\26\2\u0130\u0131\7\6\2\2\u0131")
        buf.write("\u0132\7\60\2\2\u0132\u0133\5@!\2\u0133\u0134\7\61\2\2")
        buf.write("\u0134\u0135\5*\26\2\u0135\u0137\3\2\2\2\u0136\u0130\3")
        buf.write("\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013d\3\2\2\2\u013a\u0138\3\2\2\2\u013b")
        buf.write("\u013c\7\7\2\2\u013c\u013e\5*\26\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\63\3\2\2\2\u013f\u0140\7\b")
        buf.write("\2\2\u0140\u0141\7\60\2\2\u0141\u0142\t\2\2\2\u0142\u0143")
        buf.write("\7\f\2\2\u0143\u0144\5@!\2\u0144\u0145\7\65\2\2\u0145")
        buf.write("\u0148\5@!\2\u0146\u0147\7\32\2\2\u0147\u0149\5@!\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u014b\7\61\2\2\u014b\u014c\5*\26\2\u014c\65\3\2")
        buf.write("\2\2\u014d\u014e\7\3\2\2\u014e\u014f\78\2\2\u014f\67\3")
        buf.write("\2\2\2\u0150\u0151\7\4\2\2\u0151\u0152\78\2\2\u01529\3")
        buf.write("\2\2\2\u0153\u0155\7\21\2\2\u0154\u0156\5@!\2\u0155\u0154")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0158\78\2\2\u0158;\3\2\2\2\u0159\u015a\5P)\2\u015a\u015b")
        buf.write("\7\64\2\2\u015b\u015c\7\33\2\2\u015c\u0161\3\2\2\2\u015d")
        buf.write("\u015e\7\33\2\2\u015e\u015f\7/\2\2\u015f\u0161\7\34\2")
        buf.write("\2\u0160\u0159\3\2\2\2\u0160\u015d\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162\u0164\7\60\2\2\u0163\u0165\5> \2\u0164")
        buf.write("\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166\u0167\7\61\2\2\u0167\u0168\78\2\2\u0168=\3\2\2")
        buf.write("\2\u0169\u016e\5@!\2\u016a\u016b\7\67\2\2\u016b\u016d")
        buf.write("\5@!\2\u016c\u016a\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f?\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0171\u0172\5B\"\2\u0172\u0173\t\4\2\2\u0173")
        buf.write("\u0174\5B\"\2\u0174\u0177\3\2\2\2\u0175\u0177\5B\"\2\u0176")
        buf.write("\u0171\3\2\2\2\u0176\u0175\3\2\2\2\u0177A\3\2\2\2\u0178")
        buf.write("\u0179\5D#\2\u0179\u017a\t\5\2\2\u017a\u017b\5D#\2\u017b")
        buf.write("\u017e\3\2\2\2\u017c\u017e\5D#\2\u017d\u0178\3\2\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017eC\3\2\2\2\u017f\u0180\b#\1\2\u0180")
        buf.write("\u0181\5F$\2\u0181\u0187\3\2\2\2\u0182\u0183\f\4\2\2\u0183")
        buf.write("\u0184\t\6\2\2\u0184\u0186\5F$\2\u0185\u0182\3\2\2\2\u0186")
        buf.write("\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188E\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\b$\1\2")
        buf.write("\u018b\u018c\5H%\2\u018c\u0192\3\2\2\2\u018d\u018e\f\4")
        buf.write("\2\2\u018e\u018f\t\7\2\2\u018f\u0191\5H%\2\u0190\u018d")
        buf.write("\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193G\3\2\2\2\u0194\u0192\3\2\2\2\u0195")
        buf.write("\u0196\b%\1\2\u0196\u0197\5J&\2\u0197\u019d\3\2\2\2\u0198")
        buf.write("\u0199\f\4\2\2\u0199\u019a\t\b\2\2\u019a\u019c\5J&\2\u019b")
        buf.write("\u0198\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019eI\3\2\2\2\u019f\u019d\3\2\2")
        buf.write("\2\u01a0\u01a1\7#\2\2\u01a1\u01a4\5J&\2\u01a2\u01a4\5")
        buf.write("L\'\2\u01a3\u01a0\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4K\3")
        buf.write("\2\2\2\u01a5\u01a6\7\37\2\2\u01a6\u01a9\5L\'\2\u01a7\u01a9")
        buf.write("\5N(\2\u01a8\u01a5\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9M")
        buf.write("\3\2\2\2\u01aa\u01ab\b(\1\2\u01ab\u01ac\5P)\2\u01ac\u01b1")
        buf.write("\3\2\2\2\u01ad\u01ae\f\4\2\2\u01ae\u01b0\5\60\31\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b1\u01b2\3\2\2\2\u01b2O\3\2\2\2\u01b3\u01b1\3\2\2")
        buf.write("\2\u01b4\u01b5\b)\1\2\u01b5\u01b6\5R*\2\u01b6\u01c3\3")
        buf.write("\2\2\2\u01b7\u01b8\f\4\2\2\u01b8\u01b9\7\64\2\2\u01b9")
        buf.write("\u01bf\7\33\2\2\u01ba\u01bc\7\60\2\2\u01bb\u01bd\5> \2")
        buf.write("\u01bc\u01bb\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\3")
        buf.write("\2\2\2\u01be\u01c0\7\61\2\2\u01bf\u01ba\3\2\2\2\u01bf")
        buf.write("\u01c0\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01b7\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4Q\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7")
        buf.write("\7\33\2\2\u01c7\u01c8\7/\2\2\u01c8\u01ce\7\34\2\2\u01c9")
        buf.write("\u01cb\7\60\2\2\u01ca\u01cc\5> \2\u01cb\u01ca\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\7")
        buf.write("\61\2\2\u01ce\u01c9\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01d2\5T+\2\u01d1\u01c6\3\2\2\2\u01d1")
        buf.write("\u01d0\3\2\2\2\u01d2S\3\2\2\2\u01d3\u01d4\7\31\2\2\u01d4")
        buf.write("\u01d5\7\33\2\2\u01d5\u01d7\7\60\2\2\u01d6\u01d8\5> \2")
        buf.write("\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3")
        buf.write("\2\2\2\u01d9\u01dc\7\61\2\2\u01da\u01dc\5V,\2\u01db\u01d3")
        buf.write("\3\2\2\2\u01db\u01da\3\2\2\2\u01dcU\3\2\2\2\u01dd\u01e5")
        buf.write("\7\33\2\2\u01de\u01e5\5X-\2\u01df\u01e0\7\60\2\2\u01e0")
        buf.write("\u01e1\5@!\2\u01e1\u01e2\7\61\2\2\u01e2\u01e5\3\2\2\2")
        buf.write("\u01e3\u01e5\7\26\2\2\u01e4\u01dd\3\2\2\2\u01e4\u01de")
        buf.write("\3\2\2\2\u01e4\u01df\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5")
        buf.write("W\3\2\2\2\u01e6\u01ee\7<\2\2\u01e7\u01ee\7=\2\2\u01e8")
        buf.write("\u01ee\7>\2\2\u01e9\u01ee\7?\2\2\u01ea\u01ee\5\"\22\2")
        buf.write("\u01eb\u01ee\5&\24\2\u01ec\u01ee\7;\2\2\u01ed\u01e6\3")
        buf.write("\2\2\2\u01ed\u01e7\3\2\2\2\u01ed\u01e8\3\2\2\2\u01ed\u01e9")
        buf.write("\3\2\2\2\u01ed\u01ea\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01eeY\3\2\2\2\u01ef\u01f3\5\\/\2\u01f0")
        buf.write("\u01f3\5^\60\2\u01f1\u01f3\7\33\2\2\u01f2\u01ef\3\2\2")
        buf.write("\2\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3[\3\2")
        buf.write("\2\2\u01f4\u01f5\7\13\2\2\u01f5\u01f6\7\62\2\2\u01f6\u01f7")
        buf.write("\5Z.\2\u01f7\u01f8\7\67\2\2\u01f8\u01f9\7;\2\2\u01f9\u01fa")
        buf.write("\7\63\2\2\u01fa]\3\2\2\2\u01fb\u01fc\t\t\2\2\u01fc_\3")
        buf.write("\2\2\2\63ckqx|\u0085\u008c\u0093\u009a\u00a7\u00b4\u00b9")
        buf.write("\u00be\u00c6\u00d5\u00e0\u00e7\u00ed\u00fb\u0108\u010f")
        buf.write("\u011c\u0129\u0138\u013d\u0148\u0155\u0160\u0164\u016e")
        buf.write("\u0176\u017d\u0187\u0192\u019d\u01a3\u01a8\u01b1\u01bc")
        buf.write("\u01bf\u01c3\u01cb\u01ce\u01d1\u01d7\u01db\u01e4\u01ed")
        buf.write("\u01f2")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Self'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "<INVALID>", "<INVALID>", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'==.'", "'+.'", "'::'", "'('", "')'", "'['", "']'", 
                     "'.'", "'..'", "':'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
                      "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "ID", "DOLLARID", "COMMENT", "ADDOP", 
                      "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", "ANDOP", 
                      "OROP", "EQUOP", "ASSIOP", "NEOP", "LTOP", "LTEOP", 
                      "GTOP", "GTEOP", "DOUEQUODOTOP", "ADDDOTOP", "DOUCOLON", 
                      "LB", "RB", "LSB", "RSB", "DOT", "DOUDOT", "COLON", 
                      "COMMA", "SEMI", "LP", "RP", "ARRAYSIZE", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRINGLIT", "WS", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_classbody = 2
    RULE_attrdecl = 3
    RULE_mutable = 4
    RULE_immutable = 5
    RULE_nonvalue = 6
    RULE_nonvaluedollar = 7
    RULE_value = 8
    RULE_valuedollar = 9
    RULE_methdecl = 10
    RULE_basicmeth = 11
    RULE_constructor = 12
    RULE_destructor = 13
    RULE_paralist = 14
    RULE_methodattrdecl = 15
    RULE_indexedarray = 16
    RULE_arraylist = 17
    RULE_multiarray = 18
    RULE_multiarraylist = 19
    RULE_blockstmt = 20
    RULE_stmt = 21
    RULE_assignstmt = 22
    RULE_indexexp = 23
    RULE_ifstmt = 24
    RULE_forinstmt = 25
    RULE_breakstmt = 26
    RULE_continuestmt = 27
    RULE_returnstmt = 28
    RULE_methodinvostmt = 29
    RULE_explist = 30
    RULE_exp = 31
    RULE_exp0 = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_exp4 = 36
    RULE_exp5 = 37
    RULE_exp6 = 38
    RULE_exp7 = 39
    RULE_exp8 = 40
    RULE_exp9 = 41
    RULE_operands = 42
    RULE_literals = 43
    RULE_typ = 44
    RULE_arraytyp = 45
    RULE_primitivetyp = 46

    ruleNames =  [ "program", "classdecl", "classbody", "attrdecl", "mutable", 
                   "immutable", "nonvalue", "nonvaluedollar", "value", "valuedollar", 
                   "methdecl", "basicmeth", "constructor", "destructor", 
                   "paralist", "methodattrdecl", "indexedarray", "arraylist", 
                   "multiarray", "multiarraylist", "blockstmt", "stmt", 
                   "assignstmt", "indexexp", "ifstmt", "forinstmt", "breakstmt", 
                   "continuestmt", "returnstmt", "methodinvostmt", "explist", 
                   "exp", "exp0", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "operands", "literals", 
                   "typ", "arraytyp", "primitivetyp" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    TRUE=7
    FALSE=8
    ARRAY=9
    IN=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    STRING=14
    RETURN=15
    NULL=16
    CLASS=17
    VAL=18
    VAR=19
    SELF=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    ID=25
    DOLLARID=26
    COMMENT=27
    ADDOP=28
    SUBOP=29
    MULOP=30
    DIVOP=31
    MODOP=32
    NOTOP=33
    ANDOP=34
    OROP=35
    EQUOP=36
    ASSIOP=37
    NEOP=38
    LTOP=39
    LTEOP=40
    GTOP=41
    GTEOP=42
    DOUEQUODOTOP=43
    ADDDOTOP=44
    DOUCOLON=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    DOT=50
    DOUDOT=51
    COLON=52
    COMMA=53
    SEMI=54
    LP=55
    RP=56
    ARRAYSIZE=57
    INTLIT=58
    FLOATLIT=59
    BOOLLIT=60
    STRINGLIT=61
    WS=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassdeclContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.classdecl()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 99
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def classbody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassbodyContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassbodyContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecl




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(D96Parser.CLASS)
            self.state = 102
            self.match(D96Parser.ID)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 103
                self.match(D96Parser.COLON)
                self.state = 104
                self.match(D96Parser.ID)


            self.state = 107
            self.match(D96Parser.LP)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 108
                self.classbody()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassbodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrdecl(self):
            return self.getTypedRuleContext(D96Parser.AttrdeclContext,0)


        def methdecl(self):
            return self.getTypedRuleContext(D96Parser.MethdeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classbody




    def classbody(self):

        localctx = D96Parser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classbody)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.attrdecl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.methdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def mutable(self):
            return self.getTypedRuleContext(D96Parser.MutableContext,0)


        def immutable(self):
            return self.getTypedRuleContext(D96Parser.ImmutableContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attrdecl




    def attrdecl(self):

        localctx = D96Parser.AttrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attrdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR]:
                self.state = 120
                self.mutable()
                pass
            elif token in [D96Parser.VAL]:
                self.state = 121
                self.immutable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 124
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def nonvalue(self):
            return self.getTypedRuleContext(D96Parser.NonvalueContext,0)


        def nonvaluedollar(self):
            return self.getTypedRuleContext(D96Parser.NonvaluedollarContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def valuedollar(self):
            return self.getTypedRuleContext(D96Parser.ValuedollarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mutable




    def mutable(self):

        localctx = D96Parser.MutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mutable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(D96Parser.VAR)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 127
                self.nonvalue()
                pass

            elif la_ == 2:
                self.state = 128
                self.nonvaluedollar()
                pass

            elif la_ == 3:
                self.state = 129
                self.value()
                pass

            elif la_ == 4:
                self.state = 130
                self.valuedollar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def nonvalue(self):
            return self.getTypedRuleContext(D96Parser.NonvalueContext,0)


        def nonvaluedollar(self):
            return self.getTypedRuleContext(D96Parser.NonvaluedollarContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def valuedollar(self):
            return self.getTypedRuleContext(D96Parser.ValuedollarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_immutable




    def immutable(self):

        localctx = D96Parser.ImmutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immutable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(D96Parser.VAL)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 134
                self.nonvalue()
                pass

            elif la_ == 2:
                self.state = 135
                self.nonvaluedollar()
                pass

            elif la_ == 3:
                self.state = 136
                self.value()
                pass

            elif la_ == 4:
                self.state = 137
                self.valuedollar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def nonvalue(self):
            return self.getTypedRuleContext(D96Parser.NonvalueContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_nonvalue




    def nonvalue(self):

        localctx = D96Parser.NonvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nonvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(D96Parser.ID)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 141
                self.match(D96Parser.COMMA)
                self.state = 142
                self.nonvalue()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 143
                self.match(D96Parser.COLON)
                self.state = 144
                self.typ()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonvaluedollarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def nonvalue(self):
            return self.getTypedRuleContext(D96Parser.NonvalueContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_nonvaluedollar




    def nonvaluedollar(self):

        localctx = D96Parser.NonvaluedollarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nonvaluedollar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(D96Parser.DOLLARID)
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 148
                self.match(D96Parser.COMMA)
                self.state = 149
                self.nonvalue()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 150
                self.match(D96Parser.COLON)
                self.state = 151
                self.typ()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def ASSIOP(self):
            return self.getToken(D96Parser.ASSIOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_value




    def value(self):

        localctx = D96Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(D96Parser.ID)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 155
                self.match(D96Parser.COMMA)
                self.state = 156
                self.value()
                self.state = 157
                self.match(D96Parser.COMMA)
                self.state = 158
                self.exp()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 160
                self.match(D96Parser.COLON)
                self.state = 161
                self.typ()
                self.state = 162
                self.match(D96Parser.ASSIOP)
                self.state = 163
                self.exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuedollarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def ASSIOP(self):
            return self.getToken(D96Parser.ASSIOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_valuedollar




    def valuedollar(self):

        localctx = D96Parser.ValuedollarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_valuedollar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(D96Parser.DOLLARID)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 168
                self.match(D96Parser.COMMA)
                self.state = 169
                self.value()
                self.state = 170
                self.match(D96Parser.COMMA)
                self.state = 171
                self.exp()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 173
                self.match(D96Parser.COLON)
                self.state = 174
                self.typ()
                self.state = 175
                self.match(D96Parser.ASSIOP)
                self.state = 176
                self.exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicmeth(self):
            return self.getTypedRuleContext(D96Parser.BasicmethContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methdecl




    def methdecl(self):

        localctx = D96Parser.MethdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_methdecl)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.basicmeth()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicmethContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def paralist(self):
            return self.getTypedRuleContext(D96Parser.ParalistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_basicmeth




    def basicmeth(self):

        localctx = D96Parser.BasicmethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_basicmeth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 186
            self.match(D96Parser.LB)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 187
                self.paralist()


            self.state = 190
            self.match(D96Parser.RB)
            self.state = 191
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def paralist(self):
            return self.getTypedRuleContext(D96Parser.ParalistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 194
            self.match(D96Parser.LB)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 195
                self.paralist()


            self.state = 198
            self.match(D96Parser.RB)
            self.state = 199
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(D96Parser.DESTRUCTOR)
            self.state = 202
            self.match(D96Parser.LB)
            self.state = 203
            self.match(D96Parser.RB)
            self.state = 204
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COLON)
            else:
                return self.getToken(D96Parser.COLON, i)

        def typ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.TypContext)
            else:
                return self.getTypedRuleContext(D96Parser.TypContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_paralist




    def paralist(self):

        localctx = D96Parser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(D96Parser.ID)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 207
                self.match(D96Parser.COMMA)
                self.state = 208
                self.match(D96Parser.ID)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(D96Parser.COLON)
            self.state = 215
            self.typ()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 216
                self.match(D96Parser.SEMI)
                self.state = 217
                self.match(D96Parser.ID)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 218
                    self.match(D96Parser.COMMA)
                    self.state = 219
                    self.match(D96Parser.ID)
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 225
                self.match(D96Parser.COLON)
                self.state = 226
                self.typ()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodattrdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def nonvalue(self):
            return self.getTypedRuleContext(D96Parser.NonvalueContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodattrdecl




    def methodattrdecl(self):

        localctx = D96Parser.MethodattrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_methodattrdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 233
                self.nonvalue()
                pass

            elif la_ == 2:
                self.state = 234
                self.value()
                pass


            self.state = 237
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexedarrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def arraylist(self):
            return self.getTypedRuleContext(D96Parser.ArraylistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexedarray




    def indexedarray(self):

        localctx = D96Parser.IndexedarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_indexedarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(D96Parser.ARRAY)
            self.state = 240
            self.match(D96Parser.LB)
            self.state = 241
            self.arraylist()
            self.state = 242
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_arraylist




    def arraylist(self):

        localctx = D96Parser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arraylist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.exp()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 245
                self.match(D96Parser.COMMA)
                self.state = 246
                self.exp()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiarrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def multiarraylist(self):
            return self.getTypedRuleContext(D96Parser.MultiarraylistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiarray




    def multiarray(self):

        localctx = D96Parser.MultiarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_multiarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(D96Parser.ARRAY)
            self.state = 253
            self.match(D96Parser.LB)
            self.state = 254
            self.multiarraylist()
            self.state = 255
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiarraylistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexedarray(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexedarrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexedarrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_multiarraylist




    def multiarraylist(self):

        localctx = D96Parser.MultiarraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiarraylist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.indexedarray()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 258
                self.match(D96Parser.COMMA)
                self.state = 259
                self.indexedarray()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_blockstmt




    def blockstmt(self):

        localctx = D96Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(D96Parser.LP)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 266
                self.stmt()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(D96Parser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(D96Parser.IfstmtContext,0)


        def forinstmt(self):
            return self.getTypedRuleContext(D96Parser.ForinstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(D96Parser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(D96Parser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(D96Parser.ReturnstmtContext,0)


        def methodinvostmt(self):
            return self.getTypedRuleContext(D96Parser.MethodinvostmtContext,0)


        def methodattrdecl(self):
            return self.getTypedRuleContext(D96Parser.MethodattrdeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.forinstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 278
                self.continuestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 280
                self.methodinvostmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 281
                self.methodattrdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def ASSIOP(self):
            return self.getToken(D96Parser.ASSIOP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignstmt




    def assignstmt(self):

        localctx = D96Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.exp6(0)
            self.state = 285
            self.match(D96Parser.ASSIOP)
            self.state = 286
            self.exp()
            self.state = 287
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LSB)
            else:
                return self.getToken(D96Parser.LSB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RSB)
            else:
                return self.getToken(D96Parser.RSB, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexexp




    def indexexp(self):

        localctx = D96Parser.IndexexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_indexexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 289
                    self.match(D96Parser.LSB)
                    self.state = 290
                    self.exp()
                    self.state = 291
                    self.match(D96Parser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 295 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def blockstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.BlockstmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.BlockstmtContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifstmt




    def ifstmt(self):

        localctx = D96Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(D96Parser.IF)
            self.state = 298
            self.match(D96Parser.LB)
            self.state = 299
            self.exp()
            self.state = 300
            self.match(D96Parser.RB)
            self.state = 301
            self.blockstmt()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 302
                self.match(D96Parser.ELSEIF)
                self.state = 303
                self.match(D96Parser.LB)
                self.state = 304
                self.exp()
                self.state = 305
                self.match(D96Parser.RB)
                self.state = 306
                self.blockstmt()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 313
                self.match(D96Parser.ELSE)
                self.state = 314
                self.blockstmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForinstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def DOUDOT(self):
            return self.getToken(D96Parser.DOUDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forinstmt




    def forinstmt(self):

        localctx = D96Parser.ForinstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forinstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(D96Parser.FOREACH)
            self.state = 318
            self.match(D96Parser.LB)
            self.state = 319
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 320
            self.match(D96Parser.IN)
            self.state = 321
            self.exp()
            self.state = 322
            self.match(D96Parser.DOUDOT)
            self.state = 323
            self.exp()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 324
                self.match(D96Parser.BY)
                self.state = 325
                self.exp()


            self.state = 328
            self.match(D96Parser.RB)
            self.state = 329
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakstmt




    def breakstmt(self):

        localctx = D96Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(D96Parser.BREAK)
            self.state = 332
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continuestmt




    def continuestmt(self):

        localctx = D96Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(D96Parser.CONTINUE)
            self.state = 335
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_returnstmt




    def returnstmt(self):

        localctx = D96Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(D96Parser.RETURN)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 338
                self.exp()


            self.state = 341
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodinvostmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUCOLON(self):
            return self.getToken(D96Parser.DOUCOLON, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def explist(self):
            return self.getTypedRuleContext(D96Parser.ExplistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodinvostmt




    def methodinvostmt(self):

        localctx = D96Parser.MethodinvostmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_methodinvostmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 343
                self.exp7(0)
                self.state = 344
                self.match(D96Parser.DOT)
                self.state = 345
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 347
                self.match(D96Parser.ID)
                self.state = 348
                self.match(D96Parser.DOUCOLON)
                self.state = 349
                self.match(D96Parser.DOLLARID)
                pass


            self.state = 352
            self.match(D96Parser.LB)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 353
                self.explist()


            self.state = 356
            self.match(D96Parser.RB)
            self.state = 357
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_explist




    def explist(self):

        localctx = D96Parser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp()
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 360
                self.match(D96Parser.COMMA)
                self.state = 361
                self.exp()
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp0Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp0Context,i)


        def ADDDOTOP(self):
            return self.getToken(D96Parser.ADDDOTOP, 0)

        def DOUEQUODOTOP(self):
            return self.getToken(D96Parser.DOUEQUODOTOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.exp0()
                self.state = 368
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOUEQUODOTOP or _la==D96Parser.ADDDOTOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 369
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def EQUOP(self):
            return self.getToken(D96Parser.EQUOP, 0)

        def NEOP(self):
            return self.getToken(D96Parser.NEOP, 0)

        def LTOP(self):
            return self.getToken(D96Parser.LTOP, 0)

        def GTOP(self):
            return self.getToken(D96Parser.GTOP, 0)

        def LTEOP(self):
            return self.getToken(D96Parser.LTEOP, 0)

        def GTEOP(self):
            return self.getToken(D96Parser.GTEOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp0




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp0)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.exp1(0)
                self.state = 375
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUOP) | (1 << D96Parser.NEOP) | (1 << D96Parser.LTOP) | (1 << D96Parser.LTEOP) | (1 << D96Parser.GTOP) | (1 << D96Parser.GTEOP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 376
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def ANDOP(self):
            return self.getToken(D96Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(D96Parser.OROP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 384
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 385
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 386
                    self.exp2(0) 
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def ADDOP(self):
            return self.getToken(D96Parser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 395
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 396
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADDOP or _la==D96Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 397
                    self.exp3(0) 
                self.state = 402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def MULOP(self):
            return self.getToken(D96Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(D96Parser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(D96Parser.MODOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 411
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULOP) | (1 << D96Parser.DIVOP) | (1 << D96Parser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 408
                    self.exp4() 
                self.state = 413
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(D96Parser.NOTOP, 0)

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp4




    def exp4(self):

        localctx = D96Parser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp4)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(D96Parser.NOTOP)
                self.state = 415
                self.exp4()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.ID, D96Parser.SUBOP, D96Parser.LB, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp5)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(D96Parser.SUBOP)
                self.state = 420
                self.exp5()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.ID, D96Parser.LB, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.exp6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def indexexp(self):
            return self.getTypedRuleContext(D96Parser.IndexexpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 427
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 428
                    self.indexexp() 
                self.state = 433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def explist(self):
            return self.getTypedRuleContext(D96Parser.ExplistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 437
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 438
                    self.match(D96Parser.DOT)
                    self.state = 439
                    self.match(D96Parser.ID)
                    self.state = 445
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 440
                        self.match(D96Parser.LB)
                        self.state = 442
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                            self.state = 441
                            self.explist()


                        self.state = 444
                        self.match(D96Parser.RB)

             
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUCOLON(self):
            return self.getToken(D96Parser.DOUCOLON, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def explist(self):
            return self.getTypedRuleContext(D96Parser.ExplistContext,0)


        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8




    def exp8(self):

        localctx = D96Parser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp8)
        self._la = 0 # Token type
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(D96Parser.ID)
                self.state = 453
                self.match(D96Parser.DOUCOLON)
                self.state = 454
                self.match(D96Parser.DOLLARID)
                self.state = 460
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 455
                    self.match(D96Parser.LB)
                    self.state = 457
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                        self.state = 456
                        self.explist()


                    self.state = 459
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.exp9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def explist(self):
            return self.getTypedRuleContext(D96Parser.ExplistContext,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(D96Parser.NEW)
                self.state = 466
                self.match(D96Parser.ID)
                self.state = 467
                self.match(D96Parser.LB)
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                    self.state = 468
                    self.explist()


                self.state = 471
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operands)
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.literals()
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 477
                self.match(D96Parser.LB)
                self.state = 478
                self.exp()
                self.state = 479
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 481
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def indexedarray(self):
            return self.getTypedRuleContext(D96Parser.IndexedarrayContext,0)


        def multiarray(self):
            return self.getTypedRuleContext(D96Parser.MultiarrayContext,0)


        def ARRAYSIZE(self):
            return self.getToken(D96Parser.ARRAYSIZE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literals




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literals)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 487
                self.match(D96Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 488
                self.indexedarray()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 489
                self.multiarray()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 490
                self.match(D96Parser.ARRAYSIZE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytyp(self):
            return self.getTypedRuleContext(D96Parser.ArraytypContext,0)


        def primitivetyp(self):
            return self.getTypedRuleContext(D96Parser.PrimitivetypContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typ




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_typ)
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.arraytyp()
                pass
            elif token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.primitivetyp()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 495
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def ARRAYSIZE(self):
            return self.getToken(D96Parser.ARRAYSIZE, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arraytyp




    def arraytyp(self):

        localctx = D96Parser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arraytyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(D96Parser.ARRAY)
            self.state = 499
            self.match(D96Parser.LSB)
            self.state = 500
            self.typ()
            self.state = 501
            self.match(D96Parser.COMMA)
            self.state = 502
            self.match(D96Parser.ARRAYSIZE)
            self.state = 503
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitivetypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitivetyp




    def primitivetyp(self):

        localctx = D96Parser.PrimitivetypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_primitivetyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.exp1_sempred
        self._predicates[34] = self.exp2_sempred
        self._predicates[35] = self.exp3_sempred
        self._predicates[38] = self.exp6_sempred
        self._predicates[39] = self.exp7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




