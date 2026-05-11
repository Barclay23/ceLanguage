declare i32 @emoji_printf(i8*, ...)
declare i32 @emoji_scanf(i8*, ...)
declare void @exit(i32)
@fmt_out_int = private unnamed_addr constant [4 x i8] c"%d\0A\00"
@fmt_out_double = private unnamed_addr constant [5 x i8] c"%lf\0A\00"
@fmt_in_int = private unnamed_addr constant [3 x i8] c"%d\00"
@fmt_in_double = private unnamed_addr constant [4 x i8] c"%lf\00"
@fmt_out_str = private unnamed_addr constant [4 x i8] c"%s\0A\00"
@fmt_in_str = private unnamed_addr constant [3 x i8] c"%s\00"
define i32 @main() {
entry:
  %i = alloca i32
  store i32 0, i32* %i
  br label %while_cond_1

while_cond_1:
  %2 = load i32, i32* %i
  %3 = icmp slt i32 %2, 3
  br i1 %3, label %while_body_1, label %while_end_1

while_body_1:
  %4 = load i32, i32* %i
  %5 = bitcast [4 x i8]* @fmt_out_int to i8*
  %6 = call i32 (i8*, ...) @emoji_printf(i8* %5, i32 %4)
  %7 = load i32, i32* %i
  %8 = add i32 %7, 1
  store i32 %8, i32* %i
  br label %while_cond_1

while_end_1:
  %9 = load i32, i32* %i
  %10 = bitcast [4 x i8]* @fmt_out_int to i8*
  %11 = call i32 (i8*, ...) @emoji_printf(i8* %10, i32 %9)
  ret i32 0
}