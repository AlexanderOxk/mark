import sys, os

FILE = "/marks"

def load(alias, cache_path):
    if not os.path.isdir(cache_path) or not os.path.exists(cache_path + FILE):
        print("-1")

    with open(cache_path + FILE) as f:
        for line in f.readlines():
            if line.split()[0] == alias:
                return line.split()[1]
    print("-1")

def store(cwd, alias, cache_path):
    if not os.path.isdir(cache_path):
        os.mkdirs(cache_path)

    lines = []
    if os.path.exists(cache_path + FILE):
        with open(cache_path + FILE) as f:
            lines = f.readlines()
    
    if sum([line.split()[0] == alias for line in lines]):
        for i, line in enumerate(lines):
            if line.split()[0] == alias:
                lines[i] = f"{alias} {cwd}"
    else:
        lines.append(f"{alias} {cwd}")
    
    with open(cache_path + FILE, "w") as f:
        f.writelines(lines)
    print(f"Stored '{cwd}' as '{alias}'.")

def clear(cache_path):
    os.remove(cache_path + FILE)
    print("Cleared all aliases.")

def main():
    cache_path = f"{os.getenv('HOME')}/.cache/mark"
    if sys.argv[1] == "-l":
        load(sys.argv[2], cache_path)
    elif sys.argv[1] == "-s":
        store(sys.argv[2], sys.argv[3], cache_path)
    else:
        clear(cache_path)

if __name__ == "__main__":
    main()