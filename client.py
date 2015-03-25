import sublime
import subprocess

# status returned by 'cm getstatus --format="{1}" <file>'
STATUS_PRIVATE     = 0
STATUS_CHECKED_IN  = 1
STATUS_CHECKED_OUT = 2


# Return file status
def is_controlled(filename):
    p = subprocess.Popen(['cm', 'getstatus', '--format="{1}"', filename], shell=True, stdout=subprocess.PIPE)
    while p.poll() == None:
        pass
    out = int(p.stdout.read().decode("utf-8").strip().strip("\""))
    return out != STATUS_PRIVATE


# Checkout the file
def checkout(filename):
    p = subprocess.Popen(['cm', 'checkout', filename], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while p.poll() == None:
        pass
    out = p.stdout.read().decode("utf-8").strip().strip("\"")
    if p.returncode == 0:
        sublime.status_message("[PlasticSCM] " + out.splitlines()[-1])
    else:
        sublime.error_message(p.stderr.read().decode("utf-8"))

