def collect_student_data():
    students = {}
    # dictionary initlisation
    while True:
        name = input("Enter the name of Student or ('done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        if name.lower() in (s.lower() for s in students.keys()):
            print("Student Already Exists!\n")
            continue
        
        try:
            marks = float(input(f"Enter the marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("!invalid input\n")
            continue
        
    return students
        
        
def display_student_data(students_data):
    if not students_data:
        print("Nothing to Display here")
        return
        
        
    print("====== Student Report =======")
    names = list(students_data.keys())
    marks = list(students_data.values())
    
    total_students = len(students_data)
    average_marks = sum(marks)/total_students
    max_marks = max(marks)
    min_marks = min(marks)
    
    toppers = [name for name, mark in students_data.items() if mark == max_marks]
    bottomers = [name for name, mark in students_data.items() if mark == min_marks]
    
    
    print(f"Total Students      : {total_students}")
    print(f"Average Marks       : {average_marks:.2f}")
    print(f"Highest Marks       : {max_marks:.2f} (by {', '.join(toppers)})")
    print(f"Lowest Marks        : {min_marks:.2f} (by {', '.join(bottomers)})")
    print("\nDetailed Student List:")
    
    for name, mark in students_data.items():
        print(f"{name:<20} --> {mark:.2f}")
        
         

def main():
    print("************Welcome to Student Mark Analyzer *****************")
    students_data = collect_student_data()
    display_student_data(students_data)

if __name__ == "__main__":
    main()