# Employee List
file_name = 'it_company.csv'
job_title = 'Software Engineer'
with open(file_name) as file:
   for line in file:
      if job_title in line:
         print (line)