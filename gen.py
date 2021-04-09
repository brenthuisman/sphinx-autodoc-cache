import os
from tempfile import TemporaryDirectory
from sphinx.cmd.build import main

with TemporaryDirectory() as tmpdirname:
    main(['.',tmpdirname])

