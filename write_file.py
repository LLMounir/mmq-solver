"""
Lalami Mounir
2017/11/14
Massive Music Quiz One computer
version 3.0
-------------------------------
Fonctions de manipulation de fichiers textes
"""

def write_in_file(file,text,append):
    """ Ecris dans le fichier donné le texte donné """
    if append:
        f = open(file,'a')
        f.write(text)
        f.close()
    else:
        f = open(file,'w')
        f.write(text)
        f.close()

if __name__ == "__main__":
    pass