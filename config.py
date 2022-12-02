import os
import json

def main_init():
    # Maybe only availbale in macOS and Linux. But try this first
    os.system('''echo "{\\"PaperDir\\": \\"$HOME/.cached-paper\\"}" > ~/.CASPTrc''')
    os.system('''mkdir -p  $HOME/.cached-paper''')
    os.system('''touch $HOME/.cached-paper/downloaded''')

def load_config_file():
    r"""Load a configuration file from path. or create a template file to it"""
    config_file = os.environ["HOME"]+"/.CASPTrc"
    if not os.path.isfile(config_file):
        print("First Run, Auto Creating Config File at ~/.CASPTrc")
        main_init()
    with open(config_file) as f:
        return json.load(f)
