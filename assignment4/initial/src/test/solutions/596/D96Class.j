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

.method public foo()I
Label0:
.var 0 is this LD96Class; from Label0 to Label1
	bipush 100
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is A LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
.var 2 is B LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_2
.var 3 is zoo I from Label0 to Label1
	aload_1
	invokevirtual D96Class/foo()I
	istore_3
	iload_3
	aload_2
	invokevirtual D96Class/foo()I
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method
