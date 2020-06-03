  
#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = "0.1"
DOC_DIR = "share/doc/subreaker"

doc_and_conf_files = [(DOC_DIR,
                       ["doc/AUTHORS",
                        "doc/ChangeLog_Subreaker",
                        "doc/ChangeLog_lswww",
                        "doc/example.txt",
                        "INSTALL",
                        "README",
                        "TODO",
                        "VERSION"]), ("share/man/man1",
                                      ["doc/subdomain.1.gz",
                                       "doc/subdomain-cookie.1.gz",
                                       "doc/subdomain-getcookie.1.gz"])]

# Main
setup(
    name="subreaker",
    version=VERSION,
    description="a Web application subdomain scanner",
    long_description="""\
Subreaker Black-box Subdomain Scanner """,
    url="http://www.github.com/heqmat",
    author="Emir Güner",
    author_email="hemirguner@outlook.com",
    license="GPLv2",
    platforms=["Any"],
    packages=find_packages(),
    data_files=doc_and_conf_files,
    include_package_data=True,
    scripts=[
        "bin/subreaker",
        "bin/subreaker-cookie",
        "bin/subreaker-getcookie"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=[
        'requests>=1.2.3',
        'beautifulsoup4'
    ]
)
