import os


def main():
    img_types = ["jpg", "png", "jpeg"]
    dir_path = input("Enter the directory path of the images: ")

    for i, f in enumerate(os.listdir(dir_path)):
        absname = os.path.join(dir_path, f)
        img_type = absname.split(".")[-1]

        if img_type in img_types:
            while True:
                newname = input(f"Enter the new name for {f} (without extension): ")
                newname = "{}.{}".format(newname, img_type)
                new_absname = os.path.join(dir_path, newname)
                if not os.path.exists(new_absname):
                    os.rename(absname, new_absname)
                    break
                else:
                    print(
                        "A file with this name already exists. Please enter a different name."
                    )

    print("Done renaming images.")


if __name__ == "__main__":
    main()
