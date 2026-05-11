import os
import subprocess
import glob
import sys

TEST_DIR = "emoji_tests"
COMPILER_SCRIPT = "Driver.py"
CLANG_OUT = "emojiprog.exe"

test_files = glob.glob(os.path.join(TEST_DIR, "*.emoji"))

print(f"Znaleziono {len(test_files)} plikow testowych.\n")

for test_file in test_files:
    
    print(f"Plik: {os.path.basename(test_file)}")

    print("[1/3] Translacja do LLVM IR...")
    compilation = subprocess.run([sys.executable, COMPILER_SCRIPT, test_file], capture_output=True, text=True)
    
    if compilation.returncode != 0:
        print("[BLAD] Wykryto wyjatek (np. oczekiwany blad semantyczny):")
        print(compilation.stderr.strip() or compilation.stdout.strip())
        print("\n")
        continue 

    print("[2/3] Generowanie pliku wykonywalnego (Clang)...")
    clang_process = subprocess.run(["clang", "wynik.ll", "wrapper.c", "-o", CLANG_OUT], capture_output=True, text=True)
    
    if clang_process.returncode != 0:
        print("[BLAD] Blad narzedzia Clang:")
        print(clang_process.stderr.strip())
        print("\n")
        continue

    print("[3/3] Wykonanie programu:\n")
    print("vvv WYNIK vvv")
    
    run_process = subprocess.run([f".\\{CLANG_OUT}"], capture_output=True, text=True)
    print(run_process.stdout.strip())
    
    if run_process.stderr:
        print(run_process.stderr.strip())
        
    print("^^^ KONIEC ^^^")
    print("\n")

print("Zakonczono wykonywanie wszystkich testow.")