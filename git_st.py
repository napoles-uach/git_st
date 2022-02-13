import streamlit as st
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #print('file changed')
        #print(os.popen("ls -l").read())
        os.popen("git add app.py")
        os.popen("git commit -m 'Fixes a bug.'")
        os.popen("git push")

st.title('Hi :cat: :+1:')
os.system('git config --global user.name "napoles-uach"')
os.system('git config --global user.email "jnapoles@uach.mx"')
os.system('git config --global pull.rebase false')
os.system('git clone https://napoles-uach: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@github.com/napoles-uach/simple.git')
os.system('git fetch')
os.system('git merge FETCH_HEAD')

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='app.py', recursive=False)
    observer.start()

#    try:
#        while True:
#            time.sleep(1)
#    except KeyboardInterrupt:
#        observer.stop()
#    observer.join()