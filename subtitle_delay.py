def modify_srt_file(file_path, time_value, time_unit):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if '-->' in line:
            start_time, end_time = line.split(' --> ')
            start_time = modify_timestamp(start_time.strip(), int(time_value), time_unit)
            end_time = modify_timestamp(end_time.strip(), int(time_value), time_unit)
            modified_lines.append(f'{start_time} --> {end_time}\n')
        else:
            modified_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

    print(f'{file_path} has been modified.')


def modify_timestamp(timestamp, time_value, time_unit):
    hours, minutes, rest = timestamp.split(':')
    if time_unit == 's':
        seconds = time_value
        milliseconds = 0
    elif time_unit == 'ms':
        seconds = time_value // 1000  # Convert milliseconds to seconds
        milliseconds = time_value % 1000  # Remaining milliseconds

    # Replace the non-standard comma character with a standard comma
    rest = rest.replace('،', ',')

    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(rest.split(',')[0])
    modified_total_seconds = total_seconds + seconds

    modified_hours, remaining_seconds = divmod(modified_total_seconds, 3600)
    modified_minutes, modified_seconds = divmod(remaining_seconds, 60)

    modified_milliseconds = int(rest.split(',')[1]) + milliseconds
    if modified_milliseconds > 999:
        modified_seconds += modified_milliseconds // 1000  # Add excess milliseconds to seconds
        modified_milliseconds = modified_milliseconds % 1000  # Remaining milliseconds

    modified_rest = f'{modified_seconds:02d},{modified_milliseconds:03d}'

    modified_timestamp = f'{modified_hours:02d}:{modified_minutes:02d}:{modified_rest}'
    return modified_timestamp


# Main code
srt_file_path = input("Enter the path to the SRT file: ")
time_value = input("Enter the number of time units to add/subtract: ")
time_unit = input("Enter the unit of time (s/ms): ")
modify_srt_file(srt_file_path, time_value, time_unit)
