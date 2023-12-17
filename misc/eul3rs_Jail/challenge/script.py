import random
from io import StringIO
import sys
import re 
REGEX_PATTERN = r'\s*\w+\s*\([\s\'"\[\(\{\*]+\w+[\s\'"\[\(\{]+\)\s*'
sys.addaudithook

BLACKED_LIST = ['compile', 'eval', 'exec','__import__']

eval_func = eval

for m in BLACKED_LIST:
    del __builtins__.__dict__[m]


def my_audit_hook(event, _):
    BALCKED_EVENTS = set({'pty.spawn','os.exec', 'os.posix_spawn','os.spawn','subprocess.Popen','code.__new__','function.__new__','cpython._PySys_ClearAuditHooks','open','sys._getframe'})
    if event in BALCKED_EVENTS:
        raise RuntimeError('Operation banned: {}'.format(event))

def calc():
    sys.stdout.write('You can calculate everything you want :)\n')
    sys.stdout.flush()
    sys.stdout, sys.stderr, challenge_original_stdout = StringIO(), StringIO(), sys.stdout

    try:
        _ = input('')
        if len(re.findall(REGEX_PATTERN, _)) != 0:
            sys.stdout = challenge_original_stdout
            print("Seems not right! please don't break me it!")
            return
        sys.stdout = challenge_original_stdout
        input_data = print(eval_func(_,{},{}))
    except Exception as e:
        sys.stdout = challenge_original_stdout  
        print(f"Seems not right! please don't break me it!")


WELCOME=''' 
######  #######                             
#     # #       #    # #      ###### #####  
# ### # #       #    # #      #      #    # 
# ### # #####   #    # #      #####  #    # 
# ####  #       #    # #      #      #####  
#       #       #    # #      #      #   #  
 #####  #######  ####  ###### ###### #    # 
                                                                                                                                                                                                                                                                         
'''

def main():
    print(WELCOME)
    print('Welcome to my calculator game!\n')
    calc()
    
if __name__ == '__main__':
    sys.addaudithook(my_audit_hook)
    main()
