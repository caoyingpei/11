# -*- mode: python -*-

block_cipher = None


a = Analysis(['splider.py'],
             pathex=['C:\\Users\\T450S\\workspace\\PY_CYP\\PRO_SPLIDER'],
             binaries=None,
             datas=None,
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
          name='splider',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='E:\\3.Í¼Æ¬ËØ²Ä\\¿É°®Ã¨\\ooopic_1471486633.ico')
