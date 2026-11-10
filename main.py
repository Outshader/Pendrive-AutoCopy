import wmi
import subprocess
from pathlib import Path


def main():
    c = wmi.WMI()

    watch_dog = c.Win32_VolumeChangeEvent.watch_for(EventType=2)

    with open("excluded.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if line.strip()]
    print(lines)

    destination = ".\\!copied\\"
    event = watch_dog()
    source = event.DriveName
    proc = subprocess.run(
        [
            "robocopy",
            source,
            destination,
            "/E",
            "/MT:16",
            "/R:0",
            "/W:0",
            "/XJ",
            "/XD",
            *lines,
            "/XF",
            *lines,
            "/NFL",
            "/NDL",
            "/NP",
            "/NJH",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode < 8:
        print("Process succeeded")
        print(proc.stdout)
    else:
        print(f"Process failed {proc.returncode}")


if __name__ == "__main__":
    main()
