import subprocess

def get(x, y):
  ver = '1.%d.%d' % (x, y)

  print '''  {
    "id": "clang",
    "version": "e%s",
    "bitness": 64,
    "linux_url": "https://storage.googleapis.com/webassembly/emscripten-releases-builds/old/linux/emscripten-llvm-e%s.tar.gz",
    "osx_url": "https://storage.googleapis.com/webassembly/emscripten-releases-builds/old/mac/emscripten-llvm-e%s.tar.gz",
    "windows_url": "https://storage.googleapis.com/webassembly/emscripten-releases-builds/old/win/emscripten-llvm-e%s.zip",
    "zipfile_prefix": "%s-",
    "install_path": "oldclang",
    "activated_path": "%%installation_dir%%/emscripten",
    "activated_cfg": "LLVM_ROOT='%%installation_dir%%/bin';BINARYEN_ROOT='%%installation_dir%%'",
  },''' % (ver, ver, ver, ver, ver)

  print '''
  {
    "id": "emscripten",
    "version": "%s",
    "bitness": 64,
    "linux_url": "https://storage.googleapis.com/webassembly/emscripten-releases-builds/old/unix/%s.tar.gz",
    "osx_url": "https://storage.googleapis.com/webassembly/emscripten-releases-builds/old/unix/%s.tar.gz",
    "linux_url": "https://storage.googleapis.com/webassembly/emscripten-releases-builds/old/win/%s.zip",
    "zipfile_prefix": "%s-",
    "activated_cfg": "EMSCRIPTEN_ROOT='%%installation_dir%%'",
    "activated_path": "%%installation_dir%%",
    "activated_env": "EMSCRIPTEN=%%installation_dir%%",
  },''' % (ver, ver, ver, ver, ver)

for i in range(0, 15):
  get(36, i)

for i in range(0, 41):
  get(37, i)

for i in range(0, 32):
  get(38, i)

