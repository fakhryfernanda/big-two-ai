class GameConfig:
    # Player settings
    PLAYER_1_IS_USER = False

    # Game settings
    MAX_ROUNDS = 20
    WEIGHTS = {
        "single": 1,
        "pair": 2,
        "triple": 3,
        "quad": 4,
        "five_card": 5
    }
    
    # Print settings
    PRINT_GAME_ENABLED = False
    
    # Logging settings
    LOGGING_ENABLED = True
    SIMPLIFIED_LOGGING = True

    # Profiling settings
    PROFILE_DIR = "profiling"
    TOP_STATS_COUNT = 20
    PROFILING_ENABLED = True

    # AI
    PASS_PROBABILITY = 0.05

    # Number of times to run main.py when run test
    TEST_ITERATION = 5 
