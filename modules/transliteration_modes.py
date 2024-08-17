from typing import Dict, List, Tuple


class TransliterationMode:
    def __init__(self, name: str, mappings: List[Tuple[str, str]]):
        self.name = name
        self.mappings = dict(mappings)

    def transliterate(self, text: str) -> str:
        result = []
        i = 0
        while i < len(text):
            # Check for multi-character mappings first
            for length in range(3, 0, -1):
                if text[i : i + length] in self.mappings:
                    result.append(self.mappings[text[i : i + length]])
                    i += length
                    break
            else:
                # If no mapping found, keep the original character
                result.append(text[i])
                i += 1
        return "".join(result)


class TransliterationManager:
    def __init__(self):
        self.modes: Dict[str, TransliterationMode] = {}

    def add_mode(self, name: str, mappings: List[Tuple[str, str]]):
        self.modes[name] = TransliterationMode(name, mappings)

    def get_mode(self, name: str) -> TransliterationMode:
        return self.modes.get(name)

    def get_mode_names(self) -> List[str]:
        return list(self.modes.keys())


# Initialize with existing Futhorc mode
from modules.mappings import mappings as futhorc_mappings

transliteration_manager = TransliterationManager()
transliteration_manager.add_mode("Futhorc", futhorc_mappings)

# Elder Futhark mappings
elder_futhark_mappings = [
    ("a", "ᚨ"),
    ("b", "ᛒ"),
    ("c", "ᚲ"),
    ("d", "ᛞ"),
    ("e", "ᛖ"),
    ("f", "ᚠ"),
    ("g", "ᚷ"),
    ("h", "ᚺ"),
    ("i", "ᛁ"),
    ("j", "ᛃ"),
    ("k", "ᚲ"),
    ("l", "ᛚ"),
    ("m", "ᛗ"),
    ("n", "ᚾ"),
    ("o", "ᛟ"),
    ("p", "ᛈ"),
    ("q", "ᚲ"),
    ("r", "ᚱ"),
    ("s", "ᛋ"),
    ("t", "ᛏ"),
    ("u", "ᚢ"),
    ("v", "ᚠ"),
    ("w", "ᚹ"),
    ("x", "ᚲᛋ"),
    ("y", "ᛃ"),
    ("z", "ᛉ"),
    ("th", "ᚦ"),
    ("ng", "ᛜ"),
    ("ae", "ᚨᛖ"),
    ("oe", "ᛟᛖ"),
    (" ", "᛫"),
    ("  ", ""),
    (",", "᛬"),
    (". ", "⫶"),
    ("-", "᛫"),
]
transliteration_manager.add_mode("Elder Futhark", elder_futhark_mappings)

# Younger Futhark Long-branch (Danish) runes
younger_futhark_long_branch_mappings = [
    ("a", "ᛅ"),
    ("b", "ᛒ"),
    ("c", "ᛋ"),
    ("d", "ᛏ"),
    ("e", "ᛁ"),
    ("f", "ᚠ"),
    ("g", "ᚴ"),
    ("h", "ᚼ"),
    ("i", "ᛁ"),
    ("j", "ᛁ"),
    ("k", "ᚴ"),
    ("l", "ᛚ"),
    ("m", "ᛘ"),
    ("n", "ᚾ"),
    ("o", "ᚢ"),
    ("p", "ᛒ"),
    ("q", "ᚴ"),
    ("r", "ᚱ"),
    ("s", "ᛋ"),
    ("t", "ᛏ"),
    ("u", "ᚢ"),
    ("v", "ᚢ"),
    ("w", "ᚢ"),
    ("x", "ᛋ"),
    ("y", "ᚢ"),
    ("z", "ᛋ"),
    ("th", "ᚦ"),
    ("ae", "ᛅ"),
    ("oe", "ᚢ"),
    (" ", "᛫"),
    ("  ", ""),
    (",", "᛬"),
    (". ", "⫶"),
    ("-", "᛫"),
]
transliteration_manager.add_mode(
    "Younger Futhark (Long-branch)", younger_futhark_long_branch_mappings
)

# Younger Futhark Short-twig (Swedish and Norwegian) runes
younger_futhark_short_twig_mappings = [
    ("a", "ᛆ"),
    ("b", "ᛒ"),
    ("c", "ᛌ"),
    ("d", "ᛐ"),
    ("e", "ᛁ"),
    ("f", "ᚠ"),
    ("g", "ᚴ"),
    ("h", "ᚽ"),
    ("i", "ᛁ"),
    ("j", "ᛁ"),
    ("k", "ᚴ"),
    ("l", "ᛚ"),
    ("m", "ᛘ"),
    ("n", "ᚿ"),
    ("o", "ᚢ"),
    ("p", "ᛒ"),
    ("q", "ᚴ"),
    ("r", "ᚱ"),
    ("s", "ᛌ"),
    ("t", "ᛐ"),
    ("u", "ᚢ"),
    ("v", "ᚢ"),
    ("w", "ᚢ"),
    ("x", "ᛌ"),
    ("y", "ᚢ"),
    ("z", "ᛌ"),
    ("th", "ᚦ"),
    ("ae", "ᛆ"),
    ("oe", "ᚢ"),
    (" ", "᛫"),
    ("  ", ""),
    (",", "᛬"),
    (". ", "⫶"),
    ("-", "᛫"),
]
transliteration_manager.add_mode(
    "Younger Futhark (Short-twig)", younger_futhark_short_twig_mappings
)
