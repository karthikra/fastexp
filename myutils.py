# Run this once to make folders and copy the item into those folders
for f in os.listdir("/media/karhd/DATA/petsData/images/"):
    folderName = "_".join(f.split("_")[:-1])

    if not (path/folderName).is_dir():
        (path/folderName).mkdir()
        shutil.copy(os.path.join('/media/karhd/DATA/petsData/images/', f), path/folderName)
    else:
        shutil.copy(os.path.join('/media/karhd/DATA/petsData/images/', f), path/folderName)
    