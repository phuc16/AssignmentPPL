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
.var 1 is c I from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	iconst_4
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
.var 2 is a I from Label5 to Label6
	iconst_2
	istore_2
.var 3 is c I from Label5 to Label6
	iconst_1
	istore_3
Label7:
	iload_3
	bipush 100
	if_icmpgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
Label11:
	iload_3
	invokestatic io/putInt(I)V
Label12:
	iload_3
	iload_2
	iadd
	istore_3
	goto Label7
Label8:
Label6:
Label4:
Label1:
	return
.limit stack 8
.limit locals 4
.end method
