def color(*args) -> str:
    """C = {
        "default": "0",

        "bold":       "1",
        "dim":        "2",
        "italic":     "3",
        "underlined": "4",
        "blink":      "5",
        "reverse":    "7",
        "hidden":     "8",
        "deleted":    "9",

        "resetBold":       "21",
        "resetDim":        "22",
        "resetItalic":     "23",
        "resetUnderlined": "24",
        "resetBlink":      "25",
        "resetReverse":    "27",
        "resetHidden":     "28",
        "resetDeleted":    "29",

        # Forecolors
        "chBlack":    "30",
        "chRed":      "31",
        "chGreen":    "32",
        "chYellow":   "33",
        "chBlue":     "34",
        "chMagenta":  "35",
        "chCyan":     "36",
        "chDefault":  "39",
        "chDarkGray": "90",
        "chWhite":    "97",

        # Background colors
        "bgBlack":    "40",
        "bgRed":      "41",
        "bgGreen":    "42",
        "bgYellow":   "43",
        "bgBlue":     "44",
        "bgMagenta":  "45",
        "bgCyan":     "46",
        "bgDefault":  "49",
        "bgDarkGray": "100",
        "bgWhite":    "107",
    }"""
    C = {
        "default": "0",

        "bold":       "1",
        "dim":        "2",
        "italic":     "3",
        "underlined": "4",
        "blink":      "5",
        "reverse":    "7",
        "hidden":     "8",
        "deleted":    "9",

        "resetBold":       "21",
        "resetDim":        "22",
        "resetItalic":     "23",
        "resetUnderlined": "24",
        "resetBlink":      "25",
        "resetReverse":    "27",
        "resetHidden":     "28",
        "resetDeleted":    "29",

        # Forecolors
        "chBlack":    "30",
        "chRed":      "31",
        "chGreen":    "32",
        "chYellow":   "33",
        "chBlue":     "34",
        "chMagenta":  "35",
        "chCyan":     "36",
        "chDefault":  "39",
        "chDarkGray": "90",
        "chWhite":    "97",

        # Background colors
        "bgBlack":    "40",
        "bgRed":      "41",
        "bgGreen":    "42",
        "bgYellow":   "43",
        "bgBlue":     "44",
        "bgMagenta":  "45",
        "bgCyan":     "46",
        "bgDefault":  "49",
        "bgDarkGray": "100",
        "bgWhite":    "107",
    }
    result = "\033["
    for t in args:
        if t in C:
            result += C[t] + ";"
        else:
            raise NameError
    return result[:-1] + "m"


def clearScreen():
    return "\033[2J"