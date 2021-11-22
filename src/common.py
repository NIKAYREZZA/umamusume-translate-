from ntpath import join
import os
import sys
import json


GAME_ROOT = os.path.realpath(os.path.join(os.environ['LOCALAPPDATA'], "../LocalLow/Cygames/umamusume/"))
GAME_ASSET_ROOT = os.path.join(GAME_ROOT, "dat")
GAME_META_FILE = os.path.join(GAME_ROOT, "meta")
GAME_MASTER_FILE = os.path.join(GAME_ROOT, "master/master.mdb")


def searchFiles(IMPORT_GROUP, IMPORT_ID) -> list:
    found = list()
    for root, dirs, files in os.walk("translations/"):
        depth = len(dirs[0]) if dirs else 3
        if IMPORT_GROUP and depth == 2:
            dirs[:] = [d for d in dirs if d == IMPORT_GROUP]
        elif IMPORT_ID and depth == 4:
            dirs[:] = [d for d in dirs if d == IMPORT_ID]
        found.extend(os.path.join(root, file) for file in files)
    return found

def readJson(file) -> dict:
    with open(file, "r", encoding="utf8") as f:
        return json.load(f)

def writeJsonFile(file, data):
    with open(file, "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

class Args:
    parsed = dict()

    def getArg(self, name, default=None):
        try:
            return self.parsed[name]
        except KeyError:
            return default

    def setArg(self, name, val):
        self.parsed[name] = val

    def parse(self):
        args = sys.argv[1:]
        idx = 0
        while idx < len(args):
            name = args[idx]
            if name.startswith("-"):
                try:
                    val = args[idx+1]
                except IndexError:
                    val = ""
                if val and not val.startswith("-"):
                    if val.startswith('"'):
                        while not val.endswith('"'):
                            idx += 1
                            val += args[idx + 1]
                    self.setArg(name, val)
                    idx += 2  # get next opt
                else:
                    self.setArg(name, True)
                    idx += 1
            else: raise SystemExit("Invalid arguments")
        return self

class TranslationFile:
    def __init__(self, file):
        self.file = file
        self.data = readJson(file)
        self.version = self._getVersion()

    def _getVersion(self) -> int:
        if 'version' in self.data:
            return self.data['version']
        else:
            return 1

    def getTextBlocks(self) -> list:
        if self.version > 1:
            return self.data['text']
        else:
            return list(self.data.values())[0]

    def getBundle(self):
        if self.version > 1:
            return self.data['bundle']
        else:
            return list(self.data.keys())[0]

    def save(self):
        writeJsonFile(self.file, self.data)

def usage(args: str, *msg: str):
    joinedMsg = '\n'.join(msg)
    print(f"Usage: {sys.argv[0]} {args}\n{joinedMsg}")
    raise SystemExit
