import sublime
import subprocess

# status returned by 'cm getstatus --format="{1}" <file>'
PLASTIC_PRIVATE     = 0
PLASTIC_CHECKED_IN  = 1
PLASTIC_CHECKED_OUT = 2


# Return True if file status is 'checked-in'
def is_checked_in(filename):
    p = subprocess.Popen(['cm', 'getstatus', '--format="{1}"', filename], shell=True, stdout=subprocess.PIPE)
    while p.poll() == None:
        pass
    out = int(p.stdout.read().decode("utf-8").strip().strip("\""))
    return out == PLASTIC_CHECKED_IN


# Checkout the file
def checkout(filename):
    p = subprocess.Popen(['cm', 'checkout', filename], shell=True, stdout=subprocess.PIPE)
    while p.poll() == None:
        pass
    out = p.stdout.read().decode("utf-8").strip().strip("\"")
    if p.returncode == 0:
        sublime.status_message("[PlasticSCM] " + out.splitlines()[-1])
    else:
        sublime.error_message(out)

