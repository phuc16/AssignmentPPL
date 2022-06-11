.source D96Class.java
.class public D96Class
.super java.lang.Object
.field total [I

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	putfield D96Class/total [I
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public change(I)V
Label0:
.var 0 is this LD96Class; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	aload_0
	getfield D96Class/total [I
	iload_1
	iconst_1
	isub
	bipush 100
	iastore
Label1:
	return
.limit stack 8
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is Program LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
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
	aload_1
	getfield D96Class/total [I
	iload_2
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iload_2
	invokevirtual D96Class/change(I)V
	aload_1
	getfield D96Class/total [I
	iload_2
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method
