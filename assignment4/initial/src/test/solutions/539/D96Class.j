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
.var 1 is a F from Label0 to Label1
	ldc 1.234
	fstore_1
	fload_1
	iconst_2
	i2f
	fdiv
	bipush 25
	i2f
	fmul
	sipush 2262
	i2f
	fadd
	sipush 2352
	sipush 3223
	imul
	i2f
	fsub
	sipush 2352
	i2f
	sipush 25262
	i2f
	fdiv
	sipush 2252
	i2f
	fmul
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method
