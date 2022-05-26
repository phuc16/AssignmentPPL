
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

# class Attribute:
class Attribute_:
    def __init__(self, name, mtype, static = False, const = False):
        self.name = name
        self.mtype = mtype
        self.static = static
        self.const = const

class Variable_:
    def __init__(self, name, mtype, scope, const = False):
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
    def __init__(self, name, static = False, param = [], rettype = None):
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
            if self.variable[name][-1].scope == self.scope:
                if kind == 'Variable':
                    raise Redeclared(Variable(), name)
                if kind == 'Constant':
                    raise Redeclared(Constant(), name)
                if kind == 'Parameter':
                    raise Redeclared(Parameter(), name)

            self.variable[name] += [Variable_(name, mtype, self.scope, True if kind == 'Constant' else False)]  
        else:
            self.variable[name] = [Variable_(name, mtype, self.scope, True if kind == 'Constant' else False)]

class Class_:
    def __init__(self, name, parent = None):
        self.name = name
        self.attribute = {}
        self.method = {}
        self.constructor = []
        # if parent:
        #     self.attribute = parent.attribute.copy()
        #     self.method = parent.method.copy()

    def addAttribute(self, name, mtype, static = False, const = False):
        if name in self.attribute.keys():
            raise Redeclared(Attribute(), name)

        self.attribute[name] = Attribute_(name, mtype, static, const)

    def addMethod(self, name, static = False, paramTyp = [], rettype = None):
        if name in self.method.keys():
            raise Redeclared(Method(), name)

        self.method[name] = Method_(name, static, paramTyp, rettype)

        if name == 'Constructor':
            self.constructor = self.method[name].paramTyp

    def getAttribute(self, name):
        if name not in self.attribute.keys(): 
            raise Undeclared(Attribute(), name)

        return self.attribute[name]

    def getMethod(self, name):
        if name not in self.method.keys(): 
            raise Undeclared(Method(), name)

        return self.method[name]

    def isNoEntry(self):
        return not any([x.hasMain() for x in self.method.values()]) if self.name == 'Program' else False

class Program_:
    def __init__(self):
        self._class = {}
    
    def isDecl(self, name):
        if name not in self._class.keys():
            raise Undeclared(Class(), name)

    def addClass(self, name, parent = None):
        if name in self._class.keys():
            raise Redeclared(Class(), name)

        if parent is None:
            self._class[name] = Class_(name)
        else:
            self.isDecl(parent)
            self._class[name] = Class_(name, self._class[parent])

    def getClass(self, name):
        return self._class[name]

    def isNoEntry(self):
        if any([x.isNoEntry() for x in self._class.values()]):
            raise NoEntryPoint()

