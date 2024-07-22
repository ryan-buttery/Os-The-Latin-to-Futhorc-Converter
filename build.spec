# -*- mode: python ; coding: utf-8 -*-
# run this command to build:
# pipenv run pyinstaller build.spec

# tcl_path = '/usr/share/tcltk/'
# tk_path = '/usr/share/tcltk/'

a = Analysis(
    ['app.py'],
    pathex=['./modules'],
    binaries=[],
    datas=[
        ('./icons/favicon_square.png', 'icons'),
        ('./icons/favicon_square.ico', 'icons'),
#        (os.path.join(tcl_path, 'tcl8.6'), 'tcl'),
#        (os.path.join(tk_path, 'tk8.6'), 'tk')
    ],
    hiddenimports=['substitute_text', 'filehandling', 'mappings', 'roman', 'main_window', 'about_windows'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Os',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    #icon='./icons/favicon_square.ico',  
)
