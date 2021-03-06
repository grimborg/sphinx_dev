conf_py ='''\
# Configuration file for '%(title)s'
# Created by sffms-quickstart on %(now)s.
#
# -- Options for sffms output ---------------------------------------------------

# Sets the title. The title appears on the title page and in the 
# running header. This field is required.
sffms_title = '%(title)s'

# Specifies whether to typeset this manuscript as a novel or as 
# a short story.
sffms_novel = %(novel)s

# Sets the author name. The author name appears on the title page  
# and in the running header. This field is required.
sffms_author = '%(author)s'

# Provides a free-form multi-line address, which is typically a postal
# address, but could also include a phone number, email address, or any
# other contact info you wish to include. The address is displayed on the
# title page. This field is not required, but it is strongly recommended.
sffms_address = %(address)s

# Provides your real name for use with your mailing address, if you are 
# using a pen name or are publishing under some variation of your name.
# sffms_authorname = None

# Changes the font to 12-point, 10-pitch Courier, as an alternative to 
# LaTeX's default monospace font.
# sffms_courier = False

# Indicates whether the manuscript is disposable. When set to True, this
# field causes sffms to print "Disposable Copy" under the word count on 
# the title page.
# sffms_disposable = False

# Selects whether to doublespace lines of verse. When set to True, sffms 
# doublespaces lines of verse, just as it does ordinary paragraphs.
# sffms_doublespace_verse = False

# Indicates how to space between sentences. When set to True, sffms 
# inserts one space after sentences instead of two.
# sffms_frenchspacing = False

# Overrides the entire running header with arbitrary LaTeX. Only use 
# this option if you really know what you are doing. Don't forget to 
# escape backslashes so that they will get passed to LaTeX correctly.
# sffms_msheading = None

# Changes the manuscript to be single spaced and use a non-monospaced 
# font, as with an ordinary LaTeX article or book.
# sffms_nonsubmission = False

# Removes the title page. This option only works if sffms_nonsubmission 
# is True.
# sffms_notitle = False

# Sets the paper size. Must be set to one of 'a4paper', 'letterpaper',
# or None (which is equivalent to 'letterpaper').
# sffms_papersize = None

# Controls how sffms handles "legacy" quotes, per the sffms LaTeX 
# documentation. Must be one of None, 'smart', or 'dumb'.
# sffms_quote_type = None

# Sets the title in the running header. Running headers usually look 
# nicer if you supply a shorter version of your title. 
sffms_runningtitle = %(runningtitle)s

# Changes the scene separator string from "#" using plain text or 
# arbitrary LaTeX. 
# sffms_sceneseparator = None

# Adjusts the layout according to a particular publisher's standards. 
# Must be set to one of: None, 'anon', 'baen', 'daw', 'wotf'.
# sffms_submission_type = None

# Sets your surname in the running header. Traditionally, running 
# headers use the author's surname rather than their full name.
sffms_surname = %(surname)s

# Controls the word count. When you you run LaTeX on your manuscript, 
# this also generates an automatic word count. You can override this
# by setting sffms_wordcount to a number, or suppress the wordcount 
# entirely by setting this field to None.
# sffms_wordcount = 'default'

#
# The remaining configuration values are either general Sphinx 
# settings, or settings for HTML and EPUB output. These settings are
# intentionally very minimal -- for basic HTML and EPUB output,
# you shouldn't have to change a thing. However, you can customize 
# this file much more heavily if need be. For more information, refer 
# to the Sphinx documentation at http://sphinx.pocoo.org/config.html.
#
# -- General configuration -----------------------------------------------------
#
extensions = ['sffms']
master_doc = '%(master_doc)s'
project = u'%(title)s'
copyright = u'%(copyright)s'
source_suffix = '.txt'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'haiku'
html_title = u'%(title)s'
html_short_title = %(runningtitle)s
html_static_path = ['_static']

# -- Options for EPUB output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'%(title)s'
epub_author = u'%(author)s'
epub_publisher = u'%(author)s'
epub_copyright = u'%(copyright)s'

# -- Options for LaTeX output --------------------------------------------------

# Just in case you want to build the default Sphinx LaTeX for some reason.
# This has no effect on sffms output. It's just here so your build won't fail.
latex_documents = [
  ('%(master_doc)s', '%(master_doc)s.tex', u'%(title)s',
   u'%(author)s', 'howto'),
]

'''

