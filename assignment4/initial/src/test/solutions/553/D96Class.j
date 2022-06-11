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

.method public static $factorial(I)Ljava/lang/String;
Label0:
.var 0 is n I from Label0 to Label1
	iload_0
	iconst_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	ldc "1"
	areturn
Label6:
Label4:
Label8:
	ldc "Program::$factorial(n - 1) * n"
	areturn
Label9:
Label7:
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is c I from Label0 to Label1
	bipush 6
	invokestatic D96Class/$factorial(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method
