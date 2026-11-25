# -*- coding: utf-8 -*-
"""English UI text for the EyeTrace English build (python build.py --lang en).

Keys are the variable names that EyeTrace.src.txt sets with CN("...").
"\n" is a newline. Every CN() variable must have an entry here; build.py
fails if one is missing, so a new Chinese string cannot slip into the
English build untranslated.
"""

EN = {
    "etTitle": "EyeTrace",
    "etS1": "Draft Visibility",
    "etS2": "Start Tracing",
    "etS3": "Apply Visibility",
    "etS4": "Finish Tracing",
    "etS5": "Restore Draft",
    "etS6": "Help",
    "etT0": "How much of the old draft stays visible: 0 = hidden, 100 = unchanged. Click Apply Visibility after changing it.",
    "etT1": "Use the current main color as the clean base, fade the old draft and create the ETInk layer to trace on. Only unmasked areas are affected.",
    "etT2": "Re-fade the old draft to the slider value. Lines you have already traced are not affected.",
    "etT3": "Fill the draft area back with the clean base color, leaving only your traced lines.",
    "etT4": "Put the old draft back on the model as it was. The ETInk layer is kept.",
    "etT5": "Show the help text.",
    "etS7": "Reset Brush",
    "etT7": "Reset the brush for tracing: color mode (Rgb on, Zadd off), Rgb Intensity 100, black, and keep the ETInk layer recording. Use it when lines look faint, the color is wrong, or nothing gets painted.",
    "etS8": "Ink Strength",
    "etT8": "The Rgb Intensity you want to trace with. Default 100 (solid lines). If you deliberately want semi-transparent lines, set this to the same value and the plugin will stop warning you.",
    "etMRgbA": "Note: brush Rgb Intensity is ",
    "etMRgbB": ",\nbut Ink Strength on the panel is ",
    "etMRgbC": ".\nBelow 100, lines look faint\nand mix with the draft underneath.\nIf this is on purpose, click Keep\nand set Ink Strength to match.",
    "etBSetA": "Set to ",
    "etBKeepA": "Keep ",
    "etMZadd": "\n\nNote: Zadd was on (it would change the model's shape while painting). It has been turned off; only color painting is kept.",
    "etMRgbFail": "\n\nNote: could not set Rgb Intensity to 100 automatically. Please drag Rgb Intensity at the top to 100.",
    "etMBrushOK": "Brush reset: color mode, Rgb Intensity 100, black.",
    "etBOK": "Continue",
    "etBCancel": "Cancel",
    "etBDel": "Delete Backup",
    "etBKeep": "Keep Backup",
    "etMHelp": (
        "EyeTrace Help\n\n"
        "1. Select the SubTool with the old draft and press T for Edit mode.\n"
        "2. If the eyes are part of the face mesh: mask everything except the eyes first (only unmasked areas are processed). A separate eye mesh needs no mask.\n"
        "3. Set the main color to the clean base color (usually white), set Draft Visibility, then click Start Tracing.\n"
        "4. Trace directly on the model; rotate freely to any angle. Lines go on the ETInk layer. If the brush looks faint, the color is wrong or nothing gets painted, click Reset Brush.\n"
        "5. To make the draft darker or lighter: move the slider and click Apply Visibility.\n"
        "6. When done, click Finish Tracing. The draft is cleared and only your lines remain.\n\n"
        "The plugin keeps a hidden copy of the original SubTool (name ending in ETDraft) so the draft can be restored."
    ),
    "etMNoMesh": "Please select a polymesh SubTool and press T for Edit mode first.",
    "etMBusy": "The selected layer is already the ETInk tracing layer, so tracing has started.\nUse Apply Visibility to change the draft, or Finish Tracing when you are done.",
    "etMHasBak": "This SubTool already has a draft backup (ETDraft).\nFinish Tracing or Restore Draft and delete the backup before starting again.",
    "etMNoInk": "Tracing layer not found.\nIn Tool > Layers, select the layer whose name starts with ETInk and try again.",
    "etMNoBak": "Draft backup SubTool (name ending in ETDraft) not found, so the draft cannot be restored.",
    "etMStart1": "The current main color will be used as the clean base color: ",
    "etMStart2": "\nDraft visibility: ",
    "etMStartOK": "Tracing started. Draw lines directly on the model and rotate freely.\nLines go on the ETInk layer.",
    "etMApplyOK": "Draft visibility updated.",
    "etMFinish1": "Tracing finished and the draft has been cleared.\nDelete the hidden draft backup SubTool?",
    "etMFinishOK": "Tracing finished and the draft has been cleared.",
    "etMRestoreOK": "Draft restored.",
    "etMNoColor": "Could not read the main color; using white as the clean base color.",
    "etMDupFail": "Could not duplicate the SubTool. Cancelled.",
}
