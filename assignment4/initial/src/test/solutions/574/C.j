.source C.java
.class public C
.super D

.method public getC(IF)I
Label0:
.var 0 is this LC; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
	iconst_3
	ireturn
Label1:
.limit stack 1
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LC; from Label0 to Label1
Label0:
	aload_0
	invokespecial D/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public Destructor()V
Label0:
.var 0 is this LC; from Label0 to Label1
Label1:
	return
.limit stack 0
.limit locals 1
.end method
