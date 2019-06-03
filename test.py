import os
import subprocess

def check_call(cmd):
  subprocess.check_call(cmd.split(' '))

print('update')
check_call('./emsdk update-tags')

print('test latest')
check_call('./emsdk install latest')
check_call('./emsdk activate latest')
assert 'fastcomp' in open(os.path.expanduser('~/.emscripten')).read()
assert 'upstream' not in open(os.path.expanduser('~/.emscripten')).read()
check_call('source /root/emsdk/emsdk_env.sh --build=Release')
check_call('emcc hello_world.cpp')
check_call('emcc hello_world.cpp -s WASM=0')
check_call('emcc --clear-cache')

print('test latest-releases-upstream')
check_call('python2 /root/emsdk/emsdk install latest-upstream')
check_call('./emsdk activate latest-upstream')
check_call('source /root/emsdk/emsdk_env.sh --build=Release')
check_call('emcc hello_world.cpp')
assert open(os.path.expanduser('~/.emscripten')).read().count('LLVM_ROOT') == 1
assert 'upstream' in open(os.path.expanduser('~/.emscripten')).read()
assert 'fastcomp' not in open(os.path.expanduser('~/.emscripten')).read()

print('test tot-upstream')
check_call('./emsdk install tot-upstream')
check_call('./emsdk activate tot-upstream')
check_call('source /root/emsdk/emsdk_env.sh --build=Release')
check_call('emcc hello_world.cpp')

print('test tot-fastcomp')
check_call('./emsdk install tot-fastcomp')
check_call('./emsdk activate tot-fastcomp')
check_call('source /root/emsdk/emsdk_env.sh --build=Release')
check_call('emcc hello_world.cpp')

print('test specific release (old)')
check_call('./emsdk install sdk-1.38.31-64bit')
check_call('./emsdk activate tot-fastcomp')

print('test specific release (new, short name)')
check_call('./emsdk install 1.38.33')
check_call('./emsdk activate tot-fastcomp')
assert 'fastcomp' in open(os.path.expanduser('~/.emscripten')).read()
assert 'upstream' not in open(os.path.expanduser('~/.emscripten')).read()

print('test specific release (new, full name)')
check_call('./emsdk install sdk-1.38.33-upstream-64bit')
check_call('./emsdk activate sdk-1.38.33-upstream-64bit')

print('test binaryen source build')
check_call('./emsdk install --build=Release binaryen-master-64bit')

