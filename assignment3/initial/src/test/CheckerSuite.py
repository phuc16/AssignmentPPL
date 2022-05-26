import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test0(self):
        input = """
        Class Dog {
            Val $a : Int = 3.2;
            $getDog() { }
            Constructor () { }
            Destructor () { }
        }
        Class Meow {
            $set() { }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id($a),IntType,FloatLit(3.2))"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test1(self):
        input = """
        Class A {
            Var $a: Int;
            Constructor () { }
            Destructor () { }
        }
        Class A {
            Val $b: Float;
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = """
        Class Program {main(){}}
        Class A {
            Val $a: Int = 2 + True;
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(2),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a : Float = -(1.2 +1);
                                Val b : Float = -(1 + 1);
                                Val c : Boolean = !!((1>2)&&(True || ("abc"==."cef")));
                                Val d :String = ("abc" +. "def")+."ghi";
                                Val e :String = True==1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,BooleanLit(True),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """
        Class Program {main(){}}
        Class A { }
        Class B: A {
            Val $r :Int = 2 + 2 * 2.5;
            Var a: Boolean = True;
            setA(a: Int) { }
            Constructor () { }
            Destructor () { }
        }
        """
        
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id($r),IntType,BinaryOp(+,IntLit(2),BinaryOp(*,IntLit(2),FloatLit(2.5))))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """
        Class Program {main(){}}
        Class A { }
        Class B: A {
            Var t: Float = 1.4 % 3; 
            setA(a: Int) { }
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.4),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """
        Class Program {main(){}}
        Class A {
            Var a: Array[Array[Int, 2], 2] = Array(
                                                Array(3,6),
                                                Array(8,9.2)
            );
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Illegal Array Literal: [IntLit(8),FloatLit(9.2)]"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
        input = """
        Class Program {main(){}}
        Class A {
            Var a: Int = 120;
            Val $a: C = New C();
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
        input = """
        Class Program {main(){}}
        Class A {
            Var a, t, r: Int = 120, 12 * 60 - 9, 1e4;
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(r),IntType,FloatLit(10000.0))"
        self.assertTrue(TestChecker.test(input, expect ,408))

    def test9(self):
        input = """
        Class Program {main(){}}
        Class B {
            Val C: String;
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = """
        Class Program {main(){}}
        Class A {
            Val $a: Int = 3;
            Constructor(a: Float; b: Int) { }
            Destructor () { }
        }
        Class B {
            Val $b: A = New A(1, 3.2);
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1),FloatLit(3.2)])"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        """Simple program: int main() {} """
        input = """
                    Class B{}
                    Class A{
                    b(){
                        Var b:Int = 1;
                        Var c:A;
                        Var a:C;
                    }
                    }"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12(self):
        input = """
        Class Program {main(){}}
        Class A {
            Var z: Int;
            getA(a: Int) {
                Foreach (b In 1 .. 10) { }
            }
            Constructor () { }
            Destructor () { }
        }
        """
            # Var b: Int = A.c.a;
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """
        Class Program {main(){}}
        Class A {
            Var z: Int;
            getA(a: Int) {
                Var b: Int;
                Foreach (b In 1.2 .. 10.5) { }
            }
            Constructor () { }
            Destructor () { }
        }
        """
            # Var b: Int = A.c.a;
        expect = "Type Mismatch In Statement: For(Id(b),FloatLit(1.2),FloatLit(10.5),IntLit(1),Block([])])"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = """
        Class Program {main(){}}
        Class A {
            Var z: Int;
            getA(a: Int) {
                Var b: Int;
                Foreach (b In 1 .. 100) {
                    If (b + 4) { }
                    Else { Var e: String; }
                }
            }
            Constructor () { }
            Destructor () { }
        }
        """
            # Var b: Int = A.c.a;
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(b),IntLit(4)),Block([]),Block([VarDecl(Id(e),StringType)]))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """
        Class Program {main(){}}
        Class A {
            Var z: Int;
            getA(a: Int) {
                Var b: Int;
                Foreach (b In 1 .. 100) {
                    If (b > 6) { 
                        If (b < 120) { }
                        Elseif (a > 10) { }
                        Elseif (a * 10) { }
                    }
                    Else { Var e: String; }
                }
            }
            Constructor () { }
            Destructor () { }
        }
        """
            # Var b: Int = A.c.a;
        expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),IntLit(10)),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test16(self):
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
        Class A : super {
            Var z: Int = 2;
            getA(a: Int) {
                Var b: Int = 2 + A.s.ss;
            }
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Undeclared Attribute: s"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """
        Class D {
            Var d : Int = 2 + 4 + 6 * 7;
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        Class C {
            Var c: Float = 5.2;
            Constructor(t: Float; c: String) {}
            Destructor () { }
        }
        Class A {
            Var b: Float = 3.4;
            getA(a: Float) {
                Var Cobj: C = New C(3.4, "Hello");
                a = Self.b + Cobj.c * D.d;
            }
            Constructor () { }
            Destructor () { }
        }
        """
            # Var b: Int = A.c.a;
        expect = "Illegal Member Access: FieldAccess(Id(D),Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a:Int = 2;
                                a=3;
                            }
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test19(self):
        input = """
        Class C {
            Var $c: Int = 2;
            get() { }
            Destructor () { }
            Constructor(a: Float; b: String) { }
        }
        Class Program {main(){}}
        Class A {
            Var b: Array[Int, 3];
            getA(b: Float) {
                Var a: Array[Int, 3];
                a = Array(4,5,6.7);
            }
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Illegal Array Literal: [IntLit(4),IntLit(5),FloatLit(6.7)]"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test20(self):
        input = """
        Class A {
            Var b: Array[Int, 3];
            getA(b: Float) {
                Var a: Array[Array[Int, 2], 3];
                a = Array(4,5,6);
            }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(4),IntLit(5),IntLit(6)])"
        self.assertTrue(TestChecker.test(input, expect, 420)
        )
    def test21(self):
        input = """
        Class A {
            Var b: Array[Int, 3];
            getA(a: Float) {
                Var b: Float = 12.5;
                Var a: Array[Array[Int, 2], 2];
                a = Array(
                    Array(2,3),
                    Array(b,6)
                );
            }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22(self):
        input = """
        Class C {
            getC(a: Int; b: Float) { }
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        Class A {
            method() {
                Var c: C;
                Var b: Int;
                b = c.getC(1,2.4);
            }
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(c),Id(getC),[IntLit(1),FloatLit(2.4)])"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test23(self):
        input = """
        Class D {$getD(a, b: Int) { Return "Hello From D"; }
        Constructor () { }
            Destructor () { }}
        Class C : D {getC(a: Int; b: Float) {Return 3;}
        Constructor () { }
            Destructor () { }}
        Class A {method() {
                Var c: C;
                Var b: Int;
                b = D::$getD(1,2);}
                Constructor () { }
            Destructor () { }}
        Class Program {main(){}}
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),CallExpr(Id(D),Id($getD),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
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
        Class Program {main(){Return 2.4 / 5;}}
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
        expect = "Type Mismatch In Statement: Return(BinaryOp(/,FloatLit(2.4),IntLit(5)))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """
        Class Animal{
            Var $name : String = "aaaaa";
            Var sex : String = "Male";
            Constructor () { }
            Destructor () { }
        }
        Class Program {main(){}}
        Class Dog : Animal{
            Var $a : Int = 5 + 6 - 7 * 8;
            Var $b : Float = 5.6 * 9;
            Var $c : Int = Dog::$a - 8;
            Var $d : Float = Dog::$a * Dog::$b;
            Var $e : String = Animal::$name;
            Var d : String = "Hello";
            Var e : String = Self.d;
            Var meomeo : Int = (Meo::$e - 89) * 9600;
            Bark(a, b, c : String; d, e, f : Float){}
            Constructor () { }
            Destructor () { }
        }
        Class Meo : Animal{
            Var $e : Int = 6;
            MeowMeow(a : Float){}
            Constructor () { }
            Destructor () { }
        }
        """
        expect = "Undeclared Identifier: Meo"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """
        Class Program{
            
        }
        Class Program{
            
        }
        """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
        input = """
        Class Animal{
            Var $name : String = "aaaaa";
            Var sex : String = "Male";
            Constructor(name : String) {
                
            }
            Destructor() { }
        }
        Class Meo : Animal{
            Var $e : Int = 6;
            Constructor (a : Float; b : Int) { }
            Destructor() { }
        }
        Class Dog : Animal{
            Var $meo : Meo = New Meo(5.6, 7);
            Var $a : Int = 5 + 6 - 7 * 8;
            Var $b : Float = Dog::$a;
            Var $c : Int = Dog::$a - 8;
            Var $d : Float = Dog::$a * Dog::$b;
            Var $e : String = Animal::$name;
            Var d : String = "Hello";
            Var e : String = Self.d;
            Var meomeo : Int = (Meo::$e - 89) * 9600;
            Var $arr : Array[Int, 5];
            Var $arr2 : Array[Int, 6] = Array(1, 2, 3, 4, 5, 6);
            Constructor(name : String) { }
            Bark(a, b, c : String; d, e, f : Float) { }
            Destructor() { }
            Val $ffff : Meo = New Animal("Cat");
        }
        
        Class Program {
            main () { }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id($ffff),ClassType(Id(Meo)),NewExpr(Id(Animal),[StringLit(Cat)]))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test28(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                Var e:String = a.c(1,2);
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(e),StringType,CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test29(self):
        input = """
        Class Animal {
            Constructor (a : Array[Array[Int, 2], 2]){ }
            Destructor() { }
        }
        Class Program : Animal{
            Var a : Program = New Animal(Array(Array(1, 2), Array(3, 4)));
            main () { }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ClassType(Id(Program)),NewExpr(Id(Animal),[[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)]]]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test30(self):
        input = """
        Class Unit 
        {
            Constructor (a : Int; b : String){ }
            Destructor () { }
        }
        Class Character : Unit
        {
            Constructor () { }
            Destructor () { }
        }
        Class Player : Character
        {
            Constructor (a : Array[Int, 7]; b : Float; c : String){}
            Destructor(){}
        }
        Class Health : Player
        {
            Constructor ()
            {}
            Destructor(){}
        }
        Class Program
        {
            Var a : Unit = New Unit(2, "Hieu");
            Val $b : Character = New Character();
            Var player :Player  = New Health();
            main () { }
            Destructor(){}
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(player),ClassType(Id(Player)),NewExpr(Id(Health),[]))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test31(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                a.d();
                                Var e:Float = a.b;
                                Var f:String = a.b;
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),StringType,FieldAccess(Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32(self):
        input = """
        Class Program {
            main() { }
        }
        Class Animal {
            Var d: String = "Hello" +. " World";
            Var e: Boolean = (2 > 4) && !(2 < 9);
            Var a: Animal;
            Var b: Int = 2 + 5 * 7;
            Var c: Float = 2 * 7 + 4.5 - e4;
            Constructor () { }
            Destructor () { }
        }
        
        """
        expect = "Undeclared Identifier: e4"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a : Int = 1.2;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test34(self):
        input = """
        Class sieuSuper {
            Var s: Float = 2;
        }
        Class super : sieuSuper {
            Var a: sieuSuper;
            Var $a: Int = 4;
            getSuper() {
                Self.a.s = 5.6;
            }
        }
        Class Program{main(a:Int){}}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test35(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                Val e:String = a.d(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test36(self):
        input = """
        Class B { 
            Constructor() { }
        }
        Class A : B {
            Val arr: Array[Array[Int, 2], 2] = Array(
                Array(2,3),
                Array(4,5)
            );
            getA() {
                Self.arr = Array(
                Array(2,6),
                Array(4,5)
            );
            }
        }
        
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(arr)),[[IntLit(2),IntLit(6)],[IntLit(4),IntLit(5)]])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test37(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                a.d(1+2,2--2.0,"a"+."bcd");
                                a.c(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test38(self):
        input = """
        Class Node {
            Var data: Int;
            Var next: Node;
            Constructor(data: Int) {
                Self.data = data;
            }
        }

        Class LinkedList {
            Var head: Node;
            insertHead(data: Int) {
                Self.head = New Node();
            }
        }
        
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Node),[])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test39(self):
        input = """
        Class Program {
            main(a: Int; b: Float) {
                Var a: Float;
            }
        }
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test40(self):
        input = """
        Class Program {
            main(a: Int; b: Float) {
                Var c: Float;
                If (c > 4) {
                    Var a: Float = 2;
                    Var c: Int;
                    Foreach (c In 1 .. 100 By a) { }
                }
            }
        }
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test41(self):
        input = """
        Class Program {
            Constructor(a: Int; b: Float; c: String; d: Boolean) { }
        }

        Class A : Program {
            Var a : Program = New Program(1,2,"Name" ==. "Bao",False && True);
        }
        
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(Program),[IntLit(1),IntLit(2),BinaryOp(==.,StringLit(Name),StringLit(Bao)),BinaryOp(&&,BooleanLit(False),BooleanLit(True))])"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42(self):
        input = """
        Class Program {
            main(a: Int; b: Float) {
                Var c: Float;
                If (c > 4) {
                    Var a: Float = 2;
                    Val c: Int = 2;
                    Foreach (c In 1 .. 100) { }
                }
            }
        }
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test43(self):
        input = """
        Class Program {
            Var name: String;
            Val age : Int = 18;
            main(a: Int; b: Float) {
                Val c: Int = 2;
                Val d: Float = Self.age + c + a;
                Self.name = "Hello";
                Return Self.name;
            }
        }
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test44(self):
        input = """
        Class Program {
            Var name: String;
            Val age : Int = 18;
            main(a: Int; b: Float) {
                Val c: Int = 2;
                Self.name = "Hello";
                Return Self.name;
            }
        }
        Class Name: Program {
            Var name: String = "My Name";
            main() {
                Self.name = Self.name +. "is Program";
                Return Self.age + 12 / 5 + (67 % 4);
            }
        }
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test45(self):
        input = """
        Class Program {
            Var name: String;
            Val age : Int = 18;
            main(a: Int; b: Float) {
                Val c: Int = 2;
                Self.name = "Hello";
                Return Self.name;
            }
        }
        Class Name: Program {
            Var name: String = "My Name";
            main() {
                Var a: Array[Array[Float, 3], 2];
                a[0] = Array(1,2,4);
            }
        }
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """
        Class Program {
            main() { }
        }
        Class Queue {
            Var data: Array[Int, 100000];
            front() {
                Return Self.data[0];
            }
            push(d: Int) {
                Var newArr : Array[Int, 100000];
                newArr[0] = d;
                Foreach (i In 1 .. 100001) {
                    newArr[i] = Self.data[i-1];
                }
                Self.data = newArr;
            }
        }
        
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test47(self):
        input = """
        Class Program {
            main() { }
        }
        Class Queue {
            Var data: Array[Int, 100000];
            front() {
                Return Self.data[0];
            }
            push(d: Int) {
                Var newArr : Array[Int, 100000];
                newArr[0] = d;
                Var i: Int;
                Foreach (i In 1 .. 100001) {
                    newArr[i] = Self.data[i-1];
                }
                Self.data = newArr[0];
            }
        }
        
        """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(data)),ArrayCell(Id(newArr),[IntLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test48(self):
        input = """
        Class Program {
            main() { }
        }
        Class Stack {
            Var data: Array[Int, 100000];
            front() {
                Return Self.data[0];
            }
            delete(d: Int) { }
            pop() {
                Self.delete(Self.data[last]);
            }
        }
        
        """
        expect = "Undeclared Identifier: last"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test49(self):
        input = """
        Class Program {
            main() { }
        }
        Class Stack {
            Val data: Array[Int, 3] = Array(1);
            front() {
                Return Self.data[0];
            }
            delete(d: Int) { }
            assign() {
                Seld.data[0] = 4;
            }
        }
        
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(data),ArrayType(3,IntType),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test50(self):
        input = """
        Class Program {
            Val data: Array[Int, 3] = Array(1,2,3);
            main() { 
                Val newData : Int = Self.data[1][2];
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(FieldAccess(Self(),Id(data)),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        input = """
        Class Dog {
            Var dogs: Int = 2;
        }
        Class Program {
            Var name: Dog;
            main(c: Int; b: Float) {
                Var d: Boolean;
                Var a: Program;
                d =  Dog.name.dog;
            }
        }
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        input = """
        Class A { }
        Class E {
            Var a : Int;
            Constructor(a: A; a: Int) { }
        }
        Class Program {
            Var b: A;
            Var a: E = New E(b);
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """
        Class A { }
        Class E {
            Var a : Int;
            Constructor(a: A) { }
        }
        Class Program {
            Var b: A;
            Var a: E = New E(b);
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test54(self):
        input = """
        Class A { }
        Class E {
            Var a : Int;
            Constructor(a: A) { }
        }
        Class Program {
            main() {
                Val a: Int = 3;
                Val a: Float = 4.5;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            Var $a:Int = 5;
                            Var b:Int = 4;
                        }         
                        Class B{
                        func(){
                            Var b:Int = A::$a;
                            b = A.b;
                        }
                        }"""
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test56(self):
        input = """
        Class A { }
        Class Program {
            main() {
                Val a: Array[Array[Array[Int,2],2],2]
                = Array(
                    Array(
                        Array(1,2),
                        Array(1,2)
                    ),
                    Array(
                        Array(2,3),
                        Array(5,7)
                    )
                );
                a[0][1] = 9;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1)]),IntLit(9))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test57(self):
        input = """
        Class A { }
        Class Program {
            main() {
                Val a: Array[Array[Array[Int,2],2],2]
                = Array(
                    Array(
                        Array(1,2),
                        Array(1,2)
                    ),
                    Array(
                        Array(2,3),
                        Array(5,7)
                    )
                );
                a = Array(5,6);
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),[IntLit(5),IntLit(6)])"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test58(self):
        input = """
        Class A { }
        Class Program {
            main() {
                Var a: Array[Array[Array[Int,2],2],2]
                = Array(
                    Array(
                        Array(1,2),
                        Array(1,2)
                    ),
                    Array(
                        Array(2,3),
                        Array(5,7)
                    )
                );
                a = Array(5,6);
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(5),IntLit(6)])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test59(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        }         
                        Class B{
                        func(){
                            Var b:A = New A();
                            Var c:Int = A::$a();
                            c = b.b();
                            c = A.b();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(A),Id(b),[])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test60(self):
        input = """
        Class D {
            Constructor() {}
            Destructor() {}
            Var d1 : D = New D();
            Var d2 : D = New D();
            func()
            {
                Return New D();
            }
            Lucy(a : String; position : Int)
            {
                Return "a" +. a;
            }
        }
        Class C {
            Constructor() { }
            Destructor () { }
            Var c1 : C = New C();
            Var c2 : String = "4";
            Var c3 : D = New D();
            func()
            {
                Return Self.c3;
            }
        }
        Class A{
            Constructor () { }
            Destructor () { }
            Var a1 : A = New A();
            Var a2 : C = New C();
            func()
            {
                Return Self.a2;
            }
            test()
            {
                Var d : String = Self.func().c1.func().func().d1.d2.Lucy("Tracy", 21);
                Var a : A = New A();
                Var e : String = a.func().c1.func().func().d1.d2.Lucy("Lucy", 20);
                Var f : String = a.func().c1.func().func().d1.Lucy(e, 5.5);
                Return 2;
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(FieldAccess(CallExpr(CallExpr(FieldAccess(CallExpr(Id(a),Id(func),[]),Id(c1)),Id(func),[]),Id(func),[]),Id(d1)),Id(Lucy),[Id(e),FloatLit(5.5)])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test61(self):
        input = """
        Class A {

        }
        Class D {
            Var a: A = New A(1,2,3);
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(){
                                Return 1;
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(a:Int){
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test64(self):
        input = """
        Class A {
            Constructor () {
                Return 45;
            }
            Destructor () { }
        }
        Class D {
            Var a: A = New A();
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(45))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test65(self):
        input = """
        Class A {
            Constructor (a: Int; b: Float) {
                Return;
            }
            Destructor () { 
                Return;
            }
        }
        Class D {
            Var a: A = New A();
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test66(self):
        input = """
        Class E {
            Var e: Int;
            Constructor (a: Int; b: Float) {
                Return;
            }
            Destructor () { }
        }
        Class D {
            Var a: Int = E.e;
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(E),Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test67(self):
        input = """
        Class E {
            Var e: Int;
            Constructor (a: Int; b: Float) {
                Return;
            }
            Destructor () { }
        }
        Class Program {
            main() {
                Return 2;
                Return "Hello";
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 467))
  
    def test68(self):
        input = """
        Class E {
            Var e: Int;
            Constructor (a: Int; b: Float) {
                Return;
            }
            Destructor () {
                Return;
            }
        }
        Class D {
            main() {
                Var i: Int = 2;
                Foreach(i In -1 .. 100) {
                    If (i > 3) {
                        Var j: Int = 4;
                        Foreach (j In -5 .. 9) {
                            If ((i > j) && (i + j == 9)) {
                                Break;
                            }
                            Elseif (i < j) {
                                Continue;
                            }
                            Return 12;
                        }
                    }
                }
            }
        }
        Class B {
            Var d: D;
            Var b: Int = Self.d.main();
        }
        Class Program{main(){}}
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test69(self):
        """Simple program: int main() {} """
        input = """     
                        Class B{
                        Var x:Int = 1;
                        foo(){
                            Return 1;
                        }
                        func (){
                            Var a:Int = Self.x;
                            a = Self.foo();
                            Var b:String = Self.foofoo();
                        }
                        } """
        expect = "Undeclared Method: foofoo"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test70(self):
        input = """
        Class D {
            main() {
                Var i: Int = 2;
                Foreach(i In -1 .. 100) {
                    Var j: Int = 4;
                    Foreach (j In -5 .. 9) {
                        Return 12;
                    }
                    Var k: Int;
                    Foreach (j In 10 .. 20) { 
                        Continue;
                        Foreach (k In 12 .. 234) { 
                            Break; 
                            Foreach (i In 10 .. 100) { 
                                Return "String";
                            }
                        }
                        
                    }
                }
            }
        }
        Class E {
            Var d: D;
            Var e: Int = Self.d.main();
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(e),IntType,CallExpr(FieldAccess(Self(),Id(d)),Id(main),[]))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test71(self):
        input = """
        Class D {
            main() {
                Var i: Int = 2;
                Foreach(i In -1 .. 100) {
                    Var j: Int = 4;
                    Foreach (j In -5 .. 9) {
                        Return;
                    }
                    Var k: Int;
                    Foreach (j In 10 .. 20) { 
                        Continue;
                        Foreach (k In 12 .. 234) { 
                            Break; 
                            Foreach (i In 10 .. 100) { 
                                Return "String";
                            }
                        }
                    }
                }
            }
        }
        Class E {
            Var d: D;
            Var e: Int = Self.d.main();
        }
        Class Program{main(){}}
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(e),IntType,CallExpr(FieldAccess(Self(),Id(d)),Id(main),[]))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test72(self):
        input = """
        Class D {
            main() {
                Var a:Int=3;
                Var b: Array[Int,2]=Array(a,2);
                Val c:Int = b[1];
            }
        }
        Class E {
            Var d: D;
            Var e: Int = Self.d.main();
        }
        """
        expect = "Illegal Constant Expression: ArrayCell(Id(b),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test73(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $func() {                        
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                E::$func();   
                                E::$foo();                             
                            }
                        }"""
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test74(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $func() { 
                                Return 1;                       
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                Var a:Int = E::$func();   
                                Var b:Int = E::$foo();                             
                            }
                        }"""
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test75(self):
        input = """
        Class Program {
            Var d: Int;
            main() { }
        }
        Class B {
            Val c: B = New B();
            Val d: Boolean = True;
            Var a: Program;
            getB() {
                Self.d = Self.a.d;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(d)),FieldAccess(FieldAccess(Self(),Id(a)),Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test76(self):
        input = """
        Class Program {
            Var d: Int;
            main() { }
        }
        Class B {
            Val c: B = New B();
            Var d: Boolean = True;
            Var a: Program;
            getB() {
                Self.d = Self.a.d;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(d)),FieldAccess(FieldAccess(Self(),Id(a)),Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test77(self):
        input = """
        Class Program {
            Var d: Int;
            main() { }
            Constructor (a: Int; b: Int; c: Int) { }
        }
        Class B {
            Val c: B = New B();
            Var d: Boolean = True;
            Var a: Program;
            getB() {
                Self.d = Self.a.d;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(d)),FieldAccess(FieldAccess(Self(),Id(a)),Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test78(self):
        input = """
        Class Program {
            Var d: Int;
            main() { }
            Constructor (a: Int; b: Int; c: Int) { }
        }
        Class B {
            Val c: B = New B();
            Var d: Boolean = True;
            Var a: Program;
            getB() {
                Self.d = B.d;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(B),Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test79(self):
        input = Program([
        ClassDecl(
            Id("Program"),
            [
                MethodDecl(
                    Static(),
                    Id("main"),
                    [],
                    Block([])
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        StringType(),
                        StringLiteral("Hello World")
                    )
                ),
                AttributeDecl(
                    Instance(),
                    VarDecl(
                        Id("myVar"),
                        IntType()
                    )
                )
            ]
        )
    ])
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test80(self):
        input = """
        Class Program {
            main(a: Int) { }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test81(self):
        input = """
        Class Program {
            main() { Return 2; }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82(self):
        input = """
        Class Program {
            main() { }
            main() { Return 2; }
        }
        """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test83(self):
        input = """
        Class Program {
            main() { }
            Constructor () {
                Return 1 + 8.0;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,IntLit(1),FloatLit(8.0)))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test84(self):
        input = """
        Class Program {
            main() { }
        }
        Class A {

        }
        Class B {
            foo() { 
                Var a,b: Boolean;
                Var r, pi, t: Int;
                If (a) {
                    a = False;
                }
                Elseif (b) {
                    Var c: Int = 8;
                }
                Elseif (12 == 8) {
                    r = 1;
                    pi = 3;
                }
                Elseif (9 > 0) {
                    r = 6;
                }
                Else {
                    t = a;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(t),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test85(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a:Array[Int, 2] = Array(1,1);
                                a = Array(1,1,1);
                           }               
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test86(self):
        input = """
        Class Program {
            main() { Return; }
        }
        Class Largest {
            Var a: Int = 2;
            $main(args: Array[String, 10000]) {
                Var a: Array[Int, 2] = Array(Self.a, 3);
                Val c: Int = a[1];
            }
            }
        """
        expect = "Illegal Constant Expression: ArrayCell(Id(a),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test87(self):
        input = """
        Class A{
            Var B: Int = 10;
        }
        Class Program {
            Var C: A = New A();
            main(){
                Val b: Int = Self.C.B;
            }
        }
        """
        expect = 'Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(C)),Id(B))'
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test88(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                            }
                        }
                         Class Car {
                            Var a : Int = 10;
                            foo() {
                                Var x : Int = Self.a;
                                Var y : Int = a;
                            }
                        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test99(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           fooExp(x:Float; y:String){
                                Return 1;
                           }  
                           fooCall(x:Float; y:String){}                    
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            foo(){
                                Return New A();
                            }
                            foo2(){
                                Var e:Int = Self.b.a;
                                e = Self.b.fooExp(1, "a");
                                e = Self.foo().a;
                                e = Self.foo().fooExp(1, "a");
                                Self.b.fooCall(1, "a");
                                Self.foo().fooCall(1, "a");
                                Self.g().fooCall(1, "a");
                            }
                        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test90(self):
        input = """
        Class A {
            Constructor () {
                Return 45;
            }
            Destructor () { }
        }
        Class D {
            Var a: A = New A();
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(45))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test91(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(){
                                Val a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                a[1] = Array(1,1);
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(1)]),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                        Val a:Int = 2;
                           $fooExp1(){
                                Self.a = "abc";
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test93(self):
        """Simple program: int main() {} """
        input = """
                         Class Car {
                            foo() {
                                Var a:Array[Int,2];
                                a = Array(1,2);
                                a = Array(1,2.3);
                            }
                        }"""
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.3)]"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test94(self):
        input = """
                Class A {
                    foo() {
                        Var a: Array[Int, 3] = Array(1,2,3);
                        a[4] = 5; ## Index out of bound ##
                        a[1][2] = 4; ## Error with dimension##
                    }
                }
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test95(self):
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
                                Var myStudent: Student = New Student ();
                            }
                        }
            """

        expect = "Type Mismatch In Expression: NewExpr(Id(Student),[])"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test96(self):
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New C();
                        }
            """

        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test97(self):
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New B();
                        }
            """

        expect = "Type Mismatch In Statement: VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(B),[]))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test98(self):
        input = """
                        Class Program{
                            Val $someStatic : Int = 10;
                            foo() {
                                Var Program : Float = 1.0;
                                Var x : Int = Program::$someStatic;
                           }
                        }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test99(self):
        """Simple program: int main() {} """
        input = """
                    Class c{
                        Var a:Int;
                        Var b:Int;
                        Var c:Int;
                    }
                    Class a{
                    Var a:Int;
                    Var a:Int;
                    }
                    Class b{}
                    Class d{}"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 499))