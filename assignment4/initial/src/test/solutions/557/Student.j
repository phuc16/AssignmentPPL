.source Student.java
.class public Student
.super java.lang.Object
.field name Ljava/lang/String;
.field ID I

.method public <init>(Ljava/lang/String;I)V
.var 0 is this LStudent; from Label0 to Label1
.var 1 is newName Ljava/lang/String; from Label0 to Label1
.var 2 is newID I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Student/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Student/ID I
Label1:
	return
.limit stack 6
.limit locals 3
.end method
