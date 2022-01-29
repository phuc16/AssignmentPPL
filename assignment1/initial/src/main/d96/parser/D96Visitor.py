# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classbody.
    def visitClassbody(self, ctx:D96Parser.ClassbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrdecl.
    def visitAttrdecl(self, ctx:D96Parser.AttrdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mutable.
    def visitMutable(self, ctx:D96Parser.MutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#immutable.
    def visitImmutable(self, ctx:D96Parser.ImmutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#nonvalue.
    def visitNonvalue(self, ctx:D96Parser.NonvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#nonvaluedollar.
    def visitNonvaluedollar(self, ctx:D96Parser.NonvaluedollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value.
    def visitValue(self, ctx:D96Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#valuedollar.
    def visitValuedollar(self, ctx:D96Parser.ValuedollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methdecl.
    def visitMethdecl(self, ctx:D96Parser.MethdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#basicmeth.
    def visitBasicmeth(self, ctx:D96Parser.BasicmethContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paralist.
    def visitParalist(self, ctx:D96Parser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodattrdecl.
    def visitMethodattrdecl(self, ctx:D96Parser.MethodattrdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexedarray.
    def visitIndexedarray(self, ctx:D96Parser.IndexedarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraylist.
    def visitArraylist(self, ctx:D96Parser.ArraylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiarray.
    def visitMultiarray(self, ctx:D96Parser.MultiarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiarraylist.
    def visitMultiarraylist(self, ctx:D96Parser.MultiarraylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockstmt.
    def visitBlockstmt(self, ctx:D96Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignstmt.
    def visitAssignstmt(self, ctx:D96Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexexp.
    def visitIndexexp(self, ctx:D96Parser.IndexexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifstmt.
    def visitIfstmt(self, ctx:D96Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forinstmt.
    def visitForinstmt(self, ctx:D96Parser.ForinstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakstmt.
    def visitBreakstmt(self, ctx:D96Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continuestmt.
    def visitContinuestmt(self, ctx:D96Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnstmt.
    def visitReturnstmt(self, ctx:D96Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodinvostmt.
    def visitMethodinvostmt(self, ctx:D96Parser.MethodinvostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#explist.
    def visitExplist(self, ctx:D96Parser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp0.
    def visitExp0(self, ctx:D96Parser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraytyp.
    def visitArraytyp(self, ctx:D96Parser.ArraytypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitivetyp.
    def visitPrimitivetyp(self, ctx:D96Parser.PrimitivetypContext):
        return self.visitChildren(ctx)



del D96Parser