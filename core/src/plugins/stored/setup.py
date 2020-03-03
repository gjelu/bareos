from distutils.core import setup, Extension

module1 = Extension('bareossd',
                    sources = ['/home/pstorz/git/bareos/core/python-sd.cc'],
                    include_dirs =  ['/home/pstorz/git/bareos/core/../..'],
                    libraries = ['bareos'],
                    library_dirs = ['/home/pstorz/git/bareos/b/core/src/lib/']
                    )

setup (name = 'bareossd',
       version = '20.0.0~pre280.930f8d80d.dirty',
       description = 'bareos package',
       ext_modules = [module1])
