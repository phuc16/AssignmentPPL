.source D.java
.class public D
.super java.lang.Object

.method public getD2()F
Label0:
.var 0 is this LD; from Label0 to Label1
	ldc 2.4
	iconst_5
	i2f
	fdiv
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public getD(II)F
Label0:
.var 0 is this LD; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	aload_0
	invokevirtual D/getD2()F
	freturn
Label1:
.limit stack 1
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LD; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public Destructor()V
Label0:
.var 0 is this LD; from Label0 to Label1
Label1:
	return
.limit stack 0
.limit locals 1
.end method
