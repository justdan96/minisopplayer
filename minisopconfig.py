'''
MiniSopPlayer configuration script
'''

class MiniSopConfig(object):
    # ----------------------------------------------------
    # configuration
    # ----------------------------------------------------
    #
    # Ace Stream Engine host
    # Change this if you use remote Ace Stream Engine
    # Remember that by default Ace Stream Engine listens only
    # Local host, so start it with --bind-all parameter
    sophost = 'localhost'
    # Ace Stream Engine port (autodetect for Windows)
    sopport = 8908
    # Ace Stream Engine connection timeout
    sopconntimeout = 45
    # external player to use
    sopplayer = 'vlc-wrapper'
