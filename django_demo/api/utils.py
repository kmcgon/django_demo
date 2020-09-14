import subprocess


def get_date():
    """Get the current date and time from the system."""
    return subprocess.check_output("date").decode("utf-8")


def get_cpuinfo():
    """Get all of the contents of /proc/cpuinfo.
    
    This is equivalient to 'cat /proc/cpuinfo' in bash.
    """
    with open("/proc/cpuinfo", "r") as f:
        cpuinfo = f.readlines()
        cpuinfo = [tuple(s.strip("\n").split("\t:")) for s in cpuinfo]
    return cpuinfo
