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
.var 1 is myStudent LStudent; from Label0 to Label1
	new Student
	dup
	ldc "Phuc"
	sipush 4720
	invokespecial Student/<init>(Ljava/lang/String;I)V
	astore_1
	aload_1
	getfield Student/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	getfield Student/ID I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method
