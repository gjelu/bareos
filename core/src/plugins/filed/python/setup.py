from distutils.core import setup, Extension

module1 = Extension('bareosfd',
                    sources = ['/home/pstorz/git/bareos/core/python/python-fd.cc'],
                    include_dirs =  ['/home/pstorz/git/bareos/core/../..'],
                    libraries = ['bareos'],
                    library_dirs = ['/home/pstorz/git/bareos/b/core/src/lib/']
                    )

setup (name = 'bareosfd',
       version = '20.0.0~pre280.930f8d80d.dirty',
       description = 'bareos package',
       ext_modules = [module1])
