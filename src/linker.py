#!/usr/bin/env python3

import os
import shutil

ORIG = os.path.expanduser('~')
DEST = '/datos'

TODO = [
    '.bash_it',
    '.bashrc',
    '.bazaar',
    '.config/corebird',
    '.config/filezilla',
    '.config/GIMP',
    '.config/inkscape',
    '.config/sublime-text-3',
    'Descargas',
    'Documentos',
    'Escritorio',
    '.face',
    '.fonts',
    '.gimp-2.8',
    '.gnupg',
    '.gradle',
    'Imágenes',
    '.local/share/corebird',
    'Música',
    '.nano',
    '.nanorc',
    'Música',
    'PDF',
    'Personal',
    'Plantillas',
    'Público',
    'Sync',
    '.ssh',
    '.subversion',
    'Vídeos',
]


if __name__ == '__main__':
    for element in TODO:
        if os.path.islink(os.path.join(ORIG, element)):
            print('link', element)
        else:
            print('nolink', os.path.join(DEST, element))
            print('---', os.path.join(ORIG, element))
            if os.path.exists(os.path.join(ORIG, element)): # existe origen
                print(os.path.join(DEST, element))
                if not os.path.exists(os.path.join(DEST, element)): # no existe destino
                    print(element.find('/'))
                    if element.find('/') == -1:
                        shutil.move(os.path.join(ORIG, element), DEST)
                    else:
                        dest = ''.join(element.split('/')[:-1])
                        shutil.move(os.path.join(ORIG, element),
                                    os.path.join(DEST, dest))
                else:
                    if os.path.isfile(os.path.join(ORIG, element)):
                        os.remove(os.path.join(ORIG, element))
                    elif os.path.isdir(os.path.join(ORIG, element)):
                        shutil.rmtree(os.path.join(ORIG, element))
                os.symlink(os.path.join(DEST, element),
                           os.path.join(ORIG, element))
            else: # no existe origen
                if os.path.exists(os.path.join(DEST, element)): # existe destino
                    os.symlink(os.path.join(DEST, element),
                               os.path.join(ORIG, element))
    exit(0)
