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
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	dup
	iconst_5
	iconst_1
	iastore
	dup
	bipush 6
	iconst_2
	iastore
	dup
	bipush 7
	iconst_3
	iastore
	dup
	bipush 8
	iconst_4
	iastore
	dup
	bipush 9
	iconst_5
	iastore
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
	iconst_1
	istore_2
Label2:
	iload_2
	bipush 10
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_2
	iconst_3
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
Label11:
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
Label12:
	goto Label13
Label10:
	iload_2
	iconst_3
	irem
	iconst_1
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label17:
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	iconst_2
	imul
	invokestatic io/putInt(I)V
Label18:
	goto Label19
Label16:
Label20:
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	iconst_3
	imul
	invokestatic io/putInt(I)V
Label21:
Label19:
Label13:
Label7:
	iload_2
	iconst_1
	iconst_2
	iadd
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 11
.limit locals 4
.end method
