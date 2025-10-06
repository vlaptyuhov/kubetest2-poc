import subprocess
import sys

def run_command(command):
  """Runs a shell command and checks for errors."""
  try:
    print(f"Executing: {' '.join(command)}")
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    if result.stdout:
      print(result.stdout)
    if result.stderr:
      print(result.stderr, file=sys.stderr)
  except subprocess.CalledProcessError as e:
    print(f"Error running command: {e}", file=sys.stderr)
    print(f"Stdout: {e.stdout}", file=sys.stderr)
    print(f"Stderr: {e.stderr}", file=sys.stderr)
    sys.exit(e.returncode)
  except FileNotFoundError:
    print(f"Error: Command not found: {command[0]}", file=sys.stderr)
    sys.exit(1)

def main():
  """Main function to replicate the bash script."""
  print("Running the script with kubetest2")

  # Run the kubetest2 command
  run_command(["kubetest2"])

  print("Running step 1 - setup cluster and run pre-test")
  # Add commands for step 1 here if needed

  print("Running step 2 - run tests")
  # Add commands for step 2 here if needed

  print("Running step 3 - run post-test")
  # Add commands for step 3 here if needed

  print("Finished Running the script with kubetest2")

if __name__ == "__main__":
  main()
