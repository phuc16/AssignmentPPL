.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
	iconst_1
	istore_2
Label2:
	iload_2
	iconst_4
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_2
	istore_3
Label8:
	iload_3
	iconst_4
	if_icmpgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label12:
	aload_1
	iload_3
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
Label13:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label8
Label9:
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	invokestatic io/putIntLn(I)V
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
.limit locals 4
.end method
