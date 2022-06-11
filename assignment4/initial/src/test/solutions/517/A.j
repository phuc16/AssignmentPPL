.source A.java
.class public A
.super java.lang.Object
.field b F

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc 3.4
	putfield A/b F
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public getA(F)F
Label0:
.var 0 is this LA; from Label0 to Label1
.var 1 is a F from Label0 to Label1
	fload_1
	freturn
Label1:
.limit stack 1
.limit locals 2
.end method
