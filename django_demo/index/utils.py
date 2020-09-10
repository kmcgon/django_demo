import subprocess


def get_date() -> str:
    return subprocess.check_output("date").decode("utf-8")


def get_cpuinfo():
    with open("/proc/cpuinfo", "r") as f:
        cpuinfo = f.readlines()
        cpuinfo = [tuple(s.strip("\n").split("\t:")) for s in cpuinfo]
    return cpuinfo
