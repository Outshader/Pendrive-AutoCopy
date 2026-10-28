import wmi
import subprocess
from pathlib import Path


def main():
    c = wmi.WMI()
    
    watch_dog = c.Win32_VolumeChangeEvent.watch_for(EventType=2)
    
    destination = ".\\!copied\\"
    event = watch_dog()
    source = event.DriveName
    subprocess.run([
        "robocopy",
        source,
        destination,
        "/E",
        "/MT:16",
        "/R:0",
        "/W:0",
        "/XJ", 
    ], check=False)
            
if __name__ == "__main__":
    main()