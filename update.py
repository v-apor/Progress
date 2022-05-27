import datetime
import subprocess

time = datetime.datetime.now().strftime('%d/%m/%Y')

comment = input("Enter today's update: \n")
comment = f"{time} | {comment}"

file = open("log.txt", 'a')
file.write(comment)
file.close()

commit_msg = "log " + time

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", commit_msg])
subprocess.call(["git", "push"])