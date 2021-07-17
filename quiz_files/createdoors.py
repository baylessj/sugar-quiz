# Copy below items into python manage.py shell REPL
import csv

from ragus.models import Door


with open("quiz_files/doors.csv", "r") as f:
   reader = csv.DictReader(
      f,
      fieldnames=("name", "acme_device_id")
   )
   for line in reader:
      if (line["name"] == "Door"):
         continue
      door = Door(name=line["name"], acme_device_id=line["acme_device_id"])
      door.save()