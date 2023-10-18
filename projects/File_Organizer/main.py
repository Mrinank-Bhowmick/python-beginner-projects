import sys
import os
import shutil # For moving files

def main():
    try:
        check_arguments()
        organize_directory(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(1)

def check_arguments():
    # One argument needs to be provided, that is the path of the directory to be organized
    if len(sys.argv) - 1 != 1:
        raise ValueError(f"Usage: python3 {sys.argv[0]} <directory_path>")
    directory_path = sys.argv[1]
        
    if not os.path.isdir(directory_path):
        raise ValueError(f"'{directory_path}' is not a valid directory.")
    
    if not os.listdir(directory_path):
        raise ValueError(f"'{directory_path}' is an empty directory!")

def organize_directory(directory_path):
    categories = {
        "Music": (".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".oga" ".wma", ".mid"),
        "Videos": (".mp4", ".avi", ".mkv", ".mpeg", ".wmv", ".vob", ".flv", ".mov", ".3gp", ".webm"),
        "Source Files": (".py", ".c", ".cpp", ".java", ".js", ".cs", ".html", ".css", ".php", ".json", ".xml", ".sql", ".db"),
        "Executables": (".exe", ".msi", ".sh", ".bat", ".apk", ".jar", ".deb", ".run", ".bin", ".dmg", ".iso"),
        "Pictures": (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".psd", ".ai", ".ico"),
        "Documents": (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md", ".odt", ".ods", ".odp", ".csv", ".rtf"),
        "Compressed": (".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".z", ".lz"),
        "Torrents": (".torrent",),
    }

    for category, extensions in categories.items():
        # Create folders for each category, if they don't already exist
        category_folder = os.path.join(directory_path, category)
        os.makedirs(category_folder, exist_ok=True)

        for file in os.listdir(directory_path):
            # Process only files, not directories
            if os.path.isfile(os.path.join(directory_path, file)):
                # extract the file extension of the current file
                file_extension = os.path.splitext(file)[1]
                if file_extension.lower() in extensions:
                    source_path = os.path.join(directory_path, file)
                    dest_path = os.path.join(category_folder, file)
                    shutil.move(source_path, dest_path)
                    print(f"Moved '{file}' to '{category}' folder.")

if __name__ == "__main__":
    main()