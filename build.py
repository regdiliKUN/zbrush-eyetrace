# -*- coding: utf-8 -*-
"""Build EyeTrace.txt (pure ASCII ZScript) from EyeTrace.src.txt (UTF-8).

Lines of the form   [VarSet,NAME,CN("中文文本")]   are expanded into chained
StrFromAsc VarSets, because the ZScript compiler strips non-ASCII bytes.
"\\n" inside CN("...") becomes a real newline (byte 10).
Usage: python build.py [debuglogpath]
"""
import re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / 'EyeTrace.src.txt'
DST = HERE / 'dist' / 'EyeTrace.txt'
CHUNK = 9
pat = re.compile(r'^(\s*)\[VarSet,\s*(\w+)\s*,\s*CN\("(.*)"\)\s*\]\s*$')


def expand(indent, name, text):
    data = text.replace('\\n', '\n').encode('utf-8')
    parts = ['[StrFromAsc,%d]' % b for b in data]
    out = []
    for i in range(0, max(len(parts), 1), CHUNK):
        chunk = parts[i:i + CHUNK]
        if i == 0:
            out.append('%s[VarSet,%s,[StrMerge,%s]]' % (indent, name, ','.join(chunk) if chunk else '""'))
        else:
            out.append('%s[VarSet,%s,[StrMerge,#%s,%s]]' % (indent, name, name, ','.join(chunk)))
    return out


def main():
    dbg = sys.argv[1] if len(sys.argv) > 1 else ''
    lines = SRC.read_text(encoding='utf-8').splitlines()
    out = []
    for ln in lines:
        m = pat.match(ln)
        if m:
            out.extend(expand(*m.groups()))
            continue
        out.append(ln)
    text = '\r\n'.join(out) + '\r\n'
    dev = sys.argv[2] if len(sys.argv) > 2 else 'ETApply'
    text = text.replace('__DBGPATH__', dbg).replace('__DBGON__', '1' if dbg else '0')
    text = text.replace('__DEVACTION__', dev)
    # strip non-ASCII from comments (compiler would drop them anyway)
    bad = [c for c in text if ord(c) > 127]
    if bad:
        text = ''.join(c if ord(c) < 128 else '?' for c in text)
    DST.parent.mkdir(exist_ok=True)
    DST.write_bytes(text.encode('ascii'))
    print('built', DST, len(text), 'chars; non-ascii replaced:', len(bad))


if __name__ == '__main__':
    main()
