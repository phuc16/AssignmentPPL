.source A.java
.class public A
.super java.lang.Object

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

.method public print(I)V
Label0:
.var 0 is this LA; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	iconst_1
	istore_2
Label2:
	iload_2
	iload_1
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_2
	iconst_4
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
Label11:
	iload_2
	invokestatic io/putInt(I)V
Label12:
Label10:
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 8
.limit locals 3
.end method
