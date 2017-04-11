from psutil_fetching import psutil_fetching
import sched, time, requests

# The scheduler object
s = sched.scheduler(time.time, time.sleep)

def scheduled_task():
    log = psutil_fetching()

    # POST the log on flask app
    r = requests.post("http://localhost:5000/consume", json=log)

    # Print status code and response
    print(r.status_code)

    print("Requested psutil_fetching.py")
    s.enter(5, 1, scheduled_task)

def main():
    # scheduler.enter(delay, priority, action, argument=(), kwargs={})
    s.enter(0, 1, scheduled_task) # First call, we enter directly
    s.run()

if __name__ == "__main__":
    main()
