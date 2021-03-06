import sys, os

class TerminalColor(object):
    @classmethod
    def blue(cls):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return ""
        return TerminalColor.bold(34)
    
    @classmethod
    def white(cls):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return ""
        return TerminalColor.bold(39)
    
    @classmethod
    def red(cls):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return ""
        return TerminalColor.underline(31)
    
    @classmethod
    def yellow(cls):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return ""
        return TerminalColor.underline(33)
    
    @classmethod
    def reset(cls):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return ""
        return TerminalColor.escape(0)
    
    @classmethod
    def em(cls):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return ""
        return TerminalColor.underline(39)
    
    @classmethod
    def green(cls):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return ""
        return TerminalColor.color(92)
    
    @classmethod
    def color(cls, s):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return s
        return TerminalColor.escape("0;%s" % (s))
    
    @classmethod
    def bold(cls, s):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return s
        return TerminalColor.escape("1;%s" % (s))
    
    @classmethod
    def underline(cls, s):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return s
        return TerminalColor.escape("4;%s" % (s))
    
    @classmethod
    def escape(cls, s):
        if not os.isatty(1) or os.getenv("NO_COLORS") == "1":
            return s
        
        return "\033[%sm" % (s)
    

def status(msg):
    print "%s==>%s - %s" % (TerminalColor.blue(), TerminalColor.reset(), msg)

def title(msg):
    print "%s==>%s %s%s" % (TerminalColor.blue(), TerminalColor.white(), msg, TerminalColor.reset())

def success(msg):
    print "%s==>%s %s%s" % (TerminalColor.green(), TerminalColor.white(), msg, TerminalColor.reset())

def error(msg, noexit=False, exitcode=2):
    sys.stderr.write("%sError%s: %s\n" % (TerminalColor.red(), TerminalColor.reset(), msg))
    if not noexit:
        sys.exit(exitcode)

def emphasize(msg):
    return "%s%s%s%s" % (TerminalColor.reset(), TerminalColor.em(), msg, TerminalColor.reset())


