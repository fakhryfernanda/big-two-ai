import cProfile
import pstats
import io

class GameProfiler:
    def __init__(self, directory, stats_count):
        self.directory = directory
        self.stats_count = stats_count
        self.profiler = cProfile.Profile()
        
    def start(self):
        self.profiler.enable()
        
    def stop(self):
        self.profiler.disable()
        
    def save_results(self, filename):
        stream = io.StringIO()
        stats = pstats.Stats(self.profiler, stream=stream)
        stats.strip_dirs().sort_stats("tottime").print_stats(self.stats_count)
        
        with open(filename, "w") as f:
            f.write(stream.getvalue())
            
        return stream.getvalue()
