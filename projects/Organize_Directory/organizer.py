import os
import shutil


def main():
    dir_path = input("Enter the directory path of the files: ")

    try:
        print(
            "Organising your files into [ images - music - video - executable - archive - torrent - document - code - design files]"
        )
        for filename in os.listdir(dir_path):
            absname = os.path.join(dir_path, filename)
            # Check if files are images and you can add more extensions
            if filename.lower().endswith(
                (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm")
            ):
                # If images folder doesn't exist then create new folder
                if not os.path.exists("images"):
                    os.makedirs("images")
                shutil.move(absname, "images")

            # Check if files are music and you can add more extensions
            elif filename.lower().endswith(
                (".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw")
            ):
                # If music folder doesn't exist then create new folder
                if not os.path.exists("music"):
                    os.makedirs("music")
                shutil.move(absname, "music")

            # Check if files are videos and you can add more extensions
            elif filename.lower().endswith((".webm", ".mp4")):
                # If video folder doesn't exist then create new folder
                if not os.path.exists("video"):
                    os.makedirs("video")
                shutil.move(absname, "video")

            # Check if files are executables
            elif filename.lower().endswith((".exe", ".msi", ".deb", "dmg")):
                # If executables folder doesn't exist then create new folder
                if not os.path.exists("executables"):
                    os.makedirs("executables")
                shutil.move(absname, "executables")

            # Check if files are archive files
            elif filename.lower().endswith((".rar", ".tar", ".zip", ".gz")):
                # If archive folder doesn't exist then create new folder
                if not os.path.exists("archives"):
                    os.makedirs("archives")
                shutil.move(absname, "archives")

            # Check if files are torrent files
            elif filename.lower().endswith((".torrent",)):
                # If torrent folder doesn't exist then create new folder
                if not os.path.exists("torrent"):
                    os.makedirs("torrent")
                shutil.move(absname, "torrent")

            # Check if files are documents
            elif filename.lower().endswith((".txt", ".pdf", ".docx", "doc")):
                # If documents folder doesn't exist then create new folder
                if not os.path.exists("documents"):
                    os.makedirs("documents")
                shutil.move(absname, "documents")

            # Check if files are code files
            elif filename.lower().endswith((".py", ".php", ".html", ".css", ".js")):
                # If code folder doesn't exist then create new folder
                if not os.path.exists("code"):
                    os.makedirs("code")
                shutil.move(absname, "code")

            # Check if files are design files
            elif filename.lower().endswith((".psd", ".ai")):
                # If design folder doesn't exist then create new folder
                if not os.path.exists("design-files"):
                    os.makedirs("design-files")
                shutil.move(absname, "design-files")

    except OSError:
        print("Error happened ...... try again")
    finally:
        # When script is finished clear screen and display message
        os.system("cls" if os.name == "nt" else "clear")
    print("Finished organising your files")


if __name__ == "__main__":
    main()
