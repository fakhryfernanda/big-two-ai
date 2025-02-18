import subprocess
from config import GameConfig

for i in range(GameConfig.TEST_ITERATION):
    print(f"Running iteration {i+1}/{N}...")
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    
    # Print or log the output
    print(result.stdout)
    
    # Optionally, log errors if they occur
    if result.stderr:
        print(f"Error in iteration {i+1}: {result.stderr}")
