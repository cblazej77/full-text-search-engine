import subprocess
import sys

# Metoda uruchamiająca dany skrypt
def run_script(script_path):
    print(f"Launching {script_path} ...")
    result = subprocess.run([sys.executable, script_path], text=True)
    
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error in {script_path}:\n", result.stderr)
        sys.exit(result.returncode)

if __name__ == "__main__":
    run_script("indexer_test.py")
    run_script("search_engine_test.py")
    run_script("indexer.py")
    run_script("search_engine.py")
