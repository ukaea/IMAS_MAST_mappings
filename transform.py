import argparse
import parse

def read_file(filename: str) -> list[str]:
    with open(filename) as f:
        lines = f.readlines()
    return lines

def normalise_imas(name: str) -> str:
    imas_split = name.split('/')[1:]
    name = '/'.join(imas_split)
    name = name.lower()
    return name

def parse_args_uda(name: str) -> dict:
    


def main():
    parser = argparse.ArgumentParser(
                    description='Get args',)
    parser.add_argument('filename')           # positional argument
    args = parser.parse_args()

    lines = read_file(args.filename)
    for line in lines:
        if '|' in line:
            imas_name, uda_name = line.split('|')
            imas_name = normalise_imas(imas_name)
            


            

if __name__ == "__main__":
    main()
