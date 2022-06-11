.source D96Class.java
.class public D96Class
.super java.lang.Object
.field att I

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 20
	putfield D96Class/att I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public foo()V
Label0:
.var 0 is this LD96Class; from Label0 to Label1
	aload_0
	bipush 30
	putfield D96Class/att I
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is Program LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
	aload_1
	invokevirtual D96Class/foo()V
	aload_1
	getfield D96Class/att I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
