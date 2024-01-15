
from icupy.icu import Transliterator
from icupy.icu import UnicodeString
from icupy.icu import UParseError
from icupy.icu import UTransDirection

# ID and rules for the custom transliterator
id = "LLC-Sicangu"
rules = """
            tȟ  >  ṫ;
            Tȟ  >  Ṫ;
            TȞ  >  Ṫ;
            ȟ   >  ḣ;
            Ȟ   >  Ḣ;
            čh  >  ċ;
            Čh  >  Ċ;
            ČH  >  Ċ;
        """

# Instantiate the custom transliterator
parseError = UParseError()
translit = Transliterator.create_from_rules(id, rules, UTransDirection.UTRANS_FORWARD, parseError)

# Function that transliterates the input and prints the result
def print_example(input):
    input_as_unicode = UnicodeString(input)
    translit.transliterate(input_as_unicode)
    print("BEFORE: ", input, ", AFTER: ", input_as_unicode, sep="")

# Print some examples of "deer" in Lakota
print_example("tȟáȟčha")  # Lowercase
print_example("Tȟáȟčha")  # First letter capitalized
print_example("TȞÁȞČHA")  # All capitalized
