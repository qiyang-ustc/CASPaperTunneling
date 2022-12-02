import os

def check_args(argv):
    if len(argv) != 2:
        print('Usage: caspt <origin url>')
        exit(1)

def check_if_pdf_exists(url):
    r"""Check if a PDF file with url exists in the cache directory."""
    # Can not user-config. But try this first.
    return url in open(os.environ["HOME"]+"/.cached-paper/downloaded").read()

def open_with_pdfreader(path):
    r"""Open a PDF file with path with the default PDF reader."""
    os.system('open "%s"' % path) # Maybe only availbale in macOS. But try this first