import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 201))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("Break", "Break,<EOF>", 202))

    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("ab?svn", "ab,Error Token ?", 203))

    def test_integer(self):
        self.assertTrue(TestLexer.test("Return x;", "Return,x,;,<EOF>", 204))    

    def test_lowercase_identifier1(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def"  ""","Illegal Escape In String: abc\h", 205))

    def test_lower_upper_id1(self):
        self.assertTrue(TestLexer.test(""" "abc def  """, "Unclosed String: abc def  ", 206))

    def test1(self):
        self.assertTrue(TestLexer.test("\"String with ##Comment## inside\"", "String with ##Comment## inside,<EOF>", 207))

    def test2(self):
        self.assertTrue(TestLexer.test(""" 001 """, """00,1,<EOF>""", 208))

    def test3(self):
        self.assertTrue(TestLexer.test("12_34.276e+0012 0b1_010_121abc 0X_121AF", "1234.276e+0,012,0b10101,21,abc,0,X_121AF,<EOF>", 209))

    def test4(self):
        self.assertTrue(TestLexer.test(""" "Bob talk: \\"Hi, I'm Bop.\\" " ""","Illegal Escape In String: Bob talk: \\", 210))

    def test5(self):
        self.assertTrue(TestLexer.test("012", "012,<EOF>", 211))

    def test6(self):
        self.assertTrue(TestLexer.test("0x123", "0x123,<EOF>", 212))

    def test7(self):
        self.assertTrue(TestLexer.test("0b01011", "0b0,1011,<EOF>", 213))

    def test8(self):
        self.assertTrue(TestLexer.test("12", "12,<EOF>", 214))

    def test9(self):
        self.assertTrue(TestLexer.test("0X123_456_789", "0X123456789,<EOF>", 215))

    def test10(self):
        self.assertTrue(TestLexer.test("123_", "123,_,<EOF>", 216))

    def test11(self):
        self.assertTrue(TestLexer.test("123_456_789", "123456789,<EOF>", 217))

    def test12(self):
        self.assertTrue(TestLexer.test("12__34", "12,__34,<EOF>", 218))

    def test13(self):
        self.assertTrue(TestLexer.test("0_b010", "0,_b010,<EOF>", 219))

    def test14(self):
        self.assertTrue(TestLexer.test("0X0123AF", "0X0,123,AF,<EOF>", 220))

    def test15(self):
        self.assertTrue(TestLexer.test("0.12", "0.12,<EOF>", 221))

    def test16(self):
        self.assertTrue(TestLexer.test("1_23.4e-5", "123.4e-5,<EOF>", 222))

    def test17(self):
        self.assertTrue(TestLexer.test("0.", "0.,<EOF>", 223))

    def test18(self):
        self.assertTrue(TestLexer.test("1_.4e-5", "1,_,.4e-5,<EOF>", 224))

    def test19(self):
        self.assertTrue(TestLexer.test("2e-12", "2e-12,<EOF>", 225))

    def test20(self):
        self.assertTrue(TestLexer.test("1.23E+98", "1.23E+98,<EOF>", 226))

    def test21(self):
        self.assertTrue(TestLexer.test("012.34e+56", "012,.34e+56,<EOF>", 227))

    def test22(self):
        self.assertTrue(TestLexer.test("123__456e78", "123,__456e78,<EOF>", 228))

    def test23(self):
        self.assertTrue(TestLexer.test("12e-0.34", "12e-0,.,34,<EOF>", 229))

    def test_24(self):
        self.assertTrue(TestLexer.test("12.e34-5", "12.e34,-,5,<EOF>", 230))

    def test_25(self):
        self.assertTrue(TestLexer.test("##Comment##", "<EOF>", 231))

    def test26(self):
        self.assertTrue(TestLexer.test("##Comment \n with \n multiple \n line##", "<EOF>", 232))

    def test27(self):
        self.assertTrue(TestLexer.test("##Comment \b with \f escape \r!##", "<EOF>", 233))

    def test28(self):
        self.assertTrue(TestLexer.test("##Cmt##Unterminated Comment##", "Unterminated,Comment,Error Token #", 234))

    def test29(self):
        self.assertTrue(TestLexer.test("##A Comment to be ignored##Outside of comment", "Outside,of,comment,<EOF>", 235))

    def test30(self):
        self.assertTrue(TestLexer.test("###", "Error Token #", 236))

    def test31(self):
        self.assertTrue(TestLexer.test("##Comment with some special characters !@#$%^&*()##", "<EOF>", 237))

    def test32(self):
        self.assertTrue(TestLexer.test("##Comment \n with \b escape \r char \f \\ \t##", "<EOF>", 238))

    def test33(self):
        self.assertTrue(TestLexer.test("##Comment with illegal escape char \h \g \e##", "<EOF>", 239))

    def test34(self):
        self.assertTrue(TestLexer.test("##Comment with separators []{}()|\;:'\",./?<>##", "<EOF>", 240))

    def test35(self):
        self.assertTrue(TestLexer.test("\"Hello World!\"","Hello World!,<EOF>", 241))

    def test36(self):
        self.assertTrue(TestLexer.test("\"String with \\n newline\"", "String with \\n newline,<EOF>", 242))

    def test37(self):
        self.assertTrue(TestLexer.test("\"String with double quote \'\" inside\"", "String with double quote \'\" inside,<EOF>", 243))

    def test38(self):
        self.assertTrue(TestLexer.test("\"Test unclosed string", "Unclosed String: Test unclosed string", 244))

    def test39(self):
        self.assertTrue(TestLexer.test("\"Test unclosed string with \n newline", "Unclosed String: Test unclosed string with ", 245))   

    def test40(self):
        self.assertTrue(TestLexer.test("\"Test string with \\illegal escape", "Illegal Escape In String: Test string with \\i", 246))   

    def test41(self):
        self.assertTrue(TestLexer.test("\"String with \\\\ backlash\"", "String with \\\\ backlash,<EOF>", 247))

    def test42(self):
        self.assertTrue(TestLexer.test("\"He ask me: \'\"Where is John?\'\".\"", "He ask me: \'\"Where is John?\'\".,<EOF>", 248))

    def test42(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \t\"", "This is a string containing tab \t,<EOF>", 249))

    def test43(self): 
        self.assertTrue(TestLexer.test(""" "ABC: \\" """, "Illegal Escape In String: ABC: \\" , 250))

    def test44(self):
        self.assertTrue(TestLexer.test("_var", "_var,<EOF>", 251))

    def test45(self):
        self.assertTrue(TestLexer.test("___var", "___var,<EOF>", 252))

    def test46(self):
        self.assertTrue(TestLexer.test("_Abc123_45_67e8", "_Abc123_45_67e8,<EOF>", 253))

    def test47(self):
        self.assertTrue(TestLexer.test("Uppercase", "Uppercase,<EOF>", 254))

    def test48(self):
        self.assertTrue(TestLexer.test("lowercase", "lowercase,<EOF>", 255))

    def test49(self):
        self.assertTrue(TestLexer.test("lOwErUpPeR", "lOwErUpPeR,<EOF>", 256))

    def test50(self):
        self.assertTrue(TestLexer.test("m1x3d_", "m1x3d_,<EOF>", 257))

    def test51(self):
        self.assertTrue(TestLexer.test("$mIx3d_", "$mIx3d_,<EOF>", 258))

    def test52(self):
        self.assertTrue(TestLexer.test("$Uppercase", "$Uppercase,<EOF>", 259))

    def test53(self):
        self.assertTrue(TestLexer.test("$lowercase", "$lowercase,<EOF>", 260))

    def test54(self):
        self.assertTrue(TestLexer.test("$_St_vr_34.e6", "$_St_vr_34,.e6,<EOF>", 261))

    def test55(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 262))

    def test56(self):
        self.assertTrue(TestLexer.test("$123ID_234.5e-12xinchao", "$123ID_234,.5e-12,xinchao,<EOF>", 263))

    def test57(self):
        self.assertTrue(TestLexer.test("Class A: Int {##Statements##}", "Class,A,:,Int,{,},<EOF>", 264))

    def test58(self):
        self.assertTrue(TestLexer.test("Var a, b, c : Int", "Var,a,,,b,,,c,:,Int,<EOF>", 265))

    def test59(self):
        self.assertTrue(TestLexer.test("Multiple \n lines \r testcase", "Multiple,lines,testcase,<EOF>", 266))

    def test60(self):
        self.assertTrue(TestLexer.test("0b1234abc 0x17ABCDEFGH", "0b1,234,abc,0x17ABCDEF,GH,<EOF>", 267))

    def test61(self):
        self.assertTrue(TestLexer.test(".12abc0b10010X1234AFCD", ".,12,abc0b10010X1234AFCD,<EOF>", 268))

    def test62(self):
        self.assertTrue(TestLexer.test("5982u953uwrkjjre83", "5982,u953uwrkjjre83,<EOF>", 269))

    def test63(self):
        self.assertTrue(TestLexer.test("mttq;r45hello;l/", "mttq,;,r45hello,;,l,/,<EOF>", 270))

    def test64(self):
        self.assertTrue(TestLexer.test("0_123__456", "0,_123__456,<EOF>", 271))

    def test65(self):
        self.assertTrue(TestLexer.test("1.000005E10094Sp_43$trskd*we8sdjn}{;", "1.000005E10094,Sp_43,$trskd,*,we8sdjn,},{,;,<EOF>", 272))

    def test66(self):
        self.assertTrue(TestLexer.test("yt5O3]]m*E)DkY6*Skk@1u", "yt5O3,],],m,*,E,),DkY6,*,Skk,Error Token @", 273))

    def test67(self):
        self.assertTrue(TestLexer.test("## ??? Comment [%^*()] ##", "<EOF>", 274))

    def test68(self):
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 275))

    def test69(self):
        self.assertTrue(TestLexer.test("1000.00001E10000", "1000.00001E10000,<EOF>", 276))

    def test70(self):
        self.assertTrue(TestLexer.test("""Array(1, 5, 7, 12)""", """Array,(,1,,,5,,,7,,,12,),<EOF>""", 277))

    def test71(self):
        self.assertTrue(TestLexer.test("Array(\"Kangxi\", \"Yongzheng\", \"Qianlong\")",
                        "Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>", 278))

    def test72(self):
        self.assertTrue(TestLexer.test("Array(1, 5, 7, 12)", "Array,(,1,,,5,,,7,,,12,),<EOF>", 279))

    def test73(self):
        self.assertTrue(TestLexer.test("""Array (\nArray("Volvo", "22", "18"),\nArray("Saab", "5", "2")\n)""",
                        """Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),),<EOF>""", 280))

    def test74(self):
        self.assertTrue(TestLexer.test("1.1000E1_03", "1.1000E1,_03,<EOF>", 281))

    def test75(self):
        self.assertTrue(TestLexer.test("## This is a\nmulti-line\ncomment.\n##", "<EOF>", 282))

    def test76(self):
        self.assertTrue(TestLexer.test("Val My1stCons, My2ndCons: Int = 1 + 5, 2;\nVar $x, $y : Int = 0, 0;",
                        "Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,Var,$x,,,$y,:,Int,=,0,,,0,;,<EOF>", 283))

    def test77(self):
        self.assertTrue(TestLexer.test("Class Program {\n\tmain() {\n\t\tOut.printInt(Shape::$numOfShape);\n\t}\n}",
                        "Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>", 284))

    def test78(self):
        self.assertTrue(TestLexer.test("Destructor() {Delete _D96}", "Destructor,(,),{,Delete,_D96,},<EOF>", 285))

    def test79(self):
        self.assertTrue(TestLexer.test("123_456_789__56", "123456789,__56,<EOF>", 276))

    def test80(self):
        self.assertTrue(TestLexer.test("sydr^$%$#^%^^(*@1u", "sydr,Error Token ^", 287))

    def test81(self):
        self.assertTrue(TestLexer.test("Foreach (i In 1 .. 100 By 2) {Out.printInt(i);}", 
                        "Foreach,(,i,In,1,..,100,By,2,),{,Out,.,printInt,(,i,),;,},<EOF>", 288))

    def test82(self):
        self.assertTrue(TestLexer.test(".34E2 11 .44 1.e25 .E-45", ".34E2,11,.,44,1.e25,.E-45,<EOF>", 289))

    def test83(self):
        self.assertTrue(TestLexer.test("\"\\\\\"\"", "\\\\,Unclosed String: ", 290))

    def test84(self):
        self.assertTrue(TestLexer.test("123_45__678_1.09__12_1e-10", "12345,__678_1,.,0,9,__12_1e,-,10,<EOF>", 291))

    def test85(self):
        self.assertTrue(TestLexer.test(".....", "..,..,.,<EOF>", 292))

    def test86(self):
        self.assertTrue(TestLexer.test("\"String A\"+.\"String B\"", "String A,+.,String B,<EOF>", 293))

    def test87(self):
        self.assertTrue(TestLexer.test("Var a: Array[Int, 5];", "Var,a,:,Array,[,Int,,,5,],;,<EOF>", 294))

    def test88(self):
        self.assertTrue(TestLexer.test("0b10010___01101.e-12_34+35", "0b10010,___01101,.e-12,_34,+,35,<EOF>", 295))

    def test89(self):
        self.assertTrue(TestLexer.test("\"String with ##Comment## inside\"", "String with ##Comment## inside,<EOF>", 296))   

    def test90(self):
        self.assertTrue(TestLexer.test("<=<>>==", "<=,<,>,>=,=,<EOF>", 297))

    def test91(self):
        self.assertTrue(TestLexer.test("0X1_2AB_CF0_457_H3EF 0b10157h912A;", "0X12ABCF0457,_H3EF,0b101,57,h912A,;,<EOF>", 298))

    def test92(self):
        self.assertTrue(TestLexer.test("0X_123 0_X123 0_123 1____23", "0,X_123,0,_X123,0,_123,1,____23,<EOF>", 299))

    def test93(self):
        self.assertTrue(TestLexer.test("001", "00,1,<EOF>", 300))

    def test94(self):
        self.assertTrue(TestLexer.test("01457890X12F6", "01457,890,X12F6,<EOF>", 301))

    def test95(self):
        self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 302))

    def test96(self):
        self.assertTrue(TestLexer.test("12_34.276e+0012 0b1_010_121abc 0X_121AF", "1234.276e+0,012,0b10101,21,abc,0,X_121AF,<EOF>", 303))

    def test97(self):
        self.assertTrue(TestLexer.test("?abc", "Error Token ?", 304))

    def test98(self):
        self.assertTrue(TestLexer.test("\"Is this\\\\h illegal?\"", "Is this\\\\h illegal?,<EOF>", 305))

    def test99(self):
        self.assertTrue(TestLexer.test("\"String with single quote \'this is good\'\"", "Unclosed String: String with single quote \'this is good\'\"", 306))  

    def test100(self):
        self.assertTrue(TestLexer.test("\"String with 1 backlash\\\" \'is this error\'", "Illegal Escape In String: String with 1 backlash\\", 307))

    def test101(self):
        self.assertTrue(TestLexer.test("\"String\"##Comment##ID Int 123 0b0 0X012343 Var x, y, z = Int:1,2,3", 
                        "String,ID,Int,123,0b0,0X0,12343,Var,x,,,y,,,z,=,Int,:,1,,,2,,,3,<EOF>", 308))

    def test102(self):
        self.assertTrue(TestLexer.test("x=2^y+7-8/3+z==6", "x,=,2,Error Token ^", 309))

    def test103(self):
        self.assertTrue(TestLexer.test(""" "Check if there is any error with escape char \\b\\t\\r\\f\\n\\\\\\a\\r" """, 
                        "Illegal Escape In String: Check if there is any error with escape char \\b\\t\\r\\f\\n\\\\\\a", 310))

    def test104(self):
        self.assertTrue(TestLexer.test("\"The string:\\\"", "Illegal Escape In String: The string:\\", 311))

    def test105(self): 
        self.assertTrue(TestLexer.test(""" "The string: \\""", "Unclosed String: The string: \\", 312))

    def test106(self):
        self.assertTrue(TestLexer.test("""\"The string \\'";""", "The string \\',;,<EOF>", 313))