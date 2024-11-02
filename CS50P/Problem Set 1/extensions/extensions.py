file_name = input("File Name: ")

if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name:
    print("image/jpeg")
elif ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name:
    print("application/pdf")
elif ".zip" in file_name:
    print("application/zip")
elif ".txt" in file_name:
    print("text/plain")
elif ".PDF" in file_name:
    print("application/pdf")
else:
    print("application/octet-stream")