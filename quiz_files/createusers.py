# exec(open("./quiz_files/residents.csv").read())  
from ragus.models import User, Door
import csv

with open("./quiz_files/residents.csv", "r") as f:
   reader = csv.DictReader(
      f,
      fieldnames=("last_name", "first_name", "email", "doors")
   )
   for line in reader:
      if (line["last_name"] == "Last Name") or User.objects.filter(username=line["email"]).exists():
         continue

      password = line["first_name"] + line["last_name"]
      print(line["email"])
      user=User.objects.create_user(line["email"], password=password)
      user.is_superuser=False
      user.is_staff=False

      doors = line["doors"].replace("\"", "").split(",")
      for door in doors:
         user.doors.add(*Door.objects.filter(name=door.strip()))
      user.save()