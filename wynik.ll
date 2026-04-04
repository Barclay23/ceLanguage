; --- NAGŁÓWKI I STAŁE ---
declare i32 @emoji_printf(i8*, ...)
declare i32 @emoji_scanf(i8*, ...)
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
  %24 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 2
  %25 = load i32, i32* %24
  %26 = mul i32 %25, 10
  %27 = bitcast [4 x i8]* @fmt_out_int to i8*
  %28 = call i32 (i8*, ...) @emoji_printf(i8* %27, i32 %26)
  %29 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 0
  %30 = load i32, i32* %29
  %31 = getelementptr [5 x i32], [5 x i32]* %arr, i32 0, i32 4
  %32 = load i32, i32* %31
  %33 = add i32 %30, %32
  %34 = bitcast [4 x i8]* @fmt_out_int to i8*
  %35 = call i32 (i8*, ...) @emoji_printf(i8* %34, i32 %33)
  %a = alloca i32
  store i32 1, i32* %a
  %b = alloca i32
  store i32 0, i32* %b
  %36 = and i1 0, 1
  %37 = zext i1 %36 to i32
  %38 = bitcast [4 x i8]* @fmt_out_int to i8*
  %39 = call i32 (i8*, ...) @emoji_printf(i8* %38, i32 %37)
  %40 = or i1 0, 1
  %41 = zext i1 %40 to i32
  %42 = bitcast [4 x i8]* @fmt_out_int to i8*
  %43 = call i32 (i8*, ...) @emoji_printf(i8* %42, i32 %41)
  %44 = xor i1 0, 1
  %45 = zext i1 %44 to i32
  %46 = bitcast [4 x i8]* @fmt_out_int to i8*
  %47 = call i32 (i8*, ...) @emoji_printf(i8* %46, i32 %45)
  %48 = xor i1 0, 1
  %49 = zext i1 %48 to i32
  %50 = bitcast [4 x i8]* @fmt_out_int to i8*
  %51 = call i32 (i8*, ...) @emoji_printf(i8* %50, i32 %49)
  ret i32 0
}