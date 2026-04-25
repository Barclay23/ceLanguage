#include <stdio.h>
#include <stdarg.h>


int emoji_scanf(const char* format, ...) {
    va_list args;
    va_start(args, format);
    int result = vscanf(format, args);
    va_end(args);
    return result;
}


int emoji_printf(const char* format, ...) {
    va_list args;
    va_start(args, format);
    int result = vprintf(format, args);
    va_end(args);
    return result;
}