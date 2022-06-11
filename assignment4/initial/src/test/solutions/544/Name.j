.source Name.java
.class public Name
.super java.lang.Object
.field name Ljava/lang/String;
.field age I

.method public <init>()V
.var 0 is this LName; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc "My Name"
	putfield Name/name Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public func()V
Label0:
.var 0 is this LName; from Label0 to Label1
	aload_0
	aload_0
	getfield Name/name Ljava/lang/String;
	ldc "is Program"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	putfield Name/name Ljava/lang/String;
Label1:
	return
.limit stack 5
.limit locals 1
.end method
