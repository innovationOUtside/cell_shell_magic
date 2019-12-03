"""cell_shell magic"""
__version__ = '0.0.1'

def load_ipython_extension(ipython):
    
    def shellify(lines):
        if not lines[0].startswith('%'):
            return ['%%python3']+lines
        return lines

    
    ipython.input_transformers_cleanup.append(shellify)