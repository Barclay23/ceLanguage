declare i32 @emoji_printf(i8*, ...)
declare i32 @emoji_scanf(i8*, ...)
declare void @exit(i32)
@fmt_out_int = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@fmt_out_double = private unnamed_addr constant [5 x i8] c"%lf\0A\00"
@fmt_in_int = private unnamed_addr constant [3 x i8] c"%d\00"
@fmt_in_double = private unnamed_addr constant [4 x i8] c"%lf\00"
define i32 @f() {
entry:
  ret i32 1
}
define i32 @g() {
entry:
  ret i32 2
}
define i32 @main() {
entry:
  %1 = call i32 @f()
  %2 = bitcast [4 x i8]* @fmt_out_int to i8*
  %3 = call i32 (i8*, ...) @emoji_printf(i8* %2, i32 %1)
  %4 = call i32 @g()
  %5 = bitcast [4 x i8]* @fmt_out_int to i8*
  %6 = call i32 (i8*, ...) @emoji_printf(i8* %5, i32 %4)
  %x = alloca i32
  store i32 10, i32* %x
  %y = alloca double
  store double 3.14, double* %y
  %arr = alloca [5 x i32]
  %7 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 0
  store i32 1, i32* %7
  %8 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 1
  store i32 2, i32* %8
  %9 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 2
  store i32 3, i32* %9
  %10 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 3
  store i32 4, i32* %10
  %11 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 4
  store i32 5, i32* %11
  %z = alloca i32
  store i32 0, i32* %z
  %12 = bitcast [3 x i8]* @fmt_in_int to i8*
  %13 = call i32 (i8*, ...) @emoji_scanf(i8* %12, i32* %z)
  %14 = load i32, i32* %x
  %15 = load i32, i32* %z
  %16 = add i32 %14, %15
  %17 = bitcast [4 x i8]* @fmt_out_int to i8*
  %18 = call i32 (i8*, ...) @emoji_printf(i8* %17, i32 %16)
  %19 = load double, double* %y
  %20 = fdiv double %19, 2.0
  %21 = bitcast [5 x i8]* @fmt_out_double to i8*
  %22 = call i32 (i8*, ...) @emoji_printf(i8* %21, double %20)
  %23 = load i32, i32* %x
  %24 = load i32, i32* %z
  %25 = mul i32 %24, 10
  %26 = mul i32 %25, 10
  %27 = add i32 %23, %26
  %28 = bitcast [4 x i8]* @fmt_out_int to i8*
  %29 = call i32 (i8*, ...) @emoji_printf(i8* %28, i32 %27)
  %30 = icmp uge i32 2, 5
  br i1 %30, label %bounds_err_31, label %bounds_ok_31

bounds_err_31:
  call void @exit(i32 1)
  unreachable

bounds_ok_31:
  %31 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 2
  %32 = load i32, i32* %31
  %33 = mul i32 %32, 10
  %34 = bitcast [4 x i8]* @fmt_out_int to i8*
  %35 = call i32 (i8*, ...) @emoji_printf(i8* %34, i32 %33)
  %36 = icmp uge i32 0, 5
  br i1 %36, label %bounds_err_37, label %bounds_ok_37

bounds_err_37:
  call void @exit(i32 1)
  unreachable

bounds_ok_37:
  %37 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 0
  %38 = load i32, i32* %37
  %39 = icmp uge i32 4, 5
  br i1 %39, label %bounds_err_40, label %bounds_ok_40

bounds_err_40:
  call void @exit(i32 1)
  unreachable

bounds_ok_40:
  %40 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 4
  %41 = load i32, i32* %40
  %42 = add i32 %38, %41
  %43 = bitcast [4 x i8]* @fmt_out_int to i8*
  %44 = call i32 (i8*, ...) @emoji_printf(i8* %43, i32 %42)
  %a = alloca i32
  store i32 1, i32* %a
  %b = alloca i32
  store i32 0, i32* %b
  %45 = and i1 0, 1
  %46 = zext i1 %45 to i32
  %47 = bitcast [4 x i8]* @fmt_out_int to i8*
  %48 = call i32 (i8*, ...) @emoji_printf(i8* %47, i32 %46)
  %49 = or i1 0, 1
  %50 = zext i1 %49 to i32
  %51 = bitcast [4 x i8]* @fmt_out_int to i8*
  %52 = call i32 (i8*, ...) @emoji_printf(i8* %51, i32 %50)
  %53 = xor i1 0, 1
  %54 = zext i1 %53 to i32
  %55 = bitcast [4 x i8]* @fmt_out_int to i8*
  %56 = call i32 (i8*, ...) @emoji_printf(i8* %55, i32 %54)
  %57 = xor i1 0, 1
  %58 = zext i1 %57 to i32
  %59 = bitcast [4 x i8]* @fmt_out_int to i8*
  %60 = call i32 (i8*, ...) @emoji_printf(i8* %59, i32 %58)
  %61 = icmp uge i32 1, 5
  br i1 %61, label %bounds_err_62, label %bounds_ok_62

bounds_err_62:
  call void @exit(i32 1)
  unreachable

bounds_ok_62:
  %62 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 1
  store i32 99, i32* %62
  %63 = icmp uge i32 1, 5
  br i1 %63, label %bounds_err_64, label %bounds_ok_64

bounds_err_64:
  call void @exit(i32 1)
  unreachable

bounds_ok_64:
  %64 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 1
  %65 = load i32, i32* %64
  %66 = bitcast [4 x i8]* @fmt_out_int to i8*
  %67 = call i32 (i8*, ...) @emoji_printf(i8* %66, i32 %65)
  %czyPada = alloca i1
  store i1 1, i1* %czyPada
  %czyCieplo = alloca i1
  store i1 0, i1* %czyCieplo
  %68 = load i1, i1* %czyPada
  %69 = zext i1 %68 to i32
  %70 = bitcast [4 x i8]* @fmt_out_int to i8*
  %71 = call i32 (i8*, ...) @emoji_printf(i8* %70, i32 %69)
  %72 = load i1, i1* %czyPada
  %73 = load i1, i1* %czyCieplo
  %74 = and i1 %72, %73
  %75 = zext i1 %74 to i32
  %76 = bitcast [4 x i8]* @fmt_out_int to i8*
  %77 = call i32 (i8*, ...) @emoji_printf(i8* %76, i32 %75)
  %prawda = alloca i1
  store i1 1, i1* %prawda
  %78 = load i32, i32* %z
  %79 = add i32 %78, 5
  %80 = load i32, i32* %x
  %81 = icmp sgt i32 %79, %80
  br i1 %81, label %if_then_82, label %if_else_82

if_then_82:
  %83 = load i32, i32* %x
  %84 = load i32, i32* %z
  %85 = add i32 %83, %84
  %86 = bitcast [4 x i8]* @fmt_out_int to i8*
  %87 = call i32 (i8*, ...) @emoji_printf(i8* %86, i32 %85)
  br label %if_end_82

if_else_82:
  %88 = load i32, i32* %x
  %89 = load i32, i32* %z
  %90 = mul i32 %88, %89
  %91 = bitcast [4 x i8]* @fmt_out_int to i8*
  %92 = call i32 (i8*, ...) @emoji_printf(i8* %91, i32 %90)
  br label %if_end_82

if_end_82:
  %i = alloca i32
  store i32 0, i32* %i
  br label %while_cond_93

while_cond_93:
  %94 = load i32, i32* %i
  %95 = load i32, i32* %z
  %96 = icmp slt i32 %94, %95
  br i1 %96, label %while_body_93, label %while_end_93

while_body_93:
  %97 = load i32, i32* %i
  %98 = load i32, i32* %z
  %99 = add i32 %97, %98
  %100 = bitcast [4 x i8]* @fmt_out_int to i8*
  %101 = call i32 (i8*, ...) @emoji_printf(i8* %100, i32 %99)
  %102 = load i32, i32* %i
  %103 = add i32 %102, 1
  store i32 %103, i32* %i
  br label %while_cond_93

while_end_93:
  ret i32 0
}