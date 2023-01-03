import math
import os
import string
import nltk
import sys

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])

    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """

    files = {}
    root = os.path.join(os.getcwd(), directory)
    for filename in os.listdir(root):
        filedir = os.path.join(root, filename)
        with open(filedir, mode='r', encoding='utf-8') as f:
            document = f.read().rstrip("\n")
            files[filename] = document
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    word_list = nltk.word_tokenize(document.lower())

    punctuation = string.punctuation
    stopwords = nltk.corpus.stopwords.words('english')

    result = []
    for word in word_list:
        if word in stopwords:
            continue
        else:
            all_is_punct = True
            for char in word:
                if char not in punctuation:
                    all_is_punct = False
                    break
            if not all_is_punct:
                result.append(word)
    return result


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    dict = {}
    result = {}
    num_docs = len(documents)
    for document in documents:
        doc_words = set(documents[document])
        for word in doc_words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
    for word in dict:
        result[word] = math.log(num_docs / dict[word])
    return result


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    result = {filename: 0 for filename in files}
    for word in query:
        if word in idfs:
            for filename in files:
                result[filename] += (idfs[word] * files[filename].count(word))
    result = sorted([filename for filename in files], key=lambda x: result[x], reverse=True)
    return result[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    result = {sentence: {'idf_value': 0, 'query_term_density': 0} for sentence in sentences}
    for sentence in sentences:
        words = tokenize(sentence)
        length = len(words)
        for word in query:
            if word in sentences[sentence] and word in idfs:
                result[sentence]['idf_value'] += idfs[word]
                result[sentence]['query_term_density'] += sentences[sentence].count(word)
        result[sentence]['query_term_density'] /= length
    result = sorted([sentence for sentence in sentences],
                    key=lambda x: (result[x]['idf_value'], result[x]['query_term_density']), reverse=True)
    return result[:n]


if __name__ == "__main__":
    main()
