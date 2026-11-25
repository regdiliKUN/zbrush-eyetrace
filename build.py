# -*- coding: utf-8 -*-
"""Build EyeTrace.txt (pure ASCII ZScript) from EyeTrace.src.txt (UTF-8).

Lines of the form   [VarSet,NAME,CN("中文文本")]   are expanded into chained
StrFromAsc VarSets, because the ZScript compiler strips non-ASCII bytes.
"\\n" inside CN("...") becomes a real newline (byte 10).
Usage: python build.py [--lang zh|en] [debuglogpath]
  --lang zh (default)  Chinese UI  -> dist/EyeTrace.txt
  --lang en            English UI  -> dist/en/EyeTrace.txt (text from strings_en.py)
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
    args = sys.argv[1:]
    lang = 'zh'
    if '--lang' in args:
        i = args.index('--lang')
        lang = args[i + 1] if i + 1 < len(args) else ''
        del args[i:i + 2]
    if lang not in ('zh', 'en'):
        sys.exit('--lang must be zh or en')
    en = {}
    if lang == 'en':
        sys.path.insert(0, str(HERE))
        from strings_en import EN as en
    dst = DST if lang == 'zh' else HERE / 'dist' / 'en' / 'EyeTrace.txt'
    dbg = args[0] if len(args) > 0 else ''
    lines = SRC.read_text(encoding='utf-8').splitlines()
    out = []
    missing = []
    for ln in lines:
        m = pat.match(ln)
        if m:
            indent, name, text = m.groups()
            if lang == 'en':
                if name not in en:
                    missing.append(name)
                    continue
                text = en[name]  # real newlines; expand() encodes them as byte 10
            out.extend(expand(indent, name, text))
            continue
        out.append(ln)
    if missing:
        sys.exit('strings_en.py is missing: ' + ', '.join(missing))
    text = '\r\n'.join(out) + '\r\n'
    dev = args[1] if len(args) > 1 else 'ETApply'
    text = text.replace('__DBGPATH__', dbg).replace('__DBGON__', '1' if dbg else '0')
    text = text.replace('__DEVACTION__', dev)
    # strip non-ASCII from comments (compiler would drop them anyway)
    bad = [c for c in text if ord(c) > 127]
    if bad:
        text = ''.join(c if ord(c) < 128 else '?' for c in text)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(text.encode('ascii'))
    print('built', dst, len(text), 'chars; non-ascii replaced:', len(bad))


if __name__ == '__main__':
    main()
