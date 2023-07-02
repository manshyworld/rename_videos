def color_subtitle_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    is_subtitle_text = False
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.isdigit() or '-->' in stripped_line:
            modified_lines.append(line)
            if stripped_line.isdigit():
                is_subtitle_text = False
        else:
            if not is_subtitle_text:
                subtitle_lines = []
                is_subtitle_text = True

            if stripped_line:
                subtitle_lines.append(stripped_line)

        if not stripped_line and subtitle_lines:
            modified_lines.append('<font color="#ffff00">' + '</font>\n<font color="#ffff00">'.join(subtitle_lines) + '</font>')
            is_subtitle_text = False

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(modified_lines))

    print("File has been modified.")

def remove_empty_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]  # Remove empty lines

    updated_lines = []
    for line in lines:
        if line.isdigit():
            if len(updated_lines) > 0 and updated_lines[-1] != "":
                updated_lines.append("")
            updated_lines.append(line)
        else:
            updated_lines.append(line)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(updated_lines))

# Usage color
srt_filename = input("Enter the path to the SRT file: ")
color_subtitle_file(srt_filename)

# Usage fix lines
remove_empty_lines(srt_filename)
