import os

def select_file(file_type):
    while True:
        file_path = input(f"Enter the path to the {file_type} file: ")
        if os.path.exists(file_path):
            return file_path
        print(f"File not found. Please enter a valid path to a {file_type} file.")

def conversion_type():
    while True:
        choice = input("Select conversion type (1 for MP4 to MP3, 2 for MP3 to MP4): ")
        if choice in ['1', '2']:
            return int(choice)
        print("Invalid choice. Please enter 1 or 2.")

def convert_mp4_to_mp3(file_path):
    print(f"Converting {file_path} from MP4 to MP3...")
    # Actual conversion logic would go here
    return file_path.replace('.mp4', '.mp3')

def convert_mp3_to_mp4(file_path):
    print(f"Converting {file_path} from MP3 to MP4...")
    # Actual conversion logic would go here
    return file_path.replace('.mp3', '.mp4')

def download_file(file_path):
    print(f"Downloading {file_path}...")
    # Actual download logic would go here
    print(f"File downloaded: {file_path}")

def main():
    print("Welcome to the MP4-MP3 Converter")

    # Select input file
    input_file = select_file("MP4 or MP3")

    # Choose conversion type
    conv_type = conversion_type()

    # Perform conversion
    if conv_type == 1:
        output_file = convert_mp4_to_mp3(input_file)
    else:
        output_file = convert_mp3_to_mp4(input_file)

    # Download converted file
    download_file(output_file)

if __name__ == "__main__":
    main()