def isCompatible(typ1, typ2, program):
    # print(typ1)
    # print(typ2)
    if  (type(typ1) is ClassType and type(typ2) is ClassType and typ1.classname.name == typ2.classname.name) or\
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

    global_envi = [Symbol("getInt",MType([],IntType())),
                    Symbol("putInt",MType([IntType()],VoidType())),
                    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("getFloat",MType([],FloatType())),
                    Symbol("putFloat",MType([FloatType()],VoidType())),
                    Symbol("putFloatLn",MType([FloatType()],VoidType())),
                    Symbol("putBool",MType([BoolType()],VoidType())),
                    Symbol("putBoolLn",MType([BoolType()],VoidType())),
                    Symbol("putString",MType([StringType()],VoidType())),
                    Symbol("putStringLn",MType([StringType()],VoidType())),
                    Symbol("putLn",MType([StringType()],VoidType()))
                    ]
            
    def __init__(self,ast):
        self.ast = ast

    def visit(self, ast, c):
        return ast.accept(self, c) 

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self, ast, c): 
        self.program = Program_()
        [self.visit(x, c) for x in ast.decl]
        self.program.isNoEntry()

    def visitClassDecl(self, ast, c):
        self.program.addClass(ast.classname.name, ast.parentname.name if ast.parentname else None)
        [self.visit(x, (self.program.getClass(ast.classname.name), None)) for x in ast.memlist]

    def visitAttributeDecl(self, ast, c):
        static = self.visit(ast.kind, c)
        const = type(ast.decl) is ConstDecl

        if const:
            _mtype = ast.decl.constType
            _name = ast.decl.constant.name
            # print(ast.decl.value)
            _valTyp = self.visit(ast.decl.value, c) if ast.decl.value else None
            if not (_valTyp and _valTyp[1]):
                raise IllegalConstantExpression(ast.decl.value)
        else:
            _mtype = ast.decl.varType
            _name = ast.decl.variable.name
            # print(ast.decl.varInit)
            _valTyp = self.visit(ast.decl.varInit, c) if ast.decl.varInit else None

        if type(_valTyp) is ClassType:
            if _valTyp.classname.name not in self.program._class:
                raise Undeclared(Class(), _valTyp.classname.name)

        # print(_valTyp[0])
        # print(_mtype)

        if _valTyp and not isCompatible(_mtype, _valTyp[0], self.program):
            raise TypeMismatchInConstant(ast.decl) if const else TypeMismatchInStatement(ast.decl)

        c[0].addAttribute(_name, _mtype, static, const)

    def visitMethodDecl(self, ast, c):
        if c[0].name == 'Program':
            if ast.name.name == 'main':
                if ast.param != []:
                    raise NoEntryPoint()

        c[0].addMethod(ast.name.name, type(ast.kind) is Static, ast.param)
        self.visit(ast.body, (c[0], c[0].getMethod(ast.name.name)))


    def visitBlock(self, ast, c):
        c[1].enterScope()
        [self.visit(x, c) for x in ast.inst]
        c[1].exitScope()

    def visitVarDecl(self, ast, c):
        c[1].decl(ast.variable.name, ast.varType, 'Variable')
        if type(ast.varType) is ClassType:
            if ast.varType.classname.name not in self.program._class:
                raise Undeclared(Class(), ast.varType.classname.name)

        # print(type(ast.varInit))
        _valTyp = self.visit(ast.varInit, c) if ast.varInit else None
        # print(_valTyp)
        # print(ast.varType)
        if _valTyp and not isCompatible(ast.varType, _valTyp[0], self.program):
            raise TypeMismatchInStatement(ast)

    def visitConstDecl(self, ast, c):
        c[1].decl(ast.constant.name, ast.constType, 'Constant')
        if type(ast.constType) is ClassType:
            if ast.constType.classname.name not in self.program._class:
                raise Undeclared(Class(), ast.constType.classname.name)

        _valTyp = self.visit(ast.value, c)

        if (not _valTyp) or (not _valTyp[1]):
            raise IllegalConstantExpression(ast.value)

        if _valTyp and not isCompatible(ast.constType, _valTyp[0], self.program):
            raise TypeMismatchInConstant(ast)

    # need check
    def visitAssign(self, ast, c):
        # print(ast.exp)
        _lhs = self.visit(ast.lhs, c)
        _rhs = self.visit(ast.exp, c)
        # print(type(ast.exp))
        # print(_lhs[0])
        # print(_rhs[0])
        if type(_lhs[0]) is ClassType and _lhs[0].classname.name[-1] == ',':
            raise Undeclared(Identifier(), _lhs[0].classname.name[:-1])

        if not isinstance(ast.lhs, LHS) or _lhs[1]:
            raise CannotAssignToConstant(ast)

        if not isCompatible(_lhs[0], _rhs[0], self.program):
            raise TypeMismatchInStatement(ast)

    def visitCallExpr(self, ast, c):
        # print('1')
        _obj =  self.visit(ast.obj,c)
        # if _obj is None:
        #     return
        _typ = _obj[0]
        if type(_typ) is not ClassType:
            raise TypeMismatchInExpression(ast)
        
        _instance = True
        if _typ.classname.name[-1] == ',':
            _instance = False
            _typ.classname.name = _typ.classname.name[:-1]

        _class = self.program.getClass(_typ.classname.name)
        _method = _class.getMethod(ast.method.name)

        if bool(_instance) == bool(_method.static):
            raise IllegalMemberAccess(ast)

        if not _method.rettype:
            raise TypeMismatchInExpression(ast)
        
        _paramTyp = [self.visit(x, c)[0] for x in ast.param]

        if len(_method.paramTyp) != len(_paramTyp):
            raise TypeMismatchInExpression(ast)

        for i in range(len(_method.paramTyp)):
            if not isCompatible(_method.paramTyp[i], _paramTyp[i], self.program):
                raise TypeMismatchInExpression(ast)

        return (_method.rettype, False)

    def visitId(self, ast, c):
        # print(ast.name)
        # print(c[1].variable.keys())
        if c[1]:
            if ast.name not in c[1].variable.keys() and ast.name not in self.program._class.keys():
                raise Undeclared(Identifier(), ast.name)
            
            if ast.name in self.program._class.keys():
                return (ClassType(Id(ast.name + ',')), False)
                
            if ast.name in c[1].variable:
                return (c[1].variable[ast.name][-1].mtype, c[1].variable[ast.name][-1].const)

        if ast.name not in self.program._class.keys():
            raise Undeclared(Identifier(), ast.name)

        return (ClassType(Id(ast.name + ',')), False)

    def visitCallStmt(self, ast, c): 
        _obj =  self.visit(ast.obj, c)
        # if _obj is None:
        #     return
        _typ = _obj[0]
        if type(_typ) is not ClassType:
            raise TypeMismatchInStatement(ast)
        
        _instance = True
        if _typ.classname.name[-1] == ',':
            _instance = False
            _typ.classname.name = _typ.classname.name[:-1]

        _class = self.program.getClass(_typ.classname.name)
        _method = _class.getMethod(ast.method.name)
    
        if bool(_instance) == bool(_method.static):
            raise IllegalMemberAccess(ast)

        if _method.rettype:
            raise TypeMismatchInStatement(ast)
                    
        _paramTyp = [self.visit(x, c)[0] for x in ast.param]
        if len(_method.paramTyp) != len(_paramTyp):
            raise TypeMismatchInStatement(ast)

        for i in range(len(_method.paramTyp)):
            if not isCompatible(_method.paramTyp[i], _paramTyp[i], self.program):
                raise TypeMismatchInStatement(ast)

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
        if c[1].variable[ast.id.name][-1].const:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))

        if not (type(self.visit(ast.expr1, c)[0]) is IntType and type(self.visit(ast.expr2, c)[0]) is IntType):
            raise TypeMismatchInStatement(ast)

        if ast.expr3:
            if type(self.visit(ast.expr3, c)[0]) is not IntType:
                raise TypeMismatchInStatement(ast)

        self.visit(ast.loop,c)

        c[1].exitLoop()
        c[1].exitScope()

    def visitReturn(self, ast, c):
        if c[1].name == 'Constructor':
            if ast.expr:
                raise TypeMismatchInStatement(ast)

        if c[1].name == 'Destructor':
            raise TypeMismatchInStatement(ast)

        if c[0].name == 'Program':
            if c[1].name == 'main':
                if ast.expr:
                    raise TypeMismatchInStatement(ast)

        # print(ast.expr)
        c[1].rettype = self.visit(ast.expr, c)[0] if ast.expr else None

    def visitFieldAccess(self, ast, c):
        # print(ast.obj)
        _obj = self.visit(ast.obj, c)
        # print(_obj)
        # if _obj is None:
        #     return
        if type(_obj[0]) is not ClassType:
            if not isinstance(ast.obj, Id) or ast.obj.name not in self.program._class:
                raise IllegalMemberAccess(ast.obj)
            _obj[0] = ClassType(Id(ast.obj.name + ','))

        _instance = True

        if _obj[0].classname.name[-1] == ',':
            _instance = False
            _obj[0].classname.name = _obj[0].classname.name[:-1]
            
        _class = self.program.getClass(_obj[0].classname.name)
        if ast.fieldname.name not in _class.attribute:
            raise Undeclared(Attribute(), ast.fieldname.name)
        
        if bool(_instance) == bool(_class.attribute[ast.fieldname.name].static):
            raise IllegalMemberAccess(ast)
        _attribute = _class.getAttribute(ast.fieldname.name)

        return (_attribute.mtype, _attribute.const and _obj[1])

    def visitBinaryOp(self, ast, c):
        _left = self.visit(ast.left, c)
        _right = self.visit(ast.right, c)

        if ast.op in ['+','-','*','/']:
            if not (type(_left[0]) in [IntType, FloatType] and type(_right[0]) in [IntType, FloatType]):
                raise TypeMismatchInExpression(ast)

            if type(_left[0]) is IntType and type(_right[0]) is IntType:
                return (IntType(), _left[1] and _right[1])
                
            return (FloatType(), _left[1] and _right[1])

        if ast.op == '%':
            if not (type(_left[0]) is IntType and type(_right[0]) is IntType):
                raise TypeMismatchInExpression(ast)

            return (IntType(), _left[1] and _right[1])

        if ast.op in ['<','<=','>','>=']:
            if not (type(_left[0]) in [IntType, FloatType] and type(_right[0]) in [IntType, FloatType]):
                raise TypeMismatchInExpression(ast)

            return (BoolType(), _left[1] and _right[1])

        if ast.op in ['!=','==']:
            if type(_left[0]) is not type(_right[0]):
                raise TypeMismatchInExpression(ast)
                
            if not (type(_left[0]) in [IntType, BoolType] and type(_right[0]) in [IntType, BoolType]):
                raise TypeMismatchInExpression(ast)

            return (BoolType(), _left[1] and _right[1])

        if ast.op in ['&&','||']:
            if not (type(_left[0]) is BoolType and type(_right[0]) is BoolType):
                raise TypeMismatchInExpression(ast)

            return (BoolType(), _left[1] and _right[1])

        if ast.op in ['+.','==.']:
            if not (type(_left[0]) is StringType and type(_right[0]) is StringType):
                raise TypeMismatchInExpression(ast)

            if ast.op == '+.':
                return (StringType(), _left[1] and _right[1])

            return(BoolType(), _left[1] and _right[1])

    def visitUnaryOp(self, ast, c):
        _expr = self.visit(ast.body, c)
        if ast.op == '-':
            if type(_expr[0]) not in [FloatType, IntType]:
                raise TypeMismatchInExpression(ast)
            
        if ast.op == '!':
            if type(_expr[0]) is not BoolType:
                raise TypeMismatchInExpression(ast)

        return _expr

    def visitArrayCell(self, ast, c):
        # print(ast.arr)
        _arr = self.visit(ast.arr, c)
        _idx = [self.visit(x, c)[0] for x in ast.idx]
        if type(_arr[0]) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        _rettyp = _arr[0]

        for x in _idx:
            try: 
                _rettyp = _rettyp.eleType
            except:
                raise TypeMismatchInExpression(ast)

            if type(x) is not IntType:
                raise TypeMismatchInExpression(ast)

        return (_arr[0].eleType, _arr[1])

    def visitBreak(self, ast, c):
        if not c[1].inLoop:
            raise MustInLoop(ast)

    def visitContinue(self, ast, c):
        if not c[1].inLoop:
            raise MustInLoop(ast)

    def visitNewExpr(self, ast, c):
        if ast.classname.name not in self.program._class:
            raise Undeclared(Class(), ast.classname.name)

        # print(ast.param)

        _exprTyp = [self.visit(x, c)[0] for x in ast.param] if ast.param else []
        _class = self.program.getClass(ast.classname.name)

        if len(_class.constructor) != len(_exprTyp): 
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(_class.constructor)):
            if not isCompatible(_class.constructor[i], _exprTyp[i], self.program):
                raise TypeMismatchInExpression(ast)

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

        for i in range(len(ast.value)):
            if not isCompatible(_eleTyp[i], _eleTyp[0], self.program) or type(_eleTyp[i]) is not type(_eleTyp[0]):
                raise IllegalArrayLiteral(ast)

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