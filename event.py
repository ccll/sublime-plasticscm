import sublime
import sublime_plugin
import os
import os.path
import subprocess
from . import client


def readonly(filename):
    return not os.access(filename, os.W_OK)


def ask_to_checkout():
    return sublime.ok_cancel_dialog("Would you like to checkout this file from PlasticSCM?", "Yes, Checkout")


class PlasticSCMEventListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        filename = view.file_name()
        if not filename:
            return
        if not readonly(filename):
            return
        if not client.is_controlled(filename):
            return
        if ask_to_checkout():
            client.checkout(filename)


