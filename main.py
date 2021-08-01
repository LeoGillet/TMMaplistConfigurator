import os
import sys


def count_maps_from_path(pathname):
    if os.path.exists(os.path.join(pathname)):
        count = 0
        for root, dirs, files in os.walk(pathname):
            count += len([f for f in files if f.endswith('.Gbx')])
            count += len([f for f in files if f.endswith('.gbx')])
            count += len([f for f in files if f.endswith('.GBX')])
        print(f'Directory contains {count} GBX files.')
        for root, dirs, files in os.walk(pathname):
            return files
    else:
        print(f'Directory ({pathname}) doesn\'t exist, check syntax.')



maps = count_maps_from_path(str(input("Path? : ")))
