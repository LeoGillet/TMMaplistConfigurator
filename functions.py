import os

def count_maps_from_path(pathname):
    if os.path.exists(os.path.join(pathname)):
        count = 0
        gbxList_in_Dir = []
        gbxList_in_Sub = []
        for root, dirs, files in os.walk(pathname):
            if len([f for f in files if f.endswith('.Gbx')]):
                gbxList_in_Dir.append(files)
                count += len([f for f in files if f.endswith('.Gbx')])
            elif len([f for f in files if f.endswith('.gbx')]):
                gbxList_in_Dir.append(files)
                count += len([f for f in files if f.endswith('.Gbx')])
            elif len([f for f in files if f.endswith('.GBX')]):
                gbxList_in_Dir.append(files)
                count += len([f for f in files if f.endswith('.Gbx')])
        if count != 0:
            print(f'Directory contains {count} GBX files.')
            for maps in gbxList_in_Dir:
                gbxList_in_Sub.append(maps)
            print(gbxList_in_Sub)
        else:
            print('No GBX files found in directory.')

    else:
        print(f'Directory ({pathname}) doesn\'t exist, check syntax.')



maps = count_maps_from_path(str(input("Path? : ")))
