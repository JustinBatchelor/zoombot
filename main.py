import zoom_script

if __name__ == '__main__':
    zoom_link = input("Please enter the zoom link here: ")
    meeting_date = input("Please enter the meeting date (DD-MM-YY): ")
    meeting_time = input("Please enter the meeting time (military time): ")

    zoom_script.join_meeting(zoom_link, meeting_date, meeting_time)
