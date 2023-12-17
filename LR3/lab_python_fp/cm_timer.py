from contextlib import contextmanager
import time

class Cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        delta_time = time.time() - self.start_time
        print(f"time: {round(delta_time, 3)}")

@contextmanager
def Cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        delta_time = time.time() - start_time
        print(f"time: {round(delta_time, 3)}")

if __name__ == '__main__':
    with Cm_timer_1():
        time.sleep(5.5)

    with Cm_timer_2():
        time.sleep(5.5)
