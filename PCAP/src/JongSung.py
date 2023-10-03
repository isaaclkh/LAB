import re

def ends_with_jong(kstr):
    m = re.search("[가-힣]+", kstr)
    if m:
        k = m.group()[-1]
        return (ord(k) - ord("가")) % 28 > 0
    else:
        return

def lee(kstr):
    josa = "이" if ends_with_jong(kstr) else ""
    return josa


def aa(kstr):
    josa = "아" if ends_with_jong(kstr) else "야"
    return josa
