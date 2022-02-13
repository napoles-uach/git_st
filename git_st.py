import streamlit as st
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #print('file changed')
        #print(os.popen("ls -l").read())
        os.popen("git add simple.py")
        os.popen("git commit -m 'Fixes a bug.'")
        os.popen("git push")


@st.cache
def git_call(token):
    os.system('git config --global user.name "napoles-uach"')
    os.system('git config --global user.email "jnapoles@uach.mx"')
    os.system('git config --global pull.rebase false')

    os.system(f'git clone https://napoles-uach:{token}@github.com/napoles-uach/simple.git')
    os.system('git fetch')
    os.system('git merge FETCH_HEAD')

if __name__ == "__main__":
    st.title('Hi :cat: :+1:')
    token=st.text_input('token:')
    
    git_call(token)

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='simple/simple.py', recursive=False)
    observer.start()

    input_=st.text_area('Area for Python+Streamlit code. Try: st.balloons()')
    with open('simple/simple.py', 'w') as f:
        if os.stat('simple/simple.py').st_size > 0:
            pass
        else:
            f.write('import streamlit as st\n')
        f.write(input_+'\n')

#    try:
#        while True:
#            time.sleep(1)
#    except KeyboardInterrupt:
#        observer.stop()
#    observer.join()