from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

from ast import literal_eval

class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        lst=[]
        clst = list(map(self.visit, ctx.classdecl()))
        for i in range(ctx.getChildCount()):
            if clst:
                lst.append(clst.pop(0))
        return Program(lst)

    def visitClassdecl(self, ctx: D96Parser.ClassdeclContext):
        global thisClass
        thisClass = ctx.ID(0).getText()

        lst = []
        for x in ctx.classbody():
            x = self.visit(x)
            if isinstance(x, list):
                for i in x:
                    lst.append(i)
            else:
                lst.append(x)
        
        return ClassDecl(Id(ctx.ID(0).getText()), 
                        lst, 
                        Id(ctx.ID(1).getText()) if len(ctx.ID()) == 2 else None)
    
    def visitClassbody(self, ctx: D96Parser.ClassbodyContext):
        return self.visit(ctx.getChild(0))

    def visitAttrdecl(self, ctx: D96Parser.AttrdeclContext):
        return self.visit(ctx.getChild(0))

    def visitMutable(self, ctx: D96Parser.MutableContext):
        if ctx.nonvalue():
            nonvalue = self.visit(ctx.nonvalue())
            return list(map(lambda x:
                AttributeDecl(Static(), VarDecl(x, nonvalue[1], NullLiteral() if isinstance(nonvalue[1], ClassType) else None)) if x.name[0] =='$'
                else AttributeDecl(Instance(), VarDecl(x, nonvalue[1], NullLiteral() if isinstance(nonvalue[1], ClassType) else None)), 
                nonvalue[0]))
        else:
            value = self.visit(ctx.value())
            return list(map(lambda x, y:
                AttributeDecl(Static(), VarDecl(x, value[1], y)) if x.name[0] =='$'
                else AttributeDecl(Instance(), VarDecl(x, value[1], y)), 
                value[0], value[2]))

    def visitImmutable(self, ctx: D96Parser.ImmutableContext):
        if ctx.nonvalue():
            nonvalue = self.visit(ctx.nonvalue())
            return list(map(lambda x:
                AttributeDecl(Static(), ConstDecl(x, nonvalue[1], None)) if x.name[0] =='$'
                else AttributeDecl(Instance(), ConstDecl(x, nonvalue[1], None)), 
                nonvalue[0]))
        
        else:
            value = self.visit(ctx.value())
            return list(map(lambda x, y:
                AttributeDecl(Static(), ConstDecl(x, value[1], y)) if x.name[0] =='$'
                else AttributeDecl(Instance(), ConstDecl(x, value[1], y)), 
                value[0], value[2]))

    def visitNonvalue(self, ctx: D96Parser.NonvalueContext):
        if ctx.typ():
            return ([Id(ctx.getChild(0).getText())], self.visit(ctx.typ()))
        else:
            nonvalue = self.visit(ctx.nonvalue())
            nonvalue[0].insert(0, Id(ctx.getChild(0).getText()))
            return nonvalue

    def visitValue(self, ctx: D96Parser.ValueContext):
        if ctx.ASSIOP():
            return ([Id(ctx.getChild(0).getText())], 
                    self.visit(ctx.typ()),
                    [self.visit(ctx.exp())])
        else:
            value = self.visit(ctx.value())
            value[0].insert(0, Id(ctx.getChild(0).getText()))
            value[2].append(self.visit(ctx.exp()))
            return value

    def visitMethdecl(self, ctx: D96Parser.MethdeclContext):
        return self.visit(ctx.getChild(0))

    def visitBasicmeth(self, ctx: D96Parser.BasicmethContext):
        global thisClass

        if thisClass == 'Program' and not ctx.paralist() and ctx.getChild(0).getText() == 'main':
            return  MethodDecl(Static(),
                    Id(ctx.getChild(0).getText()),
                    [], 
                    self.visit(ctx.blockstmt()))

        return  MethodDecl(Instance() if ctx.ID() else Static(),
                        Id(ctx.getChild(0).getText()),
                        self.visit(ctx.paralist()) if ctx.paralist() else [], 
                        self.visit(ctx.blockstmt()))

    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        return  MethodDecl(Instance(), 
                            Id("Constructor"), 
                            self.visit(ctx.paralist()) if ctx.paralist() else [], 
                            self.visit(ctx.blockstmt()))

    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        return  MethodDecl(Instance(), Id("Destructor"), [], self.visit(ctx.blockstmt()))

    def visitParalist(self,ctx:D96Parser.ParalistContext):
        lst = []
        sublst = []
        for x in ctx.parasingle():
            sublst = self.visit(x)
            lst += sublst
        return lst

    def visitParasingle(self,ctx:D96Parser.ParasingleContext):
        lst = []
        for x in ctx.ID():
            lst.append(VarDecl(Id(x.getText()), self.visit(ctx.typ())))
        return lst

    def visitMethodattrdecl(self, ctx: D96Parser.MethodattrdeclContext):
        if ctx.VAR():
            if ctx.nonvaluemethod():
                nonvaluemethod = self.visit(ctx.nonvaluemethod())
                return list(map(lambda x: VarDecl(x, nonvaluemethod[1], NullLiteral() if isinstance(nonvaluemethod[1], ClassType) else None), nonvaluemethod[0]))
            else:
                valuemethod = self.visit(ctx.valuemethod())
                return list(map(lambda x, y: VarDecl(x, valuemethod[1], y), valuemethod[0], valuemethod[2]))
        else:
            if ctx.nonvaluemethod():
                nonvaluemethod = self.visit(ctx.nonvaluemethod())
                return list(map(lambda x: ConstDecl(x, nonvaluemethod[1], None), nonvaluemethod[0]))
            else:
                valuemethod = self.visit(ctx.valuemethod())
                return list(map(lambda x, y: ConstDecl(x, valuemethod[1], y), valuemethod[0], valuemethod[2]))            

    def visitNonvaluemethod(self, ctx: D96Parser.NonvaluemethodContext):
        if ctx.typ():
            return ([Id(ctx.ID().getText())], self.visit(ctx.typ()))
        else:
            nonvaluemethod = self.visit(ctx.nonvaluemethod())
            nonvaluemethod[0].insert(0, Id(ctx.ID().getText()))
            return nonvaluemethod

    def visitValuemethod(self, ctx: D96Parser.ValuemethodContext):
        if ctx.ASSIOP():
            return ([Id(ctx.ID().getText())], 
                    self.visit(ctx.typ()),
                    [self.visit(ctx.exp())])
        else:
            valuemethod = self.visit(ctx.valuemethod())
            valuemethod[0].insert(0, Id(ctx.ID().getText()))
            valuemethod[2].append(self.visit(ctx.exp()))
            return valuemethod

    def visitIndexedarray(self, ctx: D96Parser.IndexedarrayContext):
        return ArrayLiteral(self.visit(ctx.arraylist()))

    def visitArraylist(self, ctx: D96Parser.ArraylistContext):
        return [self.visit(x) for x in ctx.exp()]
    
    def visitMultiarray(self, ctx: D96Parser.MultiarrayContext):
        return ArrayLiteral(self.visit(ctx.multiarraylist()))

    def visitMultiarraylist(self, ctx: D96Parser.MultiarraylistContext):
        return [self.visit(x) for x in ctx.indexedarray()]

    def visitBlockstmt(self, ctx: D96Parser.BlockstmtContext):
        stmt = []
        for x in ctx.stmt():
            x = self.visit(x)
            if isinstance(x, list):
                for i in x:
                    stmt.append(i)
            else:
                stmt.append(x)
        return Block(stmt)

    def visitStmt(self, ctx: D96Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitAssignstmt(self, ctx: D96Parser.AssignstmtContext):
        return Assign(self.visit(ctx.exp6()), self.visit(ctx.exp()))

    def visitIndexexp(self, ctx: D96Parser.IndexexpContext):
        return [self.visit(x) for x in ctx.exp()]

    def visitIfstmt(self, ctx: D96Parser.IfstmtContext):
        then = self.visit(ctx.thenstmt())
        elseifstmts = self.visit(ctx.elseifstmts())
        elsestmt = self.visit(ctx.elsestmt())
        if (len(elseifstmts) == 0):
            then.elseStmt = elsestmt
        
        else:
            for i in range(len(elseifstmts)):
                elseifstmts[len(elseifstmts) - i - 1].elseStmt = elsestmt
                elsestmt = elseifstmts[len(elseifstmts) - i - 1]
                then.elseStmt = elsestmt
        
        return then

    def visitThenstmt(self, ctx: D96Parser.ThenstmtContext):
        return If(self.visit(ctx.exp()), self.visit(ctx.blockstmt()))

    def visitElseifstmts(self, ctx: D96Parser.ElseifstmtsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.elseifstmt())] + self.visit(ctx.elseifstmts())
        return []

    def visitElseifstmt(self, ctx: D96Parser.ElseifstmtContext):
        return If(self.visit(ctx.exp()), self.visit(ctx.blockstmt()))

    def visitElsestmt(self, ctx: D96Parser.ElsestmtContext):
        if ctx.ELSE():
            return self.visit(ctx.blockstmt())
        return None

    def visitForinstmt(self, ctx: D96Parser.ForinstmtContext):
        return  For(Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.DOLLARID().getText()),
                    self.visit(ctx.exp(0)), 
                    self.visit(ctx.exp(1)), 
                    self.visit(ctx.blockstmt()), 
                    self.visit(ctx.exp(2)) if len(ctx.exp()) == 3 else IntLiteral(1))

    def visitBreakstmt(self, ctx: D96Parser.BreakstmtContext):
        return Break()

    def visitContinuestmt(self, ctx: D96Parser.ContinuestmtContext):
        return Continue()

    def visitReturnstmt(self, ctx: D96Parser.ReturnstmtContext):
        return Return(self.visit(ctx.exp()) if ctx.exp() else None)

    def visitMethodinvostmt(self, ctx: D96Parser.MethodinvostmtContext):
        return CallStmt(self.visit(ctx.exp7()) if ctx.exp7() else Id(ctx.ID().getText()),
                        Id(ctx.ID().getText()) if ctx.exp7() else Id(ctx.DOLLARID().getText()),
                        self.visit(ctx.explist()) if ctx.explist() else [])

    def visitExplist(self, ctx: D96Parser.ExplistContext):
        return [self.visit(x) for x in ctx.exp()]

    def visitExp(self, ctx: D96Parser.ExpContext):
        if ctx.getChildCount() == 3:
            if ctx.ADDDOTOP():
                return BinaryOp(ctx.ADDDOTOP().getText(),
                                self.visit(ctx.exp0(0)),
                                self.visit(ctx.exp0(1)))

            if ctx.DOUEQUODOTOP():
                return BinaryOp(ctx.DOUEQUODOTOP().getText(),
                                self.visit(ctx.exp0(0)),
                                self.visit(ctx.exp0(1)))

        return self.visit(ctx.exp0(0))

    def visitExp0(self, ctx: D96Parser.Exp0Context):
        if ctx.getChildCount() == 3:
            if ctx.EQUOP():
                return BinaryOp(ctx.EQUOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))

            if ctx.NEOP():
                return BinaryOp(ctx.NEOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))

            if ctx.LTOP():
                return BinaryOp(ctx.LTOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))

            if ctx.GTOP():
                return BinaryOp(ctx.GTOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))

            if ctx.LTEOP():
                return BinaryOp(ctx.LTEOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))

            if ctx.GTEOP():
                return BinaryOp(ctx.GTEOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))

        return self.visit(ctx.exp1(0))

    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if ctx.getChildCount() == 3:
            if ctx.ANDOP():
                return BinaryOp(ctx.ANDOP().getText(),
                                self.visit(ctx.exp1()),
                                self.visit(ctx.exp2()))

            if ctx.OROP():
                return BinaryOp(ctx.OROP().getText(),
                                self.visit(ctx.exp1()),
                                self.visit(ctx.exp2()))
        
        return self.visit(ctx.exp2())

    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if ctx.getChildCount() == 3:
            if ctx.ADDOP():
                return BinaryOp(ctx.ADDOP().getText(),
                                self.visit(ctx.exp2()),
                                self.visit(ctx.exp3()))

            if ctx.SUBOP():
                return BinaryOp(ctx.SUBOP().getText(),
                                self.visit(ctx.exp2()),
                                self.visit(ctx.exp3()))
        
        return self.visit(ctx.exp3())

    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if ctx.getChildCount() == 3:
            if ctx.MULOP():
                return BinaryOp(ctx.MULOP().getText(),
                                self.visit(ctx.exp3()),
                                self.visit(ctx.exp4()))

            if ctx.DIVOP():
                return BinaryOp(ctx.DIVOP().getText(),
                                self.visit(ctx.exp3()),
                                self.visit(ctx.exp4()))
        
            if ctx.MODOP():
                return BinaryOp(ctx.MODOP().getText(),
                                self.visit(ctx.exp3()),
                                self.visit(ctx.exp4()))

        return self.visit(ctx.exp4())

    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if ctx.NOTOP():
            return UnaryOp(ctx.NOTOP().getText(), self.visit(ctx.exp4()))
        return self.visit(ctx.exp5())

    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if ctx.SUBOP():
            return UnaryOp(ctx.SUBOP().getText(), self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())

    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.exp6()), self.visit(ctx.indexexp()))
        return self.visit(ctx.exp7())

    def visitExp7(self, ctx: D96Parser.Exp7Context):
        if ctx.getChildCount() > 1:
            if ctx.LB():
                return  CallExpr(self.visit(ctx.exp7()),
                                Id(ctx.ID().getText()),
                                self.visit(ctx.explist()) if ctx.explist() else [])
            return  FieldAccess(self.visit(ctx.exp7()),
                                Id(ctx.ID().getText()))
        return self.visit(ctx.exp8())

    def visitExp8(self, ctx: D96Parser.Exp8Context):
        if ctx.getChildCount() > 1:
            if ctx.LB():
                return  CallExpr(Id(ctx.ID().getText()),
                                Id(ctx.DOLLARID().getText()),
                                self.visit(ctx.explist()) if ctx.explist() else [])
            return  FieldAccess(Id(ctx.ID().getText()),
                                Id(ctx.DOLLARID().getText()))                
        return self.visit(ctx.exp9())

    def visitExp9(self, ctx: D96Parser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        return NewExpr(Id(ctx.ID().getText()), 
                        self.visit(ctx.explist()) if ctx.explist() else [])

    def visitOperands(self, ctx: D96Parser.OperandsContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            
            if ctx.literals():
                return self.visit(ctx.literals())

            if ctx.SELF():
                return SelfLiteral()
            
            return NullLiteral()
        
        return self.visit(ctx.exp())

    def visitLiterals(self, ctx: D96Parser.LiteralsContext):
        if ctx.INTLIT():
            intLit = ctx.INTLIT().getText()
            if (intLit[0] == '0'):
                if len(intLit) > 1:
                    if (intLit[1] not in ['X', 'x', 'B', 'b']):
                        intLit = intLit[:1] + "o" + intLit[1:]
                
            return IntLiteral(literal_eval(intLit))
        
        if ctx.FLOATLIT():
            floatLit = ctx.FLOATLIT().getText()
            if floatLit[0] == '.':
                floatLit = floatLit[:0] + "0" + floatLit[0:]
            return FloatLiteral(float(floatLit))

        if ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == 'True')

        if ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        
        if ctx.indexedarray():
            return self.visit(ctx.indexedarray())

        if ctx.multiarray():
            return self.visit(ctx.multiarray())

        if ctx.ARRAYSIZE():
            arraySize = ctx.ARRAYSIZE().getText()
            if (arraySize[0] == '0'):
                if len(arraySize) > 1:
                    if (arraySize[1] not in ['X', 'x', 'B', 'b']):
                        arraySize = arraySize[:1] + "o" + arraySize[1:]
                
            return IntLiteral(literal_eval(arraySize))

    def visitTyp(self, ctx: D96Parser.TypContext):
        if ctx.arraytyp():
            return self.visit(ctx.arraytyp())

        if ctx.primitivetyp():
            return self.visit(ctx.primitivetyp())

        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))

    def visitArraytyp(self, ctx: D96Parser.ArraytypContext):
        arraySize = ctx.ARRAYSIZE().getText()
        if (arraySize[0] == '0'):
            if len(arraySize) > 1:
                if (arraySize[1] not in ['X', 'x', 'B', 'b']):
                    arraySize = arraySize[:1] + "o" + arraySize[1:]
        return ArrayType(literal_eval(arraySize), self.visit(ctx.typ()))
    
    def visitPrimitivetyp(self, ctx: D96Parser.PrimitivetypContext):
        if ctx.INT():
            return IntType()

        if ctx.FLOAT():
            return FloatType()

        if ctx.BOOLEAN():
            return BoolType()

        return StringType()