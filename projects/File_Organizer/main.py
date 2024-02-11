import argparse
import os
import logging
import shutil  # For moving files


def main():
    try:
        args = parse_arguments()
        check_directory(args.directory_path)

        setup_logging(args.verbose)

        organize_directory(args.directory_path)
    # Catch any exceptions that may occur
    except Exception as e:
        print(e)


def parse_arguments():
    # Parse the arguments from cli, order is irrelevant
    parser = argparse.ArgumentParser(
        description="Organize files in a directory based on their extensions."
    )
    parser.add_argument(
        "directory_path", type=str, help="Path of the directory to be organized"
    )  # Required argument
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )  # Optional argument
    return parser.parse_args()


def check_directory(directory_path):
    if not os.path.isdir(directory_path):
        raise ValueError(f"'{directory_path}' is not a valid directory.")

    if not os.listdir(directory_path):
        raise ValueError(f"'{directory_path}' is an empty directory!")

    if not os.access(directory_path, os.W_OK):
        raise ValueError(f"'{directory_path}' is not writable.")


def setup_logging(verbose):
    log_level = logging.INFO if verbose else logging.WARNING
    log_format = "%(message)s"
    logging.basicConfig(level=log_level, format=log_format)


def organize_directory(directory_path):
    categories = {
        "Music": (
            ".mp3",
            ".wav",
            ".flac",
            ".m4a",
            ".aac",
            ".ogg",
            ".oga",
            ".wma",
            ".mid",
        ),
        "Videos": (
            ".mp4",
            ".avi",
            ".mkv",
            ".mpeg",
            ".wmv",
            ".vob",
            ".flv",
            ".mov",
            ".3gp",
            ".webm",
        ),
        "Source Files": (
            ".py",
            ".c",
            ".cpp",
            ".java",
            ".js",
            ".cs",
            ".html",
            ".css",
            ".php",
            ".json",
            ".xml",
            ".sql",
            ".db",
        ),
        "Executables": (
            ".exe",
            ".msi",
            ".sh",
            ".bat",
            ".apk",
            ".jar",
            ".deb",
            ".run",
            ".bin",
            ".dmg",
            ".iso",
        ),
        "Pictures": (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".svg",
            ".webp",
            ".psd",
            ".ai",
            ".ico",
        ),
        "Documents": (
            ".pdf",
            ".doc",
            ".docx",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
            ".txt",
            ".md",
            ".odt",
            ".ods",
            ".odp",
            ".csv",
            ".rtf",
        ),
        "Compressed": (
            ".zip",
            ".rar",
            ".tar",
            ".gz",
            ".7z",
            ".bz2",
            ".xz",
            ".z",
            ".lz",
        ),
        "Torrents": (".torrent",),
    }

    for category, extensions in categories.items():
        # Check if there are files with matching extensions for this category
        files_with_extension = [
            file
            for file in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, file))
            and os.path.splitext(file)[1].lower() in extensions
        ]

        if files_with_extension:
            # Create a folder for this category if it doesn't exist
            category_folder = os.path.join(directory_path, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
                logging.info(f"Creating '{category}' folder.")
            else:
                logging.info(f"'{category}' folder already exists, reusing.")

            for file in files_with_extension:
                source_path = os.path.join(directory_path, file)
                dest_path = os.path.join(category_folder, file)
                shutil.move(source_path, dest_path)
                logging.info(f"Moved '{file}' to '{category}' folder.")

    print("Organizing files complete!")


if __name__ == "__main__":
    main()
