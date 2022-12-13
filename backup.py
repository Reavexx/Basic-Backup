import os
import datetime
import shutil

# Pfad zum Verzeichnis, das gesichert werden soll
source_dir = '/Users/agishanimalthas/Downloads'
target_dir = '/Users/agishanimalthas/Downloads/backup'

last_access_time = os.path.getatime(source_dir)

if (last_access_time > datetime.timedelta(days=7)) :

    # Name des gesicherten Verzeichnisses
    backup_name = 'backup-' + source_dir.split('/')[-1]

    # Erstelle eine Kopie des Verzeichnisses im Zielverzeichnis
    shutil.copytree(source_dir, os.path.join(target_dir, backup_name))

else :
    print("There weren't any Folders found which are older than 7 days.")




