# PlasticSCM for Sublime Text 3


## Why

We are using PlasticSCM to manage our project, and we are working in 'exclusive lock' mode. While there are no official integration for Sublime Text, it is a pain to remember to **checkout** a file before editing. So I wrote this plugin.


## Features

- Prompt user and automatically **checkout** file when user start editing.
    - This is the major itch we scratch first.
    - It only applies on read-only files, so it will not annoy you if your team works in 'modify-merge' mode which does not involve a 'checkout' phase.


## TODO

- Add sidebar context menu for common PlasticSCM operations (checkin/checkout/undocheckout/cloak/ignore/annotate/history/refresh/...)

- Show file status in sidebar (added/deleted/changed/private/controlled/...)

- Show repository/workspace info in sidebar
