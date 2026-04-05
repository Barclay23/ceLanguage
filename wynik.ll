; --- NAGŁÓWKI I STAŁE ---
declare i32 @emoji_printf(i8*, ...)
declare i32 @emoji_scanf(i8*, ...)
declare void @exit(i32)
@fmt_out_int = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@fmt_out_double = private unnamed_addr constant [5 x i8] c"%lf\0A\00"
@fmt_in_int = private unnamed_addr constant [3 x i8] c"%d\00"
@fmt_in_double = private unnamed_addr constant [4 x i8] c"%lf\00"

; --- GŁÓWNY PROGRAM ---
define i32 @main() {
entry:
  %x = alloca i32
  store i32 10, i32* %x
  %y = alloca double
  store double 3.14, double* %y
  %arr = alloca [5 x i32]
  %1 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 0
  store i32 1, i32* %1
  %2 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 1
  store i32 2, i32* %2
  %3 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 2
  store i32 3, i32* %3
  %4 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 3
  store i32 4, i32* %4
  %5 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 4
  store i32 5, i32* %5
  %z = alloca i32
  store i32 0, i32* %z
  %6 = bitcast [3 x i8]* @fmt_in_int to i8*
  %7 = call i32 (i8*, ...) @emoji_scanf(i8* %6, i32* %z)
  %8 = load i32, i32* %x
  %9 = load i32, i32* %z
  %10 = add i32 %8, %9
  %11 = bitcast [4 x i8]* @fmt_out_int to i8*
  %12 = call i32 (i8*, ...) @emoji_printf(i8* %11, i32 %10)
  %13 = load double, double* %y
  %14 = fdiv double %13, 2.0
  %15 = bitcast [5 x i8]* @fmt_out_double to i8*
  %16 = call i32 (i8*, ...) @emoji_printf(i8* %15, double %14)
  %17 = load i32, i32* %x
  %18 = load i32, i32* %z
  %19 = mul i32 %18, 10
  %20 = mul i32 %19, 10
  %21 = add i32 %17, %20
  %22 = bitcast [4 x i8]* @fmt_out_int to i8*
  %23 = call i32 (i8*, ...) @emoji_printf(i8* %22, i32 %21)
  %24 = icmp uge i32 2, 5
  br i1 %24, label %bounds_err_25, label %bounds_ok_25

bounds_err_25:
  call void @exit(i32 1)
  unreachable

bounds_ok_25:
  %25 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 2
  %26 = load i32, i32* %25
  %27 = mul i32 %26, 10
  %28 = bitcast [4 x i8]* @fmt_out_int to i8*
  %29 = call i32 (i8*, ...) @emoji_printf(i8* %28, i32 %27)
  %30 = icmp uge i32 0, 5
  br i1 %30, label %bounds_err_31, label %bounds_ok_31

bounds_err_31:
  call void @exit(i32 1)
  unreachable

bounds_ok_31:
  %31 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 0
  %32 = load i32, i32* %31
  %33 = icmp uge i32 4, 5
  br i1 %33, label %bounds_err_34, label %bounds_ok_34

bounds_err_34:
  call void @exit(i32 1)
  unreachable

bounds_ok_34:
  %34 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 4
  %35 = load i32, i32* %34
  %36 = add i32 %32, %35
  %37 = bitcast [4 x i8]* @fmt_out_int to i8*
  %38 = call i32 (i8*, ...) @emoji_printf(i8* %37, i32 %36)
  %a = alloca i32
  store i32 1, i32* %a
  %b = alloca i32
  store i32 0, i32* %b
  %39 = load i32, i32* %a
  %40 = icmp ne i32 %39, 0
  %41 = and i1 %40, 1
  %42 = zext i1 %41 to i32
  %43 = bitcast [4 x i8]* @fmt_out_int to i8*
  %44 = call i32 (i8*, ...) @emoji_printf(i8* %43, i32 %42)
  %45 = load i32, i32* %b
  %46 = icmp ne i32 %45, 0
  %47 = or i1 %46, 0
  %48 = zext i1 %47 to i32
  %49 = bitcast [4 x i8]* @fmt_out_int to i8*
  %50 = call i32 (i8*, ...) @emoji_printf(i8* %49, i32 %48)
  %51 = and i1 0, 1
  %52 = zext i1 %51 to i32
  %53 = bitcast [4 x i8]* @fmt_out_int to i8*
  %54 = call i32 (i8*, ...) @emoji_printf(i8* %53, i32 %52)
  %55 = or i1 0, 1
  %56 = zext i1 %55 to i32
  %57 = bitcast [4 x i8]* @fmt_out_int to i8*
  %58 = call i32 (i8*, ...) @emoji_printf(i8* %57, i32 %56)
  %59 = xor i1 0, 1
  %60 = zext i1 %59 to i32
  %61 = bitcast [4 x i8]* @fmt_out_int to i8*
  %62 = call i32 (i8*, ...) @emoji_printf(i8* %61, i32 %60)
  %63 = xor i1 0, 1
  %64 = zext i1 %63 to i32
  %65 = bitcast [4 x i8]* @fmt_out_int to i8*
  %66 = call i32 (i8*, ...) @emoji_printf(i8* %65, i32 %64)
  %67 = icmp uge i32 1, 5
  br i1 %67, label %bounds_err_68, label %bounds_ok_68

bounds_err_68:
  call void @exit(i32 1)
  unreachable

bounds_ok_68:
  %68 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 1
  store i32 99, i32* %68
  %69 = icmp uge i32 1, 5
  br i1 %69, label %bounds_err_70, label %bounds_ok_70

bounds_err_70:
  call void @exit(i32 1)
  unreachable

bounds_ok_70:
  %70 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 1
  %71 = load i32, i32* %70
  %72 = bitcast [4 x i8]* @fmt_out_int to i8*
  %73 = call i32 (i8*, ...) @emoji_printf(i8* %72, i32 %71)
  %74 = load i32, i32* %a
  %75 = icmp ne i32 %74, 0
  %76 = and i1 %75, 1
  %77 = zext i1 %76 to i32
  %78 = bitcast [4 x i8]* @fmt_out_int to i8*
  %79 = call i32 (i8*, ...) @emoji_printf(i8* %78, i32 %77)
  %80 = load i32, i32* %b
  %81 = icmp ne i32 %80, 0
  %82 = or i1 %81, 0
  %83 = zext i1 %82 to i32
  %84 = bitcast [4 x i8]* @fmt_out_int to i8*
  %85 = call i32 (i8*, ...) @emoji_printf(i8* %84, i32 %83)
  %czyPada = alloca i1
  store i1 1, i1* %czyPada
  %czyCieplo = alloca i1
  store i1 0, i1* %czyCieplo
  %86 = load i1, i1* %czyPada
  %87 = zext i1 %86 to i32
  %88 = bitcast [4 x i8]* @fmt_out_int to i8*
  %89 = call i32 (i8*, ...) @emoji_printf(i8* %88, i32 %87)
  %90 = load i1, i1* %czyPada
  %91 = load i1, i1* %czyCieplo
  %92 = and i1 %90, %91
  %93 = zext i1 %92 to i32
  %94 = bitcast [4 x i8]* @fmt_out_int to i8*
  %95 = call i32 (i8*, ...) @emoji_printf(i8* %94, i32 %93)
  %c = alloca i32
  store i32 5, i32* %c
  %96 = load i32, i32* %c
  %97 = icmp ne i32 %96, 0
  store i1 %97, i1* %czyPada
  %98 = load i1, i1* %czyPada
  %99 = zext i1 %98 to i32
  %100 = bitcast [4 x i8]* @fmt_out_int to i8*
  %101 = call i32 (i8*, ...) @emoji_printf(i8* %100, i32 %99)
  ret i32 0
}