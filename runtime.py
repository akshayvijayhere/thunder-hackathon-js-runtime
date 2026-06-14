import subprocess

print("=== JavaScript Runtime ===")
print("Paste JS code. Type RUN on a new line to execute.\n")

code = []

while True:
    line = input()

    if line.strip() == "RUN":
        break

    code.append(line)

js_code = "\n".join(code)

result = subprocess.run(
    ["node", "-e", js_code],
    capture_output=True,
    text=True
)

if result.stdout:
    print(result.stdout)

if result.stderr:
    print(result.stderr)
