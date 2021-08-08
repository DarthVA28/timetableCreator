#PROGRAM TO CREATE COURSES TIMETABLE 

import json

days = {
    0 : {
    "A" : "8-9:30 AM",
    "B" : "9:30-11 AM",
    "C" : "",
    "D" : "",
    "E" : "",
    "F" : "",
    "H" : "11-12 AM",
    "J" : "12-1 PM",
    "K" : "",
    "L" : "",
    "M" : "5-6:30 PM"
  },
    1 : {
    "A" : "",
    "B" : "",
    "C" : "8-9AM",
    "D" : "9-10AM",
    "E" : "10-11AM",
    "F" : "11-12PM",
    "H" : "",
    "J" : "12-1 PM",
    "K" : "5-6PM",
    "L" : "6-7PM",
    "M" : ""
  },
    2 : {
    "A" : "",
    "B" : "",
    "C" : "8-9AM",
    "D" : "9-10AM",
    "E" : "10-11AM",
    "F" : "",
    "H" : "11-12PM",
    "J" : "",
    "K" : "12-1 PM",
    "L" : "",
    "M" : ""
  }, 
    3 : {
    "A" : "8-9:30 AM",
    "B" : "9:30-11 AM",
    "C" : "",
    "D" : "",
    "E" : "",
    "F" : "11-12 AM",
    "H" : "12-1 PM",
    "J" : "",
    "K" : "",
    "L" : "",
    "M" : "5-6:30 PM"
  },
    4 : {
    "A" : "",
    "B" : "",
    "C" : "8-9AM",
    "D" : "9-10AM",
    "E" : "10-11AM",
    "F" : "11-12PM",
    "H" : "",
    "J" : "12-1 PM",
    "K" : "5-6PM",
    "L" : "6-7PM",
    "M" : ""
  }
}

def createTimeTable(courses_list): 
  timetable = [[] for i in range(5)]
  f = open('course_slots.json',)
  course_slots = json.load(f)
  for course in courses_list: 
    try:
      slot = course_slots[course]
      for i in range(5): 
        if days[i][slot] != "":
          timetable[i].append((slot,course,days[i][slot]))
        timetable[i].sort()
    except KeyError as e: 
      cause = e.args[0]
      print("The slot for "+ cause + " does not seem to exist, contact admin.")

  return timetable

def printTimeTable():
  days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
  entry_no = input("Please enter your entry number: ")
  print("Please enter your courses for this semester, separated by a space. For example, MTL106, COL106, ...")
  c_list = list(input().split(", "))
  f = open("timetable_{}.txt".format(entry_no),"a")
  timetable = createTimeTable(c_list)
  for i in range(5):
    print(days[i],file=f)
    for tup in timetable[i]:
      print(tup[2] + ": " + tup[1],file=f)
    print("",file=f)

printTimeTable()

printTimeTable()
