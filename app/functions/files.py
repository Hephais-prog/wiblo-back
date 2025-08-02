import os
from pathlib import Path

from app import log, GLOBAL_DATA_PATH

def write_file_to_disk(content: str, name: str):
    """

    :param content:
    :param name:
    :return:
    """

    path = Path(os.path.join(GLOBAL_DATA_PATH, f"{name}.md"))

    with path.open("w", encoding="utf-8") as f:
        f.write(content)

    log.info(f"Fichier correctement créé : {path}")

def delete_file_from_disk(name: str):
    """

    :param name:
    :return:
    """

    path = Path(os.path.join(GLOBAL_DATA_PATH, f"{name}.md"))

    if path.exists():
            path.unlink()
            log.info(f"Fichier correctement supprimé : {path}")
    else:
        log.info(f"Le fichier {path} n'est pas la liste")
        pass