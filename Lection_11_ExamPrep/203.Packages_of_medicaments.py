def main():
    box_w = float(input())
    box_h = float(input())
    box_d = float(input())
    box_dims = [box_w, box_h, box_d]
    box_dims.sort()

    packages_fn = input()
    packages = load_packages(packages_fn)
    for p in packages:
        package_dims = p[1:]
        package_dims.sort()
        if (all(package_dims[i] < box_dims[i] for i in range(len(package_dims)))):
            print(p[0])
            

def load_packages(fn: str) -> list:
    result = []
    with open(fn, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_parts = line.split(',')
                name, w, h, d = line_parts
                result.append(
                    [name, float(w), float(h), float(d)]
                )
    return result


if __name__ == '__main__':
    main()