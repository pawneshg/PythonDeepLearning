import os

rootdir = '/root/crawler'

for root, subfolders, files in os.walk(rootdir):
    for each in files:
        path = root + '/' + each
        st = os.stat(path)
        old_mode = oct(st.st_mode)[-3:]
        old_mode_int = st.st_mode
        print(old_mode)
        #os.chmod(path, 0755)
        #python3
        os.chmod(path, 0o755)
        st = os.stat(path)
        new_mode = oct(st.st_mode)[-3:]
        print(new_mode)
        print("reverting permission .. ")
        os.chmod(path, old_mode_int)
        print("mode after reverting")
        st = os.stat(path)
        mode = oct(st.st_mode)[-3:]
        print(mode)
        

