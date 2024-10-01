import os

def get_size(path):
        size = 0
        if os.path.isfile(path):
            size = os.path.getsize(path)
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    fp = os.path.join(root, file)
                    if os.path.isfile(fp):
                        size += os.path.getsize(fp)
        return  size

def human_size(size):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024:
            break
        size /= 1024
    return f'{size:.1f} {unit}'





def main():
    pwd = os.getcwd()
    items = os.listdir(pwd)

    for item in items:
        full_path = os.path.join(pwd, item)
        size = human_size(get_size(full_path))
        print("{} {}".format(size, item))

if __name__ == "__main__":
    main()