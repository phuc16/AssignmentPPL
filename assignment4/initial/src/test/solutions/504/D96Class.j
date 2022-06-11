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
.var 1 is x I from Label0 to Label1
	iconst_1
	istore_1
Label2:
	iload_1
	bipush 15
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iconst_1
	invokestatic io/putInt(I)V
Label7:
	iload_1
	iconst_2
	iconst_2
	imul
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
.end method
