import sys
import subprocess
import os

task_file = sys.argv[1]

event = os.getenv("GITHUB_EVENT_NAME")
print("GitHub Event:", event)

commands = []

with open(task_file, "r") as f:
    for line in f:
        line = line.strip()

        if line.startswith("- run:"):
            cmd = line.replace("- run:", "").strip()
            commands.append(cmd)

print("\nCommands found:")
for c in commands:
    print(" ", c)

print("\n--- Executing ---\n")

for cmd in commands:
    subprocess.run(cmd, shell=True)