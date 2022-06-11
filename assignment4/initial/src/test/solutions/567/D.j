.source D.java
.class public D
.super java.lang.Object
.field d I

.method public <init>()V
.var 0 is this LD; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_2
	iconst_4
	iadd
	bipush 6
	bipush 7
	imul
	iadd
	putfield D/d I
Label1:
	return
.limit stack 4
.limit locals 1
.end method
