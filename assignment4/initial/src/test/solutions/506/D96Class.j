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

.method public static $sum(I)F
Label0:
.var 0 is n I from Label0 to Label1
.var 1 is a LA; from Label0 to Label1
	new A
	dup
	invokespecial A/<init>()V
	astore_1
	aload_1
	getfield A/x I
	i2f
	ldc 12.2
	iconst_2
	i2f
	fdiv
	fadd
	iload_0
	i2f
	fadd
	freturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 12
	invokestatic D96Class/$sum(I)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
