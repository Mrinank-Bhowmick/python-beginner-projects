#!/usr/bin/env python3

import cv2
import click
import os

# Author: Anju Chhetri
# Date: 10-05-2022


@click.command()
@click.option("--directory", default="None", help="Directory in which to store frames")
@click.option("--name", default="person", help="Directory in which to store frames")
def main(name, directory):
    if directory == "None":
        directory = os.getcwd()
    capture = cv2.VideoCapture(0)
    frame_count = 0
    while True:
        ret, frame = capture.read()
        frame = cv2.resize(frame, (600, 600))
        cv2.imshow("frame", frame)
        key = cv2.waitKey(50)
        if key & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
        if key & 0xFF == ord(" "):
            cv2.imwrite(f"{directory}/{name+str(frame_count)}.jpg", frame)
            print(f"got {name+str(frame_count)}")
            frame_count += 1


if __name__ == "__main__":
    main()
