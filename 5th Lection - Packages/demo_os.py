import os

def get_all_abs_filenames(start_dir: str) ->list:
    result = []
    start_dir = os.path.abspath(start_dir)
    # if not start_dir.endswith('\\'):
    #     start_dir += '\\'
    for dirpath, _dummy_dirnames, filenames in os.walk(start_dir):
        for fn in filenames:
            abs_filenames = os.path.join(dirpath, fn)
            result.append(abs_filenames)
    return result

    # print(start_dir)

all_abs_filenames = get_all_abs_filenames('./')
print("All files:")
for fn in all_abs_filenames:
    print(' - ' + fn)

