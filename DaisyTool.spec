# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py','convert.py','daisy.py'],
             #pathex=['H:\\Projects\\Saksham-DaisyBooks'],
             binaries=None,
             datas=[("daisy.ico", '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DaisyTool',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='daisy.ico')
