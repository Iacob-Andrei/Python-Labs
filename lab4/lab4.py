import os
import sys


# Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director. Funcția
# returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca
# parametru.
def ex1(path):
    extensions = [file.rsplit('.')[1] for file in os.listdir(path)]
    extensions.sort()
    print(extensions)


# Să se scrie o funcție ce primește ca argumente două căi: director si fișier. Implementati functia astfel încât în
# fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul
# directorului de la calea folder, ce incepe cu litera A.
def ex2(path, filename):
    files = os.listdir(path)
    f = open(filename, mode='w')
    for file in files:
        if file[0] == 'A':
            f.write(os.path.join(path, file))
            f.write("\n")
    f.close()


# Să se scrie o funcție ce primește ca parametru un string my_path. Dacă parametrul reprezintă calea către un fișier,
# se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul reprezintă calea către un
# director, se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie
# reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele
# (recursiv) din directorul dat ca parametru.
def count_extensions(my_path):
    ext_count = dict()

    for filename in os.listdir(my_path):
        if os.path.isfile(os.path.join(my_path, filename)):
            if filename.rsplit('.')[1] not in ext_count:
                ext_count[filename.split('.')[1]] = 1
            else:
                ext_count[filename.split('.')[1]] += 1
        else:
            ext_count.update(count_extensions(os.path.join(my_path, filename)))

    return ext_count


def ex3(my_path):
    if os.path.isfile(my_path):
        data = open(my_path, "r").read()
        print(data[-20:])
    else:
        print(count_extensions(my_path))


# Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la
# linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
def ex4(path):
    data = {file.rsplit('.')[1] for file in os.listdir(path)}
    print(list(data))


# Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o
# listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in
# fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target
# nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
def ex5(target, to_search):
    try:
        assert (os.path.isfile(target) or os.path.isdir(target)), f'{target} is not a file or directory.'

        if os.path.isfile(target):  # check for file
            data = open(target, 'r').read()
            if to_search in data:
                return [target]
        else:  # check for directory
            files = list()
            for (root, directories, files) in os.walk(target):
                for filename in files:
                    full_filename = os.path.join(root, filename)
                    data = open(full_filename, 'r').read()
                    if to_search in data:
                        files.append(full_filename)
            return files

    except ValueError as e:
        print(e)


# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește
# un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în
# procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.
def error_callback(exception):
    print(f'EXCEPTION RAISED! \'{exception}\'')


def ex6(target, to_search, err_callback):
    try:
        assert (os.path.isfile(target) or os.path.isdir(target)), f'{target} is not a file or directory.'

        if os.path.isfile(target):  # check for file
            assert (os.access(target, os.R_OK)), f'{target} can not be read'
            data = open(target, 'r').read()
            if to_search in data:
                return [target]
        else:  # check for directory
            files = list()
            for (root, directories, files) in os.walk(target):
                for filename in files:
                    full_filename = os.path.join(root, filename)
                    assert (os.access(full_filename, os.R_OK)), f'{full_filename} can not be read'
                    data = open(full_filename, 'r').read()
                    if to_search in data:
                        files.append(full_filename)
            return files

    except ValueError as e:
        err_callback(e)


# Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si
# returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea
# fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca
# se poate citi din/scrie in fisier
def ex7(path):
    info = dict()
    info['full_path'] = os.path.join(os.getcwd(), path)
    info['file_size'] = os.stat(path).st_size
    if os.path.isfile(path):
        info['file_extension'] = path.split('.')[1]
    else:
        info['file_extension'] = None
    info['can_read'] = os.access(path, os.R_OK)
    info['can_write'] = os.access(path, os.W_OK)

    print(info)


# Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un
# director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina
# directorului dir_path
def ex8(dir_path):
    for file in os.listdir(dir_path):
        file = os.path.join(dir_path, file)
        if os.path.isfile(file):
            print(file)


if __name__ == '__main__':
    # ex1("D:\Facultate\Python-Labs\lab4\\resources")

    # ex2("D:\Facultate\Python-Labs\lab4\\resources", "D:\Facultate\Python-Labs\lab4\\resources\out.txt")

    # ex3("D:\Facultate\Python-Labs\lab4\\resources\out.txt")

    # ex3("D:\Facultate\Python-Labs\lab4")

    # ex4(sys.argv[1])
    # python .\lab4.py D:\Facultate\Python-Labs\lab4\\resources

    # ex7("resources\\out.txt")

    ex8("D:\Facultate\Python-Labs\lab4\\resources")
