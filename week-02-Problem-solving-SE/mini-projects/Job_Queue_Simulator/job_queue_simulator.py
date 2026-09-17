from collections import deque

all_jobs = {}
pending_jobs = deque()
completed_jobs = []
cancelled_jobs = []

def add_job():
    id= input("Enter the id of the job")
    type = input("Enter the type of the job:")
    customer = input("Enter the customer:")
    new_job = {
        "id" : id,
        "type" : type,
        "customer": customer,
        'status' : "pending"
    }
    all_jobs[id] = new_job
    pending_jobs.append(id)


def view_pending_jobs():
    for el in pending_jobs:
        print(all_jobs[el])

def process_next_job():
    if len(pending_jobs) != 0:
        job = pending_jobs.popleft()
        if all_jobs[job]["status"] == "cancelled":
            process_next_job()
        else:
            print(f"Proceessing {all_jobs[job]['id']} for {all_jobs[job]['customer']}")
            completed_jobs.append(job)
            all_jobs[job]["status"] = "completed"

def view_completed_jobs():
    for el in completed_jobs:
        print(all_jobs[el])

def cancel_job():
    job_id = input("Enter the id of the job to cancel:")
    if job_id not in all_jobs:
        raise KeyError(job_id)
    all_jobs[job_id]["status"] = "cancelled"
    cancelled_jobs.append(job_id)

def show_statistics():
    print("Completed jobs:", len(completed_jobs))
    print("Pending jobs:", len(pending_jobs))
    print("Cancelled jobs:", len(cancelled_jobs))

def search_jobs():
    job_id = input("Enter the id of the job to search:")
    if job_id not in all_jobs:
        raise KeyError(job_id)
    print(all_jobs[job_id])

choice = ""
while choice != "8":
    print("Enter your choice:")
    print("1.Add job")
    print("2.View Pending Jobs")
    print("3.Process Next job")
    print("4.view completed jobs")
    print("5.cancel job")
    print("6.show statistics")
    print("7.Search Job")
    print("8.Exit")
    choice = input("Enter your choice:")

    if choice == "1":
        add_job()
    elif choice == "2":
        view_pending_jobs()
    elif choice == "3":
        process_next_job()
    elif choice == "4":
        view_completed_jobs()
    elif choice == "5":
        try:
            cancel_job()
        except KeyError as e:
            print(f"Job ID does not exist{e}")
    elif choice == "6":
        show_statistics()
    elif choice == "7":
        try:
            search_jobs()
        except KeyError as e:
            print(f"Job Id not found : {e}")
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice...enter choice from 1-8")
