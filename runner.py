import sys
import subprocess

task_file = sys.argv[1]

commands = []

# read markdown file
with open(task_file, "r") as f:
    for line in f:
        line = line.strip()

        if line.startswith("- run:"):
            cmd = line.replace("- run:", "").strip()
            commands.append(cmd)

print("Commands found:")
for c in commands:
    print(" ", c)

print("\n--- Executing ---\n")

# execute commands
for cmd in commands:
    subprocess.run(cmd, shell=True)