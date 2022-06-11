'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
import re
from tkinter import X

from flask import Flask
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("$getInt", MType(list(), IntType()), CName('io')),
            Symbol("$putInt", MType([IntType()], VoidType()), CName('io')),
            Symbol("$putIntLn", MType([IntType()], VoidType()), CName('io')),
            Symbol("$getFloat", MType(list(), FloatType()), CName('io')),
            Symbol("$putFloat", MType([FloatType()], VoidType()), CName('io')),
            Symbol("$putFloatLn", MType(
                [FloatType()], VoidType()), CName('io')),
            Symbol("$getBool", MType(list(), BoolType()), CName('io')),
            Symbol("$putBool", MType([BoolType()], VoidType()), CName('io')),
            Symbol("$putBoolLn", MType([BoolType()], VoidType()), CName('io')),
            Symbol("$putString", MType(
                [StringType()], VoidType()), CName('io')),
            Symbol("$putStringLn", MType(
                [StringType()], VoidType()), CName('io')),
            Symbol("$putLn", MType([StringType()], VoidType()), CName('io'))
        ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):

#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None


class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class ClassType_(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value
# class MType:
#     def __init__(self,partype,rettype):
#         self.partype = partype
#         self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

# class Attribute:


class Attribute_:
    def __init__(self, name, mtype, static=False, const=False):
        self.name = name
        self.mtype = mtype
        self.static = static
        self.const = const


class Variable_:
    def __init__(self, name, mtype, scope, const=False):
        self.name = name
        self.mtype = mtype
        self.scope = scope
        self.const = const


class Method_:
    # class MethodDecl(MemDecl):
    # kind: SIKind
    # name: Id
    # param: List[VarDecl]
    # body: Block
    def __init__(self, name, static=False, param=[], rettype=None):
        self.static = static
        self.name = name
        self.paramTyp = [x.varType for x in param]
        self.rettype = rettype
        self.inLoop = 0
        self.scope = 1
        self.variable = {}
        for para in param:
            self.decl(para.variable.name, para.varType, 'Parameter')
        self.scope = 0

    def enterScope(self):
        self.scope += 1

    def exitScope(self):
        self.scope -= 1
        for key, value in self.variable.items():
            if value:
                if value[-1].scope > self.scope:
                    self.variable[key].pop()

    def enterLoop(self):
        self.inLoop += 1

    def exitLoop(self):
        self.inLoop -= 1

    def hasMain(self):
        return self.name == 'main' and self.paramTyp == [] and self.rettype is None
        # if self.name == 'main':
        #     if self.paramTyp != []:
        #         raise NoEntryPoint()
        #     if self.rettype is not None:
        #         return

    def decl(self, name, mtype, kind):
        if name in self.variable:
            self.variable[name] += [Variable_(name, mtype,
                                              self.scope, True if kind == 'Constant' else False)]
        else:
            self.variable[name] = [
                Variable_(name, mtype, self.scope, True if kind == 'Constant' else False)]


class Class_:
    def __init__(self, name, parent=None):
        self.name = name
        self.attribute = {}
        self.method = {}
        self.constructor = []
        # if parent:
        #     self.attribute = parent.attribute.copy()
        #     self.method = parent.method.copy()

    def addAttribute(self, name, mtype, static=False, const=False):

        self.attribute[name] = Attribute_(name, mtype, static, const)

    def addMethod(self, name, static=False, paramTyp=[], rettype=None):
        self.method[name] = Method_(name, static, paramTyp, rettype)

        if name == 'Constructor':
            self.constructor = self.method[name].paramTyp

    def getAttribute(self, name):
        return self.attribute[name]

    def getMethod(self, name):
        return self.method[name]


class Program_:
    def __init__(self):
        self._class = {}

    def addClass(self, name, parent=None):
        if parent is None:
            self._class[name] = Class_(name)
        else:
            self._class[name] = Class_(name, self._class[parent])

    def getClass(self, name):
        if name == 'Program':
            name = 'D96Class'
        return self._class[name]


def isCompatible(typ1, typ2, program):
    # print(typ1)
    # print(typ2)
    if (type(typ1) is ClassType and type(typ2) is ClassType and typ1.classname.name == typ2.classname.name) or\
        (type(typ1) is type(typ2) and type(typ1) not in [ClassType, ArrayType]) or\
            (type(typ1) is FloatType and type(typ2) is IntType):
        return True

    if type(typ1) is ArrayType and type(typ2) is ArrayType:
        if type(typ1.eleType) is ArrayType and type(typ2.eleType) is ArrayType:
            return isCompatible(typ1.eleType, typ2.eleType, program)

        return typ1.size == typ2.size and isCompatible(typ1.eleType, typ2.eleType, program)

    # if type(typ1) is ArrayType:
    #     return isCompatible(typ1.eleType, typ2, program)

    # if type(typ2) is ArrayType:
    #     return isCompatible(typ1, typ2.eleType, program)

    return False


class StaticChecker(BaseVisitor):

    global_envi = []

    def __init__(self, ast):
        self.ast = ast
        self.io = ClassDecl(
            Id("io"),
            [
                MethodDecl(
                    Static(),
                    Id("$getInt"),
                    [],
                    Block([Return(IntType())])
                ),
                MethodDecl(
                    Static(),
                    Id("$putInt"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$putIntLn"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$getFloat"),
                    [],
                    Block([Return(FloatType())])
                ),
                MethodDecl(
                    Static(),
                    Id("$putFloat"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$putFloatLn"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$getBool"),
                    [],
                    Block([Return(BoolType())])
                ),
                MethodDecl(
                    Static(),
                    Id("$putBool"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$putBoolLn"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$putString"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$putStringLn"),
                    [],
                    Block([])
                ),
                MethodDecl(
                    Static(),
                    Id("$putLn"),
                    [],
                    Block([])
                )
            ]
        )

    def visit(self, ast, c):
        return ast.accept(self, c)

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        self.program = Program_()

        self.visit(self.io, c)
        [self.visit(x, c) for x in ast.decl]

    def visitClassDecl(self, ast, c):
        ast.classname.name = 'D96Class' if ast.classname.name == 'Program' else ast.classname.name
        self.program.addClass(ast.classname.name,
                              ast.parentname.name if ast.parentname else None)
        [self.visit(x, (self.program.getClass(ast.classname.name), None))
         for x in ast.memlist]

    def visitAttributeDecl(self, ast, c):
        static = self.visit(ast.kind, c)
        const = type(ast.decl) is ConstDecl

        if const:
            _mtype = ast.decl.constType
            _name = ast.decl.constant.name
            # print(ast.decl.value)
            _valTyp = self.visit(ast.decl.value, c) if ast.decl.value else None

        else:
            _mtype = ast.decl.varType
            _name = ast.decl.variable.name
            # print(ast.decl.varInit)
            _valTyp = self.visit(
                ast.decl.varInit, c) if ast.decl.varInit else None

        # print(_valTyp[0])
        # print(_mtype)

        c[0].addAttribute(_name, _mtype, static, const)

    def visitMethodDecl(self, ast, c):
        c[0].addMethod(ast.name.name, type(ast.kind) is Static, ast.param)
        self.visit(ast.body, (c[0], c[0].getMethod(ast.name.name)))

    def visitBlock(self, ast, c):
        c[1].enterScope()
        [self.visit(x, c) for x in ast.inst]
        c[1].exitScope()

    def visitVarDecl(self, ast, c):
        c[1].decl(ast.variable.name, ast.varType, 'Variable')

        # print(type(ast.varInit))
        _valTyp = self.visit(ast.varInit, c) if ast.varInit else None
        # print(_valTyp)
        # print(ast.varType)

    def visitConstDecl(self, ast, c):
        c[1].decl(ast.constant.name, ast.constType, 'Constant')

        _valTyp = self.visit(ast.value, c)

    # need check
    def visitAssign(self, ast, c):
        # print(ast.exp)
        _lhs = self.visit(ast.lhs, c)
        _rhs = self.visit(ast.exp, c)
        # print(type(ast.exp))
        # print(_lhs[0])
        # print(_rhs[0])

    def visitCallExpr(self, ast, c):
        # print('1')
        _obj = self.visit(ast.obj, c)
        # if _obj is None:
        #     return
        _typ = _obj[0]

        _instance = True
        if _typ.classname.name[-1] == ',':
            _instance = False
            _typ.classname.name = _typ.classname.name[:-1]

        _class = self.program.getClass(_typ.classname.name)
        _method = _class.getMethod(ast.method.name)

        _paramTyp = [self.visit(x, c)[0] for x in ast.param]

        return (_method.rettype, False)

    def visitId(self, ast, c):
        # print(ast.name)
        # print(c[1].variable.keys())
        if c[1]:
            if ast.name in self.program._class.keys():
                return (ClassType(Id(ast.name + ',')), False)

            if ast.name in c[1].variable:
                return (c[1].variable[ast.name][-1].mtype, c[1].variable[ast.name][-1].const)

        return (ClassType(Id(ast.name + ',')), False)

    def visitCallStmt(self, ast, c):
        _obj = self.visit(ast.obj, c)
        # if _obj is None:
        #     return
        _typ = _obj[0]

        _instance = True
        if _typ.classname.name[-1] == ',':
            _instance = False
            _typ.classname.name = _typ.classname.name[:-1]

        _class = self.program.getClass(_typ.classname.name)
        _method = _class.getMethod(ast.method.name)

        _paramTyp = [self.visit(x, c)[0] for x in ast.param]

    def visitIf(self, ast, c):
        if type(self.visit(ast.expr, c)[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.thenStmt, c)

        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

    def visitFor(self, ast, c):
        c[1].enterScope()
        c[1].enterLoop()

        # print(ast.id.name)
        self.visit(ast.id, c)
        # print(type(self.visit(ast.id, c)[0]))
        # print(c[1].name)
        # print(c[1].variable[ast.id.name][-1].const)

        self.visit(ast.loop, c)

        c[1].exitLoop()
        c[1].exitScope()

    def visitReturn(self, ast, c):

        # print(ast.expr)
        c[1].rettype = self.visit(ast.expr, c)[0] if ast.expr else None

    def visitFieldAccess(self, ast, c):
        # print(ast.obj)
        _obj = self.visit(ast.obj, c)
        # if _obj is None:
        #     return
        if type(_obj[0]) is not ClassType:
            _obj[0] = ClassType(Id(ast.obj.name + ','))

        _instance = True

        if _obj[0].classname.name[-1] == ',':
            _instance = False
            _obj[0].classname.name = _obj[0].classname.name[:-1]

        _class = self.program.getClass(_obj[0].classname.name)

        _attribute = _class.getAttribute(ast.fieldname.name)

        return (_attribute.mtype, _attribute.const and _obj[1])

    def visitBinaryOp(self, ast, c):
        _left = self.visit(ast.left, c)
        _right = self.visit(ast.right, c)

        if ast.op in ['+', '-', '*', '/']:

            if type(_left[0]) is IntType and type(_right[0]) is IntType:
                return (IntType(), _left[1] and _right[1])

            return (FloatType(), _left[1] and _right[1])

        if ast.op == '%':
            return (IntType(), _left[1] and _right[1])

        if ast.op in ['<', '<=', '>', '>=']:
            return (BoolType(), _left[1] and _right[1])

        if ast.op in ['!=', '==']:
            return (BoolType(), _left[1] and _right[1])

        if ast.op in ['&&', '||']:
            return (BoolType(), _left[1] and _right[1])

        if ast.op in ['+.', '==.']:
            if not (type(_left[0]) is StringType and type(_right[0]) is StringType):
                raise TypeMismatchInExpression(ast)

            if ast.op == '+.':
                return (StringType(), _left[1] and _right[1])

            return(BoolType(), _left[1] and _right[1])

    def visitUnaryOp(self, ast, c):
        _expr = self.visit(ast.body, c)

        return _expr

    def visitArrayCell(self, ast, c):
        # print(ast.arr)
        _arr = self.visit(ast.arr, c)
        _idx = [self.visit(x, c)[0] for x in ast.idx]

        _rettyp = _arr[0]

        for x in _idx:
            _rettyp = _rettyp.eleType

        return (_arr[0].eleType, _arr[1])

    def visitBreak(self, ast, c):
        if not c[1].inLoop:
            raise MustInLoop(ast)

    def visitContinue(self, ast, c):
        if not c[1].inLoop:
            raise MustInLoop(ast)

    def visitNewExpr(self, ast, c):

        # print(ast.param)

        _exprTyp = [self.visit(x, c)[0]
                    for x in ast.param] if ast.param else []
        _class = self.program.getClass(ast.classname.name)

        return (ClassType(ast.classname), True)

    def visitStatic(self, ast, c):
        return True

    def visitInstance(self, ast, c):
        return False

    def visitIntLiteral(self, ast, c):
        return (IntType(), True)

    def visitFloatLiteral(self, ast, c):
        return (FloatType(), True)

    def visitBooleanLiteral(self, ast, c):
        return (BoolType(), True)

    def visitStringLiteral(self, ast, c):
        return (StringType(), True)

    def visitNullLiteral(self, ast, c):
        return None

    def visitSelfLiteral(self, ast, c):
        return (ClassType(Id(c[0].name)), True)

    def visitArrayLiteral(self, ast, c):
        _eleTyp = [self.visit(x, c)[0] for x in ast.value]

        return (ArrayType(len(ast.value), _eleTyp[0]), True)

    def visitIntType(self, ast, c):
        return (IntType(), True)

    def visitFloatType(self, ast, c):
        return (FloatType(), True)

    def visitBoolType(self, ast, c):
        return (BoolType(), True)

    def visitStringType(self, ast, c):
        return (StringType(), True)

    def visitArrayType(self, ast, c):
        return ast.eleType

    def visitVoidType(self, ast, c):
        return (VoidType(), True)


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.program = StaticChecker(self.astTree)
        self.program.check()

    def visitProgram(self, ast, o):
        # print(self.program.program.getClass('io').method)
        self.classEnv = []
        for x in ast.decl:
            self.classEnv += self.visit(x, 3)

        [self.visit(i, o) for i in ast.decl]
        return o

    def visitClassDecl(self, ast, o):
        if o == 3:
            self.className = 'D96Class' if ast.classname.name == 'Program' else ast.classname.name
            self.emit = Emitter(self.path + '/' + self.className + '.j')
            classEnv = []
            for x in ast.memlist:
                classEnv.append(self.visit(x, 3))
            return classEnv

        self.className = 'D96Class' if ast.classname.name == 'Program' else ast.classname.name
        self.emit = Emitter(self.path + '/' + self.className + '.j')
        if not ast.parentname:
            self.isHaveParent = False
            self.emit.printout(self.emit.emitPROLOG(
                self.className, 'java.lang.Object'))
        else:
            self.isHaveParent = True
            self.emit.printout(self.emit.emitPROLOG(
                self.className, ast.parentname.name))

        self.cast = ast
        isHaveCon = False
        for x in ast.memlist:
            self.visit(x, 0)
            if type(x) == MethodDecl and x.name.name == 'Constructor':
                isHaveCon = True

        if not isHaveCon:
            self.genMETHOD(MethodDecl(Instance(), Id('Constructor'), [], Block([])),
                           self.env + self.classEnv, Frame('Constructor', VoidType()))

        [self.visit(ele, SubBody(None, self.env + self.classEnv))
         for ele in ast.memlist if type(ele) is MethodDecl]

        self.emit.emitEPILOG()
        return o

    def genMETHOD(self, consdecl, o, frame):
        rettype = frame.returnType

        isCon = type(
            rettype) is VoidType and consdecl.name.name == 'Constructor'

        isMain = consdecl.name.name == 'main'

        methodName = '<init>' if isCon else consdecl.name.name

        intype = [ArrayPointerType(StringType())] if isMain else [
            x.varType for x in consdecl.param]
        mtype = MType(intype, rettype)

        if isCon:
            self.contype = mtype

        body = consdecl.body

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, isinstance(consdecl.kind, Static), frame))

        frame.enterScope(True)

        glenv = o
        lcenv = []
        e = SubBody(frame, lcenv)
        penv = []
        p = SubBody(frame, penv)

        if isCon:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    'this',
                    ClassType_(self.className),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame
                )
            )
            for x in consdecl.param:
                p = self.visit(x, p)

        elif isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    'args',
                    ArrayPointerType(StringType()),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame
                )
            )

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if isCon:
            self.emit.printout(self.emit.emitREADVAR(
                'this', ClassType_(self.className), 0, frame))

            if not self.isHaveParent:
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            else:
                self.emit.printout(self.emit.emitINVOKESPECIAL(
                    frame, self.cast.parentname.name + '/<init>', self.contype))

            for x in self.cast.memlist:
                if type(x) is AttributeDecl and type(x.kind) is Instance:
                    if isinstance(x.decl, VarDecl) and x.decl.varInit and type(x.decl.varInit) is not NullLiteral:
                        self.emit.printout(self.emit.emitREADVAR(
                            'this', ClassType_(self.className), 0, frame))
                        self.emit.printout(self.visit(x, frame))

        elif type(consdecl.kind) is Instance:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    'this',
                    ClassType_(self.className),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame
                )
            )
            for x in consdecl.param:
                p = self.visit(x, p)

        elif type(consdecl.kind) is Static:
            for x in consdecl.param:
                p = self.visit(x, p)

        for x in body.inst:
            if isinstance(x, StoreDecl):
                e = self.visit(x, SubBody(frame, p.sym + e.sym + glenv))

        [self.visit(x, SubBody(frame, p.sym + e.sym + glenv))
         for x in body.inst if isinstance(x, Stmt)]

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(rettype) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()

    def visitAttributeDecl(self, ast, o):
        self.isStatic = isinstance(ast.kind, Static)
        return self.visit(ast.decl, o)

    def visitMethodDecl(self, ast, o):
        # _method = Method()
        # print(_method.visit(ast, 1))
        # print(self.program.program.getClass(self.className).getMethod(ast.name.name).rettype)
        rettype = self.program.program.getClass(
            self.className).getMethod(ast.name.name).rettype

        if rettype is None:
            rettype = VoidType()

        if o != 0 and o != 3:
            frame = Frame(ast.name.name, rettype)
            self.genMETHOD(ast, o.sym, frame)

        return Symbol(ast.name.name, MType([x.varType for x in ast.param], rettype), CName(self.className))

    def visitBlock(self, ast, o):
        o.frame.enterScope(False)

        glenv = o.sym
        lcenv = []
        e = SubBody(o.frame, lcenv)
        self.emit.printout(self.emit.emitLABEL(
            o.frame.getStartLabel(), o.frame))

        for x in ast.inst:
            if isinstance(x, StoreDecl):
                e = self.visit(x, e)

        [self.visit(x, SubBody(o.frame, e.sym + glenv))
         for x in ast.inst if isinstance(x, Stmt)]

        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))

        o.frame.exitScope()

    def visitVarDecl(self, ast, o):
        if o == 3:
            return Symbol(ast.variable.name, ast.varType, CName(self.className))

        if o == 0:
            self.emit.printout(self.emit.emitATTRIBUTE(
                ast.variable.name, ast.varType, False, None, self.isStatic))
            return

        # if type(ast.varType) is ArrayType and not ast.varInit:
        #     ast.varInit = ArrayLiteral([])

        if isinstance(o, Frame):
            if ast.varInit and type(ast.varInit) is not NullLiteral:
                if self.isStatic:
                    self.emit.printout(self.visit(ast.varInit, o)[0])
                    return self.emit.emitPUTSTATIC(self.className + '/' + ast.variable.name, ast.varType, o)
                self.emit.printout(self.visit(ast.varInit, o)[0])
                return self.emit.emitPUTFIELD(self.className + '/' + ast.variable.name, ast.varType, o)
            return

        _idx = o.frame.getNewIndex()

        if type(ast.varType) is ClassType and ast.varType.classname.name == 'Program':
            ast.varType = ClassType(Id('D96Class'))

        self.emit.printout(
            self.emit.emitVAR(
                _idx,
                ast.variable.name,
                ast.varType,
                o.frame.getStartLabel(),
                o.frame.getEndLabel(),
                o.frame
            )
        )

        if ast.varInit and type(ast.varInit) is not NullLiteral:
            self.emit.printout(self.visit(ast.varInit, o)[0])
            self.emit.printout(self.emit.emitWRITEVAR(
                ast.variable.name, ast.varType, _idx, o.frame))
        # print(ast.variable.name)
        # print(type(ast.varType) is ClassType)
        # sym = next(filter(lambda x: type(x.mtype) is ClassType and x.mtype.classname.name == self.className, [Symbol(ast.variable.name, ast.varType, Index(_idx))] + o.sym), None)
        # print(sym.value.value)
        return SubBody(o.frame, [Symbol(ast.variable.name, ast.varType, Index(_idx))] + o.sym)

    def visitConstDecl(self, ast, o):
        if o == 3:
            return Symbol(ast.constant.name, ast.constType, CName(self.className))
        elif o == 0:
            self.emit.printout(self.emit.emitATTRIBUTE(
                ast.constant.name, ast.constType, False, False, self.isStatic))
            return

        if isinstance(o, Frame):
            if ast.value and type(ast.value) is not NullLiteral:
                if self.isStatic:
                    self.emit.printout(self.visit(ast.value, o)[0])
                    return self.emit.emitPUTSTATIC(self.className + '/' + ast.constant.name, ast.constType, o)
                self.emit.printout(self.visit(ast.value, o)[0])
                return self.emit.emitPUTFIELD(self.className + '/' + ast.constant.name, ast.constType, o)
            return

        _idx = o.frame.getNewIndex()

        self.emit.printout(
            self.emit.emitVAR(
                _idx,
                ast.constant.name,
                ast.constType,
                o.frame.getStartLabel(),
                o.frame.getEndLabel(),
                o.frame
            )
        )

        if ast.value and type(ast.value) is not NullLiteral:
            self.emit.printout(self.visit(ast.value, o)[0])
            self.emit.printout(self.emit.emitWRITEVAR(
                ast.constant.name, ast.constType, _idx, o.frame))

        return SubBody(o.frame, [Symbol(ast.constant.name, ast.constType, Index(_idx))] + o.sym)

    def visitAssign(self, ast, o):
        o.frame.push()
        o.frame.push()

        expr, exprTyp = self.visit(
            ast.exp, Access(o.frame, o.sym, False, True))
        lhs, lhsTyp = self.visit(ast.lhs, Access(o.frame, o.sym, True, True))

        if isinstance(lhsTyp, FloatType) and isinstance(exprTyp, IntType):
            expr = expr + self.emit.emitI2F(o.frame)

        if isinstance(ast.lhs, ArrayCell):
            self.emit.printout(
                lhs + expr + self.visit(ast.lhs, Access(o.frame, o.sym, True, False)))
        elif isinstance(ast.lhs, FieldAccess):
            self.emit.printout(
                lhs + expr + self.visit(ast.lhs, Access(o.frame, o.sym, True, False))[0])
        else:
            self.emit.printout(expr + lhs)

        o.frame.pop()
        o.frame.pop()

    def visitCallExpr(self, ast, o):
        _obj = self.visit(ast.obj, Access(o.frame, o.sym, False, False))[0]

        sym = next(filter(lambda x: x.name == ast.method.name and type(
            x.value) is CName, o.sym), None)

        sym = next(filter(lambda x: x.name == ast.method.name, o.sym), None)

        cname = sym.value.value
        ctype = sym.mtype

        in_ = ''
        for param in ast.param:
            expr = self.visit(param, Access(o.frame, o.sym, False, True))[0]
            in_ += expr

        if _obj:
            return in_ + _obj + self.emit.emitINVOKEVIRTUAL(cname + '/' + ast.method.name, ctype, o.frame), ctype.rettype
        if cname == 'io':
            return in_ + self.emit.emitINVOKESTATIC(cname + '/' + ast.method.name[1:], ctype, o.frame), ctype.rettype
        return in_ + self.emit.emitINVOKESTATIC(cname + '/' + ast.method.name, ctype, o.frame), ctype.rettype

    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, o.sym), None)

        if sym:
            _typ = sym.mtype
            if isinstance(o, Access) and o.isLeft:
                return self.emit.emitWRITEVAR(sym.name, _typ, sym.value.value, o.frame), sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name, _typ, sym.value.value, o.frame), sym.mtype
        return None, None

    def visitCallStmt(self, ast, o):
        # sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        _obj = self.visit(ast.obj, Access(o.frame, o.sym, False, True))[0]
        sym = next(filter(lambda x: x.name == ast.method.name and type(
            x.value) is CName, o.sym), None)

        cname = sym.value.value
        ctype = sym.mtype

        in_ = ('', [])
        for param in ast.param:
            expr, exprTyp = self.visit(
                param, Access(o.frame, o.sym, False, True))
            in_ = (in_[0] + expr, in_[1].append(exprTyp))

        if _obj:
            self.emit.printout(
                _obj + in_[0] + self.emit.emitINVOKEVIRTUAL(cname + '/' + ast.method.name, ctype, o.frame))
        else:
            if cname == 'io':
                self.emit.printout(
                    in_[0] + self.emit.emitINVOKESTATIC(cname + '/' + ast.method.name[1:], ctype, o.frame))
            else:
                self.emit.printout(
                    in_[0] + self.emit.emitINVOKESTATIC(cname + '/' + ast.method.name, ctype, o.frame))

    def visitFor(self, ast, o):
        self.loop = ast

        o.frame.enterLoop()

        _continue = o.frame.getContinueLabel()
        _break = o.frame.getBreakLabel()

        self.visit(Assign(ast.id, ast.expr1), o)

        self.emit.printout(self.emit.emitLABEL(_continue, o.frame))

        self.emit.printout(self.visit(
            BinaryOp('<=', ast.id, ast.expr2), Access(o.frame, o.sym, False, True))[0])
        self.emit.printout(self.emit.emitIFFALSE(_break, o.frame))

        self.visit(ast.loop, o)

        self.visit(Assign(ast.id, BinaryOp('+', ast.id, ast.expr3)), o)

        self.emit.printout(self.emit.emitGOTO(_continue, o.frame))
        self.emit.printout(self.emit.emitLABEL(_break, o.frame))

        o.frame.exitLoop()

    def visitIf(self, ast, o):
        expr, _ = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
        _then = o.frame.getNewLabel()

        self.emit.printout(expr)
        self.emit.printout(self.emit.emitIFFALSE(_then, o.frame))
        self.visit(ast.thenStmt, o)

        if ast.elseStmt:
            _else = o.frame.getNewLabel()
            if type(o.frame.returnType) is VoidType:
                self.emit.printout(self.emit.emitGOTO(_else, o.frame))

        self.emit.printout(self.emit.emitLABEL(_then, o.frame))

        if ast.elseStmt:
            self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(_else, o.frame))

    def visitReturn(self, ast, o):
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))
        else:
            expr, exprTyp = self.visit(
                ast.expr, Access(o.frame, o.sym, False, True))
            if type(o.frame.returnType) is FloatType and type(exprTyp) is IntType:
                self.emit.printout(
                    expr + self.emit.emitI2F(o.frame) + self.emit.emitRETURN(FloatType(), o.frame))
            else:
                self.emit.printout(
                    expr + self.emit.emitRETURN(exprTyp, o.frame))

    def visitFieldAccess(self, ast, o):
        _obj = self.visit(ast.obj, Access(
            o.frame, o.sym, o.isLeft, o.isFirst))[0]

        sym = next(filter(lambda x: x.name == ast.fieldname.name and type(
            x.value) is CName, o.sym), None)
        if isinstance(o, Access):
            if o.isLeft:
                if _obj:
                    if o.isFirst:
                        res = _obj
                    else:
                        res = self.emit.emitPUTFIELD(
                            sym.value.value + '/' + ast.fieldname.name, sym.mtype, o.frame)
                    return (res, sym.mtype)
                return self.emit.emitPUTSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o.frame), sym.mtype
            else:
                if _obj:
                    res = _obj + self.emit.emitGETFIELD(
                        sym.value.value + '/' + ast.fieldname.name, sym.mtype, o.frame)
                    return res, sym.mtype

                return self.emit.emitGETSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o.frame), sym.mtype

    def visitBinaryOp(self, ast, o):
        frame = o if isinstance(o, Frame) else o.frame
        _left, _leftTyp = self.visit(ast.left, o)
        _right, _righTyp = self.visit(ast.right, o)

        typ1 = _leftTyp.eleType if type(
            _leftTyp) is ArrayPointerType else _leftTyp
        typ2 = _righTyp.eleType if type(
            _righTyp) is ArrayPointerType else _righTyp

        if type(typ1) is type(typ2):
            if ast.op in ['+', '-']:
                code = self.emit.emitADDOP(ast.op, typ1, frame)
                res = _leftTyp

            elif ast.op == '*':
                code = self.emit.emitMULOP(ast.op, typ1, frame)
                res = _leftTyp

            elif ast.op == '/':
                _left = _left + self.emit.emitI2F(frame) if (type(_leftTyp) is IntType or (type(
                    _leftTyp) is ArrayPointerType and type(_leftTyp.eleType) is IntType)) else _left
                _right = _right + self.emit.emitI2F(frame) if (type(_righTyp) is IntType or (
                    type(_righTyp) is ArrayPointerType and type(_righTyp.eleType) is IntType)) else _right
                code = self.emit.emitMULOP(ast.op, FloatType(), frame)
                res = FloatType()

            elif ast.op == '%':
                code = self.emit.emitMOD(frame)
                res = IntType()

            elif ast.op == '&&':
                code = self.emit.emitANDOP(frame)
                res = BoolType()

            elif ast.op == '||':
                code = self.emit.emitOROP(frame)
                res = BoolType()

            elif ast.op in ['<', '<=', '>', '>=', '!=', '==']:
                code = self.emit.emitREOP(ast.op, typ1, frame)
                res = BoolType()

            elif ast.op == '==.':
                return self.emit.emitPUSHICONST(str(_left == _right).lower(), o if isinstance(o, Frame) else o.frame), BoolType()

            elif ast.op == '+.':
                code = self.emit.emitINVOKEVIRTUAL(
                    'java/lang/String/concat', MType([StringType()], StringType()), frame)
                res = StringType()

        else:
            _left = _left + self.emit.emitI2F(frame) if (type(_leftTyp) is IntType or (type(
                _leftTyp) is ArrayPointerType and type(_leftTyp.eleType) is IntType)) else _left
            _right = _right + self.emit.emitI2F(frame) if (type(_righTyp) is IntType or (
                type(_righTyp) is ArrayPointerType and type(_righTyp.eleType) is IntType)) else _right

            if ast.op in ['+', '-']:
                code = self.emit.emitADDOP(ast.op, FloatType(), frame)
                res = FloatType()

            elif ast.op in ['*', '/']:
                code = self.emit.emitMULOP(ast.op, FloatType(), frame)
                res = FloatType()

            elif ast.op in ['<', '<=', '>', '>=', '!=', '==']:
                code = self.emit.emitREOP(ast.op, FloatType(), frame)
                res = BoolType()

        return _left + _right + code, res

    def visitUnaryOp(self, ast, o):
        frame = o if isinstance(o, Frame) else o.frame
        body, bodyTyp = self.visit(ast.body, o)
        _typ = bodyTyp.eleType if type(
            bodyTyp) is ArrayPointerType else bodyTyp

        if ast.op == '!':
            return body + self.emit.emitNOT(StringType(), frame), BoolType()

        return body + self.emit.emitNEGOP(_typ, frame), _typ

    def visitArrayCell(self, ast, o):
        ast.idx = [BinaryOp('-', x, IntLiteral(1)) for x in ast.idx]

        frame = o if isinstance(o, Frame) else o.frame
        _arr, arrTyp = self.visit(ast.arr, Access(frame, o.sym, False, True))
        _idx, _ = self.visit(ast.idx[0], Access(frame, o.sym, False, True))

        if isinstance(o, Access) and o.isLeft and o.isFirst:
            return _arr + _idx, arrTyp.eleType

        elif isinstance(o, Access) and o.isLeft and not o.isFirst:
            return self.emit.emitASTORE(arrTyp.eleType, frame)

        else:
            return _arr + _idx + self.emit.emitALOAD(arrTyp.eleType, frame), arrTyp.eleType
        # code = ''
        # res = None

        # if type(ast.arr) is Id:
        #     sym = next(filter(lambda x: x.name == ast.arr.name and type(
        #         x.mtype) is ArrayType, o.sym), None)
        #     res = sym.mtype.eleType

        #     if o.isLeft:
        #         if o.isFirst:
        #             _aload = (self.emit.emitREADVAR(ast.arr.name,
        #                       sym.mtype, sym.value.value, o.frame))
        #             _idx, _ = self.visit(ast.idx, Access(
        #                 o.frame, o.sym, False, False))
        #             # print(_aload)
        #             code = _aload + _idx
        #         else:
        #             code = self.emit.emitASTORE(res, o.frame)
        #     else:
        #         _aload = (self.emit.emitREADVAR(ast.arr.name,
        #                   sym.mtype, sym.value.value, o.frame))
        #         _idx, _ = self.visit(ast.idx[0], Access(
        #             o.frame, o.sym, False, False))
        #         _iaload = self.emit.emitALOAD(res, o.frame)
        #         code = _aload + _idx + _iaload
        # else:
        #     if o.isLeft:
        #         if o.isFirst:
        #             _aload, typ1 = self.visit(ast.arr, Access(
        #                 o.frame, o.sym, o.isLeft, o.isFirst))
        #             _idx, _ = self.visit(ast.idx, Access(
        #                 o.frame, o.sym, False, False))
        #             code = _aload + _idx
        #             res = typ1.eleType
        #         else:
        #             code = self.emit.emitASTORE(IntType(), o.frame)
        #     else:
        #         _aload, typ1 = self.visit(ast.arr, Access(
        #             o.frame, o.sym, o.isLeft, o.isFirst))
        #         _idx, _ = self.visit(ast.idx, Access(
        #             o.frame, o.sym, False, False))
        #         _iaload = self.emit.emitALOAD(res, o.frame)
        #         code = _aload + _idx + _iaload
        #         res = typ1.eleType

        # return code, res

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getBreakLabel(), o.frame))

    def visitContinue(self, ast, o):
        # print(o)
        # print(self.loop.id)
        self.visit(Assign(self.loop.id, BinaryOp(
            '+', self.loop.id, self.loop.expr3)), o)
        
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getContinueLabel(), o.frame))

    def visitNewExpr(self, ast, o):
        _frame = o if isinstance(o, Frame) else o.frame
        _new = self.emit.emitNEW(
            'D96Class' if ast.classname.name == 'Program' else ast.classname.name, _frame)
        _dup = self.emit.emitDUP(_frame)
        _para = "".join([self.visit(para, _frame)[0] for para in ast.param])

        _inv = self.emit.emitINVOKESPECIAL(_frame, ('D96Class' if ast.classname.name == 'Program' else ast.classname.name) + '/<init>', MType(self.program.program.getClass(
            ast.classname.name).getMethod('Constructor').paramTyp, VoidType()) if _para else self.contype)

        return _new + _dup + _para + _inv, ClassType_(ast.classname)

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o if isinstance(o, Frame) else o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o if isinstance(o, Frame) else o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o if isinstance(o, Frame) else o.frame), BoolType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"' + ast.value + '"', StringType(), o if isinstance(o, Frame) else o.frame), StringType()

    def visitNullLiteral(self, ast, o):
        pass

    def visitSelfLiteral(self, ast, o):
        if isinstance(o, Access) and o.isLeft:
            return self.emit.emitREADVAR('', ClassType_(self.className), 0, o.frame), ClassType_(self.className)
        else:
            return self.emit.emitREADVAR('', ClassType_(self.className), 0, o.frame), ClassType_(self.className)

    def visitArrayLiteral(self, ast, o):
        if ast.value == []:
            return

        _frame = o if isinstance(o, Frame) else o.frame

        _typ = ''
        in_ = VoidType()
        if type(ast.value[0]) is IntLiteral:
            _typ = 'int'
            in_ = IntType()
        elif type(ast.value[0]) is FloatLiteral:
            _typ = 'float'
            in_ = FloatType()
        elif type(ast.value[0]) is StringLiteral:
            _typ = 'java/lang/String'
            in_ = StringType()
        elif type(ast.value[0]) is BooleanLiteral:
            _typ = 'boolean'
            in_ = BoolType()
        elif type(ast.value[0]) is ArrayLiteral:
            self.visit(ast.value[0], o)

        res = ''
        res += self.emit.emitPUSHICONST(len(ast.value), _frame)
        if _typ == 'java/lang/String':
            res += self.emit.emitANEWARRAY(_typ, _frame)
        else:
            res += self.emit.emitNEWARRAY(_typ, _frame)

        for i in range(len(ast.value)):
            res += self.emit.emitDUP(_frame)
            res += self.emit.emitPUSHICONST(i, _frame)
            res += self.visit(ast.value[i], o)[0]
            res += self.emit.emitASTORE(in_, _frame)

        return res, ArrayPointerType(in_)
