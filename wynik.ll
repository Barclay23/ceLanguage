declare i32 @emoji_printf(i8*, ...)
declare i32 @emoji_scanf(i8*, ...)
declare void @exit(i32)
@fmt_out_int = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@fmt_out_double = private unnamed_addr constant [5 x i8] c"%lf\0A\00"
@fmt_in_int = private unnamed_addr constant [3 x i8] c"%d\00"
@fmt_in_double = private unnamed_addr constant [4 x i8] c"%lf\00"
@fmt_out_str = private unnamed_addr constant [4 x i8] c"%s\0A\00"
@fmt_in_str = private unnamed_addr constant [3 x i8] c"%s\00"
@.str.lit.0 = private unnamed_addr constant [12 x i8] c"Hello World\00"
@.str.lit.1 = private unnamed_addr constant [5 x i8] c"brak\00"
@.str.lit.2 = private unnamed_addr constant [10 x i8] c"zapisano.\00"
define i32 @main() {
entry:
  %powitanie = alloca i8*
  %1 = bitcast [12 x i8]* @.str.lit.0 to i8*
  store i8* %1, i8** %powitanie
  %2 = load i8*, i8** %powitanie
  %3 = bitcast [4 x i8]* @fmt_out_str to i8*
  %4 = call i32 (i8*, ...) @emoji_printf(i8* %3, i8* %2)
  %imie = alloca i8*
  %5 = bitcast [5 x i8]* @.str.lit.1 to i8*
  store i8* %5, i8** %imie
  %6 = bitcast [3 x i8]* @fmt_in_str to i8*
  %7 = alloca [256 x i8]
  %8 = bitcast [256 x i8]* %7 to i8*
  %9 = call i32 (i8*, ...) @emoji_scanf(i8* %6, i8* %8)
  store i8* %8, i8** %imie
  %odpowiedz = alloca i8*
  %10 = bitcast [10 x i8]* @.str.lit.2 to i8*
  store i8* %10, i8** %odpowiedz
  %11 = load i8*, i8** %odpowiedz
  %12 = bitcast [4 x i8]* @fmt_out_str to i8*
  %13 = call i32 (i8*, ...) @emoji_printf(i8* %12, i8* %11)
  %14 = load i8*, i8** %imie
  %15 = bitcast [4 x i8]* @fmt_out_str to i8*
  %16 = call i32 (i8*, ...) @emoji_printf(i8* %15, i8* %14)
  ret i32 0
}