usage: macvpnhelper [-h] [--duration DURATION] [--clickspeed CLICKSPEED]
                    [--fillpassword FILLPASSWORD] [--updatepass UPDATEPASS]
                    [--loginonly] [--warning WARNING] [--simulate] [--reset]
                    [--vpn VPN]

optional arguments:
  -h, --help            show this help message and exit
  --duration DURATION, -d DURATION
                        (time in hours|'wd'|'fd') E.g., 8h, the amount of time
                        (in hours) to keep the VPN active. Use 'wd' to do 9-12
                        and 1-6 (default), or 'fd' to do 9-6.
  --clickspeed CLICKSPEED, -cs CLICKSPEED
                        (superfast|fast|normal|slow|superslow) adjust based on
                        responsiveness of your GUI
  --fillpassword FILLPASSWORD, -fp FILLPASSWORD
                        (yes|no|andReturn) type in password and optionally hit
                        return in the dialogs. CAUTION: since this password is
                        provided to the GUI, it is possible that intermediate
                        clicks will result in your password being typed to,
                        e.g., chat dialogs. 'yes' is therefore safer than
                        'andReturn.'
  --updatepass UPDATEPASS, -up UPDATEPASS
                        (chrome|firefox|anyothername) opens TrustArc password
                        portal in browser.
  --loginonly, -l       Logs in once and quits.
  --warning WARNING, -w WARNING
                        (yes|no|warnOnly) Displays warning message when vpn
                        disconnects. If warnOnly is set, the program will
                        display warning messages when the vpn is disconnected
                        but not attempt to do anything else.
  --simulate, -s        When set, script which would be executed is instead
                        printed to the terminal.
  --reset               Use to reset your login information.
  --vpn VPN, -n VPN     Name of VPN to connect to. Must match your configured
                        connection.