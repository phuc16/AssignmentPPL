# Generated from c:\Users\USER PC\Documents\HCMUT\212\PPL\Assignment\assignment4\initial\src\main\d96\parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u02d3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\5\2\u009e\n\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\7\33")
        buf.write("\u0132\n\33\f\33\16\33\u0135\13\33\3\34\3\34\6\34\u0139")
        buf.write("\n\34\r\34\16\34\u013a\3\35\3\35\3\35\3\35\7\35\u0141")
        buf.write("\n\35\f\35\16\35\u0144\13\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3;\7;")
        buf.write("\u0194\n;\f;\16;\u0197\13;\3;\5;\u019a\n;\3;\6;\u019d")
        buf.write("\n;\r;\16;\u019e\7;\u01a1\n;\f;\16;\u01a4\13;\3;\5;\u01a7")
        buf.write("\n;\3<\3<\3<\3<\7<\u01ad\n<\f<\16<\u01b0\13<\3<\5<\u01b3")
        buf.write("\n<\3<\6<\u01b6\n<\r<\16<\u01b7\7<\u01ba\n<\f<\16<\u01bd")
        buf.write("\13<\3=\3=\3=\7=\u01c2\n=\f=\16=\u01c5\13=\3=\5=\u01c8")
        buf.write("\n=\3=\6=\u01cb\n=\r=\16=\u01cc\7=\u01cf\n=\f=\16=\u01d2")
        buf.write("\13=\3=\5=\u01d5\n=\3>\3>\3>\7>\u01da\n>\f>\16>\u01dd")
        buf.write("\13>\3>\5>\u01e0\n>\3>\6>\u01e3\n>\r>\16>\u01e4\7>\u01e7")
        buf.write("\n>\f>\16>\u01ea\13>\3?\3?\3?\3?\7?\u01f0\n?\f?\16?\u01f3")
        buf.write("\13?\3?\5?\u01f6\n?\3?\6?\u01f9\n?\r?\16?\u01fa\7?\u01fd")
        buf.write("\n?\f?\16?\u0200\13?\3?\5?\u0203\n?\3@\3@\3@\3@\7@\u0209")
        buf.write("\n@\f@\16@\u020c\13@\3@\5@\u020f\n@\3@\6@\u0212\n@\r@")
        buf.write("\16@\u0213\7@\u0216\n@\f@\16@\u0219\13@\3A\3A\7A\u021d")
        buf.write("\nA\fA\16A\u0220\13A\3A\5A\u0223\nA\3A\6A\u0226\nA\rA")
        buf.write("\16A\u0227\7A\u022a\nA\fA\16A\u022d\13A\3A\5A\u0230\n")
        buf.write("A\3B\3B\7B\u0234\nB\fB\16B\u0237\13B\3B\5B\u023a\nB\3")
        buf.write("B\6B\u023d\nB\rB\16B\u023e\7B\u0241\nB\fB\16B\u0244\13")
        buf.write("B\3C\3C\3C\3C\5C\u024a\nC\3C\3C\3D\3D\3D\3D\5D\u0252\n")
        buf.write("D\3D\3D\3E\3E\7E\u0258\nE\fE\16E\u025b\13E\3E\5E\u025e")
        buf.write("\nE\3E\6E\u0261\nE\rE\16E\u0262\7E\u0265\nE\fE\16E\u0268")
        buf.write("\13E\3E\5E\u026b\nE\3F\3F\7F\u026f\nF\fF\16F\u0272\13")
        buf.write("F\3G\3G\5G\u0276\nG\3G\3G\7G\u027a\nG\fG\16G\u027d\13")
        buf.write("G\3G\5G\u0280\nG\3H\3H\3H\5H\u0285\nH\3H\3H\3H\3H\3H\3")
        buf.write("H\5H\u028d\nH\3H\3H\3I\3I\3I\3I\3I\3I\7I\u0297\nI\fI\16")
        buf.write("I\u029a\13I\3I\3I\3I\3J\6J\u02a0\nJ\rJ\16J\u02a1\3J\3")
        buf.write("J\3K\3K\3K\3L\3L\3L\3L\3L\3L\7L\u02af\nL\fL\16L\u02b2")
        buf.write("\13L\3L\3L\3L\5L\u02b7\nL\3L\3L\3M\3M\3M\3M\3M\3M\7M\u02c1")
        buf.write("\nM\fM\16M\u02c4\13M\3M\3M\5M\u02c8\nM\3M\3M\3M\3M\5M")
        buf.write("\u02ce\nM\5M\u02d0\nM\3M\3M\3\u0142\2N\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2{\2}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085<\u0087=\u0089\2\u008b\2\u008d")
        buf.write("\2\u008f>\u0091?\u0093@\u0095A\u0097B\u0099C\3\2\31\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\4\2ZZzz\4\2\63;CH\4\2\62;CH\3")
        buf.write("\2aa\3\2\639\3\2\629\4\2DDdd\3\2\62\63\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv")
        buf.write("\3\2))\3\2$$\5\2\13\f\17\17\"\"\n\2$$))^^ddhhppttvv\4")
        buf.write("\2\f\f\17\17\3\2^^\6\3\f\f\17\17$$^^\2\u030f\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008f\3\2")
        buf.write("\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2")
        buf.write("\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u009d\3\2\2\2\5\u009f")
        buf.write("\3\2\2\2\7\u00a5\3\2\2\2\t\u00ae\3\2\2\2\13\u00b1\3\2")
        buf.write("\2\2\r\u00b8\3\2\2\2\17\u00bd\3\2\2\2\21\u00c5\3\2\2\2")
        buf.write("\23\u00ca\3\2\2\2\25\u00d0\3\2\2\2\27\u00d6\3\2\2\2\31")
        buf.write("\u00d9\3\2\2\2\33\u00dd\3\2\2\2\35\u00e3\3\2\2\2\37\u00eb")
        buf.write("\3\2\2\2!\u00f2\3\2\2\2#\u00f9\3\2\2\2%\u00fe\3\2\2\2")
        buf.write("\'\u0104\3\2\2\2)\u0108\3\2\2\2+\u010c\3\2\2\2-\u0111")
        buf.write("\3\2\2\2/\u011d\3\2\2\2\61\u0128\3\2\2\2\63\u012c\3\2")
        buf.write("\2\2\65\u012f\3\2\2\2\67\u0136\3\2\2\29\u013c\3\2\2\2")
        buf.write(";\u014a\3\2\2\2=\u014c\3\2\2\2?\u014e\3\2\2\2A\u0150\3")
        buf.write("\2\2\2C\u0152\3\2\2\2E\u0154\3\2\2\2G\u0156\3\2\2\2I\u0159")
        buf.write("\3\2\2\2K\u015c\3\2\2\2M\u015f\3\2\2\2O\u0161\3\2\2\2")
        buf.write("Q\u0164\3\2\2\2S\u0166\3\2\2\2U\u0169\3\2\2\2W\u016b\3")
        buf.write("\2\2\2Y\u016e\3\2\2\2[\u0172\3\2\2\2]\u0175\3\2\2\2_\u0178")
        buf.write("\3\2\2\2a\u017a\3\2\2\2c\u017c\3\2\2\2e\u017e\3\2\2\2")
        buf.write("g\u0180\3\2\2\2i\u0182\3\2\2\2k\u0185\3\2\2\2m\u0187\3")
        buf.write("\2\2\2o\u0189\3\2\2\2q\u018b\3\2\2\2s\u018d\3\2\2\2u\u018f")
        buf.write("\3\2\2\2w\u01a8\3\2\2\2y\u01be\3\2\2\2{\u01d6\3\2\2\2")
        buf.write("}\u01eb\3\2\2\2\177\u0204\3\2\2\2\u0081\u022f\3\2\2\2")
        buf.write("\u0083\u0231\3\2\2\2\u0085\u0249\3\2\2\2\u0087\u0251\3")
        buf.write("\2\2\2\u0089\u026a\3\2\2\2\u008b\u026c\3\2\2\2\u008d\u0273")
        buf.write("\3\2\2\2\u008f\u028c\3\2\2\2\u0091\u0290\3\2\2\2\u0093")
        buf.write("\u029f\3\2\2\2\u0095\u02a5\3\2\2\2\u0097\u02a8\3\2\2\2")
        buf.write("\u0099\u02ba\3\2\2\2\u009b\u009e\5\21\t\2\u009c\u009e")
        buf.write("\5\23\n\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\4\3\2\2\2\u009f\u00a0\7D\2\2\u00a0\u00a1\7t\2\2\u00a1")
        buf.write("\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7m\2\2\u00a4")
        buf.write("\6\3\2\2\2\u00a5\u00a6\7E\2\2\u00a6\u00a7\7q\2\2\u00a7")
        buf.write("\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7k\2\2\u00aa")
        buf.write("\u00ab\7p\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\b\3\2\2\2\u00ae\u00af\7K\2\2\u00af\u00b0\7h\2\2\u00b0")
        buf.write("\n\3\2\2\2\u00b1\u00b2\7G\2\2\u00b2\u00b3\7n\2\2\u00b3")
        buf.write("\u00b4\7u\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\f\3\2\2\2\u00b8\u00b9\7G\2\2\u00b9")
        buf.write("\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7g\2\2\u00bc")
        buf.write("\16\3\2\2\2\u00bd\u00be\7H\2\2\u00be\u00bf\7q\2\2\u00bf")
        buf.write("\u00c0\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7c\2\2\u00c2")
        buf.write("\u00c3\7e\2\2\u00c3\u00c4\7j\2\2\u00c4\20\3\2\2\2\u00c5")
        buf.write("\u00c6\7V\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7w\2\2\u00c8")
        buf.write("\u00c9\7g\2\2\u00c9\22\3\2\2\2\u00ca\u00cb\7H\2\2\u00cb")
        buf.write("\u00cc\7c\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce\7u\2\2\u00ce")
        buf.write("\u00cf\7g\2\2\u00cf\24\3\2\2\2\u00d0\u00d1\7C\2\2\u00d1")
        buf.write("\u00d2\7t\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write("\u00d5\7{\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7K\2\2\u00d7")
        buf.write("\u00d8\7p\2\2\u00d8\30\3\2\2\2\u00d9\u00da\7K\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc\32\3\2\2\2\u00dd")
        buf.write("\u00de\7H\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7q\2\2\u00e0")
        buf.write("\u00e1\7c\2\2\u00e1\u00e2\7v\2\2\u00e2\34\3\2\2\2\u00e3")
        buf.write("\u00e4\7D\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7q\2\2\u00e6")
        buf.write("\u00e7\7n\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9\7c\2\2\u00e9")
        buf.write("\u00ea\7p\2\2\u00ea\36\3\2\2\2\u00eb\u00ec\7U\2\2\u00ec")
        buf.write("\u00ed\7v\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7k\2\2\u00ef")
        buf.write("\u00f0\7p\2\2\u00f0\u00f1\7i\2\2\u00f1 \3\2\2\2\u00f2")
        buf.write("\u00f3\7T\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("\u00f6\7w\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write("\"\3\2\2\2\u00f9\u00fa\7P\2\2\u00fa\u00fb\7w\2\2\u00fb")
        buf.write("\u00fc\7n\2\2\u00fc\u00fd\7n\2\2\u00fd$\3\2\2\2\u00fe")
        buf.write("\u00ff\7E\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7c\2\2\u0101")
        buf.write("\u0102\7u\2\2\u0102\u0103\7u\2\2\u0103&\3\2\2\2\u0104")
        buf.write("\u0105\7X\2\2\u0105\u0106\7c\2\2\u0106\u0107\7n\2\2\u0107")
        buf.write("(\3\2\2\2\u0108\u0109\7X\2\2\u0109\u010a\7c\2\2\u010a")
        buf.write("\u010b\7t\2\2\u010b*\3\2\2\2\u010c\u010d\7U\2\2\u010d")
        buf.write("\u010e\7g\2\2\u010e\u010f\7n\2\2\u010f\u0110\7h\2\2\u0110")
        buf.write(",\3\2\2\2\u0111\u0112\7E\2\2\u0112\u0113\7q\2\2\u0113")
        buf.write("\u0114\7p\2\2\u0114\u0115\7u\2\2\u0115\u0116\7v\2\2\u0116")
        buf.write("\u0117\7t\2\2\u0117\u0118\7w\2\2\u0118\u0119\7e\2\2\u0119")
        buf.write("\u011a\7v\2\2\u011a\u011b\7q\2\2\u011b\u011c\7t\2\2\u011c")
        buf.write(".\3\2\2\2\u011d\u011e\7F\2\2\u011e\u011f\7g\2\2\u011f")
        buf.write("\u0120\7u\2\2\u0120\u0121\7v\2\2\u0121\u0122\7t\2\2\u0122")
        buf.write("\u0123\7w\2\2\u0123\u0124\7e\2\2\u0124\u0125\7v\2\2\u0125")
        buf.write("\u0126\7q\2\2\u0126\u0127\7t\2\2\u0127\60\3\2\2\2\u0128")
        buf.write("\u0129\7P\2\2\u0129\u012a\7g\2\2\u012a\u012b\7y\2\2\u012b")
        buf.write("\62\3\2\2\2\u012c\u012d\7D\2\2\u012d\u012e\7{\2\2\u012e")
        buf.write("\64\3\2\2\2\u012f\u0133\t\2\2\2\u0130\u0132\t\3\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134\66\3\2\2\2\u0135\u0133\3\2")
        buf.write("\2\2\u0136\u0138\7&\2\2\u0137\u0139\t\3\2\2\u0138\u0137")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b8\3\2\2\2\u013c\u013d\7%\2\2\u013d")
        buf.write("\u013e\7%\2\2\u013e\u0142\3\2\2\2\u013f\u0141\13\2\2\2")
        buf.write("\u0140\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0142\u0140\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145\u0146\7%\2\2\u0146\u0147\7%\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\b\35\2\2\u0149:\3\2\2\2\u014a\u014b")
        buf.write("\7-\2\2\u014b<\3\2\2\2\u014c\u014d\7/\2\2\u014d>\3\2\2")
        buf.write("\2\u014e\u014f\7,\2\2\u014f@\3\2\2\2\u0150\u0151\7\61")
        buf.write("\2\2\u0151B\3\2\2\2\u0152\u0153\7\'\2\2\u0153D\3\2\2\2")
        buf.write("\u0154\u0155\7#\2\2\u0155F\3\2\2\2\u0156\u0157\7(\2\2")
        buf.write("\u0157\u0158\7(\2\2\u0158H\3\2\2\2\u0159\u015a\7~\2\2")
        buf.write("\u015a\u015b\7~\2\2\u015bJ\3\2\2\2\u015c\u015d\7?\2\2")
        buf.write("\u015d\u015e\7?\2\2\u015eL\3\2\2\2\u015f\u0160\7?\2\2")
        buf.write("\u0160N\3\2\2\2\u0161\u0162\7#\2\2\u0162\u0163\7?\2\2")
        buf.write("\u0163P\3\2\2\2\u0164\u0165\7>\2\2\u0165R\3\2\2\2\u0166")
        buf.write("\u0167\7>\2\2\u0167\u0168\7?\2\2\u0168T\3\2\2\2\u0169")
        buf.write("\u016a\7@\2\2\u016aV\3\2\2\2\u016b\u016c\7@\2\2\u016c")
        buf.write("\u016d\7?\2\2\u016dX\3\2\2\2\u016e\u016f\7?\2\2\u016f")
        buf.write("\u0170\7?\2\2\u0170\u0171\7\60\2\2\u0171Z\3\2\2\2\u0172")
        buf.write("\u0173\7-\2\2\u0173\u0174\7\60\2\2\u0174\\\3\2\2\2\u0175")
        buf.write("\u0176\7<\2\2\u0176\u0177\7<\2\2\u0177^\3\2\2\2\u0178")
        buf.write("\u0179\7*\2\2\u0179`\3\2\2\2\u017a\u017b\7+\2\2\u017b")
        buf.write("b\3\2\2\2\u017c\u017d\7]\2\2\u017dd\3\2\2\2\u017e\u017f")
        buf.write("\7_\2\2\u017ff\3\2\2\2\u0180\u0181\7\60\2\2\u0181h\3\2")
        buf.write("\2\2\u0182\u0183\7\60\2\2\u0183\u0184\7\60\2\2\u0184j")
        buf.write("\3\2\2\2\u0185\u0186\7<\2\2\u0186l\3\2\2\2\u0187\u0188")
        buf.write("\7.\2\2\u0188n\3\2\2\2\u0189\u018a\7=\2\2\u018ap\3\2\2")
        buf.write("\2\u018b\u018c\7}\2\2\u018cr\3\2\2\2\u018d\u018e\7\177")
        buf.write("\2\2\u018et\3\2\2\2\u018f\u0190\7\62\2\2\u0190\u01a6\t")
        buf.write("\4\2\2\u0191\u0195\t\5\2\2\u0192\u0194\t\6\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u01a2\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0198\u019a\t\7\2\2\u0199\u0198\3\2\2\2\u0199\u019a\3")
        buf.write("\2\2\2\u019a\u019c\3\2\2\2\u019b\u019d\t\6\2\2\u019c\u019b")
        buf.write("\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u0199\3\2\2\2")
        buf.write("\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3")
        buf.write("\2\2\2\u01a3\u01a7\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7")
        buf.write("\7\62\2\2\u01a6\u0191\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("v\3\2\2\2\u01a8\u01a9\7\62\2\2\u01a9\u01aa\t\4\2\2\u01aa")
        buf.write("\u01ae\t\5\2\2\u01ab\u01ad\t\6\2\2\u01ac\u01ab\3\2\2\2")
        buf.write("\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3")
        buf.write("\2\2\2\u01af\u01bb\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3")
        buf.write("\t\7\2\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b5\3\2\2\2\u01b4\u01b6\t\6\2\2\u01b5\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3")
        buf.write("\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b2\3\2\2\2\u01ba\u01bd")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("x\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01d4\7\62\2\2\u01bf")
        buf.write("\u01c3\t\b\2\2\u01c0\u01c2\t\t\2\2\u01c1\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01d0\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c8")
        buf.write("\t\7\2\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01ca\3\2\2\2\u01c9\u01cb\t\t\2\2\u01ca\u01c9\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01c7\3\2\2\2\u01cf\u01d2")
        buf.write("\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d5\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d5\7\62\2")
        buf.write("\2\u01d4\u01bf\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5z\3\2")
        buf.write("\2\2\u01d6\u01d7\7\62\2\2\u01d7\u01db\t\b\2\2\u01d8\u01da")
        buf.write("\t\t\2\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db")
        buf.write("\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01e8\3\2\2\2")
        buf.write("\u01dd\u01db\3\2\2\2\u01de\u01e0\t\7\2\2\u01df\u01de\3")
        buf.write("\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01e3")
        buf.write("\t\t\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7\3\2\2\2")
        buf.write("\u01e6\u01df\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3")
        buf.write("\2\2\2\u01e8\u01e9\3\2\2\2\u01e9|\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01eb\u01ec\7\62\2\2\u01ec\u0202\t\n\2\2\u01ed")
        buf.write("\u01f1\7\63\2\2\u01ee\u01f0\t\13\2\2\u01ef\u01ee\3\2\2")
        buf.write("\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01fe\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f6\t\7\2\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3\2\2\2")
        buf.write("\u01f6\u01f8\3\2\2\2\u01f7\u01f9\t\13\2\2\u01f8\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01f5\3\2\2\2")
        buf.write("\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3")
        buf.write("\2\2\2\u01ff\u0203\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0203")
        buf.write("\7\62\2\2\u0202\u01ed\3\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("~\3\2\2\2\u0204\u0205\7\62\2\2\u0205\u0206\t\n\2\2\u0206")
        buf.write("\u020a\7\63\2\2\u0207\u0209\t\13\2\2\u0208\u0207\3\2\2")
        buf.write("\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b")
        buf.write("\3\2\2\2\u020b\u0217\3\2\2\2\u020c\u020a\3\2\2\2\u020d")
        buf.write("\u020f\t\7\2\2\u020e\u020d\3\2\2\2\u020e\u020f\3\2\2\2")
        buf.write("\u020f\u0211\3\2\2\2\u0210\u0212\t\13\2\2\u0211\u0210")
        buf.write("\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u020e\3\2\2\2")
        buf.write("\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3")
        buf.write("\2\2\2\u0218\u0080\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u021e")
        buf.write("\t\f\2\2\u021b\u021d\t\r\2\2\u021c\u021b\3\2\2\2\u021d")
        buf.write("\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2")
        buf.write("\u021f\u022b\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u0223\t")
        buf.write("\7\2\2\u0222\u0221\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225")
        buf.write("\3\2\2\2\u0224\u0226\t\r\2\2\u0225\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228\u022a\3\2\2\2\u0229\u0222\3\2\2\2\u022a\u022d\3")
        buf.write("\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u0230")
        buf.write("\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u0230\7\62\2\2\u022f")
        buf.write("\u021a\3\2\2\2\u022f\u022e\3\2\2\2\u0230\u0082\3\2\2\2")
        buf.write("\u0231\u0235\t\f\2\2\u0232\u0234\t\r\2\2\u0233\u0232\3")
        buf.write("\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236")
        buf.write("\3\2\2\2\u0236\u0242\3\2\2\2\u0237\u0235\3\2\2\2\u0238")
        buf.write("\u023a\t\7\2\2\u0239\u0238\3\2\2\2\u0239\u023a\3\2\2\2")
        buf.write("\u023a\u023c\3\2\2\2\u023b\u023d\t\r\2\2\u023c\u023b\3")
        buf.write("\2\2\2\u023d\u023e\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f")
        buf.write("\3\2\2\2\u023f\u0241\3\2\2\2\u0240\u0239\3\2\2\2\u0241")
        buf.write("\u0244\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2")
        buf.write("\u0243\u0084\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u024a\5")
        buf.write("w<\2\u0246\u024a\5{>\2\u0247\u024a\5\177@\2\u0248\u024a")
        buf.write("\5\u0083B\2\u0249\u0245\3\2\2\2\u0249\u0246\3\2\2\2\u0249")
        buf.write("\u0247\3\2\2\2\u0249\u0248\3\2\2\2\u024a\u024b\3\2\2\2")
        buf.write("\u024b\u024c\bC\3\2\u024c\u0086\3\2\2\2\u024d\u0252\5")
        buf.write("u;\2\u024e\u0252\5y=\2\u024f\u0252\5}?\2\u0250\u0252\5")
        buf.write("\u0081A\2\u0251\u024d\3\2\2\2\u0251\u024e\3\2\2\2\u0251")
        buf.write("\u024f\3\2\2\2\u0251\u0250\3\2\2\2\u0252\u0253\3\2\2\2")
        buf.write("\u0253\u0254\bD\4\2\u0254\u0088\3\2\2\2\u0255\u0259\t")
        buf.write("\f\2\2\u0256\u0258\t\r\2\2\u0257\u0256\3\2\2\2\u0258\u025b")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u0266\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025e\t\7\2\2")
        buf.write("\u025d\u025c\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0260\3")
        buf.write("\2\2\2\u025f\u0261\t\r\2\2\u0260\u025f\3\2\2\2\u0261\u0262")
        buf.write("\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263\3\2\2\2\u0263")
        buf.write("\u0265\3\2\2\2\u0264\u025d\3\2\2\2\u0265\u0268\3\2\2\2")
        buf.write("\u0266\u0264\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u026b\3")
        buf.write("\2\2\2\u0268\u0266\3\2\2\2\u0269\u026b\7\62\2\2\u026a")
        buf.write("\u0255\3\2\2\2\u026a\u0269\3\2\2\2\u026b\u008a\3\2\2\2")
        buf.write("\u026c\u0270\5g\64\2\u026d\u026f\t\r\2\2\u026e\u026d\3")
        buf.write("\2\2\2\u026f\u0272\3\2\2\2\u0270\u026e\3\2\2\2\u0270\u0271")
        buf.write("\3\2\2\2\u0271\u008c\3\2\2\2\u0272\u0270\3\2\2\2\u0273")
        buf.write("\u0275\t\16\2\2\u0274\u0276\t\17\2\2\u0275\u0274\3\2\2")
        buf.write("\2\u0275\u0276\3\2\2\2\u0276\u027f\3\2\2\2\u0277\u027b")
        buf.write("\t\f\2\2\u0278\u027a\t\r\2\2\u0279\u0278\3\2\2\2\u027a")
        buf.write("\u027d\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2")
        buf.write("\u027c\u0280\3\2\2\2\u027d\u027b\3\2\2\2\u027e\u0280\7")
        buf.write("\62\2\2\u027f\u0277\3\2\2\2\u027f\u027e\3\2\2\2\u0280")
        buf.write("\u008e\3\2\2\2\u0281\u0282\5\u0089E\2\u0282\u0284\5\u008b")
        buf.write("F\2\u0283\u0285\5\u008dG\2\u0284\u0283\3\2\2\2\u0284\u0285")
        buf.write("\3\2\2\2\u0285\u028d\3\2\2\2\u0286\u0287\5\u008bF\2\u0287")
        buf.write("\u0288\5\u008dG\2\u0288\u028d\3\2\2\2\u0289\u028a\5\u0089")
        buf.write("E\2\u028a\u028b\5\u008dG\2\u028b\u028d\3\2\2\2\u028c\u0281")
        buf.write("\3\2\2\2\u028c\u0286\3\2\2\2\u028c\u0289\3\2\2\2\u028d")
        buf.write("\u028e\3\2\2\2\u028e\u028f\bH\5\2\u028f\u0090\3\2\2\2")
        buf.write("\u0290\u0298\7$\2\2\u0291\u0297\n\20\2\2\u0292\u0293\7")
        buf.write("^\2\2\u0293\u0297\t\21\2\2\u0294\u0295\t\22\2\2\u0295")
        buf.write("\u0297\t\23\2\2\u0296\u0291\3\2\2\2\u0296\u0292\3\2\2")
        buf.write("\2\u0296\u0294\3\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296")
        buf.write("\3\2\2\2\u0298\u0299\3\2\2\2\u0299\u029b\3\2\2\2\u029a")
        buf.write("\u0298\3\2\2\2\u029b\u029c\7$\2\2\u029c\u029d\bI\6\2\u029d")
        buf.write("\u0092\3\2\2\2\u029e\u02a0\t\24\2\2\u029f\u029e\3\2\2")
        buf.write("\2\u02a0\u02a1\3\2\2\2\u02a1\u029f\3\2\2\2\u02a1\u02a2")
        buf.write("\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\u02a4\bJ\2\2\u02a4")
        buf.write("\u0094\3\2\2\2\u02a5\u02a6\13\2\2\2\u02a6\u02a7\bK\7\2")
        buf.write("\u02a7\u0096\3\2\2\2\u02a8\u02b0\7$\2\2\u02a9\u02af\n")
        buf.write("\20\2\2\u02aa\u02ab\7^\2\2\u02ab\u02af\t\21\2\2\u02ac")
        buf.write("\u02ad\t\22\2\2\u02ad\u02af\t\23\2\2\u02ae\u02a9\3\2\2")
        buf.write("\2\u02ae\u02aa\3\2\2\2\u02ae\u02ac\3\2\2\2\u02af\u02b2")
        buf.write("\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b0\u02b1\3\2\2\2\u02b1")
        buf.write("\u02b6\3\2\2\2\u02b2\u02b0\3\2\2\2\u02b3\u02b4\7^\2\2")
        buf.write("\u02b4\u02b7\n\25\2\2\u02b5\u02b7\7^\2\2\u02b6\u02b3\3")
        buf.write("\2\2\2\u02b6\u02b5\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02b9")
        buf.write("\bL\b\2\u02b9\u0098\3\2\2\2\u02ba\u02c2\7$\2\2\u02bb\u02c1")
        buf.write("\n\20\2\2\u02bc\u02bd\7^\2\2\u02bd\u02c1\t\21\2\2\u02be")
        buf.write("\u02bf\t\22\2\2\u02bf\u02c1\t\23\2\2\u02c0\u02bb\3\2\2")
        buf.write("\2\u02c0\u02bc\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1\u02c4")
        buf.write("\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3")
        buf.write("\u02cf\3\2\2\2\u02c4\u02c2\3\2\2\2\u02c5\u02d0\t\26\2")
        buf.write("\2\u02c6\u02c8\t\27\2\2\u02c7\u02c6\3\2\2\2\u02c7\u02c8")
        buf.write("\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02d0\7\2\2\3\u02ca")
        buf.write("\u02cb\t\22\2\2\u02cb\u02cd\t\23\2\2\u02cc\u02ce\t\30")
        buf.write("\2\2\u02cd\u02cc\3\2\2\2\u02ce\u02d0\3\2\2\2\u02cf\u02c5")
        buf.write("\3\2\2\2\u02cf\u02c7\3\2\2\2\u02cf\u02ca\3\2\2\2\u02d0")
        buf.write("\u02d1\3\2\2\2\u02d1\u02d2\bM\t\2\u02d2\u009a\3\2\2\2")
        buf.write("C\2\u009d\u0133\u013a\u0142\u0195\u0199\u019e\u01a2\u01a6")
        buf.write("\u01ae\u01b2\u01b7\u01bb\u01c3\u01c7\u01cc\u01d0\u01d4")
        buf.write("\u01db\u01df\u01e4\u01e8\u01f1\u01f5\u01fa\u01fe\u0202")
        buf.write("\u020a\u020e\u0213\u0217\u021e\u0222\u0227\u022b\u022f")
        buf.write("\u0235\u0239\u023e\u0242\u0249\u0251\u0259\u025d\u0262")
        buf.write("\u0266\u026a\u0270\u0275\u027b\u027f\u0284\u028c\u0296")
        buf.write("\u0298\u02a1\u02ae\u02b0\u02b6\u02c0\u02c2\u02c7\u02cd")
        buf.write("\u02cf\n\b\2\2\3C\2\3D\3\3H\4\3I\5\3K\6\3L\7\3M\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    FOREACH = 7
    TRUE = 8
    FALSE = 9
    ARRAY = 10
    IN = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    RETURN = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    SELF = 21
    CONSTRUCTOR = 22
    DESTRUCTOR = 23
    NEW = 24
    BY = 25
    ID = 26
    DOLLARID = 27
    COMMENT = 28
    ADDOP = 29
    SUBOP = 30
    MULOP = 31
    DIVOP = 32
    MODOP = 33
    NOTOP = 34
    ANDOP = 35
    OROP = 36
    EQUOP = 37
    ASSIOP = 38
    NEOP = 39
    LTOP = 40
    LTEOP = 41
    GTOP = 42
    GTEOP = 43
    DOUEQUODOTOP = 44
    ADDDOTOP = 45
    DOUCOLON = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    DOT = 51
    DOUDOT = 52
    COLON = 53
    COMMA = 54
    SEMI = 55
    LP = 56
    RP = 57
    ARRAYSIZE = 58
    INTLIT = 59
    FLOATLIT = 60
    STRINGLIT = 61
    WS = 62
    ERROR_CHAR = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Self'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", 
            "'+.'", "'::'", "'('", "')'", "'['", "']'", "'.'", "'..'", "':'", 
            "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
            "DESTRUCTOR", "NEW", "BY", "ID", "DOLLARID", "COMMENT", "ADDOP", 
            "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", "ANDOP", "OROP", 
            "EQUOP", "ASSIOP", "NEOP", "LTOP", "LTEOP", "GTOP", "GTEOP", 
            "DOUEQUODOTOP", "ADDDOTOP", "DOUCOLON", "LB", "RB", "LSB", "RSB", 
            "DOT", "DOUDOT", "COLON", "COMMA", "SEMI", "LP", "RP", "ARRAYSIZE", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "BOOLLIT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
                  "ID", "DOLLARID", "COMMENT", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "NOTOP", "ANDOP", "OROP", "EQUOP", "ASSIOP", 
                  "NEOP", "LTOP", "LTEOP", "GTOP", "GTEOP", "DOUEQUODOTOP", 
                  "ADDDOTOP", "DOUCOLON", "LB", "RB", "LSB", "RSB", "DOT", 
                  "DOUDOT", "COLON", "COMMA", "SEMI", "LP", "RP", "HEXADECIMAL", 
                  "HEXNOTNULL", "OCTAL", "OCTNOTNULL", "BINARY", "BINNOTNULL", 
                  "DECIMAL", "DECNOTNULL", "ARRAYSIZE", "INTLIT", "INTPART", 
                  "DECPART", "EXPPART", "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[65] = self.ARRAYSIZE_action 
            actions[66] = self.INTLIT_action 
            actions[70] = self.FLOATLIT_action 
            actions[71] = self.STRINGLIT_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ARRAYSIZE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                        self.text = self.text[1:-1]
                    
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                        raise ErrorToken(self.text) 
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                        raise IllegalEscape(self.text[1:])
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                        if self.text[-1] in ['\n', '\r']:
                            raise UncloseString(self.text[1:-1])
                        raise UncloseString(self.text[1:])
                    
     


