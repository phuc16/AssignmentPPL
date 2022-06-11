.source D.java
.class public D
.super java.lang.Object

.method public getD()Ljava/lang/String;
Label0:
.var 0 is this LD; from Label0 to Label1
	ldc "Hello From D"
	areturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LD; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public Destructor()V
Label0:
.var 0 is this LD; from Label0 to Label1
Label1:
	return
.limit stack 0
.limit locals 1
.end method
