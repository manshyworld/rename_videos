
def modify_srt_file(file_path, seconds):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if '-->' in line:
            start_time, end_time = line.split(' --> ')
            start_time = modify_timestamp(start_time.strip(), seconds)
            end_time = modify_timestamp(end_time.strip(), seconds)
            modified_lines.append(f'{start_time} --> {end_time}\n')
        else:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

    print(f'{file_path} has been modified.')


def modify_timestamp(timestamp, seconds):
    hours, minutes, rest = timestamp.split(':')
    seconds = int(seconds)

    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(rest.split(',')[0])
    modified_total_seconds = total_seconds + seconds

    modified_hours, remaining_seconds = divmod(modified_total_seconds, 3600)
    modified_minutes, modified_seconds = divmod(remaining_seconds, 60)
    modified_rest = f'{modified_seconds:02d}{rest[2:]}'  # Keep the original milliseconds

    modified_timestamp = f'{modified_hours:02d}:{modified_minutes:02d}:{modified_rest}'
    return modified_timestamp


# Main code
srt_file_path = input("Enter the path to the SRT file: ")
seconds = input("Enter the number of seconds to add/subtract: ")
modify_srt_file(srt_file_path, seconds)
