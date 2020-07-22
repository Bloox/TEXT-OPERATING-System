import os, time
#trees
from pathlib import Path
from itertools import islice
import msvcrt as m
import keyboard
import pyautogui
from selenium import webdriver

space =  '    '
branch = '│   '
tee =    '├── '
last =   '└── '
from colored import fg, bg, attr
error = fg('#fa5a5a') + bg('#333333')
res = attr('reset')
import subprocess
subprocess.call('', shell=True)
def tree_graphic(dir_path: Path, level: int=-1, limit_to_directories: bool=False,
         length_limit: int=1000):
    """Given a directory Path object print a visual tree structure"""
    dir_path = Path(dir_path) # accept string coerceable to Path
    files = 0
    directories = 0
    def inner(dir_path: Path, prefix: str='', level=-1):
        nonlocal files, directories
        if not level: 
            return # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else: 
            contents = list(dir_path.iterdir())
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield prefix + pointer + path.name
                directories += 1
                extension = branch if pointer == tee else space 
                yield from inner(path, prefix=prefix+extension, level=level-1)
            elif not limit_to_directories:
                yield prefix + pointer + path.name
                files += 1
    print(dir_path.name)
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        print(line)
    if next(iterator, None):
        print(f'... length_limit, {length_limit}, reached, counted:')
    print(f'\n{directories} directories' + (f', {files} files' if files else ''))

def tree(root):
    res = attr('reset')
    fi_c = fg('#60fc8f') + bg("#000000")
    fo_c = fg('#60e2fc') + bg("#000000")
    print('-----------')
    tab_folders = []
    tab_file = []
    for root, dirs, files in os.walk(root):
        i =0
        kot = "\e"
        for d in dirs:
            
            e = True
            a = os.path.join(root, d)
            
            if a[:13] == ".\__pycache__":
                e = False
            if a.count(kot[0]) >= 3:
                e = False
            if e == True:
                print(fo_c+ "folder:  "+a + res)
                tab_folders.append(a)  
            i += 1
        i =0
        
        for f in files:
            e = os.path.join(root, f)
            a = e.endswith('.pyc')
            if e.count(kot[0]) >= 3:
                a = True
            if a == False:
                print(fi_c +"file:    "+e + res)
                tab_file.append(e)
            
    return tab_file,tab_folders
def tree_print(root):
    tab_folders = []
    tab_file = []
    for root, dirs, files in os.walk(root):
        i =0
        kot = "\e"
        for d in dirs:
            
            e = True
            a = os.path.join(root, d)
            
            if a[:13] == ".\__pycache__":
                e = False
            if a.count(kot[0]) >= 3:
                e = False
            if e == True:
                
                tab_folders.append(a)  
            i += 1
        i =0
        
        for f in files:
            e = os.path.join(root, f)
            a = e.endswith('.pyc')
            if e.count(kot[0]) >= 3:
                a = True
            if a == False:
                
                tab_file.append(e)
            
    return tab_file,tab_folders
def tree_n(root):
    tab_folders = []
    tab_file = []
    for root, dirs, files in os.walk(root):
        i =0
        kot = "\e"
        for d in dirs:
            
            e = True
            a = os.path.join(root, d)
            

            if e == True:
                print("folder:  "+a)
                tab_folders.append(a)  
            i += 1
        i =0
        
        for f in files:
            e = os.path.join(root, f)
            a = False
            if a == False:
                print("file:    "+e)
                tab_file.append(e)
            
    return tab_file,tab_folders
    
def tree_print_n(root, l):
    tab_folders = []
    tab_file = []
    tab_file2 = []
    for root, dirs, files in os.walk(root):
        i =0
        kot = "\e"
        for d in dirs:
            
            e = True
            a = os.path.join(root, d)
            
            if a.count(kot[0]) >= l:
                e = False

            if e == True:
                
                tab_folders.append(a)  
            i += 1
        i =0
        
        for f in files:
            e = os.path.join(root, f)
            a = False
            if e.count(kot[0]) >= l:
                a = True
            if a == False:
                
                tab_file.append(e)
            if a == True:
                if e.count(kot[0]) >= l+2:
                    a = False
                if a == True:
                    tab_file2.append(e)
    return tab_file,tab_folders,tab_file2
