TRANSLATIONS = {
    "High financial risk detected": "उच्च वित्तीय जोखिम पाया गया",
    "Healthy financial position": "स्वस्थ वित्तीय स्थिति",
}

def translate(text, lang):
    if lang == "hi":
        return TRANSLATIONS.get(text, text)
    return text
