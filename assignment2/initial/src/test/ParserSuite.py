import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test0(self):
        input = """
            Class Dog: Animal { }
            Class Snake: De { }
            Class butterfly {
                __str__() {
                    Var a, b, c, d, e: Int = 0,0,0,0,0;
                    Val a,b,c,d,$e: Int;
                }
            }
            """
        expect = "Error on line 7 col 32: $e"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test1(self):
        input = """
            Class Dog: Animal {
                $gaugau() {
                    a = b[7][2];
                }
            }
            Class Snake: De {
                $OpOp() {
                    Return Self.Op;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test2(self):
        input = """
            Class Program {
                getName() {
                    Var b: Float = 0.3;
                }
                main() {
                    Var a: Int;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test3(self):
        input = """
            Class A {
                getName() {
                    Var b: Float = 0.3;
                }
                func() {
                    If (a >= b) {
                        Var a: Int = 0;
                        a = a + 3;
                    }
                    Elseif (b >= c) {
                        Self.getName(a >= b);
                    }
                    Elseif (12 >= g) {
                        Self.insert("String");
                    }
                    Else {
                        GiaBao = Hieu;
                        Hung = Vi;
                    }
                }

                setAge(age: Int) {
                    Self.age = age;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test4(self):
        input = """ 
            Class MeowMeow: Dog {
                Var b: Int;
                Var $a, c, d: Float = .e4, 2., 78.9;
                Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test5(self):
        input = """
            Class mini {
                loop(a: Int; b: Float) {
                    Foreach (i In 0 .. 150 By i <= 8) {
                        sum = sum + a[i];
                    }
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test6(self):
        input = """
            Class Pro {
                Main(a: Int; b: Int) {
                    Return a || b < c.get(1,2) && 23 + 1.4;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test7(self):
        input = """
            Class Pro {
                MainMenu(a: Int; b: Int) {
                    Self.arr[4] = b.getName() + a.exp();
                }
            }
            Class ProMax {
                iPhone13(){
                    Return 40000000;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test8(self):
        input = """
                Class MyClass {
                    Var name: String;
                    Var age: Int = 0;
                    $printName() {
                        Out.print(Self.name);
                    }
                    setAge(_age: Int) {
                        Self.age = _age;
                    }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test9(self):
        input = """
            Class $Dog {
                Var $d: Int = 0x12345;
                foo() {
                    func(a,b,c);
                    Return result;
                }
            }
            Class Program {
                main(){

                }
            }
        """
        expect = "Error on line 2 col 18: $Dog"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test10(self):
        input = """
            Class super {
                get(){

                }
            }
            Class child: super {
                set() {
                    Return super::get();
                }
            }
        """
        expect = "Error on line 9 col 34: get"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test11(self):
        input = """
            Class myClass {
                method() {
                    Foreach (i In 0 .. 100 By e <= i) {
                        a[1][2] = a[1][1] + b[1][3][i];
                    }
                    Return a <= b;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test12(self):
        input = """
            Class ari {
                $_getMethod() {
                    Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
                }
            }
            Class Program {
                main() {
                    a = (myConst + b) && a + b + abcde;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        input = """
            Class myDog {
                method(a: Array[Int, 4]) {
                    Return a[0]
                }
            }
        """
        expect = "Error on line 5 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        input = """
            Class myVar {
                Constructor(arr: Array[Float, 3]) {
                    Self.a = arr[1];
                    Self.b = arr[2];
                    Self.c = arr[2][1];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        input = """
            Class Program {
                main(){

                }
            }
            Class Des {
                Destructor() {
                    Stand.Delete().All(0);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self):
        input = """
            Class Main {
                menu() {
                    t = R::$test()[2] >= 8;
                    Return Self.arr;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        input = """
            Class Program {
                dethod() {
                    Return Self.method();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """
            Class Meow {
                returnMethod() {

                }
                Constructor() {
                    Self.init = value;
                }
                Destructor() {
                    Mew.EraseAll();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        input = """
            Class foo {
                Var Foo: Array[Int, -5] = 0xFF;
            }
        """
        expect = "Error on line 3 col 36: -"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        input = """
            Class ari {
                Constructor(a, b : Int)
                {
                    Out.print("Contructor");
                }
                Destructor()
                {
                    Out.print("Destructor");
                }
                $_getMethod() {
                    Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
                }
            }
            Class Program {
                Constructor(a, b : Int)
                {
                    Out.print("Contructor");
                }
                Destructor()
                {
                    Out.print("Destructor");
                }
                main() {
                    a = (myConst + b) && a + b + abcde;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test21(self):
        input = """
            Class Program {
                main() {
                    Out.print("Hello From Main");
                }
            }
            Class iden {

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        input = """
            Class myFunc {
                func(s: Int; r: String) {
                    Return Stand.Str(s + r);
                }
            }
            Class Program {
                main() {

                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        input = """
            Class Program {
                main(){}
            }

            Class class1 {
                Var name: String;
            }
            Class class2 {
                Val $height: Float = 1.75;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test24(self):
        input = """
            Class obj {
                Var _obj: Int = 0, 9;
            }
            Class Program {
                main() {
                    func(Array("a", "b", "c"));
                    Return Self.arr;
                }
            }
        """
        expect = "Error on line 3 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test25(self):
        input = """
            Class Program {
                main() {
                    Var a,b: Array[Float, 4.5];
                }
            }
            Class lop {
                attr(a, b: Int) {
                    Return a[4] != b[1].name;
                }
            }
        """
        expect = "Error on line 4 col 42: 4.5"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test26(self):
        input = """
            Class parent {
                Var lname, fname: String = "";
                $getName() {
                    Return Self.name[2];
                }
                setName(name: Int) {
                    lname = name[0];
                }
            }
        """
        expect = "Error on line 3 col 45: ;"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test27(self):
        input = """
            Class Program {
                main() {
                    Return New object();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        input = """
            Class Program {
                main(a: Int; b: Float) {
                    Return New A().B().C();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """
            Class Func {
                Constructor(){Return name;}
            }
            Class B {
                Return statements;
            }
        """
        expect = "Error on line 6 col 16: Return"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class className {
                Destructor(param: Int, param_2: String) {

                }
            }
        """
        expect = "Error on line 8 col 27: param"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test31(self):
        input = """
            Class Dog {
                Var name: Int;
                Var age: Int = 2, 6, 4;
            }
            Class Program {
                main() {

                }
            }
        """
        expect = "Error on line 4 col 32: ,"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test32(self):
        input = """
            Class Program {
                main() {
                    Foreach (idx In 1 .. 100 + 5 By a[i] >= 9) {
                        If (a[i][1] != b[1]) {
                            Return;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test33(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class Another {
                function() {
                    A.Main()::$dollar();
                }
            }
        """
        expect = "Error on line 9 col 28: ::"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test34(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class Name {
                hello(s1, s2, s3: String) {
                    Return Str.concat(s1, s2, s3);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test35(self):
        input = """
            Class Program {
                main() {
                    Out.print(Dog.sound());
                }
            }
            Class Dog {
                sound() {
                    Return New Animal().dogSound();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        input = """
            Class Program {
                Var a: Int = 0;
                main() {
                    a = New obj("string 1");
                    Out.print(a.age);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class Method {
                newMethod(a: String) {
                    Return "This is a \\nstring"[1].getText();
                }
            }
        """
        expect = "Error on line 9 col 50: ."
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = """
            Class Program {
                Var a, b, c: Int = 1, 2, 3 >= 9 + 5;
                main() {
                    If (a >= b) {
                        Foreach (i In 0 .. c[5][3].length By 1) {
                            If (c[i]) {
                                Continue;
                            }
                            Else {
                                Break;
                            }
                        }
                    }
                }
            }
        """
        expect = "Error on line 6 col 50: ."
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class newClass {
                Val count: Int = 150;
                Val sum, rate: Float = 10.2, 34.4;
                PrintOut() {
                    Return Self.count * Self.rate;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """
            Class Program {
                main() {
                    Stand.getVector();
                }
            }
            Class myClass {
                $method() {
                    Return Self.sound()[2];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test41(self):
        input = """
            Class class {
                Var a, b, c: Int = 3, 4, 5;
                $print() {
                    Return Array(a,b,c);
                }
            }
            Class Program {
                main() {

                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class Par {
                Var con: String;
                Var me: Float = 0.2;
                $get() {
                    Local.Store.sieuthi();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """
            Class Program {
                main() {

                }
            }
            Out.print(a, b, 3);
        """
        expect = "Error on line 7 col 12: Out"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """
            Class Program {
                main() {
                    If (a == b) {
                        Foreach (i In 1 .. len By 2) {
                            Continue;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """
            Class Program {
                main() {
                    Dog.name = Cat.name +. "1";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class Meo: Dog {
                $get() {
                    Self.name = Dog::name;
                }
            }
        """
        expect = "Error on line 9 col 37: name"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """
            If (a >= b) {
                Return Program;
            }
            Class Program {
                main() {

                }
            }
            Class Buffalo: $Animals {
                Dog.scopeMethod();
            }
        """
        expect = "Error on line 2 col 12: If"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """
            Class Program {
                main() {

                }
            }
            Foreach (i In 0 .. 10 By 1 + 2 + 3 + a.get - b.name) {
                Continue;
                Break;
            }
        """
        expect = "Error on line 7 col 12: Foreach"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class A {
                Return New B(A);
            }
        """
        expect = "Error on line 8 col 16: Return"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class B: A {
                Var a, b: Float = 3.5, 5;
                Return a;
            }
        """
        expect = "Error on line 9 col 16: Return"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test51(self):
        input = """
            Class Program {
                main() {

                }

                func(){
                    test();
                    test().a().b().c().d();

                    test()::a()::b()::c()::d();
                } 
            }
            
        """
        expect = "Error on line 8 col 24: ("
        self.assertTrue(TestParser.test(input, expect, 251))

    def test52(self):
        input = """
            Class Main {
                If (a<=b)
                Else Return
            }
        """
        expect = "Error on line 3 col 16: If"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        input = """
            Self.age = 2;
        """
        expect = "Error on line 2 col 12: Self"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test54(self):
        input = """
            Class V {
                Val arr = Array[Array[Int, 0b1], 0xAF];
            }
        """
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class B {$method(){}}
            Class C {$method(){}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        input = """
            Class Program {
                main() {PPL() {}}
                Var method(): Int;
            }
        """
        expect = "Error on line 3 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        input = """
            Class B: A, T {
                Var b: Int = 0;
            }
        """
        expect = "Error on line 2 col 22: ,"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        input = """
            Class B {
                Var b, c : Int = 10.42;
            }
        """
        expect = "Error on line 3 col 38: ;"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        input = """
            Class i {
                method() {
                    a = Self.age + 34 - 9 * B.getString();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        input = """
            Class Program {
                main() {
                    a[0] = "String 1" ==. "string \\'";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test61(self):
        input = """
            Class B {
                B.call();
            }
        """
        expect = "Error on line 3 col 17: ."
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        input = """
            Class Program {
                Constructor(a, b: Float; c: Int) {
                    a = c + 1;
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test63(self):
        input = """
            Class Construc {
                Destruc() {
                    Des.DeleteAll();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test64(self):
        input = """
            Class C {
                Var a: Int = func();
                Val constVar: String = "Hello";
                Val a,b,c: Int = 0.9, 1.0;
            }
        """
        expect = "Error on line 3 col 33: ("
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        input = """
            Class Program {
                main() {
                    func_declare() {
                        Return main().text();
                    }
                }
            }
        """
        expect = "Error on line 4 col 32: ("
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        input = """
            Class Program {
                Var b: Int = A::$f()[1] + a.g() * 4 + !y;
                Var a: Stu = New Teach(New Stu());
                Var d: Boolean = 4 >= f && t <= 2 || 7 == !b + 3;
            }
        """
        expect = "Error on line 5 col 45: <="
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        input = """
            Class method {
                $getName() {
                    Out.print(B.$name);
                    Return C.get;
                }
            }
        """
        expect = "Error on line 4 col 32: $name"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """
            Class Method: Param {
                m() {
                    a = T::$get() + New X().G() - A.b().f().t();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test69(self):
        input = """
            Class Program {
                main() {
                    a[1][2][3][4] = b[4][3].c(d[1]);
                }
                method () { }
            }
        """
        expect = "Error on line 4 col 43: ."
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3] + className.b()[4];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test71(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class B {
                Constructor(a,b,c: Int) {
                    Return Self.a + b + 4;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test72(self):
        input = """
            Class Program {
                main() {
                    Var $g: Int;
                }
            }
        """
        expect = "Error on line 4 col 24: $g"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test73(self):
        input = """
            Class A {
                method() {
                    Var a, b, $c: Float = 1.0, 2.3;
                }
            }
        """
        expect = "Error on line 4 col 30: $c"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test74(self):
        input = """
            Class _R {
                Val $y: Int = 12;
                _F() {
                    Val _, _, _: String = 3, 4, 5;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test75(self):
        input = """
            Class Program {
                main() {
                    Out.ar() {
                        Return New ClassName();
                    }
                }
            }
        """
        expect = "Error on line 4 col 29: {"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test76(self):
        input = """
            Class Program {
                Var stu: Stu = New Stu();
                mainStu() {
                    Stu[1] = FUNC.stu().stu1().stu2()[5];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test77(self):
        input = """
            Class myArray {
                Var Arr: Array[Array[Int, 2], 0b0];
            }
        """
        expect = "Error on line 3 col 46: 0b0"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test78(self):
        input = """
            Class myArray {
                Var Arr: Array[Int, 3] = Array(
                                            Array(3,4,5),
                                            Array(1,2)
                                        );
                Method() {
                    Out.print(Arr[1][2]);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test79(self):
        input = """
            Class Name {
                Continue;
                Break;
                Return;
            }
        """
        expect = "Error on line 3 col 16: Continue"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test80(self):
        input = """
            Class Program {
                main() {
                    Foreach(a[0] In 0+4 .. b <= c By get().count) {
                        Break;
                    }
                }
            }
        """
        expect = "Error on line 4 col 29: ["
        self.assertTrue(TestParser.test(input, expect, 280))

    def test81(self):
        input = """
            Class dfskjf_jdss {
                Rfsfsa() {
                    Val $r: Int = 20;
                }
            }
        """
        expect = "Error on line 4 col 24: $r"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test82(self):
        input = """
            Class D96 {
                Construc() {
                    Val arr: Array[Array[Array[Float, 00],0x3_23],4];
                }
            }
        """
        expect = "Error on line 4 col 54: 00"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test83(self):
        input = """
            Class Soc {
                
                function() {
                    Return A::$name() + t();
                }
            }
        """
        expect = "Error on line 5 col 41: ("
        self.assertTrue(TestParser.test(input, expect, 283))
    
    def test84(self):
        input = """
            Class test {
                Var t, y: Int = 1, 2;
                method(a,b,c:Int; r:Func) {
                    If (a + b > 0) {
                        Foreach(i In 1 .. 12 By r) {
                            If (2 + 5) {
                                If (f >= t) {
                                    Continue;
                                }
                            }
                        }
                    }
                    Elseif (t * 7) {
                        If (34) { }
                        Else { Return; }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test85(self):
        input = """
            Class name {
                method () {
                    a = name::$age;
                    b = name::$age().b();
                    c = age;
                    d = age();
                }
            }
        """
        expect = "Error on line 7 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 285))

    def test86(self):
        input = """
            Class MyClass {
                Var $a: Int = 0; ## This is comment ##
                Method () {
                    Self.constructor(a,b,c);
                    name.method();
                    If (r) {
                        Return t; ##This is also a comment##
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test87(self):
        input = """
            Class name {
                method () {
                    a = name::$age;
                    c = age;
                    e = $age();
                }
            }
        """
        expect = "Error on line 6 col 24: $age"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test88(self):
        input = """
            Class MyClass {
                Val count: Int = 0;
                setCount() {
                    Return Self.count + Self.count() - name::$turn() * age.$Age();
                }
            }
        """
        expect = "Error on line 5 col 75: $Age"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test89(self):
        input = """
            Class InLit: Type {
                __str__(str: String) {
                    Self.str = str;
                    Self.a = Self.count() + expr.$dollar();
                }
            }
        """
        expect = "Error on line 5 col 49: $dollar"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test90(self):
        input = """
            Class Note {
                m() {
                    a = name[0].length;
                    b = age.len[1][2];
                    c = age::$Len().t()[2];
                }
            }
        """
        expect = "Error on line 4 col 31: ."
        self.assertTrue(TestParser.test(input, expect, 290))

    def test91(self):
        input = """
            Class Test{
            Var ins: Int;
            Var $static: Int;
            
            Test(){
                Var a: Int= Self::ins;
                Var b: Int= Self::$static;
            }
            }
        """
        expect = "Error on line 7 col 32: ::"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test92(self):
        input = """
            Class B {
                Val b: Int = 0;
                Val a: Float = Self.a.b.c().t[1];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test93(self):
        input = """
            Class Program {
                main() {
                    Return ClassName::a::b::c.d;
                }
            }
        """
        expect = "Error on line 4 col 38: a"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test94(self):
        input = """
            Class Program {
                main() {
                    b = Main::$get()[1];
                    a = Main[0][1][2].get();
                }
            }
        """
        expect = "Error on line 5 col 37: ."
        self.assertTrue(TestParser.test(input, expect, 294))

    def test95(self):
        input = """
            Class myClass {
                Val a: Int = Main.a.get();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test96(self):
        input = """
            Class ReString {
                Var string: Student = New ReString("Bao");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test97(self):
        input = """
            Class myClass {
                _method() {
                    Name.a[1][2] = Self.get().set.get();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test98(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class A: B {
                Val c: C = New C();
            }
            Class C {
                Var b: A;
                c__ount__() {
                    Return C::$name + C.getName().str[2];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        input = """
            Class Program {
                $method() {
                    Foreach(i In -3 .. -1 By -100) {
                        Foreach(j In 0 .. -0xFF By 0b1) {
                            Var a: Float = 0.2;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test100(self):
        input = """Class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 300))

    def test101(self):
        input = """
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                $getNumOfShape() {
                    Return $numOfShape;
                }
            }
        """
        expect = "Error on line 7 col 27: $numOfShape"
        self.assertTrue(TestParser.test(input, expect, 301))

    def test102(self):
        input = """ 
            Class Program {
                main() {
                    Foreach (x In 5 .. 2) {
                        Out.printInt(arr[x]);
                    }
                } 
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 302))

    def test103(self):
        input = """ 
            Class Program {
                main() {
                    Foreach (x In 5 .. 2) {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                        Shape::$getNumOfShape();
                    }
                } 
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 303))
        
    def test104(self):
        input = """ 
            Class Program {
                main() {
                    If (x > 5) {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                        Shape::$getNumOfShape();
                    }
                    Else {

                    }
                    Elseif {

                    }
                } 
            }
        """
        expect = "Error on line 15 col 20: Elseif"
        self.assertTrue(TestParser.test(input, expect, 304))

    def test105(self):
        input = """ 
            Class Program {
                main() {
                    If (x > 5) {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                        Shape::$getNumOfShape();
                    }
                    Elseif (a == 10) {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                        Shape::$getNumOfShape();   
                    }
                    Elseif (1 + 2) {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                        Shape::$getNumOfShape();   
                    }
                    Else {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                    }
                } 
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 305))

    def test106(self):
        input = """ 
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
                $getNumOfShape() {

                }
            }
            Class Rectangle: Shape {
                getArea() {
                    Return Self.length * Self.width;
                }
            }
            Class Program {
                main() {
                    Out.printInt(Shape::$numOfShape);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 306))

    def test107(self):
        input = """ 
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
                $getNumOfShape() {

                }
            }
            Class Rectangle: Shape {
                getArea() {
                    Foreach (x In 5 .. 2) {
                        Var a: Array[Int, 3] = Array(1,2,3);
                        If(x > 2){
                            Out.printInt(a[0]);
                        }
                        Elseif(x == 2){
                            Out.printInt(a[1]);
                        }
                        Else{
                            Out.printInt(a[2]);
                        }
                    }
                }
            }
            Class Program {
                main() {
                    If(x > 2){
                        Out.printInt(a[0]);
                    }
                    Elseif(x == 2){
                        Out.printInt(a[1]);
                        Break;
                    }
                    Elseif(x == 3){
                        Continue;
                    }
                    Elseif(x == 4){
                        Return;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 307))