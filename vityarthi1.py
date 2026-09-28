#Factory worker attendence system

workers = []

def add_worker():

    worker_id = input("Enter worker ID:")
    name = input("Enter worker name:")
    department = input("Enter department:")
    shift = input("Enter shift:")

    worker = [ worker_id ,name ,department ,shift ,0 ,0 ]

    workers.append(worker)

    print("Worker added successfully!:")


def mark_attendance():
    if len(workers)==0:
        print("No workers available")
        return

    worker_id = input("Enter worker ID :")

    for worker in workers :
        if worker[0] == worker_id :

            status = input("Enter attendance (P/A)")

            if status == "P" or status == "p" :

             worker[4] = worker[4]+ 1

             print("Attendance marked present sucessfully:")

            else:
                print("Invalid attendance status:")

            return
    print("worker ID is not found:")


def display_workers():
    if len(workers)==0:
        print("no worker available")
        return

    print("\n==========WORKER DEALAILS===========")

    for worker in workers :
        print("Worker ID:", worker[0])
        print("Name :", worker[1])
        print("Department :", worker[2])
        print("Shift ;", worker[3])
        print("present days:", worker[4])
        print("Absent days:", worker[5])
        print("-------------------------")


def attendance_summary():
    if len(workers) == 0 :
        print("no worker is available")
        return

    worker_id = input("Enter worker id:")

    for worker in workers :
        if worker[0]==worker_id :
            present = worker[4]
            absent= worker[5]
            total_days = present + absent

            if total_days > 0 :
                percentage  =( present/ total_days)*100

            else:
                percentage = 0

            print("\n==========ATTENDANCE SUMMARY===========")
            print("Worker name:", worker[1])
            print("Present Days:", present)
            print("Absent Days ;", absent)
            print("Total Days:", total_days)
            print("Attendance", percentage, "%")

            return
    print("Worker ID is not Found:")


def attendance_alert():
    if len(workers) == 0:
        print("No Woeker available")

        return
    
    for worker in workers :

        present = worker[4]
        absent = worker[5]
        total_days = present + absent

        if total_days > 0 :
            percentage = (present/total_days)*100

        else:
            percentage = 0

        print("\nWorker:",worker[1])

        if percentage < 75:
            print("ALert ; Attendance is low Please Maintain your Attendance")

        else:
            print("Attendance is satisfactory,KEEP DOING:")

def main():
    while True:

        print("=================================")
        print("WORKER ATTENDANCE SYSTEM:")
        print("=================================")

        print("1. Add worker:")
        print("2. Mark Attendance:")
        print("3. Display Workers:")
        print("4. Attendance Summary:")
        print("5. Attendance Alert:")
        print("6. Exit:")

        choice = input("Enter your choice")

        if choice == "1":
            add_worker()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            display_workers()

        elif choice == "4":
            attendance_summary()

        elif choice == "5":
            attendance_alert()

        elif choice == "6":
            print("6. Exit")
            break
        else :
            print("Invalid choice: Please Enter Valid Choice")

main()