opening_lines = [
    "It was a dark and stormy night...",
    "It is a truth universally acknowledged, that a single man in possession \nof a good fortune must be in want of a wife.",
    "Call me Ishmael.",
    "You don't know about me without you have read a book by the name of \nThe Adventures of Tom Sawyer; but that ain't no matter.",
    "Happy families are all alike; every unhappy family is unhappy in its own way.",
    "One morning, when Gregor Samsa woke from troubled dreams, he found \nhimself transformed in his bed into a horrible vermin.",
    "Alice was beginning to get very tired of sitting by her sister on the \nbank, and of having nothing to do: once or twice she had peeped into the \nbook her sister was reading, but it had no pictures or conversations in \nit, 'and what is the use of a book,' thought Alice 'without pictures or \nconversation?'",
    "Dorothy lived in the midst of the great Kansas prairies, with Uncle \nHenry, who was a farmer, and Aunt Em, who was the farmer's wife.",
    "Happy families are all alike; every unhappy family is unhappy in \nits own way.",
    "I am a sick man.... I am a spiteful man.  I am an unattractive man.  \nMy liver hurts.",
    "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet \nhole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, \nsandy hole with nothing in it to sit down on or to eat: it was a \nhobbit-hole, and that means comfort.",
    "It was a queer, sultry summer, the summer they electrocuted \nthe Rosenbergs, and I didn't know what I was doing in New York.",
    "The most merciful thing in the world, I think, is the inability \nof the human mind to correlate all its contents.",
    "Marley was dead, to begin with.",
    "We were somewhere around Barstow on the edge of the desert when \nthe drugs began to take hold.",
    "His name was Gaal Dornick and he was just a country boy who had \nnever seen Trantor before.",
    "A screaming comes across the sky.",
    "Mr Sherlock Holmes, who was usually very late in the mornings, \nsave upon those not infrequent occasions when he stayed up all night, \nwas seated at the breakfast table.",
    "Some years ago there was in the city of York a society of magicians.",
    "It was seven o'clock of a very warm evening in the Seeonee hills \nwhen Father Wolf woke up from his day's rest, scratched himself, yawned, \nand spread out his paws one after the other to get rid of the sleepy feeling in their tips.",
    "It was inevitable: the scent of bitter almonds always reminded him \nof the fate of unrequited love.",
    "It was a bright cold day in April, and the clocks were striking thirteen.",
    "Robert Cohn was once middleweight boxing champion of Princeton. \nDo not think that I am very much impressed by that as a boxing title, \nbut it meant a lot to Cohn.",
    "Nick Naylor had been called many things since becoming the \nchief spokesman for the Academy of Tobacco Studies, but until now no one \nhad actually compared him to Satan.",
    "There was a boy called Eustace Clarence Scrubb, and he almost deserved it."
]

story_ms = '''\
.. Master manuscript file, created by sffms-quickstart on %(now)s. 
   You may add new paragraphs (and optionally, new scene breaks) directly 
   to this file. (Note: this paragraph is a comment and will not appear
   in your story's output.)

%(reST_title)s

%(opening_line_a)s

Scene Break
===========

%(opening_line_b)s

'''

novel_ms = '''\
.. Master manuscript file, created by sffms-quickstart on %(now)s. 
   You should not write new chapter content directly into this file. Instead, 
   you should create new .txt files in the same directory and then add their
   names to the list below. (Note: this paragraph is a comment and will not 
   appear in your novel's output.)

%(reST_title)s

.. toctree::
   :maxdepth: 2
   
   new_chapter.txt
   more_stuff.txt
'''

novel_new_chapter = '''\
****************
In the Beginning
****************

%(opening_line_a)s
'''

novel_more_stuff = '''\
**********************
I Need a Chapter Title
**********************

%(opening_line_b)s
'''

# Adapted from the sphinx-quickstart manual. Added sffms targets
# and stripped out some of the more obscure targets.
makefile = '''\
# Makefile for sffms manuscripts
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml epub latex latexpdf sffms sffmspdf text

help:
\t@echo "Please use \\`make <target>' where <target> is one of"
\t@echo "  html       to make standalone HTML files"
\t@echo "  dirhtml    to make HTML files named index.html in directories"
\t@echo "  singlehtml to make a single large HTML file"
\t@echo "  epub       to make an EPUB book"
\t@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
\t@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
\t@echo "  sffms      to make LaTeX files for Standard Manuscript Format"
\t@echo "  sffmspdf   to make LaTeX files for Standard Manuscript Format and run them through pdflatex"
\t@echo "  text       to make text files"

clean:
\t-rm -rf $(BUILDDIR)/*

html:
\t$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
\t@echo
\t@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
\t$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
\t@echo
\t@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
\t$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
\t@echo
\t@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

epub:
\t$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
\t@echo
\t@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
\t$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
\t@echo
\t@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
\t@echo "Run \\`make' in that directory to run these through (pdf)latex" \\
\t      "(use \\`make latexpdf' here to do that automatically)."

latexpdf:
\t$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
\t@echo "Running LaTeX files through pdflatex..."
\tmake -C $(BUILDDIR)/latex all-pdf
\t@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

sffms:
\t$(SPHINXBUILD) -b sffms $(ALLSPHINXOPTS) $(BUILDDIR)/sffms
\t@echo
\t@echo "Build finished; the LaTeX files are in $(BUILDDIR)/sffms."
\t@echo "Run \\`make' in that directory to run these through (pdf)latex" \\
\t      "(use \\`make sffmspdf' here to do that automatically)."

sffmspdf:
\t$(SPHINXBUILD) -b sffms $(ALLSPHINXOPTS) $(BUILDDIR)/sffms
\t@echo "Running LaTeX files through pdflatex..."
\tmake -C $(BUILDDIR)/sffms all-pdf
\t@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/sffms."

text:
\t$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
\t@echo
\t@echo "Build finished. The text files are in $(BUILDDIR)/text."
'''

makefile_sffms = '''\
# Makefile for sffms LaTeX output

ALLDOCS = $(basename $(wildcard *.tex))
ALLPDF = $(addsuffix .pdf,$(ALLDOCS))

all: $(ALLPDF)
all-pdf: $(ALLPDF)

LATEXOPTS =

%.pdf: %.tex
\tlatex $(LATEXOPTS) '$<'
\tlatex $(LATEXOPTS) '$<'
\tpdflatex $(LATEXOPTS) '$<'
\tpdflatex $(LATEXOPTS) '$<'

clean:
\trm -f *.dvi *.log *.ind *.aux *.toc *.syn *.idx *.out *.ilg *.pla

.PHONY: all all-pdf clean
'''