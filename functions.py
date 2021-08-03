import os

def find_maps_from_path(pathname):
    gbxList_in_Dir = []
    if os.path.exists(os.path.join(pathname)):
        count = 0
        for root, dirs, files in os.walk(pathname):
            if len([f for f in files if f.endswith('.Gbx')]):
                for maps in files:
                    gbxList_in_Dir.append(maps)
                    count += 1
            elif len([f for f in files if f.endswith('.gbx')]):
                for maps in files:
                    gbxList_in_Dir.append(maps)
                    count += 1
            elif len([f for f in files if f.endswith('.GBX')]):
                for maps in files:
                    gbxList_in_Dir.append(maps)
                    count += 1
        if count != 0:
            print(f'Directory contains {count} GBX files.')
            print(gbxList_in_Dir)
        else:
            print('No GBX files found in directory.')

    else:
        print(f'Directory ({pathname}) doesn\'t exist, check syntax.')
    return gbxList_in_Dir, count


def show_help():
    return 1

def show_about():
    print("F9 key pressed, starting About screen")
    return 1

def generate_file():
    return 1

def key_pressed(event):
    # print(f'Key {event.keysym} was pressed.')
    if event.keysym == 'F9':
        show_about()