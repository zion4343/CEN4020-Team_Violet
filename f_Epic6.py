'''
The functions developed in Epic 6
'''
'''
Import
'''
import numpy as np


def applyForJob(username, jobPostings, jobNumber):
  #student cannot apply for a job that they posted.
  if (username == jobPostings[jobNumber]["posted_by"]):
    print("The job is the one you posted")
    print("You cannot apply to the job")
    return 0
  #Once they have applied for a job, they cannot apply for it again.
  elif (username in jobPostings[jobNumber]["applied_by"]["appliedUser"]):
    print("You already applied for a job")
    return 0
  #Input the information to apply
  print("Enter the information to apply for the job")
  jobPostings[jobNumber]["applied_by"]["appliedUser"].append(username)
  jobPostings[jobNumber]["applied_by"]["graduationDate"].append(
      input("Enter your graduation date(mm/dd/yyyy): "))
  jobPostings[jobNumber]["applied_by"]["startWorkingDate"].append(
      input("Enter a date that you can start working(mm/dd/yyyy): "))
  jobPostings[jobNumber]["applied_by"]["reason"].append(
      input(
          "Enter a paragraph text explaining why you think that you would be a good fit for this job: "
      ))

  # Save the updated job postings
  np.save("job_postings.npy", jobPostings)

  print("You applied for the job successfully")
  return 1


def saveJob(username, jobPostings, jobNumber):
  if username in jobPostings[jobNumber]["saved_by"]["savedUser"]:
    print("you already saved the job")
    return 0
  else:
    jobPostings[jobNumber]["saved_by"]["savedUser"].append(username)
    print("You saved the job!")

    # Save the updated job postings
    np.save("job_postings.npy", jobPostings)

    return 1


def appliedJobs(username, jobPostings, jobNumber):
  count = 0
  for jobNumber in range(len(jobPostings)):
    if username in jobPostings[jobNumber]["applied_by"]["appliedUser"]:
      count += 1
  print(" ")
  print("You have applied for " + str(count) + " jobs")
  print("Here are the jobs you have applied for:")
  for jobNumber in range(len(jobPostings)):
    if username in jobPostings[jobNumber]["applied_by"]["appliedUser"]:
      print("Job " + str(jobNumber + 1) + ":")
      print("Posted by: " + jobPostings[jobNumber]["posted_by"])
      print("Title: " + jobPostings[jobNumber]["title"])
      print("Description: " + jobPostings[jobNumber]["description"])
      print("Location: " + jobPostings[jobNumber]["location"])
      print("Salary: " + jobPostings[jobNumber]["salary"])
      print(" ")
      return 1


def notAppliedJobs(username, jobPostings, jobNumber):
  not_applied_jobs = []
  for jobNumber in range(len(jobPostings)):
    if username not in jobPostings[jobNumber]["applied_by"]["appliedUser"]:
      not_applied_jobs.append(jobNumber)

  # Display the jobs the user has not applied for
  if len(not_applied_jobs) == 0:
    print("You have applied for all available jobs.")
  else:
    print("Jobs you have not applied for:")
    for jobNumber in not_applied_jobs:
      print("Job " + str(jobNumber + 1) + ":")
      print("Posted by: " + jobPostings[jobNumber]["posted_by"])
      print("Title: " + jobPostings[jobNumber]["title"])
      print("Description: " + jobPostings[jobNumber]["description"])
      print("Location: " + jobPostings[jobNumber]["location"])
      print("Salary: " + jobPostings[jobNumber]["salary"])
      print(" ")
      return 1


def savedJobs(username, jobPostings, jobNumber):
  count = 0
  for jobNumber in range(len(jobPostings)):
    if username in jobPostings[jobNumber]["saved_by"]["savedUser"]:
      count += 1
  print(" ")
  print("You have saved " + str(count) + " jobs")
  print("Here are the jobs you have saved:")
  for jobNumber in range(len(jobPostings)):
    if username in jobPostings[jobNumber]["saved_by"]["savedUser"]:
      print("Job " + str(jobNumber + 1) + ":")
      print("Posted by: " + jobPostings[jobNumber]["posted_by"])
      print("Title: " + jobPostings[jobNumber]["title"])
      print("Description: " + jobPostings[jobNumber]["description"])
      print("Location: " + jobPostings[jobNumber]["location"])
      print("Salary: " + jobPostings[jobNumber]["salary"])
      print(" ")
  print("Do you want to unsave any of these jobs?")
  print("1. Yes")
  print("2. No")

  choice = int(input("Enter your choice: "))
  while (choice < 1):
    choice = int(input("Invalid Input, Try again: "))

  if choice == "1":
    print(" ")
    print("Which job do you want to unsave?")
    job_number = int(input("Enter the job number: "))
    if job_number in jobPostings:
      jobPostings[job_number]["saved_by"]["savedUser"].remove(username)
      print("Job " + str(job_number) + " has been unsaved.")
    else:
      print("Invalid job number.")
  elif choice == "2":
    print("Okay, no problem.")
    return 1
