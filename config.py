class GameConfig:        
    # Game settings
    MAX_ROUNDS = 20
    WEIGHTS = {
        "single": 1,
        "pair": 2,
        "triple": 3,
        "quad": 4,
        "five_card": 5
    }
    
    # Feature settings
    LOGGING_ENABLED = False
    PROFILE_DIR = "profiling"
    TOP_STATS_COUNT = 20
    PROFILING_ENABLED = False
    PRINT_GAME_ENABLED = False
    
    # AI
    PASS_PROBABILITY = 0.1

    # Number of times to run main.py when run test
    TEST_ITERATION = 5 
