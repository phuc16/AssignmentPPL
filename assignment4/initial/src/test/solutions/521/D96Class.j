.source D96Class.java
.class public D96Class
.super java.lang.Object
.field y I

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_1
	putfield D96Class/y I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a LA; from Label0 to Label1
	new A
	dup
	invokespecial A/<init>()V
	astore_1
	aload_1
	getfield A/x I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
