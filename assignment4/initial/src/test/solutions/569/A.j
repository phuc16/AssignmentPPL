.source A.java
.class public A
.super java.lang.Object
.field b [I

.method public getA(F)V
Label0:
.var 0 is this LA; from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is a [I from Label0 to Label1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	ldc 6.7
	iastore
	astore_2
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
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
.var 0 is this LA; from Label0 to Label1
Label1:
	return
.limit stack 0
.limit locals 1
.end method
