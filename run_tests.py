import subprocess
from config import GameConfig

N = GameConfig.TEST_ITERATION

for i in range(N):
    print(f"Running iteration {i+1}/{N}...")
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    
    # Print or log the output
    print(result.stdout)
    
    # Optionally, log errors if they occur
    if result.stderr:
        print(f"Error in iteration {i+1}: {result.stderr}")
