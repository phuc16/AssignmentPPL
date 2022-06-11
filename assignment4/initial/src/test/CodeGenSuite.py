import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test500(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("b"),
                                IntType(),
                                IntLiteral(1)
                            )
                        ),
                        AttributeDecl(
                            Static(),
                            VarDecl(
                                Id("$a"),
                                IntType(),
                                IntLiteral(1)
                            )
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([                            
                                VarDecl(
                                    Id("score"),
                                    IntType(),
                                    IntLiteral(1)
                                )
                            ])
                        )
                    ]
                )
            ]
        )
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_501(self):
        input = """Class Program {
            main() {
                io::$putIntLn(1);
            }
        }
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    def test_502(self):
        input = """
            Class A{
                Var x:Int = 11;
            }
            Class Program{
                Var y:Int = 1;

                main(){
                    Var a:A = New A();
                    io::$putInt(a.x);
                }
            }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_503(self):
        input = """Class Program {
            $factorial(n: Int) {
                If (n <= 1) {
                    Return "1";
                }
                Else {
                    Return "Program::$factorial(n - 1) * n";
                }
            }  
            main() {
                Var c: Int;
                io::$putStringLn(Program::$factorial(6));
            }
        }"""
        expect = str("Program::$factorial(n - 1) * n\n")
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_504(self):
        input = """Class Program {
            main() {
                Var x: Int;
                Foreach (x In 1 .. 15 By 2 * 2) {
                    io::$putInt(1);
                }
            }
        }"""
        expect = "1111"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_505(self):
        input = """Class Program {
            main() {
                Var a:Int = 11;
                io::$putIntLn(a);
            }
        }"""
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_506(self):
        input = """
            Class A{
                Var x:Int = 11;
            }
            Class Program{
                $sum(n: Int) {
                    Var a:A = New A();
                    Return a.x + 12.2/2  + n;             
                }

                main(){
                    io::$putFloat(Program::$sum(12));
                }
            }"""
        expect = "29.1"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_507(self):
        input = """
                Class Student
                {
                    Var name: String;
                    Var ID: Int;
                    Constructor(newName: String; newID : Int)
                    {
                        Self.name = newName;
                        Self.ID = newID;
                    }
                }
                Class Program
                {
                    main()
                    {
                        Var myStudent: Student = New Student("Phuc", 4720);
                        io::$putStringLn(myStudent.name);
                        io::$putInt(myStudent.ID);
                    }
                }
            """
        expect = "Phuc\n4720"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_508(self):
        input = """Class Program {
                Var x: Int = 11;
                abc(){
                    Self.x = 10;
                    io::$putInt(Self.x);
                }
                main() {
                    Var a: Program = New Program();
                    a.abc();
                }
            }"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_509(self):
        input = """Class Program {
                   $x(n: Int){
                       Return 11;
                   }
                    main() {
                        io::$putInt(Program::$x(6));
                    }
                }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_510(self):
        input = """Class Program {
                   $x(){
                       Return 11;
                   }
                    main() {
                        io::$putInt(Program::$x());
                    }
                }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_511(self):
        input = """
        Class A {
            print(a: Int) {
                Var b: Int;
                Foreach (b In 1 .. a) {
                    If (b > 4) { 
                        io::$putInt(b);
                    }
                }
            }
        }
        Class Program {
            main() {
                Var a: A = New A();
                a.print(15);
            }
        }
        """
        expect = "56789101112131415"
        self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    def test_512(self):
        input = """Class Program {
            main() {
                Val a:Int = 11;
                io::$putIntLn(a);
            }
        }"""
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_513(self):
        input = """
        Class Animal {
            Var d: String = "Hello" +. " World";
            Var e: Boolean = (2 > 4);
            Var a: Animal;
            Var b: Int = 2 + 5 * 7;
            Var c: Float = 2 * 7 + 4.5;
            get() {
                io::$putFloatLn(Self.c);
                io::$putString(Self.d);
            }
        }
        Class Program {
            main() { 
                Var animal: Animal = New Animal();
                animal.get();
            }
        }
        
        """
        expect = "18.5\nHello World"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_514(self):
        input = """Class Program{
            $mehthod(){

                Var a: Array[Int, 3] = Array(1,2,3);
                Return a;
            }
            main(){
                Var a: Array[Int, 3] = Array(1,2,3);
                io::$putInt(a[1]);
            }
            }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_515(self):
        input = """
        Class Animal {
            Var d: Boolean = "Hello" ==. " World";
            Var e: Boolean = (2 > 4);
            Var a: Animal;
            Var b: Int = 2 + 5 * 7;
            Var c: Float = 2 * 7 + 4.5;
            get() {
                io::$putFloatLn(Self.c);
                io::$putBool(Self.d);
            }
        }
        Class Program {
            main() { 
                Var animal: Animal = New Animal();
                animal.get();
            }
        }
        
        """
        expect = "18.5\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_516(self):
        input = """
        Class Program {main(){}}
        Class supsuper {
            Var ss: Int = 2;
            Constructor () { }
            Destructor () { }
        }
        Class super : supsuper {
            Var s: supsuper;
            Constructor () { }
            Destructor () { }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_517(self):
        input = """
        Class D {
            Var d : Int = 2 + 4 + 6 * 7;

        }
        Class C {
            Var c: Float = 5.2;
            Constructor(t: Float; c: String) {}
        }
        Class A {
            Var b: Float = 3.4;
            getA(a: Float) {
                Return a;
            }
        }
        Class Program {
            main(){
                Var a: A = New A();
                io::$putFloatLn(a.b);
            }
        }
        """
        expect = "3.4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_518(self):
        """Simple program: int main() {} """
        input = """
        Class Program{
            main(){
                Var a:Int = 2;
                a = 3;
                io::$putFloatLn(4 / a + 3 / 3 - 2.5);
            }
        }"""
        expect = "-0.16666651\n"
        self.assertTrue(TestCodeGen.test(input, expect, 518))
        
    def test_519(self):
        input = """
        Class C {
            Var $c: Int = 2;
            get() { }
            Destructor () { }
            Constructor(a: Float; b: String) { }
        }
        
        Class A {
            Var b: Array[Int, 3];
            getA(b: Float) {
                Var a: Array[Int, 3];
                a = Array(4,5,6.7);
            }
            Constructor () { }
            Destructor () { }
        }

        Class Program {main(){}}
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_520(self):
        input = """
        Class A {
            Var b: Array[Int, 3];
            getA(b: Float) {
                Var a: Array[Array[Int, 2], 3];
            }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_521(self):
        input = """
            Class A{
                Var x:Int = 11;
            }
            Class Program{
                Var y:Int = 1;

                main(){
                    Var a:A = New A();
                    io::$putInt(a.x);
                }
            }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_522(self):
        input = """
        Class C {
            Var z: Float = 6.9;
            getC(a: Int; b: Float) { 
                Return 12.2;
            }
        }
        Class Program {
            main(){
                Var b: C = New C();
                io::$putFloat(b.z);
            }
        }
        """
        expect = "6.9"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_523(self):
        input = """
        Class D {getD() { Return "Hello From D"; }
        Constructor () { }
            Destructor () { }}
        Class C : D {getC(a: Int; b: Float) {Return 3;}
        Constructor () { }
            Destructor () { }}
        Class A {method() {
                Var c: C;
                Var b: Int;}
                Constructor () { }
            Destructor () { }}
        Class Program {
            main(){
                Var d: D = New D();
                io::$putStringLn(d.getD());
            }
        }
        """
        expect = "Hello From D\n"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_524(self):
        input = """
        Class D {
            getD2() {
                Return 2.4 / 5;
            }
            getD(a, b: Int) { 
                Return Self.getD2();
            }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){io::$putFloatLn(2.4 / 5);}}
        Class C : D {
            getC(a: Int; b: Float) {
                Return 3;
            }
            Constructor () { }
            Destructor () { }
        }
        Class A {
            method() {
                Var c: C;
                Var b: Int;
                b = c.getC(1,2);
            }
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "0.48000002\n"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_525(self):
        input = """
        Class Program {
            main(){
                Var a: Boolean = "Phuc" ==. ("Sam" +. "Phuc");
                io::$putBoolLn(a);
            }
        }
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test26(self):
        input = """
        Class Program{
            main(){}
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 426))

    def test_527(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Foreach (i In 1 .. 4){
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_528(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 5] = Array(4, 3, 2, 1, 0);
                Var i: Int;
                Foreach (i In 1 .. 5){
                    If (i == 2) {
                        io::$putInt(a[i]);
                    }
                    Else {
                        io::$putInt(i);
                    }
                }
            }
        }
        """
        expect = "13345"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_529(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 5] = Array(4, 3, 2, 1, 0);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 5){
                    If (i % 3 == 0) {
                        io::$putInt(a[i]);
                    }
                    Elseif (i % 3 == 1) {
                        io::$putInt(a[i] * 2);
                    }
                    Else {
                        io::$putInt(a[i] * 3);
                    }
                }
            }
        }
        """
        expect = "89220"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_530(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 10] = Array(4, 3, 2, 1, 0, 1, 2, 3, 4, 5);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 10 By 1 + 2){
                    If (i % 3 == 0) {
                        io::$putInt(a[i]);
                    }
                    Elseif (i % 3 == 1) {
                        io::$putInt(a[i] * 2);
                    }
                    Else {
                        io::$putInt(a[i] * 3);
                    }
                }
            }
        }
        """
        expect = "82410"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_531(self):
        input = """Class Program{
            $mehthod(){

                Var a: Array[Int, 3] = Array(1,2,3);
                Return a;
            }
            main(){
                Var a: Array[Int, 3] = Program::$mehthod();
                io::$putInt(a[1]);
            }
            }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_532(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Foreach (i In 1 .. 4){
                    If (i == 3){
                        Break;
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "01"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_533(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Foreach (i In 1 .. 4){
                    If (i == 2){
                        Continue;
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "023"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_534(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In i .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "01230123123233"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_535(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In i .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putIntLn(a[i]);
                }
            }
        }
        """
        expect = "01230\n1231\n232\n33\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_536(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In 1 .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "01230012310123201233"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_537(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In 1 .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putIntLn(a[i]);
                }
            }
        }
        """
        expect = "01230\n01231\n01232\n01233\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_538(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(3, 2, 1, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In i .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putIntLn(a[i]);
                }
            }
        }
        """
        expect = "32133\n2132\n131\n33\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_539(self):
        input = """
        Class Program {
            main() {
                Var a: Float = 1.234;
                io::$putFloat(a/2*25+2262-2352*3223+2352/25262*2252);
            }
        }
        
        """
        expect = "-7578009.0"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_540(self):
        input = """
        Class Program {
            main() {
                Var c: Int = 5;
                If (c > 4) {
                    Var a: Int = 2;
                    Var c: Int;
                    Foreach (c In 1 .. 100 By a) { 
                        io::$putInt(c);
                    }
                }
            }
        }
        
        """
        expect = "13579111315171921232527293133353739414345474951535557596163656769717375777981838587899193959799"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_541(self):
        input = """
        Class Program {
            main() {
                Var c: Int = 3;
                If (c > 4) {
                    Var a: Int = 2;
                    Var c: Int;
                    Foreach (c In 1 .. 100 By a) { 
                        io::$putInt(c);
                    }
                }
            }
        }
        
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_542(self):
        input = """
        Class Program {
            main() {
                Var c: Int = 10;
                If (c > 4) {
                    Var a: Int = 4;
                    Var b: Int;
                    Foreach (b In 1 .. 100 By c - a) { 
                        io::$putInt(b);
                    }
                }
            }
        }
        
        """
        expect = "17131925313743495561677379859197"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_543(self):
        input = """
        Class Program {
            main() {
                Var newArr : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                Var i: Int;
                newArr[1] = 100;
                io::$putInt(newArr[1]);
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_544(self):
        input = """
        Class Name {
            Var name: String = "My Name";
            Val age : Int = 18;
            func() {
                Self.name = Self.name +. "is Program";
            }
        }
        Class Program {
            main() {
                Var name: Name = New Name();
                name.func();
                io::$putString(name.name);
            }
        }
        """
        expect = "My Nameis Program"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_545(self):
        input = """
        Class Name {
            Var name: String = "My Name";
            Val age : Int = 18;
            func() {
                Self.name = Self.name +. "is Program";
                Return Self.age;
            }
        }
        Class Program {
            main() {
                Var name: Name = New Name();
                io::$putStringLn(name.name);
                io::$putIntLn(name.func());
                io::$putStringLn(name.name);
            }
        }
        """
        expect = "My Name\n0\nMy Nameis Program\n"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_546(self):
        input = """
        Class Program {
            foo(){
                Return 100;
            }
            main(){
                Var A: Program = New Program();
                Var B: Program = New Program();
                Var zoo: Int = A.foo();
                io::$putInt(zoo + B.foo());
            }
        }
        """
        expect = "200"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_547(self):
        input = """
        Class Program {
            Var att: Int = 20;
            foo(){
                Self.att = 30;
            }
            main(){
                Var Program: Program = New Program();
                Program.foo();
                io::$putInt(Program.att);
            }
        }
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_548(self):
        input = """
        Class Program {
            foo(){
                io::$putInt(1);
            }
            main(){
                Var Program: Program = New Program();
                Var i: Int;
                Foreach (i In 1 .. 10){
                    Program.foo();
                } 
            }
        }
        """
        expect = "1111111111"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_549(self):
        input = """
        Class Program {
            main(){
                Var i: Int = 7;
                io::$putBool(i == 7);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_550(self):
        input = """
        Class Program {
            Var total: Array[Int, 4] = Array(0, 0, 0, 0);
            change(i : Int){
                Self.total[i] = 100;
            }
        
            main(){
                Var Program: Program = New Program();
                Var i: Int = 0;
                Foreach (i In 1 .. 4){
                    io::$putInt(Program.total[i]);
                    Program.change(i);
                    io::$putInt(Program.total[i]);
                }
            }
        }
        """
        expect = "0100010001000100"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_551(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4) {
                    Foreach (j In 1 .. 4){
                        If (j == 2){
                            Continue;
                        }
                        io::$putInt(a[i]);        
                    }
                }
            }
        }
        """
        expect = "000111222333"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_552(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4) {
                    Foreach (j In 1 .. 4){
                        If (j == 2){
                            Continue;
                        }
                        io::$putInt(a[j]);        
                    }
                }
            }
        }
        """
        expect = "023023023023"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_553(self):
        input = """Class Program {
            $factorial(n: Int) {
                If (n <= 1) {
                    Return "1";
                }
                Else {
                    Return "Program::$factorial(n - 1) * n";
                }
            }  
            main() {
                Var c: Int;
                io::$putStringLn(Program::$factorial(6));
            }
        }"""
        expect = str("Program::$factorial(n - 1) * n\n")
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_554(self):
        input = """Class Program {
            main() {
                Var x: Int;
                Foreach (x In 1 .. 15 By 2 * 2) {
                    io::$putInt(1);
                }
            }
        }"""
        expect = "1111"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_555(self):
        input = """Class Program {
            main() {
                Var a:Int = 11;
                io::$putIntLn(a);
            }
        }"""
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_556(self):
        input = """
            Class A{
                Var x:Int = 11;
            }
            Class Program{
                $sum(n: Int) {
                    Var a:A = New A();
                    Return a.x + 12.2/2  + n;             
                }

                main(){
                    io::$putFloat(Program::$sum(12));
                }
            }"""
        expect = "29.1"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_557(self):
        input = """
                Class Student
                {
                    Var name: String;
                    Var ID: Int;
                    Constructor(newName: String; newID : Int)
                    {
                        Self.name = newName;
                        Self.ID = newID;
                    }
                }
                Class Program
                {
                    main()
                    {
                        Var myStudent: Student = New Student("Phuc", 4720);
                        io::$putStringLn(myStudent.name);
                        io::$putInt(myStudent.ID);
                    }
                }
            """
        expect = "Phuc\n4720"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_558(self):
        input = """Class Program {
                Var x: Int = 11;
                abc(){
                    Self.x = 10;
                    io::$putInt(Self.x);
                }
                main() {
                    Var a: Program = New Program();
                    a.abc();
                }
            }"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_559(self):
        input = """Class Program {
                   $x(n: Int){
                       Return 11;
                   }
                    main() {
                        io::$putInt(Program::$x(6));
                    }
                }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_560(self):
        input = """Class Program {
                   $x(){
                       Return 11;
                   }
                    main() {
                        io::$putInt(Program::$x());
                    }
                }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_561(self):
        input = """
        Class A {
            print(a: Int) {
                Var b: Int;
                Foreach (b In 1 .. a) {
                    If (b > 4) { 
                        io::$putInt(b);
                    }
                }
            }
        }
        Class Program {
            main() {
                Var a: A = New A();
                a.print(15);
            }
        }
        """
        expect = "56789101112131415"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test_562(self):
        input = """Class Program {
            main() {
                Val a:Int = 11;
                io::$putIntLn(a);
            }
        }"""
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_563(self):
        input = """
        Class Animal {
            Var d: String = "Hello" +. " World";
            Var e: Boolean = (2 > 4);
            Var a: Animal;
            Var b: Int = 2 + 5 * 7;
            Var c: Float = 2 * 7 + 4.5;
            get() {
                io::$putFloatLn(Self.c);
                io::$putString(Self.d);
            }
        }
        Class Program {
            main() { 
                Var animal: Animal = New Animal();
                animal.get();
            }
        }
        
        """
        expect = "18.5\nHello World"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_564(self):
        input = """Class Program{
            $mehthod(){

                Var a: Array[Int, 3] = Array(1,2,3);
                Return a;
            }
            main(){
                Var a: Array[Int, 3] = Array(1,2,3);
                io::$putInt(a[1]);
            }
            }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_565(self):
        input = """
        Class Animal {
            Var d: Boolean = "Hello" ==. " World";
            Var e: Boolean = (2 > 4);
            Var a: Animal;
            Var b: Int = 2 + 5 * 7;
            Var c: Float = 2 * 7 + 4.5;
            get() {
                io::$putFloatLn(Self.c);
                io::$putBool(Self.d);
            }
        }
        Class Program {
            main() { 
                Var animal: Animal = New Animal();
                animal.get();
            }
        }
        
        """
        expect = "18.5\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_566(self):
        input = """
        Class Program {main(){}}
        Class supsuper {
            Var ss: Int = 2;
            Constructor () { }
            Destructor () { }
        }
        Class super : supsuper {
            Var s: supsuper;
            Constructor () { }
            Destructor () { }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_567(self):
        input = """
        Class D {
            Var d : Int = 2 + 4 + 6 * 7;

        }
        Class C {
            Var c: Float = 5.2;
            Constructor(t: Float; c: String) {}
        }
        Class A {
            Var b: Float = 3.4;
            getA(a: Float) {
                Return a;
            }
        }
        Class Program {
            main(){
                Var a: A = New A();
                io::$putFloatLn(a.b);
            }
        }
        """
        expect = "3.4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_568(self):
        """Simple program: int main() {} """
        input = """
        Class Program{
            main(){
                Var a:Int = 2;
                a = 3;
                io::$putFloatLn(4 / a + 3 / 3 - 2.5);
            }
        }"""
        expect = "-0.16666651\n"
        self.assertTrue(TestCodeGen.test(input, expect, 568))
        
    def test_569(self):
        input = """
        Class C {
            Var $c: Int = 2;
            get() { }
            Destructor () { }
            Constructor(a: Float; b: String) { }
        }
        
        Class A {
            Var b: Array[Int, 3];
            getA(b: Float) {
                Var a: Array[Int, 3];
                a = Array(4,5,6.7);
            }
            Constructor () { }
            Destructor () { }
        }

        Class Program {main(){}}
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_570(self):
        input = """
        Class A {
            Var b: Array[Int, 3];
            getA(b: Float) {
                Var a: Array[Array[Int, 2], 3];
            }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_571(self):
        input = """
        Class Program {
            main(){
                Var a: Array[Int, 2] = Array(2,3);
                io::$putIntLn(a[1]);
            }
        }
        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_572(self):
        input = """
        Class C {
            Var z: Float = 6.9;
            getC(a: Int; b: Float) { 
                Return 12.2;
            }
        }
        Class Program {
            main(){
                Var b: C = New C();
                io::$putFloat(b.z);
            }
        }
        """
        expect = "6.9"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_573(self):
        input = """
        Class D {getD() { Return "Hello From D"; }
        Constructor () { }
            Destructor () { }}
        Class C : D {getC(a: Int; b: Float) {Return 3;}
        Constructor () { }
            Destructor () { }}
        Class A {method() {
                Var c: C;
                Var b: Int;}
                Constructor () { }
            Destructor () { }}
        Class Program {
            main(){
                Var d: D = New D();
                io::$putStringLn(d.getD());
            }
        }
        """
        expect = "Hello From D\n"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_574(self):
        input = """
        Class D {
            getD2() {
                Return 2.4 / 5;
            }
            getD(a, b: Int) { 
                Return Self.getD2();
            }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){io::$putFloatLn(2.4 / 5);}}
        Class C : D {
            getC(a: Int; b: Float) {
                Return 3;
            }
            Constructor () { }
            Destructor () { }
        }
        Class A {
            method() {
                Var c: C;
                Var b: Int;
                b = c.getC(1,2);
            }
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "0.48000002\n"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_575(self):
        input = """
        Class Program {
            main(){
                Var a: Boolean = "Phuc" ==. ("Sam" +. "Phuc");
                io::$putBoolLn(a);
            }
        }
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test576(self):
        input = """
        Class Program{
            main(){}
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 476))

    def test_577(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Foreach (i In 1 .. 4){
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_578(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 5] = Array(4, 3, 2, 1, 0);
                Var i: Int;
                Foreach (i In 1 .. 5){
                    If (i == 2) {
                        io::$putInt(a[i]);
                    }
                    Else {
                        io::$putInt(i);
                    }
                }
            }
        }
        """
        expect = "13345"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_579(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 5] = Array(4, 3, 2, 1, 0);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 5){
                    If (i % 3 == 0) {
                        io::$putInt(a[i]);
                    }
                    Elseif (i % 3 == 1) {
                        io::$putInt(a[i] * 2);
                    }
                    Else {
                        io::$putInt(a[i] * 3);
                    }
                }
            }
        }
        """
        expect = "89220"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_580(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 10] = Array(4, 3, 2, 1, 0, 1, 2, 3, 4, 5);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 10 By 1 + 2){
                    If (i % 3 == 0) {
                        io::$putInt(a[i]);
                    }
                    Elseif (i % 3 == 1) {
                        io::$putInt(a[i] * 2);
                    }
                    Else {
                        io::$putInt(a[i] * 3);
                    }
                }
            }
        }
        """
        expect = "82410"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_581(self):
        input = """Class Program{
            $mehthod(){

                Var a: Array[Int, 3] = Array(1,2,3);
                Return a;
            }
            main(){
                Var a: Array[Int, 3] = Program::$mehthod();
                io::$putInt(a[1]);
            }
            }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_582(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Foreach (i In 1 .. 4){
                    If (i == 3){
                        Break;
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "01"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_583(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Foreach (i In 1 .. 4){
                    If (i == 2){
                        Continue;
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "023"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_584(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In i .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "01230123123233"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_585(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In i .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putIntLn(a[i]);
                }
            }
        }
        """
        expect = "01230\n1231\n232\n33\n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_586(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In 1 .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putInt(a[i]);
                }
            }
        }
        """
        expect = "01230012310123201233"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_587(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(0, 1, 2, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In 1 .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putIntLn(a[i]);
                }
            }
        }
        """
        expect = "01230\n01231\n01232\n01233\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_588(self):
        input = """  
        Class Program {
            main () {
                Var a: Array[Int, 4] = Array(3, 2, 1, 3);
                Var i: Int;
                Var j: Int;
                Foreach (i In 1 .. 4){
                    Foreach (j In i .. 4){
                        io::$putInt(a[j]);
                    }
                    io::$putIntLn(a[i]);
                }
            }
        }
        """
        expect = "32133\n2132\n131\n33\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_589(self):
        input = """
        Class Program {
            main() {
                Var a: Float = 1.234;
                io::$putFloat(a/2*25+2262-2352*3223+2352/25262*2252);
            }
        }
        
        """
        expect = "-7578009.0"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_590(self):
        input = """
        Class Program {
            main() {
                Var c: Int = 5;
                If (c > 4) {
                    Var a: Int = 2;
                    Var c: Int;
                    Foreach (c In 1 .. 100 By a) { 
                        io::$putInt(c);
                    }
                }
            }
        }
        
        """
        expect = "13579111315171921232527293133353739414345474951535557596163656769717375777981838587899193959799"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_591(self):
        input = """
        Class Program {
            main() {
                Var c: Int = 3;
                If (c > 4) {
                    Var a: Int = 2;
                    Var c: Int;
                    Foreach (c In 1 .. 100 By a) { 
                        io::$putInt(c);
                    }
                }
            }
        }
        
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_592(self):
        input = """
        Class Program {
            main() {
                Var c: Int = 10;
                If (c > 4) {
                    Var a: Int = 4;
                    Var b: Int;
                    Foreach (b In 1 .. 100 By c - a) { 
                        io::$putInt(b);
                    }
                }
            }
        }
        
        """
        expect = "17131925313743495561677379859197"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_593(self):
        input = """
        Class Program {
            main() {
                Var newArr : Array[Int, 5] = Array(1, 2, 3, 4, 5);
                Var i: Int;
                newArr[1] = 100;
                io::$putInt(newArr[1]);
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_594(self):
        input = """
        Class Name {
            Var name: String = "My Name";
            Val age : Int = 18;
            func() {
                Self.name = Self.name +. "is Program";
            }
        }
        Class Program {
            main() {
                Var name: Name = New Name();
                name.func();
                io::$putString(name.name);
            }
        }
        """
        expect = "My Nameis Program"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_595(self):
        input = """
        Class Name {
            Var name: String = "My Name";
            Val age : Int = 18;
            func() {
                Self.name = Self.name +. "is Program";
                Return Self.age;
            }
        }
        Class Program {
            main() {
                Var name: Name = New Name();
                io::$putStringLn(name.name);
                io::$putIntLn(name.func());
                io::$putStringLn(name.name);
            }
        }
        """
        expect = "My Name\n0\nMy Nameis Program\n"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_596(self):
        input = """
        Class Program {
            foo(){
                Return 100;
            }
            main(){
                Var A: Program = New Program();
                Var B: Program = New Program();
                Var zoo: Int = A.foo();
                io::$putInt(zoo + B.foo());
            }
        }
        """
        expect = "200"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_597(self):
        input = """
        Class Program {
            Var att: Int = 20;
            foo(){
                Self.att = 30;
            }
            main(){
                Var Program: Program = New Program();
                Program.foo();
                io::$putInt(Program.att);
            }
        }
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_598(self):
        input = """
        Class Program {
            foo(){
                io::$putInt(1);
            }
            main(){
                Var Program: Program = New Program();
                Var i: Int;
                Foreach (i In 1 .. 10){
                    Program.foo();
                } 
            }
        }
        """
        expect = "1111111111"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_599(self):
        input = """
        Class Program {
            main(){
                Var i: Int = 7;
                io::$putBool(i == 7);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 599))