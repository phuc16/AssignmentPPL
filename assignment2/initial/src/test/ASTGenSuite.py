import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test0(self):
        input = """
            Class Dog: Animal { }
            Class Snake: De { }
            Class butterfly {
                __str__() {
                    Var a, b, c, d, e: Int = 0,0,0,0,0;
                    Val a,b,c,d,e: Int;
                }
            }
            """
        expect = "Program([ClassDecl(Id(Dog),Id(Animal),[]),ClassDecl(Id(Snake),Id(De),[]),ClassDecl(Id(butterfly),[MethodDecl(Id(__str__),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),VarDecl(Id(d),IntType,IntLit(0)),VarDecl(Id(e),IntType,IntLit(0)),ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None),ConstDecl(Id(c),IntType,None),ConstDecl(Id(d),IntType,None),ConstDecl(Id(e),IntType,None)]))])])"
        self.assertTrue(TestAST.test(input, expect, 200))

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
        expect = "Program([ClassDecl(Id(Dog),Id(Animal),[MethodDecl(Id($gaugau),Static,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(7),IntLit(2)]))]))]),ClassDecl(Id(Snake),Id(De),[MethodDecl(Id($OpOp),Static,[],Block([Return(FieldAccess(Self(),Id(Op)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 201))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getName),Instance,[],Block([VarDecl(Id(b),FloatType,FloatLit(0.3))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType)]))])])"
        self.assertTrue(TestAST.test(input, expect, 202))
    
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
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(getName),Instance,[],Block([VarDecl(Id(b),FloatType,FloatLit(0.3))])),MethodDecl(Id(func),Instance,[],Block([If(BinaryOp(>=,Id(a),Id(b)),Block([VarDecl(Id(a),IntType,IntLit(0)),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3)))]),If(BinaryOp(>=,Id(b),Id(c)),Block([Call(Self(),Id(getName),[BinaryOp(>=,Id(a),Id(b))])]),If(BinaryOp(>=,IntLit(12),Id(g)),Block([Call(Self(),Id(insert),[StringLit(String)])]),Block([AssignStmt(Id(GiaBao),Id(Hieu)),AssignStmt(Id(Hung),Id(Vi))]))))])),MethodDecl(Id(setAge),Instance,[param(Id(age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(age)),Id(age))]))])])"
        self.assertTrue(TestAST.test(input, expect, 203))
    
    def test4(self):
        input = """ 
            Class MeowMeow: Dog {
                Var b: Int;
                Var $a, c, d: Float = .e4, 2., 78.9;
                Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
            }
            """
        expect = "Program([ClassDecl(Id(MeowMeow),Id(Dog),[AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(78.9))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)]))])])"
        self.assertTrue(TestAST.test(input, expect, 204))

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
        expect = "Program([ClassDecl(Id(mini),[MethodDecl(Id(loop),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([For(Id(i),IntLit(0),IntLit(150),BinaryOp(<=,Id(i),IntLit(8)),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),ArrayCell(Id(a),[Id(i)])))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 205))
    
    def test6(self):
        input = """
            Class Pro {
                Main(a: Int; b: Int) {
                    Return a || b < c.get(1,2) && 23 + 1.4;
                }
            }
            """
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id(Main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(<,BinaryOp(||,Id(a),Id(b)),BinaryOp(&&,CallExpr(Id(c),Id(get),[IntLit(1),IntLit(2)]),BinaryOp(+,IntLit(23),FloatLit(1.4)))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 206))
    
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
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id(MainMenu),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[IntLit(4)]),BinaryOp(+,CallExpr(Id(b),Id(getName),[]),CallExpr(Id(a),Id(exp),[])))]))]),ClassDecl(Id(ProMax),[MethodDecl(Id(iPhone13),Instance,[],Block([Return(IntLit(40000000))]))])])"
        self.assertTrue(TestAST.test(input, expect, 207))

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
        expect = "Program([ClassDecl(Id(MyClass),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(age),IntType,IntLit(0))),MethodDecl(Id($printName),Static,[],Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(name))])])),MethodDecl(Id(setAge),Instance,[param(Id(_age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(age)),Id(_age))]))])])"
        self.assertTrue(TestAST.test(input, expect, 208))

    def test9(self):
        input = """
            Class PPL {
                Var score: Int = 0x7_45;
                getScore() {
                    Self.score(a,b,c);
                    Return score;
                }
            }
        """
        expect = "Program([ClassDecl(Id(PPL),[AttributeDecl(Instance,VarDecl(Id(score),IntType,IntLit(1861))),MethodDecl(Id(getScore),Instance,[],Block([Call(Self(),Id(score),[Id(a),Id(b),Id(c)]),Return(Id(score))]))])])"
        self.assertTrue(TestAST.test(input, expect, 209))

    def test10(self):
        input = """
            Class PPL {
                getScore(){

                }
            }
            Class quiz:PPL {
                getScore() {
                    Return quiz::$getScore();
                }
            }
        """
        expect = "Program([ClassDecl(Id(PPL),[MethodDecl(Id(getScore),Instance,[],Block([]))]),ClassDecl(Id(quiz),Id(PPL),[MethodDecl(Id(getScore),Instance,[],Block([Return(CallExpr(Id(quiz),Id($getScore),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 210))
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
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(0),IntLit(100),BinaryOp(<=,Id(e),Id(i)),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(1)]),ArrayCell(Id(b),[IntLit(1),IntLit(3),Id(i)])))])]),Return(BinaryOp(<=,Id(a),Id(b)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 211))

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
        expect = "Program([ClassDecl(Id(ari),[MethodDecl(Id($_getMethod),Static,[],Block([Return(BinaryOp(>=,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(12),FloatLit(1.2)),Id(c)),UnaryOp(!,Id(b))),BinaryOp(||,BinaryOp(||,IntLit(8),IntLit(4)),BinaryOp(+,Id(a),Id(b)))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(&&,BinaryOp(+,Id(myConst),Id(b)),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(abcde))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 212))

    def test13(self):
        input = """
            Class Champions{
                Var Name : String;
                Var Skill : Array[String, 4];
            }
            Class Yasuo {
                getHP() {
                    Return Self.HP;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Champions),[AttributeDecl(Instance,VarDecl(Id(Name),StringType)),AttributeDecl(Instance,VarDecl(Id(Skill),ArrayType(4,StringType)))]),ClassDecl(Id(Yasuo),[MethodDecl(Id(getHP),Instance,[],Block([Return(FieldAccess(Self(),Id(HP)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 213))

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
        expect = "Program([ClassDecl(Id(myVar),[MethodDecl(Id(Constructor),Instance,[param(Id(arr),ArrayType(3,FloatType))],Block([AssignStmt(FieldAccess(Self(),Id(a)),ArrayCell(Id(arr),[IntLit(1)])),AssignStmt(FieldAccess(Self(),Id(b)),ArrayCell(Id(arr),[IntLit(2)])),AssignStmt(FieldAccess(Self(),Id(c)),ArrayCell(Id(arr),[IntLit(2),IntLit(1)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 214))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Des),[MethodDecl(Id(Destructor),Instance,[],Block([Call(CallExpr(Id(Stand),Id(Delete),[]),Id(All),[IntLit(0)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 215))

    def test16(self):
        input = """
            Class Main {
                menu() {
                    t = R::$test()[2] >= 8;
                    Return Self.arr;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Main),[MethodDecl(Id(menu),Instance,[],Block([AssignStmt(Id(t),BinaryOp(>=,ArrayCell(CallExpr(Id(R),Id($test),[]),[IntLit(2)]),IntLit(8))),Return(FieldAccess(Self(),Id(arr)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 216))

    def test17(self):
        input = """
            Class Program {
                dethod() {
                    Return Self.method();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(dethod),Instance,[],Block([Return(CallExpr(Self(),Id(method),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 217))

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
        expect = "Program([ClassDecl(Id(Meow),[MethodDecl(Id(returnMethod),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(init)),Id(value))])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Mew),Id(EraseAll),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 218))

    def test19(self):
        input = """
            Class foo {
                Var Foo: Array[Int, 5] = 0xFF;
            }
        """
        expect = "Program([ClassDecl(Id(foo),[AttributeDecl(Instance,VarDecl(Id(Foo),ArrayType(5,IntType),IntLit(255)))])])"
        self.assertTrue(TestAST.test(input, expect, 219))

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
        expect = "Program([ClassDecl(Id(ari),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Call(Id(Out),Id(print),[StringLit(Contructor)])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Out),Id(print),[StringLit(Destructor)])])),MethodDecl(Id($_getMethod),Static,[],Block([Return(BinaryOp(>=,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(12),FloatLit(1.2)),Id(c)),UnaryOp(!,Id(b))),BinaryOp(||,BinaryOp(||,IntLit(8),IntLit(4)),BinaryOp(+,Id(a),Id(b)))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Call(Id(Out),Id(print),[StringLit(Contructor)])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Out),Id(print),[StringLit(Destructor)])])),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(&&,BinaryOp(+,Id(myConst),Id(b)),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(abcde))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 220))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[StringLit(Hello From Main)])]))]),ClassDecl(Id(iden),[])])"
        self.assertTrue(TestAST.test(input, expect, 221))

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
        expect = "Program([ClassDecl(Id(myFunc),[MethodDecl(Id(func),Instance,[param(Id(s),IntType),param(Id(r),StringType)],Block([Return(CallExpr(Id(Stand),Id(Str),[BinaryOp(+,Id(s),Id(r))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 222))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(class1),[AttributeDecl(Instance,VarDecl(Id(name),StringType))]),ClassDecl(Id(class2),[AttributeDecl(Static,ConstDecl(Id($height),FloatType,FloatLit(1.75)))])])"
        self.assertTrue(TestAST.test(input, expect, 223))

    def test24(self):
        input = """
            Class obj {
                Var _obj, _obj_: Int = 0, 9;
            }
            Class Program {
                main() {
                    Return Self.arr;
                }
            }
        """
        expect = "Program([ClassDecl(Id(obj),[AttributeDecl(Instance,VarDecl(Id(_obj),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(_obj_),IntType,IntLit(9)))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(FieldAccess(Self(),Id(arr)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 224))

    def test25(self):
        input = """
            Class Program {
                main() {
                    Var a,b: Array[Float, 4];
                }
            }
            Class lop {
                attr(a, b: Int) {
                    Return a[4] != b[1];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(4,FloatType)),VarDecl(Id(b),ArrayType(4,FloatType))]))]),ClassDecl(Id(lop),[MethodDecl(Id(attr),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(!=,ArrayCell(Id(a),[IntLit(4)]),ArrayCell(Id(b),[IntLit(1)])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 225))

    def test26(self):
        input = """
            Class parent {
                Var lname, fname: String = "1914720", "Phuc";
                $getName() {
                    Return Self.name[2];
                }
                setName(name: Int) {
                    lname = name[0];
                }
            }
        """
        expect = "Program([ClassDecl(Id(parent),[AttributeDecl(Instance,VarDecl(Id(lname),StringType,StringLit(1914720))),AttributeDecl(Instance,VarDecl(Id(fname),StringType,StringLit(Phuc))),MethodDecl(Id($getName),Static,[],Block([Return(ArrayCell(FieldAccess(Self(),Id(name)),[IntLit(2)]))])),MethodDecl(Id(setName),Instance,[param(Id(name),IntType)],Block([AssignStmt(Id(lname),ArrayCell(Id(name),[IntLit(0)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 226))

    def test27(self):
        input = """
            Class Program {
                main() {
                    Return New object();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(NewExpr(Id(object),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 227))

    def test28(self):
        input = """
            Class Program {
                main(a: Int; b: Float) {
                    Return New A().B().C();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([Return(CallExpr(CallExpr(NewExpr(Id(A),[]),Id(B),[]),Id(C),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 228))

    def test29(self):
        input = """
            Class Func {
                Constructor(){Return name;}
            }
            Class B {

            }
        """
        expect = "Program([ClassDecl(Id(Func),[MethodDecl(Id(Constructor),Instance,[],Block([Return(Id(name))]))]),ClassDecl(Id(B),[])])"
        self.assertTrue(TestAST.test(input, expect, 229))

    def test30(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class className {
                Destructor() {

                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(className),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 230))

    def test31(self):
        input = """
            Class Dog {
                Var name: Int;
                Var age: Int = 20;
            }
            Class Program {
                main() {

                }
            }
        """
        expect = "Program([ClassDecl(Id(Dog),[AttributeDecl(Instance,VarDecl(Id(name),IntType)),AttributeDecl(Instance,VarDecl(Id(age),IntType,IntLit(20)))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 231))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(idx),IntLit(1),BinaryOp(+,IntLit(100),IntLit(5)),BinaryOp(>=,ArrayCell(Id(a),[Id(i)]),IntLit(9)),Block([If(BinaryOp(!=,ArrayCell(Id(a),[Id(i),IntLit(1)]),ArrayCell(Id(b),[IntLit(1)])),Block([Return()]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 232))

    def test33(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class Another {
                function() {
                    A.Main();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Another),[MethodDecl(Id(function),Instance,[],Block([Call(Id(A),Id(Main),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 233))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Name),[MethodDecl(Id(hello),Instance,[param(Id(s1),StringType),param(Id(s2),StringType),param(Id(s3),StringType)],Block([Return(CallExpr(Id(Str),Id(concat),[Id(s1),Id(s2),Id(s3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 234))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[CallExpr(Id(Dog),Id(sound),[])])]))]),ClassDecl(Id(Dog),[MethodDecl(Id(sound),Instance,[],Block([Return(CallExpr(NewExpr(Id(Animal),[]),Id(dogSound),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 235))

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
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(obj),[StringLit(string 1)])),Call(Id(Out),Id(print),[FieldAccess(Id(a),Id(age))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 236))

    def test37(self):
        input = """
             Class limitSpeed {
                newLimit(a: String) {
                    Return "Limit speed \\nat" ;
                }
            }
        """
        expect = "Program([ClassDecl(Id(limitSpeed),[MethodDecl(Id(newLimit),Instance,[param(Id(a),StringType)],Block([Return(StringLit(Limit speed \\nat))]))])])" 
        self.assertTrue(TestAST.test(input, expect, 237))

    def test38(self):
        input = """
            Class Program {
                Var a, b, c: Int = 1, 2, 3 >= 9 + 5;
                main() {
                    If (a >= b) {
                        Foreach (i In 0 .. c.length By 1) {
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
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(>=,IntLit(3),BinaryOp(+,IntLit(9),IntLit(5))))),MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>=,Id(a),Id(b)),Block([For(Id(i),IntLit(0),FieldAccess(Id(c),Id(length)),IntLit(1),Block([If(ArrayCell(Id(c),[Id(i)]),Block([Continue]),Block([Break]))])])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 238))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(newClass),[AttributeDecl(Instance,ConstDecl(Id(count),IntType,IntLit(150))),AttributeDecl(Instance,ConstDecl(Id(sum),FloatType,FloatLit(10.2))),AttributeDecl(Instance,ConstDecl(Id(rate),FloatType,FloatLit(34.4))),MethodDecl(Id(PrintOut),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(count)),FieldAccess(Self(),Id(rate))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 239))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Stand),Id(getVector),[])]))]),ClassDecl(Id(myClass),[MethodDecl(Id($method),Static,[],Block([Return(ArrayCell(CallExpr(Self(),Id(sound),[]),[IntLit(2)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 240))

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
        expect = "Program([ClassDecl(Id(class),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(4))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(5))),MethodDecl(Id($print),Static,[],Block([Return([Id(a),Id(b),Id(c)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 241))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Par),[AttributeDecl(Instance,VarDecl(Id(con),StringType)),AttributeDecl(Instance,VarDecl(Id(me),FloatType,FloatLit(0.2))),MethodDecl(Id($get),Static,[],Block([Call(FieldAccess(Id(Local),Id(Store)),Id(sieuthi),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 242))

    def test43(self):
        input = """
            Class League {
                getVersion() {
                    Return Self.name(i) || Self.Skill;
                }
            }
        """
        expect = "Program([ClassDecl(Id(League),[MethodDecl(Id(getVersion),Instance,[],Block([Return(BinaryOp(||,CallExpr(Self(),Id(name),[Id(i)]),FieldAccess(Self(),Id(Skill))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 243))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([For(Id(i),IntLit(1),Id(len),IntLit(2),Block([Continue])])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 244))

    def test45(self):
        input = """
            Class Program {
                main() {
                    Dog.name = Cat.name +. "1";
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(Dog),Id(name)),BinaryOp(+.,FieldAccess(Id(Cat),Id(name)),StringLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 245))

    def test46(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class Meo: Dog {
                $get() {
                    Self.name = Dog::$name;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Meo),Id(Dog),[MethodDecl(Id($get),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(name)),FieldAccess(Id(Dog),Id($name)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 246))

    def test47(self):
        input = """
        Class Client{
            Check(){
            If (player >= 10000) {
                    Return a;
                }
            }
            
        } 
        """
        expect = "Program([ClassDecl(Id(Client),[MethodDecl(Id(Check),Instance,[],Block([If(BinaryOp(>=,Id(player),IntLit(10000)),Block([Return(Id(a))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 347))


    def test48(self):
        input = """
            Class Program {
                main() {
                    Foreach (i In 0 .. 10 By 1 + 2 + 3 + a.get - b.name) {
                        Continue;
                        Break;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(0),IntLit(10),BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),FieldAccess(Id(a),Id(get))),FieldAccess(Id(b),Id(name))),Block([Continue,Break])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 248))

    def test49(self):
        input = """
            Class Champions {
                method() {
                    Return Champs[Q][K][A] + Champ.name()[0];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Champions),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(Champs),[Id(Q),Id(K),Id(A)]),ArrayCell(CallExpr(Id(Champ),Id(name),[]),[IntLit(0)])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 249))

    def test50(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class B: A {
                Var a, b: Float = 3.5, 5;
                main(a: Int) {
                    Return a;
                }
                
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(B),Id(A),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(3.5))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(5))),MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 250))

    def test51(self):
        input = """
            Class CSGO {
                bunny(){
                    Self.speed().acce().map();
                } 
            }
            
        """
        expect = "Program([ClassDecl(Id(CSGO),[MethodDecl(Id(bunny),Instance,[],Block([Call(CallExpr(CallExpr(Self(),Id(speed),[]),Id(acce),[]),Id(map),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 251))

    def test52(self):
        input = """
            Class CSGO {
                fireRate() {
                    setRate = Gun::$increaseAccord(1,2)[1];
                    setRecoil = Gun.setAccord()[x][y][z];
                }
            }
        """
        expect = "Program([ClassDecl(Id(CSGO),[MethodDecl(Id(fireRate),Instance,[],Block([AssignStmt(Id(setRate),ArrayCell(CallExpr(Id(Gun),Id($increaseAccord),[IntLit(1),IntLit(2)]),[IntLit(1)])),AssignStmt(Id(setRecoil),ArrayCell(CallExpr(Id(Gun),Id(setAccord),[]),[Id(x),Id(y),Id(z)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 252))

    def test53(self):
        input = """
            Class CSGO{ 
                Var agentAccelerate: Float = 0xA001;
                Val $confirmKill, $confirmDeath: Boolean = True, True;
            }
        """
        expect = "Program([ClassDecl(Id(CSGO),[AttributeDecl(Instance,VarDecl(Id(agentAccelerate),FloatType,IntLit(40961))),AttributeDecl(Static,ConstDecl(Id($confirmKill),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($confirmDeath),BoolType,BooleanLit(True)))])])"
        self.assertTrue(TestAST.test(input, expect, 253))

    def test54(self):
        input = """
            Class V {
                Val arr: Array[Array[Int, 0b1], 0xAF];
            }
        """
        expect = "Program([ClassDecl(Id(V),[AttributeDecl(Instance,ConstDecl(Id(arr),ArrayType(175,ArrayType(1,IntType)),None))])])"
        self.assertTrue(TestAST.test(input, expect, 254))

    def test55(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class B {$method(){}}
            Class C {$method(){}}
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(B),[MethodDecl(Id($method),Static,[],Block([]))]),ClassDecl(Id(C),[MethodDecl(Id($method),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 255))

    def test56(self):
        input = """
            Class CSGO {
                Val gunDame : Array[Array[Int,2],2] = gun[Dame[0b1001]];
                setRecoil(){
                    {
                        {Return recoil;}
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(CSGO),[AttributeDecl(Instance,ConstDecl(Id(gunDame),ArrayType(2,ArrayType(2,IntType)),ArrayCell(Id(gun),[ArrayCell(Id(Dame),[IntLit(9)])]))),MethodDecl(Id(setRecoil),Instance,[],Block([Block([Block([Return(Id(recoil))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 256))

    def test57(self):
        input = """
            Class B: A {
                Var b: Int = 0;
            }
        """
        expect = "Program([ClassDecl(Id(B),Id(A),[AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input, expect, 257))

    def test58(self):
        input = """
            Class B {
                Var b, c : Int = 10, 42;
            }
        """
        expect = "Program([ClassDecl(Id(B),[AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(42)))])])"
        self.assertTrue(TestAST.test(input, expect, 258))

    def test59(self):
        input = """
            Class i {
                method() {
                    a = Self.age + 34 - 9 * B.getString();
                }
            }
        """
        expect = "Program([ClassDecl(Id(i),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,FieldAccess(Self(),Id(age)),IntLit(34)),BinaryOp(*,IntLit(9),CallExpr(Id(B),Id(getString),[]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 259))

    def test60(self):
        input = """
            Class FO4 {
                createPlayer() {
                    playerBool[0] = "name" ==. ": age \\'";
                }
            }
        """
        expect = "Program([ClassDecl(Id(FO4),[MethodDecl(Id(createPlayer),Instance,[],Block([AssignStmt(ArrayCell(Id(playerBool),[IntLit(0)]),BinaryOp(==.,StringLit(name),StringLit(: age \\')))]))])])"
        self.assertTrue(TestAST.test(input, expect, 260))

    def test61(self):
        input = """
            Class graphic {
                Computer(){
                    {{{{{{}}}}}}
                }
            }
        """
        expect = "Program([ClassDecl(Id(graphic),[MethodDecl(Id(Computer),Instance,[],Block([Block([Block([Block([Block([Block([Block([])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 261))

    def test62(self):
        input = """
            Class Program {
                Constructor(a, b: Float; c: Int) {
                    a = c + 1;
                    Return;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType),param(Id(b),FloatType),param(Id(c),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,Id(c),IntLit(1))),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 262))

    def test63(self):
        input = """
            Class Construc {
                Destruc() {
                    Des.DeleteAll();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Construc),[MethodDecl(Id(Destruc),Instance,[],Block([Call(Id(Des),Id(DeleteAll),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 263))

    def test64(self):
        input = """
            Class C {
                Var a: Int = 10;
                Val constVar: String = "Hello";
                Val a,b,c: Int = 0.9, 1.0, 1.1;
            }
        """
        expect = "Program([ClassDecl(Id(C),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(10))),AttributeDecl(Instance,ConstDecl(Id(constVar),StringType,StringLit(Hello))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,FloatLit(0.9))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,FloatLit(1.0))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,FloatLit(1.1)))])])"
        self.assertTrue(TestAST.test(input, expect, 264))

    def test65(self):
        input = """
            Class Program {
                main() {
                    Return main.text();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(CallExpr(Id(main),Id(text),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 265))

    def test66(self):
        input = """
            Class Program {
                Var b: Int = A::$f()[1] + a.g() * 4 + !y;
                Var a: Stu = New Teach(New Stu());
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(+,ArrayCell(CallExpr(Id(A),Id($f),[]),[IntLit(1)]),BinaryOp(*,CallExpr(Id(a),Id(g),[]),IntLit(4))),UnaryOp(!,Id(y))))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Stu)),NewExpr(Id(Teach),[NewExpr(Id(Stu),[])])))])])"
        self.assertTrue(TestAST.test(input, expect, 266))

    def test67(self):
        input = """
            Class method {
                $getName() {
                    Out.print(B::$name);
                    Return C.get;
                }
            }
        """
        expect = "Program([ClassDecl(Id(method),[MethodDecl(Id($getName),Static,[],Block([Call(Id(Out),Id(print),[FieldAccess(Id(B),Id($name))]),Return(FieldAccess(Id(C),Id(get)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 267))

    def test68(self):
        input = """
            Class Method: Param {
                m() {
                    a = T::$get() + New X().G() - A.b().f().t();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Method),Id(Param),[MethodDecl(Id(m),Instance,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,CallExpr(Id(T),Id($get),[]),CallExpr(NewExpr(Id(X),[]),Id(G),[])),CallExpr(CallExpr(CallExpr(Id(A),Id(b),[]),Id(f),[]),Id(t),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 268))

    def test69(self):
        input = """
            Class Program {
                main() {
                    a[1][2][3][4] = b.c(d[1]);
                }
                method () { }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]),CallExpr(Id(b),Id(c),[ArrayCell(Id(d),[IntLit(1)])]))])),MethodDecl(Id(method),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 269))

    def test70(self):
        input = """
            Class E {
                method() {
                    Return a[1][2][3] + className.b()[4];
                }
            }
        """
        expect = "Program([ClassDecl(Id(E),[MethodDecl(Id(method),Instance,[],Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(CallExpr(Id(className),Id(b),[]),[IntLit(4)])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 270))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(B),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(a)),Id(b)),IntLit(4)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 271))

    def test72(self):
        input = """
            Class Program{
                main(){
                    
                }
            }
            Class Fornite:Program{
                
            }
            Class Char : Fortnite{
                voice() {
                    Var stringVoice: String;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Fornite),Id(Program),[]),ClassDecl(Id(Char),Id(Fortnite),[MethodDecl(Id(voice),Instance,[],Block([VarDecl(Id(stringVoice),StringType)]))])])"
        self.assertTrue(TestAST.test(input, expect, 272))

    def test73(self):
        input = """
            Class Fortnite {
                method1() { }
                method2() { }
                main() { }
                main(a,b: Int) { }
            }
        """
        expect = "Program([ClassDecl(Id(Fortnite),[MethodDecl(Id(method1),Instance,[],Block([])),MethodDecl(Id(method2),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 273))

    def test74(self):
        input = """
            Class _R {
                Val $y: Int = 12;
                _F() {
                    Val _, _, _: String = 3, 4, 5;
                }
            }
        """
        expect = "Program([ClassDecl(Id(_R),[AttributeDecl(Static,ConstDecl(Id($y),IntType,IntLit(12))),MethodDecl(Id(_F),Instance,[],Block([ConstDecl(Id(_),StringType,IntLit(3)),ConstDecl(Id(_),StringType,IntLit(4)),ConstDecl(Id(_),StringType,IntLit(5))]))])])"
        self.assertTrue(TestAST.test(input, expect, 274))

    def test75(self):
        input = """
            Class Program {
                main() {
                    Out.ar();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(ar),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 275))

    def test76(self):
        input = """
            Class Program {
                Var stu: Stu = New Stu();
                mainStu() {
                    Stu[1] = FUNC.stu().stu1().stu2()[5];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(stu),ClassType(Id(Stu)),NewExpr(Id(Stu),[]))),MethodDecl(Id(mainStu),Instance,[],Block([AssignStmt(ArrayCell(Id(Stu),[IntLit(1)]),ArrayCell(CallExpr(CallExpr(CallExpr(Id(FUNC),Id(stu),[]),Id(stu1),[]),Id(stu2),[]),[IntLit(5)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 276))

    def test77(self):
        input = """
            Class myArray {
                Var Arr: Array[Array[Int, 2], 0b11000];
            }
        """
        expect = "Program([ClassDecl(Id(myArray),[AttributeDecl(Instance,VarDecl(Id(Arr),ArrayType(24,ArrayType(2,IntType))))])])"
        self.assertTrue(TestAST.test(input, expect, 277))

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
        expect = "Program([ClassDecl(Id(myArray),[AttributeDecl(Instance,VarDecl(Id(Arr),ArrayType(3,IntType),[[IntLit(3),IntLit(4),IntLit(5)],[IntLit(1),IntLit(2)]])),MethodDecl(Id(Method),Instance,[],Block([Call(Id(Out),Id(print),[ArrayCell(Id(Arr),[IntLit(1),IntLit(2)])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 278))

    def test79(self):
        input = """
            Class Fortnite{
            Var a: Array[Array[String, 3],3] = Array (
                Array("Shotgun", "22", "18"),
                Array("Ak", "5", "2"),
                Array("Hand gun", "17", "15")
            );
        }
        """
        expect = "Program([ClassDecl(Id(Fortnite),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Shotgun),StringLit(22),StringLit(18)],[StringLit(Ak),StringLit(5),StringLit(2)],[StringLit(Hand gun),StringLit(17),StringLit(15)]]))])])"
        self.assertTrue(TestAST.test(input, expect, 279))

    def test80(self):
        input = """
            Class BubbleSort {
                Var arr: Array[Int, 1000000];
                $sort() {
                    Var i, j: Int;
                    Foreach (i In 0 .. n - 1) {
                        Foreach (j In 0 .. n - i - 1) {
                            If (arr[j] > arr[j+1]) {
                                Std.swap(arr[j], arr[j+1]);
                            }
                        }
                    }
                }
                set(arr: Array[Int, 1000000]) {
                    Self.arr = arr;
                }
            }
        """
        expect = "Program([ClassDecl(Id(BubbleSort),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000000,IntType))),MethodDecl(Id($sort),Static,[],Block([VarDecl(Id(i),IntType),VarDecl(Id(j),IntType),For(Id(i),IntLit(0),BinaryOp(-,Id(n),IntLit(1)),IntLit(1),Block([For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,Id(n),Id(i)),IntLit(1)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])),Block([Call(Id(Std),Id(swap),[ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[BinaryOp(+,Id(j),IntLit(1))])])]))])])])])])),MethodDecl(Id(set),Instance,[param(Id(arr),ArrayType(1000000,IntType))],Block([AssignStmt(FieldAccess(Self(),Id(arr)),Id(arr))]))])])"
        self.assertTrue(TestAST.test(input, expect, 280))

    def test81(self):
        input = """
            Class dfskjf_jdss {
                Rfsfsa() {
                    Val r: Int = 20;
                }
            }
        """
        expect = "Program([ClassDecl(Id(dfskjf_jdss),[MethodDecl(Id(Rfsfsa),Instance,[],Block([ConstDecl(Id(r),IntType,IntLit(20))]))])])"
        self.assertTrue(TestAST.test(input, expect, 281))

    def test82(self):
        input = """
            Class D96 {
                Construc() {
                    Val arr: Array[Array[Array[Float, 1],0x3_23],4];
                }
            }
        """
        expect = "Program([ClassDecl(Id(D96),[MethodDecl(Id(Construc),Instance,[],Block([ConstDecl(Id(arr),ArrayType(4,ArrayType(803,ArrayType(1,FloatType))),None)]))])])"
        self.assertTrue(TestAST.test(input, expect, 282))

    def test83(self):
        input = """
            Class Soc {
                function() {
                    Return A::$name() + A.t();
                }
            }
        """
        expect = "Program([ClassDecl(Id(Soc),[MethodDecl(Id(function),Instance,[],Block([Return(BinaryOp(+,CallExpr(Id(A),Id($name),[]),CallExpr(Id(A),Id(t),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 283))
    
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
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(t),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(y),IntType,IntLit(2))),MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(r),ClassType(Id(Func)))],Block([If(BinaryOp(>,BinaryOp(+,Id(a),Id(b)),IntLit(0)),Block([For(Id(i),IntLit(1),IntLit(12),Id(r),Block([If(BinaryOp(+,IntLit(2),IntLit(5)),Block([If(BinaryOp(>=,Id(f),Id(t)),Block([Continue]))]))])])]),If(BinaryOp(*,Id(t),IntLit(7)),Block([If(IntLit(34),Block([]),Block([Return()]))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 284))
        
    def test85(self):
        input = """
            Class name {
                method () {
                    a = name::$age;
                    b = name::$age().b();
                    c = age;
                    d = name.age();
                }
            }
        """
        expect = "Program([ClassDecl(Id(name),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),FieldAccess(Id(name),Id($age))),AssignStmt(Id(b),CallExpr(CallExpr(Id(name),Id($age),[]),Id(b),[])),AssignStmt(Id(c),Id(age)),AssignStmt(Id(d),CallExpr(Id(name),Id(age),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 285))

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
        expect = "Program([ClassDecl(Id(MyClass),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(0))),MethodDecl(Id(Method),Instance,[],Block([Call(Self(),Id(constructor),[Id(a),Id(b),Id(c)]),Call(Id(name),Id(method),[]),If(Id(r),Block([Return(Id(t))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 286))

    def test87(self):
        input = """
            Class name {
                method () {
                    a = name::$age;
                    c = age;
                    e = name.age();
                }
            }
        """
        expect = "Program([ClassDecl(Id(name),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),FieldAccess(Id(name),Id($age))),AssignStmt(Id(c),Id(age)),AssignStmt(Id(e),CallExpr(Id(name),Id(age),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 287))

    def test88(self):
        input = """
            Class MyClass {
                Val count: Int = 0;
                setCount() {
                    Return Self.count + Self.count() - name::$turn() * age.Age();
                }
            }
        """
        expect = "Program([ClassDecl(Id(MyClass),[AttributeDecl(Instance,ConstDecl(Id(count),IntType,IntLit(0))),MethodDecl(Id(setCount),Instance,[],Block([Return(BinaryOp(-,BinaryOp(+,FieldAccess(Self(),Id(count)),CallExpr(Self(),Id(count),[])),BinaryOp(*,CallExpr(Id(name),Id($turn),[]),CallExpr(Id(age),Id(Age),[]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 288))

    def test89(self):
        input = """
            Class InLit: Type {
                __str__(str: String) {
                    Self.str = str;
                    Self.a = Self.count() + expr::$dollar() - expr.dollar();
                }
            }
        """
        expect = "Program([ClassDecl(Id(InLit),Id(Type),[MethodDecl(Id(__str__),Instance,[param(Id(str),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(str)),Id(str)),AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(-,BinaryOp(+,CallExpr(Self(),Id(count),[]),CallExpr(Id(expr),Id($dollar),[])),CallExpr(Id(expr),Id(dollar),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 289))

    def test90(self):
        input = """
            Class Note {
                m() {
                    a = name[0];
                    b = age.len[1][2];
                    c = age::$Len().t()[2];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Note),[MethodDecl(Id(m),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(name),[IntLit(0)])),AssignStmt(Id(b),ArrayCell(FieldAccess(Id(age),Id(len)),[IntLit(1),IntLit(2)])),AssignStmt(Id(c),ArrayCell(CallExpr(CallExpr(Id(age),Id($Len),[]),Id(t),[]),[IntLit(2)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 290))

    def test91(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class program {
                main() {

                }
            }
            Class TFT {
                main() {
                    nameLen = name[0];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(program),[MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(TFT),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(nameLen),ArrayCell(Id(name),[IntLit(0)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """
            Class B {
                Val b: Int = 0;
                Val a: Float = Self.a.b.c().t[1];
            }
        """
        expect = "Program([ClassDecl(Id(B),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,ArrayCell(FieldAccess(CallExpr(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),Id(c),[]),Id(t)),[IntLit(1)])))])])"
        self.assertTrue(TestAST.test(input, expect, 292))

    def test93(self):
        input = """
            Class Program {
                main() {
                    Return ClassName::$a;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(FieldAccess(Id(ClassName),Id($a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 293))

    def test94(self):
        input = """
            Class Program {
                main() {
                    b = Main::$get()[1];
                    a = Main[0][1][2];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(b),ArrayCell(CallExpr(Id(Main),Id($get),[]),[IntLit(1)])),AssignStmt(Id(a),ArrayCell(Id(Main),[IntLit(0),IntLit(1),IntLit(2)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 294))

    def test95(self):
        input = """
            Class myClass {
                Val a: Int = Main.a.get();
            }
        """
        expect = "Program([ClassDecl(Id(myClass),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,CallExpr(FieldAccess(Id(Main),Id(a)),Id(get),[])))])])"
        self.assertTrue(TestAST.test(input, expect, 295))

    def test96(self):
        input = """
            Class ReString {
                Var string: Student = New ReString("Bao");
            }
        """
        expect = "Program([ClassDecl(Id(ReString),[AttributeDecl(Instance,VarDecl(Id(string),ClassType(Id(Student)),NewExpr(Id(ReString),[StringLit(Bao)])))])])"
        self.assertTrue(TestAST.test(input, expect, 296))

    def test97(self):
        input = """
            Class myClass {
                _method() {
                    Name.a[1][2] = Self.get().set.get();
                }
            }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(_method),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(Id(Name),Id(a)),[IntLit(1),IntLit(2)]),CallExpr(FieldAccess(CallExpr(Self(),Id(get),[]),Id(set)),Id(get),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 297))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(C)),NewExpr(Id(C),[])))]),ClassDecl(Id(C),[AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(A)),NullLiteral())),MethodDecl(Id(c__ount__),Instance,[],Block([Return(BinaryOp(+,FieldAccess(Id(C),Id($name)),ArrayCell(FieldAccess(CallExpr(Id(C),Id(getName),[]),Id(str)),[IntLit(2)])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 298))

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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($method),Static,[],Block([For(Id(i),UnaryOp(-,IntLit(3)),UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(100)),Block([For(Id(j),IntLit(0),UnaryOp(-,IntLit(255)),IntLit(1),Block([VarDecl(Id(a),FloatType,FloatLit(0.2))])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 299))

    def test100(self):
        input = """Class main{}"""
        expect = "Program([ClassDecl(Id(main),[])])"
        self.assertTrue(TestAST.test(input,expect, 300))

    def test101(self):
        input = """ 
            Class Program {
                main() {
                    Foreach (x In 5 .. 2) {
                        Out.printInt(arr[x]);
                    }
                } 
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 301))

    def test102(self):
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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),Call(Id(Shape),Id($getNumOfShape),[])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 302))

    def test103(self):
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
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(x),IntLit(5)),Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),Call(Id(Shape),Id($getNumOfShape),[])]),If(BinaryOp(==,Id(a),IntLit(10)),Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),Call(Id(Shape),Id($getNumOfShape),[])]),If(BinaryOp(+,IntLit(1),IntLit(2)),Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),Call(Id(Shape),Id($getNumOfShape),[])]),Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 303))

    def test104(self):
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
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)])),MethodDecl(Id($getNumOfShape),Static,[],Block([]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 304))

    def test105(self):
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
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,FloatType),[FloatLit(1.2),FloatLit(3.6),FloatLit(3400000.0),FloatLit(230000.0),FloatLit(127000.0)])),MethodDecl(Id($getNumOfShape),Static,[],Block([]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([VarDecl(Id(a),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)]),If(BinaryOp(>,Id(x),IntLit(2)),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(a),[IntLit(0)])])]),If(BinaryOp(==,Id(x),IntLit(2)),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(a),[IntLit(1)])])]),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(a),[IntLit(2)])])])))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(x),IntLit(2)),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(a),[IntLit(0)])])]),If(BinaryOp(==,Id(x),IntLit(2)),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(a),[IntLit(1)])]),Break]),If(BinaryOp(==,Id(x),IntLit(3)),Block([Continue]),If(BinaryOp(==,Id(x),IntLit(4)),Block([Return()])))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 305))
