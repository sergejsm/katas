import re

dict = {"[\.,']": "", "too?": "2", "fore?": "4", "oo": "00", "be": "b",
        "are": "r", "you": "u", "please": "plz", "people": "ppl",
        "really": "rly", "have": "haz", "know": "no", "s": "z"}


def n00bify(text):
    for word in dict:
        text = re.sub(word, dict[word], text, flags=re.IGNORECASE)

    if text[0] in "hH":
        text = text.upper()

    if text[0] in "wW":
        text = "LOL " + text

    if len(re.sub("[\?!]*", "", text)) >= 32:
        text = re.sub("\A(LOL |)", "\g<1>OMG ", text)

    text = " ".join(w.upper() if i % 2 != 0 else w for i, w in enumerate(text.split()))

    text = re.sub("(\?|!)", "\g<1>" * len(text.split()), text).replace("!!", "!1")

    return text