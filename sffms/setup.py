from distutils.core import setup

setup(
    name = 'sffms',
    packages = ['sffms', 'sffms.quickstart'],
    version = '0.9.4',
    description = 'Sffms-style LaTeX output for Sphinx',
    author = 'Evan Goer',
    author_email = 'evan@goer.org',
    url = 'https://github.com/evangoer/sphinx_dev/tree/master/sffms',
    requires = ['Sphinx (>=1.0)'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Artistic Software',
        'Topic :: Documentation',
        'Topic :: Text Processing :: Markup :: LaTeX',
    ],
    entry_points = {
        'console_scripts': [
            'sffms-quickstart = sffms.quickstart:main'
        ]
    },
    long_description = '''\
    sffms LaTeX Extension for Sphinx
    ================================

    Implements sffms-style LaTeX output for reST + Sphinx, as specified by
    http://www.mcdemarco.net/sffms/.

    Sffms is a LaTeX document class for typesetting fiction manuscripts.
    This is in contrast with the default Sphinx LaTeX Builder, which is 
    designed for typesetting technical articles and manuals. The sffms 
    Builder outputs "Standard Manuscript Format", 12-pt monospaced font 
    with 1-inch margins and running headers. The package also exposes many 
    configuration options for customizing your output.

    You can use this package to author short stories and novels in reST 
    rather than raw LaTeX, taking advantage of Sphinx's flexible HTML 
    and EPUB capabilities while still being able to typeset your manuscript 
    properly for submission to publishers.

    .. note:: The sffms Builder only supports a small number of directives
         and roles that are appropriate for fiction writing, such as
         paragraphs, sections, and certain inline styles. The Builder
         ignores ReST elements that have no direct counterpart
         in the sffms specification.
    '''
)
