# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\u020c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\6\2l\n\2\r\2\16\2m\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3v\n\3\3\3\3\3\7\3z\n\3\f\3\16\3}\13\3\3\3\3\3")
        buf.write("\3\4\3\4\5\4\u0083\n\4\3\5\3\5\5\5\u0087\n\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\5\6\u008e\n\6\3\7\3\7\3\7\5\7\u0093\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u009a\n\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00a7\n\t\3\n\3\n\3\n\5\n\u00ac")
        buf.write("\n\n\3\13\3\13\3\13\5\13\u00b1\n\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\5\f\u00b9\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\6\16\u00c4\n\16\r\16\16\16\u00c5\3\16\3\16\7\16")
        buf.write("\u00ca\n\16\f\16\16\16\u00cd\13\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\7\17\u00d4\n\17\f\17\16\17\u00d7\13\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\5\20\u00df\n\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00e8\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00f5\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\7\24\u00ff\n\24")
        buf.write("\f\24\16\24\u0102\13\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\7\26\u010c\n\26\f\26\16\26\u010f\13\26\3\27")
        buf.write("\3\27\7\27\u0113\n\27\f\27\16\27\u0116\13\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0123")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\6\32")
        buf.write("\u012e\n\32\r\32\16\32\u012f\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u0140")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\5\37")
        buf.write("\u014b\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0156\n \3 ")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\5#\u0163\n#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\5$\u016e\n$\3$\3$\5$\u0172\n$\3$\3")
        buf.write("$\3$\3%\3%\3%\7%\u017a\n%\f%\16%\u017d\13%\3&\3&\3&\3")
        buf.write("&\3&\5&\u0184\n&\3\'\3\'\3\'\3\'\3\'\5\'\u018b\n\'\3(")
        buf.write("\3(\3(\3(\3(\3(\7(\u0193\n(\f(\16(\u0196\13(\3)\3)\3)")
        buf.write("\3)\3)\3)\7)\u019e\n)\f)\16)\u01a1\13)\3*\3*\3*\3*\3*")
        buf.write("\3*\7*\u01a9\n*\f*\16*\u01ac\13*\3+\3+\3+\5+\u01b1\n+")
        buf.write("\3,\3,\3,\5,\u01b6\n,\3-\3-\3-\3-\3-\7-\u01bd\n-\f-\16")
        buf.write("-\u01c0\13-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01ca\n.\3.\5.")
        buf.write("\u01cd\n.\7.\u01cf\n.\f.\16.\u01d2\13.\3/\3/\3/\3/\3/")
        buf.write("\5/\u01d9\n/\3/\5/\u01dc\n/\3/\5/\u01df\n/\3\60\3\60\3")
        buf.write("\60\3\60\5\60\u01e5\n\60\3\60\3\60\5\60\u01e9\n\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01f3\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01fc\n\62\3\63")
        buf.write("\3\63\3\63\5\63\u0201\n\63\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\65\3\65\3\65\2\7NPRXZ\66\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfh\2\n\3\2\34\35\3\2\25\26\3\2./\4\2\'\'")
        buf.write(")-\3\2%&\3\2\37 \3\2!#\3\2\16\21\2\u0219\2k\3\2\2\2\4")
        buf.write("q\3\2\2\2\6\u0082\3\2\2\2\b\u0086\3\2\2\2\n\u008a\3\2")
        buf.write("\2\2\f\u008f\3\2\2\2\16\u0094\3\2\2\2\20\u009b\3\2\2\2")
        buf.write("\22\u00ab\3\2\2\2\24\u00ad\3\2\2\2\26\u00b5\3\2\2\2\30")
        buf.write("\u00bd\3\2\2\2\32\u00cb\3\2\2\2\34\u00d0\3\2\2\2\36\u00db")
        buf.write("\3\2\2\2 \u00e2\3\2\2\2\"\u00e9\3\2\2\2$\u00f6\3\2\2\2")
        buf.write("&\u00fb\3\2\2\2(\u0103\3\2\2\2*\u0108\3\2\2\2,\u0110\3")
        buf.write("\2\2\2.\u0122\3\2\2\2\60\u0124\3\2\2\2\62\u012d\3\2\2")
        buf.write("\2\64\u0131\3\2\2\2\66\u0135\3\2\2\28\u013f\3\2\2\2:\u0141")
        buf.write("\3\2\2\2<\u014a\3\2\2\2>\u014c\3\2\2\2@\u015a\3\2\2\2")
        buf.write("B\u015d\3\2\2\2D\u0160\3\2\2\2F\u016d\3\2\2\2H\u0176\3")
        buf.write("\2\2\2J\u0183\3\2\2\2L\u018a\3\2\2\2N\u018c\3\2\2\2P\u0197")
        buf.write("\3\2\2\2R\u01a2\3\2\2\2T\u01b0\3\2\2\2V\u01b5\3\2\2\2")
        buf.write("X\u01b7\3\2\2\2Z\u01c1\3\2\2\2\\\u01de\3\2\2\2^\u01e8")
        buf.write("\3\2\2\2`\u01f2\3\2\2\2b\u01fb\3\2\2\2d\u0200\3\2\2\2")
        buf.write("f\u0202\3\2\2\2h\u0209\3\2\2\2jl\5\4\3\2kj\3\2\2\2lm\3")
        buf.write("\2\2\2mk\3\2\2\2mn\3\2\2\2no\3\2\2\2op\7\2\2\3p\3\3\2")
        buf.write("\2\2qr\7\24\2\2ru\7\34\2\2st\7\67\2\2tv\7\34\2\2us\3\2")
        buf.write("\2\2uv\3\2\2\2vw\3\2\2\2w{\7:\2\2xz\5\6\4\2yx\3\2\2\2")
        buf.write("z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177")
        buf.write("\7;\2\2\177\5\3\2\2\2\u0080\u0083\5\b\5\2\u0081\u0083")
        buf.write("\5\22\n\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\7\3\2\2\2\u0084\u0087\5\n\6\2\u0085\u0087\5\f\7\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\79\2\2\u0089\t\3\2\2\2\u008a\u008d\7\26\2")
        buf.write("\2\u008b\u008e\5\16\b\2\u008c\u008e\5\20\t\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\13\3\2\2\2\u008f\u0092")
        buf.write("\7\25\2\2\u0090\u0093\5\16\b\2\u0091\u0093\5\20\t\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\r\3\2\2\2\u0094")
        buf.write("\u0099\t\2\2\2\u0095\u0096\78\2\2\u0096\u009a\5\16\b\2")
        buf.write("\u0097\u0098\7\67\2\2\u0098\u009a\5d\63\2\u0099\u0095")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u009a\17\3\2\2\2\u009b\u00a6")
        buf.write("\t\2\2\2\u009c\u009d\78\2\2\u009d\u009e\5\20\t\2\u009e")
        buf.write("\u009f\78\2\2\u009f\u00a0\5J&\2\u00a0\u00a7\3\2\2\2\u00a1")
        buf.write("\u00a2\7\67\2\2\u00a2\u00a3\5d\63\2\u00a3\u00a4\7(\2\2")
        buf.write("\u00a4\u00a5\5J&\2\u00a5\u00a7\3\2\2\2\u00a6\u009c\3\2")
        buf.write("\2\2\u00a6\u00a1\3\2\2\2\u00a7\21\3\2\2\2\u00a8\u00ac")
        buf.write("\5\24\13\2\u00a9\u00ac\5\26\f\2\u00aa\u00ac\5\30\r\2\u00ab")
        buf.write("\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2")
        buf.write("\u00ac\23\3\2\2\2\u00ad\u00ae\t\2\2\2\u00ae\u00b0\7\61")
        buf.write("\2\2\u00af\u00b1\5\32\16\2\u00b0\u00af\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\7\62\2\2\u00b3")
        buf.write("\u00b4\5,\27\2\u00b4\25\3\2\2\2\u00b5\u00b6\7\30\2\2\u00b6")
        buf.write("\u00b8\7\61\2\2\u00b7\u00b9\5\32\16\2\u00b8\u00b7\3\2")
        buf.write("\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\7\62\2\2\u00bb\u00bc\5,\27\2\u00bc\27\3\2\2\2\u00bd\u00be")
        buf.write("\7\31\2\2\u00be\u00bf\7\61\2\2\u00bf\u00c0\7\62\2\2\u00c0")
        buf.write("\u00c1\5,\27\2\u00c1\31\3\2\2\2\u00c2\u00c4\5\34\17\2")
        buf.write("\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c3\3")
        buf.write("\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\79\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c3\3\2\2\2\u00ca")
        buf.write("\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2")
        buf.write("\u00cc\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00cf\5")
        buf.write("\34\17\2\u00cf\33\3\2\2\2\u00d0\u00d5\7\34\2\2\u00d1\u00d2")
        buf.write("\78\2\2\u00d2\u00d4\7\34\2\2\u00d3\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7")
        buf.write("\67\2\2\u00d9\u00da\5d\63\2\u00da\35\3\2\2\2\u00db\u00de")
        buf.write("\t\3\2\2\u00dc\u00df\5 \21\2\u00dd\u00df\5\"\22\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\79\2\2\u00e1\37\3\2\2\2\u00e2\u00e7\7\34")
        buf.write("\2\2\u00e3\u00e4\78\2\2\u00e4\u00e8\5 \21\2\u00e5\u00e6")
        buf.write("\7\67\2\2\u00e6\u00e8\5d\63\2\u00e7\u00e3\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e8!\3\2\2\2\u00e9\u00f4\7\34\2\2\u00ea")
        buf.write("\u00eb\78\2\2\u00eb\u00ec\5\"\22\2\u00ec\u00ed\78\2\2")
        buf.write("\u00ed\u00ee\5J&\2\u00ee\u00f5\3\2\2\2\u00ef\u00f0\7\67")
        buf.write("\2\2\u00f0\u00f1\5d\63\2\u00f1\u00f2\7(\2\2\u00f2\u00f3")
        buf.write("\5J&\2\u00f3\u00f5\3\2\2\2\u00f4\u00ea\3\2\2\2\u00f4\u00ef")
        buf.write("\3\2\2\2\u00f5#\3\2\2\2\u00f6\u00f7\7\f\2\2\u00f7\u00f8")
        buf.write("\7\61\2\2\u00f8\u00f9\5&\24\2\u00f9\u00fa\7\62\2\2\u00fa")
        buf.write("%\3\2\2\2\u00fb\u0100\5J&\2\u00fc\u00fd\78\2\2\u00fd\u00ff")
        buf.write("\5J&\2\u00fe\u00fc\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\'\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0103\u0104\7\f\2\2\u0104\u0105\7\61\2\2\u0105")
        buf.write("\u0106\5*\26\2\u0106\u0107\7\62\2\2\u0107)\3\2\2\2\u0108")
        buf.write("\u010d\5$\23\2\u0109\u010a\78\2\2\u010a\u010c\5$\23\2")
        buf.write("\u010b\u0109\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3")
        buf.write("\2\2\2\u010d\u010e\3\2\2\2\u010e+\3\2\2\2\u010f\u010d")
        buf.write("\3\2\2\2\u0110\u0114\7:\2\2\u0111\u0113\5.\30\2\u0112")
        buf.write("\u0111\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2")
        buf.write("\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0114\3")
        buf.write("\2\2\2\u0117\u0118\7;\2\2\u0118-\3\2\2\2\u0119\u0123\5")
        buf.write("\60\31\2\u011a\u0123\5\64\33\2\u011b\u0123\5> \2\u011c")
        buf.write("\u0123\5@!\2\u011d\u0123\5B\"\2\u011e\u0123\5D#\2\u011f")
        buf.write("\u0123\5F$\2\u0120\u0123\5\36\20\2\u0121\u0123\5,\27\2")
        buf.write("\u0122\u0119\3\2\2\2\u0122\u011a\3\2\2\2\u0122\u011b\3")
        buf.write("\2\2\2\u0122\u011c\3\2\2\2\u0122\u011d\3\2\2\2\u0122\u011e")
        buf.write("\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123/\3\2\2\2\u0124\u0125\5X-\2\u0125")
        buf.write("\u0126\7(\2\2\u0126\u0127\5J&\2\u0127\u0128\79\2\2\u0128")
        buf.write("\61\3\2\2\2\u0129\u012a\7\63\2\2\u012a\u012b\5J&\2\u012b")
        buf.write("\u012c\7\64\2\2\u012c\u012e\3\2\2\2\u012d\u0129\3\2\2")
        buf.write("\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\63\3\2\2\2\u0131\u0132\5\66\34\2\u0132")
        buf.write("\u0133\58\35\2\u0133\u0134\5<\37\2\u0134\65\3\2\2\2\u0135")
        buf.write("\u0136\7\6\2\2\u0136\u0137\7\61\2\2\u0137\u0138\5J&\2")
        buf.write("\u0138\u0139\7\62\2\2\u0139\u013a\5,\27\2\u013a\67\3\2")
        buf.write("\2\2\u013b\u013c\5:\36\2\u013c\u013d\58\35\2\u013d\u0140")
        buf.write("\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u013b\3\2\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u01409\3\2\2\2\u0141\u0142\7\7\2\2\u0142")
        buf.write("\u0143\7\61\2\2\u0143\u0144\5J&\2\u0144\u0145\7\62\2\2")
        buf.write("\u0145\u0146\5,\27\2\u0146;\3\2\2\2\u0147\u0148\7\b\2")
        buf.write("\2\u0148\u014b\5,\27\2\u0149\u014b\3\2\2\2\u014a\u0147")
        buf.write("\3\2\2\2\u014a\u0149\3\2\2\2\u014b=\3\2\2\2\u014c\u014d")
        buf.write("\7\t\2\2\u014d\u014e\7\61\2\2\u014e\u014f\t\2\2\2\u014f")
        buf.write("\u0150\7\r\2\2\u0150\u0151\5J&\2\u0151\u0152\7\66\2\2")
        buf.write("\u0152\u0155\5J&\2\u0153\u0154\7\33\2\2\u0154\u0156\5")
        buf.write("J&\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0158\7\62\2\2\u0158\u0159\5,\27\2\u0159")
        buf.write("?\3\2\2\2\u015a\u015b\7\4\2\2\u015b\u015c\79\2\2\u015c")
        buf.write("A\3\2\2\2\u015d\u015e\7\5\2\2\u015e\u015f\79\2\2\u015f")
        buf.write("C\3\2\2\2\u0160\u0162\7\22\2\2\u0161\u0163\5J&\2\u0162")
        buf.write("\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0165\79\2\2\u0165E\3\2\2\2\u0166\u0167\5Z.\2\u0167")
        buf.write("\u0168\7\65\2\2\u0168\u0169\7\34\2\2\u0169\u016e\3\2\2")
        buf.write("\2\u016a\u016b\7\34\2\2\u016b\u016c\7\60\2\2\u016c\u016e")
        buf.write("\7\35\2\2\u016d\u0166\3\2\2\2\u016d\u016a\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0171\7\61\2\2\u0170\u0172\5H%\2")
        buf.write("\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3")
        buf.write("\2\2\2\u0173\u0174\7\62\2\2\u0174\u0175\79\2\2\u0175G")
        buf.write("\3\2\2\2\u0176\u017b\5J&\2\u0177\u0178\78\2\2\u0178\u017a")
        buf.write("\5J&\2\u0179\u0177\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017cI\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u017f\5L\'\2\u017f\u0180\t\4\2\2\u0180")
        buf.write("\u0181\5L\'\2\u0181\u0184\3\2\2\2\u0182\u0184\5L\'\2\u0183")
        buf.write("\u017e\3\2\2\2\u0183\u0182\3\2\2\2\u0184K\3\2\2\2\u0185")
        buf.write("\u0186\5N(\2\u0186\u0187\t\5\2\2\u0187\u0188\5N(\2\u0188")
        buf.write("\u018b\3\2\2\2\u0189\u018b\5N(\2\u018a\u0185\3\2\2\2\u018a")
        buf.write("\u0189\3\2\2\2\u018bM\3\2\2\2\u018c\u018d\b(\1\2\u018d")
        buf.write("\u018e\5P)\2\u018e\u0194\3\2\2\2\u018f\u0190\f\4\2\2\u0190")
        buf.write("\u0191\t\6\2\2\u0191\u0193\5P)\2\u0192\u018f\3\2\2\2\u0193")
        buf.write("\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195O\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0198\b)\1\2")
        buf.write("\u0198\u0199\5R*\2\u0199\u019f\3\2\2\2\u019a\u019b\f\4")
        buf.write("\2\2\u019b\u019c\t\7\2\2\u019c\u019e\5R*\2\u019d\u019a")
        buf.write("\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0Q\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2")
        buf.write("\u01a3\b*\1\2\u01a3\u01a4\5T+\2\u01a4\u01aa\3\2\2\2\u01a5")
        buf.write("\u01a6\f\4\2\2\u01a6\u01a7\t\b\2\2\u01a7\u01a9\5T+\2\u01a8")
        buf.write("\u01a5\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01abS\3\2\2\2\u01ac\u01aa\3\2\2")
        buf.write("\2\u01ad\u01ae\7$\2\2\u01ae\u01b1\5T+\2\u01af\u01b1\5")
        buf.write("V,\2\u01b0\u01ad\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1U\3")
        buf.write("\2\2\2\u01b2\u01b3\7 \2\2\u01b3\u01b6\5V,\2\u01b4\u01b6")
        buf.write("\5X-\2\u01b5\u01b2\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6W")
        buf.write("\3\2\2\2\u01b7\u01b8\b-\1\2\u01b8\u01b9\5Z.\2\u01b9\u01be")
        buf.write("\3\2\2\2\u01ba\u01bb\f\4\2\2\u01bb\u01bd\5\62\32\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bfY\3\2\2\2\u01c0\u01be\3\2\2")
        buf.write("\2\u01c1\u01c2\b.\1\2\u01c2\u01c3\5\\/\2\u01c3\u01d0\3")
        buf.write("\2\2\2\u01c4\u01c5\f\4\2\2\u01c5\u01c6\7\65\2\2\u01c6")
        buf.write("\u01cc\7\34\2\2\u01c7\u01c9\7\61\2\2\u01c8\u01ca\5H%\2")
        buf.write("\u01c9\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3")
        buf.write("\2\2\2\u01cb\u01cd\7\62\2\2\u01cc\u01c7\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01c4\3\2\2\2")
        buf.write("\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3")
        buf.write("\2\2\2\u01d1[\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4")
        buf.write("\7\34\2\2\u01d4\u01d5\7\60\2\2\u01d5\u01db\7\35\2\2\u01d6")
        buf.write("\u01d8\7\61\2\2\u01d7\u01d9\5H%\2\u01d8\u01d7\3\2\2\2")
        buf.write("\u01d8\u01d9\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\7")
        buf.write("\62\2\2\u01db\u01d6\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01df\5^\60\2\u01de\u01d3\3\2\2\2")
        buf.write("\u01de\u01dd\3\2\2\2\u01df]\3\2\2\2\u01e0\u01e1\7\32\2")
        buf.write("\2\u01e1\u01e2\7\34\2\2\u01e2\u01e4\7\61\2\2\u01e3\u01e5")
        buf.write("\5H%\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e9\7\62\2\2\u01e7\u01e9\5`\61\2\u01e8")
        buf.write("\u01e0\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9_\3\2\2\2\u01ea")
        buf.write("\u01f3\5b\62\2\u01eb\u01f3\7\34\2\2\u01ec\u01ed\7\61\2")
        buf.write("\2\u01ed\u01ee\5J&\2\u01ee\u01ef\7\62\2\2\u01ef\u01f3")
        buf.write("\3\2\2\2\u01f0\u01f3\7\27\2\2\u01f1\u01f3\7\23\2\2\u01f2")
        buf.write("\u01ea\3\2\2\2\u01f2\u01eb\3\2\2\2\u01f2\u01ec\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3a\3\2\2")
        buf.write("\2\u01f4\u01fc\7=\2\2\u01f5\u01fc\7>\2\2\u01f6\u01fc\7")
        buf.write("\3\2\2\u01f7\u01fc\7?\2\2\u01f8\u01fc\5$\23\2\u01f9\u01fc")
        buf.write("\5(\25\2\u01fa\u01fc\7<\2\2\u01fb\u01f4\3\2\2\2\u01fb")
        buf.write("\u01f5\3\2\2\2\u01fb\u01f6\3\2\2\2\u01fb\u01f7\3\2\2\2")
        buf.write("\u01fb\u01f8\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3")
        buf.write("\2\2\2\u01fcc\3\2\2\2\u01fd\u0201\5f\64\2\u01fe\u0201")
        buf.write("\5h\65\2\u01ff\u0201\7\34\2\2\u0200\u01fd\3\2\2\2\u0200")
        buf.write("\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2\u0201e\3\2\2\2\u0202")
        buf.write("\u0203\7\f\2\2\u0203\u0204\7\63\2\2\u0204\u0205\5d\63")
        buf.write("\2\u0205\u0206\78\2\2\u0206\u0207\7<\2\2\u0207\u0208\7")
        buf.write("\64\2\2\u0208g\3\2\2\2\u0209\u020a\t\t\2\2\u020ai\3\2")
        buf.write("\2\2\63mu{\u0082\u0086\u008d\u0092\u0099\u00a6\u00ab\u00b0")
        buf.write("\u00b8\u00c5\u00cb\u00d5\u00de\u00e7\u00f4\u0100\u010d")
        buf.write("\u0114\u0122\u012f\u013f\u014a\u0155\u0162\u016d\u0171")
        buf.write("\u017b\u0183\u018a\u0194\u019f\u01aa\u01b0\u01b5\u01be")
        buf.write("\u01c9\u01cc\u01d0\u01d8\u01db\u01de\u01e4\u01e8\u01f2")
        buf.write("\u01fb\u0200")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Self'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'==.'", "'+.'", "'::'", "'('", "')'", "'['", "']'", 
                     "'.'", "'..'", "':'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "BOOLLIT", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "ID", "DOLLARID", "COMMENT", 
                      "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", 
                      "ANDOP", "OROP", "EQUOP", "ASSIOP", "NEOP", "LTOP", 
                      "LTEOP", "GTOP", "GTEOP", "DOUEQUODOTOP", "ADDDOTOP", 
                      "DOUCOLON", "LB", "RB", "LSB", "RSB", "DOT", "DOUDOT", 
                      "COLON", "COMMA", "SEMI", "LP", "RP", "ARRAYSIZE", 
                      "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_classbody = 2
    RULE_attrdecl = 3
    RULE_mutable = 4
    RULE_immutable = 5
    RULE_nonvalue = 6
    RULE_value = 7
    RULE_methdecl = 8
    RULE_basicmeth = 9
    RULE_constructor = 10
    RULE_destructor = 11
    RULE_paralist = 12
    RULE_parasingle = 13
    RULE_methodattrdecl = 14
    RULE_nonvaluemethod = 15
    RULE_valuemethod = 16
    RULE_indexedarray = 17
    RULE_arraylist = 18
    RULE_multiarray = 19
    RULE_multiarraylist = 20
    RULE_blockstmt = 21
    RULE_stmt = 22
    RULE_assignstmt = 23
    RULE_indexexp = 24
    RULE_ifstmt = 25
    RULE_thenstmt = 26
    RULE_elseifstmts = 27
    RULE_elseifstmt = 28
    RULE_elsestmt = 29
    RULE_forinstmt = 30
    RULE_breakstmt = 31
    RULE_continuestmt = 32
    RULE_returnstmt = 33
    RULE_methodinvostmt = 34
    RULE_explist = 35
    RULE_exp = 36
    RULE_exp0 = 37
    RULE_exp1 = 38
    RULE_exp2 = 39
    RULE_exp3 = 40
    RULE_exp4 = 41
    RULE_exp5 = 42
    RULE_exp6 = 43
    RULE_exp7 = 44
    RULE_exp8 = 45
    RULE_exp9 = 46
    RULE_operands = 47
    RULE_literals = 48
    RULE_typ = 49
    RULE_arraytyp = 50
    RULE_primitivetyp = 51

    ruleNames =  [ "program", "classdecl", "classbody", "attrdecl", "mutable", 
                   "immutable", "nonvalue", "value", "methdecl", "basicmeth", 
                   "constructor", "destructor", "paralist", "parasingle", 
                   "methodattrdecl", "nonvaluemethod", "valuemethod", "indexedarray", 
                   "arraylist", "multiarray", "multiarraylist", "blockstmt", 
                   "stmt", "assignstmt", "indexexp", "ifstmt", "thenstmt", 
                   "elseifstmts", "elseifstmt", "elsestmt", "forinstmt", 
                   "breakstmt", "continuestmt", "returnstmt", "methodinvostmt", 
                   "explist", "exp", "exp0", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp8", "exp9", "operands", "literals", 
                   "typ", "arraytyp", "primitivetyp" ]

    EOF = Token.EOF
    BOOLLIT=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    TRUE=8
    FALSE=9
    ARRAY=10
    IN=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    STRING=15
    RETURN=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    SELF=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    NEW=24
    BY=25
    ID=26
    DOLLARID=27
    COMMENT=28
    ADDOP=29
    SUBOP=30
    MULOP=31
    DIVOP=32
    MODOP=33
    NOTOP=34
    ANDOP=35
    OROP=36
    EQUOP=37
    ASSIOP=38
    NEOP=39
    LTOP=40
    LTEOP=41
    GTOP=42
    GTEOP=43
    DOUEQUODOTOP=44
    ADDDOTOP=45
    DOUCOLON=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    DOT=51
    DOUDOT=52
    COLON=53
    COMMA=54
    SEMI=55
    LP=56
    RP=57
    ARRAYSIZE=58
    INTLIT=59
    FLOATLIT=60
    STRINGLIT=61
    WS=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.classdecl()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 109
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(D96Parser.CLASS)
            self.state = 112
            self.match(D96Parser.ID)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 113
                self.match(D96Parser.COLON)
                self.state = 114
                self.match(D96Parser.ID)


            self.state = 117
            self.match(D96Parser.LP)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLARID))) != 0):
                self.state = 118
                self.classbody()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrdecl(self):
            return self.getTypedRuleContext(D96Parser.AttrdeclContext,0)


        def methdecl(self):
            return self.getTypedRuleContext(D96Parser.MethdeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassbody" ):
                return visitor.visitClassbody(self)
            else:
                return visitor.visitChildren(self)




    def classbody(self):

        localctx = D96Parser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classbody)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.attrdecl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrdecl" ):
                return visitor.visitAttrdecl(self)
            else:
                return visitor.visitChildren(self)




    def attrdecl(self):

        localctx = D96Parser.AttrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attrdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR]:
                self.state = 130
                self.mutable()
                pass
            elif token in [D96Parser.VAL]:
                self.state = 131
                self.immutable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 134
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def nonvalue(self):
            return self.getTypedRuleContext(D96Parser.NonvalueContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mutable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable" ):
                return visitor.visitMutable(self)
            else:
                return visitor.visitChildren(self)




    def mutable(self):

        localctx = D96Parser.MutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mutable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(D96Parser.VAR)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 137
                self.nonvalue()
                pass

            elif la_ == 2:
                self.state = 138
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def nonvalue(self):
            return self.getTypedRuleContext(D96Parser.NonvalueContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_immutable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutable" ):
                return visitor.visitImmutable(self)
            else:
                return visitor.visitChildren(self)




    def immutable(self):

        localctx = D96Parser.ImmutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immutable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(D96Parser.VAL)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 142
                self.nonvalue()
                pass

            elif la_ == 2:
                self.state = 143
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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
            return D96Parser.RULE_nonvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonvalue" ):
                return visitor.visitNonvalue(self)
            else:
                return visitor.visitChildren(self)




    def nonvalue(self):

        localctx = D96Parser.NonvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nonvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 147
                self.match(D96Parser.COMMA)
                self.state = 148
                self.nonvalue()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 149
                self.match(D96Parser.COLON)
                self.state = 150
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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
            return D96Parser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = D96Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 154
                self.match(D96Parser.COMMA)
                self.state = 155
                self.value()
                self.state = 156
                self.match(D96Parser.COMMA)
                self.state = 157
                self.exp()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 159
                self.match(D96Parser.COLON)
                self.state = 160
                self.typ()
                self.state = 161
                self.match(D96Parser.ASSIOP)
                self.state = 162
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethdecl" ):
                return visitor.visitMethdecl(self)
            else:
                return visitor.visitChildren(self)




    def methdecl(self):

        localctx = D96Parser.MethdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_methdecl)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.basicmeth()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicmeth" ):
                return visitor.visitBasicmeth(self)
            else:
                return visitor.visitChildren(self)




    def basicmeth(self):

        localctx = D96Parser.BasicmethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_basicmeth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self.match(D96Parser.LB)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 173
                self.paralist()


            self.state = 176
            self.match(D96Parser.RB)
            self.state = 177
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 180
            self.match(D96Parser.LB)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 181
                self.paralist()


            self.state = 184
            self.match(D96Parser.RB)
            self.state = 185
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(D96Parser.DESTRUCTOR)
            self.state = 188
            self.match(D96Parser.LB)
            self.state = 189
            self.match(D96Parser.RB)
            self.state = 190
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parasingle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParasingleContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParasingleContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = D96Parser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 193 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 192
                        self.parasingle()
                        self.state = 195 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==D96Parser.ID):
                            break

                    self.state = 197
                    self.match(D96Parser.SEMI) 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 204
            self.parasingle()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParasingleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parasingle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParasingle" ):
                return visitor.visitParasingle(self)
            else:
                return visitor.visitChildren(self)




    def parasingle(self):

        localctx = D96Parser.ParasingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parasingle)
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
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodattrdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def nonvaluemethod(self):
            return self.getTypedRuleContext(D96Parser.NonvaluemethodContext,0)


        def valuemethod(self):
            return self.getTypedRuleContext(D96Parser.ValuemethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodattrdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodattrdecl" ):
                return visitor.visitMethodattrdecl(self)
            else:
                return visitor.visitChildren(self)




    def methodattrdecl(self):

        localctx = D96Parser.MethodattrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_methodattrdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 218
                self.nonvaluemethod()
                pass

            elif la_ == 2:
                self.state = 219
                self.valuemethod()
                pass


            self.state = 222
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonvaluemethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def nonvaluemethod(self):
            return self.getTypedRuleContext(D96Parser.NonvaluemethodContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_nonvaluemethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonvaluemethod" ):
                return visitor.visitNonvaluemethod(self)
            else:
                return visitor.visitChildren(self)




    def nonvaluemethod(self):

        localctx = D96Parser.NonvaluemethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nonvaluemethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(D96Parser.ID)
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 225
                self.match(D96Parser.COMMA)
                self.state = 226
                self.nonvaluemethod()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 227
                self.match(D96Parser.COLON)
                self.state = 228
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


    class ValuemethodContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def valuemethod(self):
            return self.getTypedRuleContext(D96Parser.ValuemethodContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def ASSIOP(self):
            return self.getToken(D96Parser.ASSIOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_valuemethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValuemethod" ):
                return visitor.visitValuemethod(self)
            else:
                return visitor.visitChildren(self)




    def valuemethod(self):

        localctx = D96Parser.ValuemethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_valuemethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(D96Parser.ID)
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.state = 232
                self.match(D96Parser.COMMA)
                self.state = 233
                self.valuemethod()
                self.state = 234
                self.match(D96Parser.COMMA)
                self.state = 235
                self.exp()
                pass
            elif token in [D96Parser.COLON]:
                self.state = 237
                self.match(D96Parser.COLON)
                self.state = 238
                self.typ()
                self.state = 239
                self.match(D96Parser.ASSIOP)
                self.state = 240
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


    class IndexedarrayContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexedarray" ):
                return visitor.visitIndexedarray(self)
            else:
                return visitor.visitChildren(self)




    def indexedarray(self):

        localctx = D96Parser.IndexedarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_indexedarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(D96Parser.ARRAY)
            self.state = 245
            self.match(D96Parser.LB)
            self.state = 246
            self.arraylist()
            self.state = 247
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylist" ):
                return visitor.visitArraylist(self)
            else:
                return visitor.visitChildren(self)




    def arraylist(self):

        localctx = D96Parser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraylist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.exp()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 250
                self.match(D96Parser.COMMA)
                self.state = 251
                self.exp()
                self.state = 256
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiarray" ):
                return visitor.visitMultiarray(self)
            else:
                return visitor.visitChildren(self)




    def multiarray(self):

        localctx = D96Parser.MultiarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(D96Parser.ARRAY)
            self.state = 258
            self.match(D96Parser.LB)
            self.state = 259
            self.multiarraylist()
            self.state = 260
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiarraylistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiarraylist" ):
                return visitor.visitMultiarraylist(self)
            else:
                return visitor.visitChildren(self)




    def multiarraylist(self):

        localctx = D96Parser.MultiarraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_multiarraylist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.indexedarray()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 263
                self.match(D96Parser.COMMA)
                self.state = 264
                self.indexedarray()
                self.state = 269
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = D96Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.LP)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.NULL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 271
                self.stmt()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.forinstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.continuestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 285
                self.methodinvostmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 286
                self.methodattrdecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 287
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = D96Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.exp6(0)
            self.state = 291
            self.match(D96Parser.ASSIOP)
            self.state = 292
            self.exp()
            self.state = 293
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexpContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexexp" ):
                return visitor.visitIndexexp(self)
            else:
                return visitor.visitChildren(self)




    def indexexp(self):

        localctx = D96Parser.IndexexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_indexexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 295
                    self.match(D96Parser.LSB)
                    self.state = 296
                    self.exp()
                    self.state = 297
                    self.match(D96Parser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 301 
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def thenstmt(self):
            return self.getTypedRuleContext(D96Parser.ThenstmtContext,0)


        def elseifstmts(self):
            return self.getTypedRuleContext(D96Parser.ElseifstmtsContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(D96Parser.ElsestmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = D96Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.thenstmt()
            self.state = 304
            self.elseifstmts()
            self.state = 305
            self.elsestmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThenstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_thenstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThenstmt" ):
                return visitor.visitThenstmt(self)
            else:
                return visitor.visitChildren(self)




    def thenstmt(self):

        localctx = D96Parser.ThenstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_thenstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(D96Parser.IF)
            self.state = 308
            self.match(D96Parser.LB)
            self.state = 309
            self.exp()
            self.state = 310
            self.match(D96Parser.RB)
            self.state = 311
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifstmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseifstmt(self):
            return self.getTypedRuleContext(D96Parser.ElseifstmtContext,0)


        def elseifstmts(self):
            return self.getTypedRuleContext(D96Parser.ElseifstmtsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseifstmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifstmts" ):
                return visitor.visitElseifstmts(self)
            else:
                return visitor.visitChildren(self)




    def elseifstmts(self):

        localctx = D96Parser.ElseifstmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elseifstmts)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.elseifstmt()
                self.state = 314
                self.elseifstmts()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.SELF, D96Parser.NEW, D96Parser.ID, D96Parser.LB, D96Parser.LP, D96Parser.RP, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)

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


    class ElseifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifstmt" ):
                return visitor.visitElseifstmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifstmt(self):

        localctx = D96Parser.ElseifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elseifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(D96Parser.ELSEIF)
            self.state = 320
            self.match(D96Parser.LB)
            self.state = 321
            self.exp()
            self.state = 322
            self.match(D96Parser.RB)
            self.state = 323
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = D96Parser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elsestmt)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(D96Parser.ELSE)
                self.state = 326
                self.blockstmt()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.SELF, D96Parser.NEW, D96Parser.ID, D96Parser.LB, D96Parser.LP, D96Parser.RP, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)

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


    class ForinstmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForinstmt" ):
                return visitor.visitForinstmt(self)
            else:
                return visitor.visitChildren(self)




    def forinstmt(self):

        localctx = D96Parser.ForinstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forinstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(D96Parser.FOREACH)
            self.state = 331
            self.match(D96Parser.LB)
            self.state = 332
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 333
            self.match(D96Parser.IN)
            self.state = 334
            self.exp()
            self.state = 335
            self.match(D96Parser.DOUDOT)
            self.state = 336
            self.exp()
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 337
                self.match(D96Parser.BY)
                self.state = 338
                self.exp()


            self.state = 341
            self.match(D96Parser.RB)
            self.state = 342
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = D96Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(D96Parser.BREAK)
            self.state = 345
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = D96Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(D96Parser.CONTINUE)
            self.state = 348
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = D96Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(D96Parser.RETURN)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 351
                self.exp()


            self.state = 354
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodinvostmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvostmt" ):
                return visitor.visitMethodinvostmt(self)
            else:
                return visitor.visitChildren(self)




    def methodinvostmt(self):

        localctx = D96Parser.MethodinvostmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_methodinvostmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 356
                self.exp7(0)
                self.state = 357
                self.match(D96Parser.DOT)
                self.state = 358
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 360
                self.match(D96Parser.ID)
                self.state = 361
                self.match(D96Parser.DOUCOLON)
                self.state = 362
                self.match(D96Parser.DOLLARID)
                pass


            self.state = 365
            self.match(D96Parser.LB)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 366
                self.explist()


            self.state = 369
            self.match(D96Parser.RB)
            self.state = 370
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = D96Parser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.exp()
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 373
                self.match(D96Parser.COMMA)
                self.state = 374
                self.exp()
                self.state = 379
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.exp0()
                self.state = 381
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOUEQUODOTOP or _la==D96Parser.ADDDOTOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 382
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp0)
        self._la = 0 # Token type
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.exp1(0)
                self.state = 388
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUOP) | (1 << D96Parser.NEOP) | (1 << D96Parser.LTOP) | (1 << D96Parser.LTEOP) | (1 << D96Parser.GTOP) | (1 << D96Parser.GTEOP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 389
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 397
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 398
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 399
                    self.exp2(0) 
                self.state = 404
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 408
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 409
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADDOP or _la==D96Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 410
                    self.exp3(0) 
                self.state = 415
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 419
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 420
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULOP) | (1 << D96Parser.DIVOP) | (1 << D96Parser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 421
                    self.exp4() 
                self.state = 426
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = D96Parser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp4)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(D96Parser.NOTOP)
                self.state = 428
                self.exp4()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.ID, D96Parser.SUBOP, D96Parser.LB, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp5)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(D96Parser.SUBOP)
                self.state = 433
                self.exp5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.ID, D96Parser.LB, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 444
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 440
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 441
                    self.indexexp() 
                self.state = 446
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 450
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 451
                    self.match(D96Parser.DOT)
                    self.state = 452
                    self.match(D96Parser.ID)
                    self.state = 458
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 453
                        self.match(D96Parser.LB)
                        self.state = 455
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                            self.state = 454
                            self.explist()


                        self.state = 457
                        self.match(D96Parser.RB)

             
                self.state = 464
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = D96Parser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp8)
        self._la = 0 # Token type
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(D96Parser.ID)
                self.state = 466
                self.match(D96Parser.DOUCOLON)
                self.state = 467
                self.match(D96Parser.DOLLARID)
                self.state = 473
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 468
                    self.match(D96Parser.LB)
                    self.state = 470
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                        self.state = 469
                        self.explist()


                    self.state = 472
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(D96Parser.NEW)
                self.state = 479
                self.match(D96Parser.ID)
                self.state = 480
                self.match(D96Parser.LB)
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.ID) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAYSIZE) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                    self.state = 481
                    self.explist()


                self.state = 484
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_operands)
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.ARRAYSIZE, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.literals()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.match(D96Parser.LB)
                self.state = 491
                self.exp()
                self.state = 492
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 494
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 495
                self.match(D96Parser.NULL)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literals)
        try:
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 500
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 501
                self.match(D96Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 502
                self.indexedarray()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 503
                self.multiarray()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 504
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_typ)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.arraytyp()
                pass
            elif token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.primitivetyp()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytyp" ):
                return visitor.visitArraytyp(self)
            else:
                return visitor.visitChildren(self)




    def arraytyp(self):

        localctx = D96Parser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arraytyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(D96Parser.ARRAY)
            self.state = 513
            self.match(D96Parser.LSB)
            self.state = 514
            self.typ()
            self.state = 515
            self.match(D96Parser.COMMA)
            self.state = 516
            self.match(D96Parser.ARRAYSIZE)
            self.state = 517
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitivetypContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitivetyp" ):
                return visitor.visitPrimitivetyp(self)
            else:
                return visitor.visitChildren(self)




    def primitivetyp(self):

        localctx = D96Parser.PrimitivetypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_primitivetyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
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
        self._predicates[38] = self.exp1_sempred
        self._predicates[39] = self.exp2_sempred
        self._predicates[40] = self.exp3_sempred
        self._predicates[43] = self.exp6_sempred
        self._predicates[44] = self.exp7_sempred
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
         




