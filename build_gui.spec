# -*- mode: python ; coding: utf-8 -*-
# run this command to build:
# pipenv run pyinstaller build_gui.spec

a = Analysis(
    ['gui.py'],
    pathex=['/home/ryanb/source/futhorc-transliterationtron-9000'],
    binaries=[],
    datas=[],
    hiddenimports=['filehandling', 'mappings', 'roman'],
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
    name='futhorc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
