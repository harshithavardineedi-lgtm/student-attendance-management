import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "attendance.csv"

# Create sample attendance data if file does not exist
def create_sample_data():
    if not os.path.exists(FILE_NAME):

        data = {
            "Student_ID": [101, 102, 103, 104, 105],
            "Name": ["Rahul", "Anjali", "Kiran", "Sneha", "Arjun"],
            "Total_Classes": [50, 50, 50, 50, 50],
            "Classes_Attended": [45, 38, 42, 49, 30]
        }

        df = pd.DataFrame(data)

        # Calculate attendance percentage
        df["Attendance_Percentage"] = (
            df["Classes_Attended"] / df["Total_Classes"]
        ) * 100

        # Attendance status
        df["Status"] = df["Attendance_Percentage"].apply(
            lambda x: "Eligible" if x >= 75 else "Shortage"
        )

        df.to_csv(FILE_NAME, index=False)

# Load attendance data
def load_data():
    return pd.read_csv(FILE_NAME)

# View all records
def view_records():
    df = load_data()
    print("\n--- Student Attendance Records ---")
    print(df)

# Add new student attendance
def add_student():
    df = load_data()

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    total_classes = int(input("Enter Total Classes: "))
    attended = int(input("Enter Classes Attended: "))

    percentage = (attended / total_classes) * 100

    status = "Eligible" if percentage >= 75 else "Shortage"

    new_record = pd.DataFrame({
        "Student_ID": [student_id],
        "Name": [name],
        "Total_Classes": [total_classes],
        "Classes_Attended": [attended],
        "Attendance_Percentage": [percentage],
        "Status": [status]
    })

    df = pd.concat([df, new_record], ignore_index=True)

    df.to_csv(FILE_NAME, index=False)

    print("Student attendance added successfully!")

# Search student
def search_student():
    df = load_data()

    sid = int(input("Enter Student ID to search: "))

    result = df[df["Student_ID"] == sid]

    if not result.empty:
        print("\nStudent Found:")
        print(result)
    else:
        print("Student not found.")

# Attendance analysis
def attendance_analysis():
    df = load_data()

    print("\n--- Attendance Analysis ---")

    avg_attendance = df["Attendance_Percentage"].mean()

    highest = df.loc[df["Attendance_Percentage"].idxmax()]

    lowest = df.loc[df["Attendance_Percentage"].idxmin()]

    print(f"Average Attendance: {avg_attendance:.2f}%")

    print("\nHighest Attendance:")
    print(highest)

    print("\nLowest Attendance:")
    print(lowest)

# Plot attendance graph
def attendance_graph():
    df = load_data()

    plt.figure(figsize=(8, 5))

    plt.bar(df["Name"], df["Attendance_Percentage"])

    plt.xlabel("Student Name")
    plt.ylabel("Attendance Percentage")
    plt.title("Student Attendance Analysis")

    plt.ylim(0, 100)

    plt.show()

# Main menu
def main():

    create_sample_data()

    while True:

        print("\n===== Student Attendance Management =====")
        print("1. View Attendance Records")
        print("2. Add Student Attendance")
        print("3. Search Student")
        print("4. Attendance Analysis")
        print("5. Show Attendance Graph")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_records()

        elif choice == "2":
            add_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            attendance_analysis()

        elif choice == "5":
            attendance_graph()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

# Run program
if __name__ == "__main__":
    main()