#!/usr/bin/env python3

import os
import shutil

ORIG = os.path.expanduser('~')
DEST = '/datos'
DEST_DOT = '/datos/dotfiles'
TODO = [
    'Android',
    'android-studio',
    '.AndroidStudio3.0',
    'apps',
    '.bazaar',
    'Descargas',
    'Documentos',
    'Encfs',
    'Escritorio',
    'filezilla',
    '.gconf',
    '.gimp-2.8',
    '.git-credential-cache',
    '.gnupg',
    '.gradle',
    'Imágenes',
   '.local/share/gnome-shell/extensions',
    '.mozilla',
    'Música',
    '.mutt',
    'PDF',
    'Personal',
    'Público',
    'Sync',
    '.ssh',
    '.subversion',
    'temporal',
    '.thunderbird',
    'Vídeos',
    '.vscode',
    '.rednotebook',
]
DOTFILES = [
    '.audacity-data',
    '.bash_it',
    '.bashrc',
    '.config/corebird',
    '.config/filezilla',
    '.config/inkscape',
    '.config/libreoffice/4/user/template',
    '.face',
    '.fontconfig',
    '.fonts',
    '.gitconfig',
    '.lftprc',
    '.local/share/applications',
    '.local/share/icons',
    '.nano',
    '.nanorc',
    'Plantillas',
    '.vim',
    '.vimrc',
]


if __name__ == '__main__':
    for element in TODO:
        if os.path.islink(os.path.join(ORIG, element)):
            if os.path.realpath(os.path.join(ORIG, element)) ==\
                    os.path.join(DEST, element):
                print('link', element, 'ok')
            else:
                print('link', element, 'false')
                os.remove(os.path.join(ORIG, element))
                os.symlink(os.path.join(DEST, element),
                           os.path.join(ORIG, element))
        else:
            print('nolink', os.path.join(DEST, element))
            print('---', os.path.join(ORIG, element))
            # existe origen
            if os.path.exists(os.path.join(ORIG, element)):
                print(os.path.join(DEST, element))
                # no existe destino
                if not os.path.exists(os.path.join(DEST, element)):
                    print(element.find('/'))
                    if element.find('/') == -1:
                        shutil.move(os.path.join(ORIG, element), DEST)
                    else:
                        shutil.move(os.path.join(ORIG, element),
                                    os.path.join(DEST, element))
                else:
                    if os.path.isfile(os.path.join(ORIG, element)):
                        os.remove(os.path.join(ORIG, element))
                    elif os.path.isdir(os.path.join(ORIG, element)):
                        shutil.rmtree(os.path.join(ORIG, element))
                os.symlink(os.path.join(DEST, element),
                           os.path.join(ORIG, element))
            # no existe origen
            else:
                # existe destino
                if os.path.exists(os.path.join(DEST, element)):
                    os.symlink(os.path.join(DEST, element),
                               os.path.join(ORIG, element))
    for element in DOTFILES:
        if os.path.islink(os.path.join(ORIG, element)):
            if os.path.realpath(os.path.join(ORIG, element)) ==\
                    os.path.join(DEST_DOT, element):
                print('link', element, 'ok')
            else:
                print('link', element, 'false')
                os.remove(os.path.join(ORIG, element))
                os.symlink(os.path.join(DEST_DOT, element),
                           os.path.join(ORIG, element))
        else:
            print('nolink', os.path.join(DEST_DOT, element))
            print('---', os.path.join(ORIG, element))
            # existe origen
            if os.path.exists(os.path.join(ORIG, element)):
                print(os.path.join(DEST_DOT, element))
                # no existe destino
                if not os.path.exists(os.path.join(DEST_DOT, element)):
                    print(element.find('/'))
                    if element.find('/') == -1:
                        shutil.move(os.path.join(ORIG, element), DEST_DOT)
                    else:
                        shutil.move(os.path.join(ORIG, element),
                                    os.path.join(DEST_DOT, element))
                else:
                    if os.path.isfile(os.path.join(ORIG, element)):
                        os.remove(os.path.join(ORIG, element))
                    elif os.path.isdir(os.path.join(ORIG, element)):
                        shutil.rmtree(os.path.join(ORIG, element))
                os.symlink(os.path.join(DEST_DOT, element),
                           os.path.join(ORIG, element))
            # no existe origen
            else:
                # existe destino
                if os.path.exists(os.path.join(DEST_DOT, element)):
                    os.symlink(os.path.join(DEST_DOT, element),
                               os.path.join(ORIG, element))
    exit(0)
