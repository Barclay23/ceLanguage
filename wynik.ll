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
  %arr = alloca [3 x i32]
  %1 = getelementptr [3 x i32], [3 x i32]* %arr, i32 0, i32 0
  store i32 1, i32* %1
  %2 = getelementptr [3 x i32], [3 x i32]* %arr, i32 0, i32 1
  store i32 2, i32* %2
  %3 = getelementptr [3 x i32], [3 x i32]* %arr, i32 0, i32 2
  store i32 3, i32* %3
  %4 = icmp uge i32 100, 3
  br i1 %4, label %bounds_err_5, label %bounds_ok_5

bounds_err_5:
  call void @exit(i32 1)
  unreachable

bounds_ok_5:
  %5 = getelementptr [3 x i32], [3 x i32]* %arr, i32 0, i32 100
  store i32 99, i32* %5
  %6 = icmp uge i32 100, 3
  br i1 %6, label %bounds_err_7, label %bounds_ok_7

bounds_err_7:
  call void @exit(i32 1)
  unreachable

bounds_ok_7:
  %7 = getelementptr [3 x i32], [3 x i32]* %arr, i32 0, i32 100
  %8 = load i32, i32* %7
  %9 = bitcast [4 x i8]* @fmt_out_int to i8*
  %10 = call i32 (i8*, ...) @emoji_printf(i8* %9, i32 %8)
  %czyPada = alloca i1
  store i1 1, i1* %czyPada
  %czyCieplo = alloca i1
  store i1 0, i1* %czyCieplo
  %11 = load i1, i1* %czyPada
  %12 = zext i1 %11 to i32
  %13 = bitcast [4 x i8]* @fmt_out_int to i8*
  %14 = call i32 (i8*, ...) @emoji_printf(i8* %13, i32 %12)
  %15 = load i1, i1* %czyPada
  %16 = load i1, i1* %czyCieplo
  %17 = and i1 %15, %16
  %18 = zext i1 %17 to i32
  %19 = bitcast [4 x i8]* @fmt_out_int to i8*
  %20 = call i32 (i8*, ...) @emoji_printf(i8* %19, i32 %18)
  ret i32 0
}