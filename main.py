def calculate_average_cgpa():
  num_courses = int(input("Enter the number of courses: "))
  total_credit = 0
  total_cgpa_credit = 0

  for i in range(1,num_courses+1):
    course_credit = float(input(f"Enter credit for course {i}: "))
    course_cgpa = float(input(f"Enter CGPA for course {i}: "))
    cgpa_credit = course_credit * course_cgpa
    total_credit += course_credit

    total_cgpa_credit += cgpa_credit
  average_cgpa = total_cgpa_credit / total_credit

  print("Average CGPA: ", average_cgpa)

calculate_average_cgpa()