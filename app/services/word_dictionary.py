from datamuse import datamuse


def get_synonym_words(word: str):
    """ Gets similar words from onelookup datamuse library for the given word

    Args:
        word (str): word input

    Returns:
        TODO: fill in return type
        _type_: _description_
    """
    api = datamuse.Datamuse()
    similar_words = api.words(ml=word)
    return similar_words
