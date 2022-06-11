.source Animal.java
.class public Animal
.super java.lang.Object
.field d Z
.field e Z
.field a LAnimal;
.field b I
.field c F

.method public <init>()V
.var 0 is this LAnimal; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield Animal/d Z
	aload_0
	iconst_2
	iconst_4
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	putfield Animal/e Z
	aload_0
	iconst_2
	iconst_5
	bipush 7
	imul
	iadd
	putfield Animal/b I
	aload_0
	iconst_2
	bipush 7
	imul
	i2f
	ldc 4.5
	fadd
	putfield Animal/c F
Label1:
	return
.limit stack 9
.limit locals 1
.end method

.method public get()V
Label0:
.var 0 is this LAnimal; from Label0 to Label1
	aload_0
	getfield Animal/c F
	invokestatic io/putFloatLn(F)V
	aload_0
	getfield Animal/d Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
