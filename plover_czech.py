from typing import Tuple, Dict, List, Optional

# STP+CKVRLNIEAOSTP.CKVNIE*
KEYS: Tuple[str] = (
    '#',
    'S-', 'T-', 'P-', '+-', 'C-', 'K-', 'V-', 'R-', 'L-', 'N-',
    'I-', 'E-',
    '-A', '-O',
    '-S', '-T', '-P', '-.', '-C', '-K', '-V', '-N', '-I', '-E',
    # Plover is not pleased with '*' here instead of '-*' for some reason
    '-*'
)

# Although for aesthetic reasons I'd prefer for -* sugared to *, adding it here
# also unfortunately turns strokes like -C* into C*, which is super ambiguous,
# and as noted above, Plover doesn't seem to accept '*' instead of '-*', at
# least in the posititon I've placed it
IMPLICIT_HYPHEN_KEYS: Tuple[str] = ('I-', 'E-', '-A', '-O')

# I'm not actually entirely sure what the purpose of this tuple is
SUFFIX_KEYS: Tuple[str] = ()

NUMBER_KEY: str = '#'

NUMBERS: Dict[str, str] = {
    'S-': '1-',
    'P-': '2-',
    'C-': '3-',
    'V-': '4-',
    'L-': '5-',
    '-S': '-6',
    '-P': '-7',
    '-C': '-8',
    '-V': '-9',
    '-I': '-0',
}

# Doesn't seem to work, so we'll use -* instead.
#
# Don't personally like the undo stroke being on the
# weakest finger on your hand, though.
# UNDO_STROKE_STENO: str = '-./-./-.'
UNDO_STROKE_STENO: str = '-*'

ORTHOGRAPHY_RULES: List[Tuple[str, str]] = []
ORTHOGRAPHY_RULES_ALIASES: Dict[str, str] = {}
ORTHOGRAPHY_WORDLIST: Optional[str] = None

# It seems that most protocols other than Gemini PR don't really encode the *
# keys (in English stenotype) as 4 separate keys, (or the S- keys, either)
# which is necessary here, so they don't get invited to the party.
KEYMAPS: Dict[str, Dict[str, Tuple[str]]] = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : 'S1-',
        'T-'        : 'S2-',
        'P-'        : 'T-',
        '+-'        : 'K-',
        'C-'        : 'P-',
        'K-'        : 'W-',
        'V-'        : 'H-',
        'R-'        : 'R-',
        'L-'        : '*1',
        'N-'        : '*2',
        'I-'        : 'A-',
        'E-'        : 'O-',
        '-A'        : '-E',
        '-O'        : '-U',
        '-S'        : '*3',
        '-T'        : '*4',
        '-P'        : '-F',
        '-.'        : '-R',
        '-C'        : '-P',
        '-K'        : '-B',
        '-V'        : '-L',
        '-N'        : '-G',
        '-I'        : '-T',
        '-E'        : '-S',
        '-*'        : ('-D', '-Z'),
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : 'a',
        'T-'        : 'q',
        'P-'        : 'w',
        '+-'        : 's',
        'C-'        : 'e',
        'K-'        : 'd',
        'V-'        : 'r',
        'R-'        : 'f',
        'L-'        : 't',
        'N-'        : 'g',
        'I-'        : 'c',
        'E-'        : 'v',
        '-A'        : 'n',
        '-O'        : 'm',
        '-S'        : 'y',
        '-T'        : 'h',
        '-P'        : 'u',
        '-.'        : 'j',
        '-C'        : 'i',
        '-K'        : 'k',
        '-V'        : 'o',
        '-N'        : 'l',
        '-I'        : 'p',
        '-E'        : ';',
        '-*'        : ('[', '\''),
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    }
}

DICTIONARIES_ROOT: str = 'asset:plover:assets'
DEFAULT_DICTIONARIES: List[str] = []
