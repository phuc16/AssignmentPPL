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
.var 1 is b LC; from Label0 to Label1
	new C
	dup
	invokespecial C/<init>()V
	astore_1
	aload_1
	getfield C/z F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
