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
.var 1 is a I from Label0 to Label1
	iconst_2
	istore_1
	iconst_3
	istore_1
	iconst_4
	i2f
	iload_1
	i2f
	fdiv
	iconst_3
	i2f
	iconst_3
	i2f
	fdiv
	fadd
	ldc 2.5
	fsub
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method
