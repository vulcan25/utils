#!/usr/bin/python

import subprocess, getopt
import sys

PRETEND = False
#PRETEND = True

def script(dest_title):
    
    """ copy essential files to host set in dest_title"""
    #args_length = len(sys.argv)
    #args = str(sys.argv)
    
    root = '/nfs/'+dest_title
    
    # Create home directory
    
    run_command([ 'mkdir',root+'/home/user/.ssh' ])
    run_command([ 'chown','user',root+'/home/user' ])
    
    # Copy file across
    
    files = ('/etc/passwd',
                '/etc/group',
                '/etc/shadow',
                '/home/user/.zshrc',
                '/home/user/.ssh/authorized_keys',
                '/etc/resolv.conf',
                '/etc/hosts',
                '/etc/sudoers',
                '/etc/ssh/sshd_config'
                )
                
    for source in files:
        #print('cp '+source+' /srv/'+dest_title+source)
        run_command( ['cp','-p',source, root+source])
    
def run_command(command):
    if PRETEND:
        print ('[execute] '+' '.join(command) )
    else: # actually execute
        return subprocess.call(command, shell=False, stderr=subprocess.STDOUT)
    

def main(argv):
    HELP = 'gather.py -h -t <title>'
    
    title = ''
    
    try:
        opts, args = getopt.getopt(argv,'ht:',['title ='])
    except getopt.GetoptError:
        print (HELP)
        sys.exit(2)
        
    for opt,arg in opts:
        if opt == '-h':
            print(HELP)
            sys.exit()
        elif opt in ('-t','title='):
            title = arg
            
    if title == '':
        print(HELP)
        sys.exit
    else:
        script(title)

if __name__ == "__main__":
    main(sys.argv[1:])
