"""Libsass compiler for django-pipeline.
Speedups development and/or production when compiling sass assets. No need of
ruby sass anymore.
"""

import sass
import codecs
from pipeline.compilers import CompilerBase
from django.conf import settings


class LibSassCompiler(CompilerBase):
    output_extension = "css"

    def match_file(self, filename):
        return filename.endswith((".scss", ".sass"))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        myfile = codecs.open(outfile, "w", "utf-8")

        if settings.DEBUG:
            myfile.write(sass.compile(filename=infile))
        else:
            myfile.write(sass.compile(filename=infile, output_style="compressed"))
        return myfile.close()
