def write_time(time, protocol):
    fileObj = open("timecapture.txt",  "a")
    time_text = f"Tempo total do {protocol}: {time}ms"
    fileObj.write(time_text + "\n")
    fileObj.close()

def erase():
    fileObj = open("timecapture.txt", "w")
    fileObj.write("")
    fileObj.close()