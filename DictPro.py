course = {
    "title": "Python Course",
    "time": 20,
    "videoCount": 23,
    "tags": ["python course", "free python course", "online"],
    "session": [
        {
            "title": "session-1",
            "time": 9,
        },
        {
            "title": "session-2",
            "time": 12,
        }
    ],
    "relatedCourses": [
        {
            "title": "Kotlin Course",
            "time": 20,
            "videoCount": 23,
            "tags": ["kotlin course", "free kotlin course", "online"],
        },
        {
            "title": "Java Course",
            "time": 20,
            "videoCount": 23,
            "tags": ["java course", "free java course", "online"],
        }
    ]
}

# for related in course["relatedCourses"]:
#     print(related["title"])

totalTime = 0

for session in course["session"]:
    totalTime += session["time"]

print(totalTime)
