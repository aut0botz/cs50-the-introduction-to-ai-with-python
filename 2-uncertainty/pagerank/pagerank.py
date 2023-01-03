import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # initialize
    prob_dist = {}
    pages_all = len(corpus.keys())
    pages_out = len(corpus[page])

    if pages_out < 1:
        # no page out, so every page is 1/n
        for key in corpus.keys():
            prob_dist[key] = 1 / pages_all
    else:
        # random_factor (1-d)probability to choose all pages randomly
        # choice_factor (d)probability to choose neighbors
        random_factor = (1 - damping_factor) / pages_all
        choice_factor = damping_factor / pages_out
        for key in corpus.keys():
            if key in corpus[page]:
                prob_dist[key] = random_factor + choice_factor
            else:
                prob_dist[key] = random_factor

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # initialize
    sample = None
    samples_dict = {}
    samples_dict = samples_dict.fromkeys(list(corpus.keys()), 0)

    # sample
    for i in range(n):
        if sample:
            # get the probability distribution of all pages and choose one page
            prob_dist = transition_model(corpus, sample, damping_factor)
            sample = random.choices(list(prob_dist.keys()), list(prob_dist.values()), k=1)[0]
        else:
            # random choice one page
            sample = random.choice(list(corpus.keys()))
        samples_dict[sample] += 1
    for i in samples_dict:
        samples_dict[i] /= n
    return samples_dict


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages_all = len(corpus.keys())
    iterate_old = {}
    iterate_new = {}
    iterate_old = iterate_old.fromkeys(list(corpus.keys()), 1 / pages_all)

    while True:
        for page in corpus:
            iterate_new[page] = 0
            for linked_page in corpus:
                linked_page_out_len = len(corpus[linked_page])
                if page in corpus[linked_page]:
                    # iterate_old implies the probability that wo are on this page at any given time
                    iterate_new[page] += iterate_old[linked_page] / linked_page_out_len
                if linked_page_out_len == 0:
                    # A page that has no links at all should be interpreted as having one link
                    # for every page in the corpus (including itself).
                    iterate_new[page] += iterate_old[linked_page] / pages_all
            iterate_new[page] *= damping_factor
            iterate_new[page] += (1 - damping_factor) / pages_all
        difference = max([abs(iterate_new[i] - iterate_old[i]) for i in corpus])
        if difference < 0.01:
            break
        else:
            iterate_old = iterate_new.copy()
    return iterate_new


if __name__ == "__main__":
    main()
