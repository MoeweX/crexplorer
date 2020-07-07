#!/usr/bin/env python3

from timeit import Timer
import multiprocessing
import math
import time
import cherrypy
import os
from datetime import datetime
from pythonping import ping

try:
    logFilePath = os.environ["LOGFILE"]
    logFile = open(logFilePath, "a", 1)
    print("Writing logs to " + logFilePath)
except KeyError as e:
    print("Logging to file is disabled, to enable provide a LOGFILE environment variable")
except Exception as e:
    print(repr(e))

def log(text):
    now = datetime.now()
    toLog = now.strftime("%H:%M:%S - ") + text
    if "LOGFILE" in os.environ:
        logFile.write(toLog + "\n")
    print(toLog)

def fibonacci(n):
    a = 0
    b = 1
    r = -1
    if n < 0:
        log("Incorrect input")
        return
    elif n == 0:
        r = a
    elif n == 1:
        r = b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        r = b
    # log("Fibonacci number {0!s} is {1!s}".format(n, r))

def parallized_fibonacci_benchmark(i, runs_per_core, measurements):
    t = Timer(lambda: fibonacci(10000))
    measurements[i] = t.repeat(number=runs_per_core, repeat=3)

class Server(object):
    @cherrypy.expose
    def run(self, max_memory=10):
        single_run(int(max_memory))
        return("Run completed, results are written to console.")

def single_run(max_memory):
    start_printing = max(max_memory - 100, int(max_memory / 2))

    log("Starting CPU benchmark")
    manager = multiprocessing.Manager()
    measurements = manager.dict()

    processes = []
    cores = multiprocessing.cpu_count()
    for i in range(0,cores):
        runs_per_core = int(2000 / cores)
        p = multiprocessing.Process(target=parallized_fibonacci_benchmark, args=(i,runs_per_core,measurements))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    # determine total results for all operations
    results = [0.0, 0.0, 0.0]
    for m in measurements.values():
        results[0] = results[0] + m[0]
        results[1] = results[1] + m[1]
        results[2] = results[2] + m[2]

    mean = sum(results) / len(results)
    var  = sum(pow(x-mean,2) for x in results) / len(results)
    std  = math.sqrt(var)  # standard deviation
    log("CPU-Time needed for CPU benchmark: {0!s}s (SD={1!s}s)".format(mean, std))

    log("Trying to allocate up to {1!s}mb of memory, printing allocated amount starting at {0!s}mb:".format(start_printing, max_memory))
    longstring = []
    for x in range(1, max_memory + 1):
        longstring.append("1" * 10**6)
        if (x >= start_printing):
            log("{0!s}mb".format(len(longstring)))
    longstring = []

    log("\nWas able to allocate all needed memory")

def ping_helper(targetAddress):
    while True:
        log("Ping to {0!s} is {1!s}ms".format(targetAddress, ping(targetAddress, count=1).rtt_avg_ms))
        time.sleep(5)

def webserver_helper():
    conf = {
        "global": {
            "server.socket_port": int(os.environ["PORT"]),
            "server.socket_host": "0.0.0.0"
        }
    }
    cherrypy.quickstart(Server(), "/", conf)

if __name__ == "__main__":

    if "PING" in os.environ:
        log("Starting to ping " + os.environ["PING"])
        pingP = multiprocessing.Process(target=ping_helper, args=(os.environ["PING"],))
        pingP.start()
    else:
        log("Pinging is disabled, to enable provide a PING environment variable that contains the target address")

    if "PORT" in os.environ:
        log("Starting CRExplorer webserver at port {0!s}, a request could look like http://localhost:{0!s}/run?max_memory=30".format(os.environ["PORT"]))
        serverP = multiprocessing.Process(target=webserver_helper)
        serverP.start()
        input("Press a key to exit")
        os.exit(0)
    else:
        # parse input
        memory_s = input("How much megabyte of memory should we allocate? Enter a number: ")
        max_memory = int(memory_s)
        single_run(max_memory)
        os._exit(0)
