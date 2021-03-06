# statistical_sampling.py
import atexit, signal, traceback

def print_handler(signum, call_stack):
    line = traceback.extract_stack(call_stack)[0]
    print(f'line: {line.line} (signum={signum})')

def start(handler, interval=1):
    signal.signal(signal.SIGPROF, handler)
    signal.setitimer(signal.ITIMER_PROF, interval, interval)
    atexit.register(lambda: signal.setitimer(
        signal.ITIMER_PROF, 0))

start(print_handler)
result = 7 ** 7 ** 7
print(len(str(result)))
