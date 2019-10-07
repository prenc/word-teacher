import time


class TimeCounter:
    def __init__(self):
        self.program_start_time = time.time()
        self.start_time = 0
        self.elapsed_time = 0
        self.counted_times = []

    def start_counting(self):
        self.start_time = time.time()

    def stop_counting(self):
        self.elapsed_time = time.time() - self.start_time
        self.counted_times.append(self.elapsed_time)
        return self.elapsed_time

    def info(self):
        return f"{self.elapsed_time:.2f}s"

    def time_stats(self):
        return (
            f"Time Stats:\n"
            f"Average time for correct answer: {sum(self.counted_times) / len(self.counted_times):.2f}s\n"
            f"Quickest correct answer: {min(self.counted_times):.2f}s\n"
            f"Longest correct answer: {max(self.counted_times):.2f}s\n"
            f"It took you {time.time() - self.program_start_time:.2f}s to get all the answers."
        )