#preparin select


#-----------
tab = tree(".")
print("-----------------------------------------------------")
filer = tab[0]
fi_count = len(filer)
print(f'w folderze jest:{fi_count} plików', 'blue')
folders = tab[1]
fl_count = len(folders)
print(f'w folderze jest:{fl_count} folderów')
er = True
while er:
    selected = fg("#ebcc34") + bg("#000000")
    unselected = fg("#eb3489") + bg("#000000")
    k = False
    h1 = fg('#fcb160') + bg('#2c3634')
    fi_c = fg('#60fc8f') + bg("#000000")
    fo_c = fg('#60e2fc') + bg("#000000")
    kot = '\l'
    print(h1+ f'---{os.getcwd()}---'+ res)
    tab = tree_print_n(".",3)
    filer = tab[0]
    fi_count = len(filer)
    print(fi_c + f'w folderze jest:{fi_count} plików' + res)
    folders = tab[1]
    fl_count = len(folders)
    print(fo_c + f'w folderze jest:{fl_count} folderów' + res)
    print(h1 +"-----------------------------------------------------" + res)
    cmd = input(">")
    print("-----------------------------------------------------" + res)
    if cmd[0:3] == 'py ':
        xer = cmd[3:]
        zer = xer.split(' ')
        os.system(f'python {zer[0]}.py {zer[1]}')
    if cmd[0:6] == 'python':
        os.system('python')
    if cmd[0:4] == "calc":
        a = cmd[5:].split(' ')
        z = -1
        dzia = []
        liczby = []
        for i in range(0,len(a)):
            try:
                inter = int(a[i])
                liczby.append(inter)
            except:
                dzia.append(a[i])
            
        if len(liczby) == 1:
            if liczby[0]==42:
                wynik = "Sens życie i istnienia~!"
            else:
                print('to nie działanie')
                wynik = 0
        else:
            if len(dzia) == 0:
                print("to nie działanie")
                wynik = 0
            else:
                for i in range(0,len(dzia)):
                    
                    if dzia[i]=="+":
                        wynik =liczby[i]+liczby[i+1]
                        liczby[i+1] = wynik
                        
                    if dzia[i]=="-":
                        wynik =liczby[i]-liczby[i+1]
                        liczby[i+1] = wynik
                        
                    if dzia[i]=="*":
                        wynik =liczby[i]*liczby[i+1]
                        liczby[i+1] = wynik
                        
                    if dzia[i]=="/":
                        wynik =liczby[i]/liczby[i+1]
                        liczby[i+1] = wynik
                    
                
        print(f"było: {len(dzia)} działań")
        print(f'wynik:{wynik}')
        input('Plis enter')
        k = True

    if cmd[0:11] == 'open folder':
        tab = tree_print(".")
        filer = tab[0]
        fi_count = len(filer)
        folders = tab[1]
        fl_count = len(folders)
        if fl_count != 0:
            pr = 0
            while fl_count>= pr:
                print(fo_c + f'folder nr: {pr+1} name: {folders[pr-1]}' + res)
                pr += 1
            print("------")
            g = input("nr:")
            
            try:
                odp = int(g)
                odp -= 2
            except:
                print(error+"nie ma takiego pliku"+ res)
                odp = 0
            try:
                active_f = folders[odp]
                
            except:
                active_f = folders[0]
                print(error + "nie ma takiego folderu :O" + res)
            
            e = os.getcwd()
            
            os.chdir(f'{e}{active_f[1:]}')
            print(res)
            k = True
    if cmd[0:6] == 'explor':
        if cmd[7:] == "open":
            print("yes sir")
            os.startfile(os.getcwd())
    if cmd[0:4] == "tree":
        tab = tree(".")
        print("-----------------------------------------------------")
        filer = tab[0]
        fi_count = len(filer)
        print(fi_c + f'w folderze jest:{fi_count} plików' +res)
        folders = tab[1]
        fl_count = len(folders)
        print(fo_c + f'w folderze jest:{fl_count} folderów'+ res)
    if cmd[0:4] == "exit":
        er = False
        k = True
    if cmd[0:4] == "back":
        e = os.getcwd()
        a =e.split(kot[0])
        
        count = len(a)
        b = 0
        res = ""
        t = True

        while t:
            res += a[b] + kot[0]
            b += 1
            print(res)
            if b == count-1:
                t = False
        os.chdir(res)
        k = True
    if cmd[0:6]== 'f_tree':
        tab = tree_n(".")
        print("-----------------------------------------------------")
        filer = tab[0]
        fi_count = len(filer)
        print(f'w folderze jest:{fi_count} plików')
        folders = tab[1]
        fl_count = len(folders)
        print(f'w folderze jest:{fl_count} folderów')
    if cmd[0:5] == "color":
        c = input("color:")
        os.system("color " + c)
    if cmd[0:3] == "cls" or cmd[0:5] == "clear":
        os.system("cls")
    print("--------------------" +res)
    if cmd[0:3] == 'viv' or cmd[0:len('vive')] == "vive":
        tree_graphic(Path.home() / os.getcwd(), level=2)
    if cmd[0:3] == "new":
        os.system("cls")
        select = 0
        print("Options:")
        print("1:   new folder")
        print("2: new file")
        new_select = True
        def enter():
            global new_select
            new_select = False
            return new_select
        def one():
            global selected
            global unselected
            global res
            os.system('cls')
            print("Options:")
            print(selected+"1:   new folder"+res)
            print(unselected+ "2: new file"+res)
        def two():
            global selected
            global unselected
            global res
            os.system('cls')
            print("Options:")
            print(unselected+"1:   new folder"+res)
            print(selected+ "2: new file"+res)
        time.sleep(1)
        while new_select:
            if keyboard.is_pressed('1')==True:
                one()
            if keyboard.is_pressed('2')==True:
                two()
            if keyboard.is_pressed('enter')==True:
                new_select = False
        input('>')
        print(select)
        k = True
    if cmd[0:4] == "clock":
        os.system("clock")
    if cmd[0:4] == "cmd ":
        print(cmd[4:])
        os.chdir(cmd[4:])
    if cmd[0:7] == "restart":
        os.system('explor')
    if cmd[0:9] == "whatsapp":
        print("whatsapp")
        os.startfile(f'C:{kot[0]}Users{kot[0]}joach{kot[0]}AppData{kot[0]}Local{kot[0]}WhatsApp{kot[0]}WhatsApp.exe')
        #x=72, y=114)
        pyautogui.moveTo(72, 114)
        pyautogui.click()
    if cmd[0:3] == "pip":
        if cmd[4:]=="list":
            os.system('pip list')
        if cmd[4:7]=="add":
            os.system(f'pip install {cmd[8:]}')
        if cmd[4:7]=="del":
            os.system(f'pip uninstall {cmd[8:]}')
    if cmd[0:4] == "app ":
        e = os.getcwd()
        os.chdir('C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
        print("app list:")
        tab = tree_print_n(".",0)
        filer = tab[0]
        fi_count = len(filer)
        folders = tab[1]
        fill_in = tab[2]
        fl_count = len(folders)
        print(fi_count)
        for a in range(0,len(filer)):
            x = filer[a]
            print(x[2:])
            print('-----------')
        print("------------------------------")
        tab = tree_print_n(".",1)
        filer = tab[0]
        fi_count = len(filer)
        folders = tab[1]
        fill_in = tab[2]
        fl_count = len(folders)
        print(fi_count)
        app = []
        app_color = fg('#fc03e8') + bg('#2e2d2e')
        o = 0
        for a in range(0,len(fill_in)):
            x = fill_in[a]
            a -= o
            if x.endswith('.lnk') or x.endswith('.exe'):
                s = x[:-4]
                
                s = s.split(kot[0])
                
                print(app_color+f'{a+1}: {s[-1]}'+res)
                app.append(x)
            else:
                o +=1
        
        app_nr = input("app nr:")
        
        ler = int(app_nr)
        ler -=1
        
        s = app[ler]
        print(f'{os.getcwd()}{s[1:]}')
        os.startfile(f'{os.getcwd()}{s[1:]}')
        
        
        os.chdir(f'{e}')

    if k == True:
        os.system('cls')
    
    