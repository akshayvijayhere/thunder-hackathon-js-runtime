import sys
import subprocess

def execute_js(code):
    result = subprocess.run(
        ["node", "-e", code],
        capture_output=True,
        text=True
    )

    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    else:
        code = sys.stdin.read()

    execute_js(code)
