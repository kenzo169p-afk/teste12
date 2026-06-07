import sys
import email.message

class CgiModule:
    @staticmethod
    def parse_header(line):
        m = email.message.Message()
        m['content-type'] = line
        params = m.get_params()
        if params is None:
            return m.get_content_type(), {}
        # get_params returns a list of (key, val) tuples
        return m.get_content_type(), {k: v for k, v in params[1:]}

sys.modules['cgi'] = CgiModule

import os
from pywebcopy import save_webpage

url = 'https://topchoicecorretora.com.br/'
download_folder = 'c:/Users/gordo/Desktop/teste/teste12/'

kwargs = {'bypass_robots': True, 'project_name': 'topchoicecorretora'}

try:
    save_webpage(url, download_folder, **kwargs)
    print("Website copied successfully.")
except Exception as e:
    print(f"Error: {e}")
