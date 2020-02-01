from collections import defaultdict
from gensim import corpora, models, similarities
import re
import string

def check_similarity(doc):
    documents = [
        "Firefighter Bill Slade sacrificed his life while trying to put out the massive Australian wildfires. Please donate to pledge your support to Mr. Bill Slade's family and to help the wildfire support.",
        "On her birthday, Miss Universe 2018, Catriona Gray, would like to continue to share and give smiles to Philippine children this 2020. Join her as she continuously raise funds and awareness to the plight of children who are born with cleft. This fundraising project will be directly donated to the non-profit organisation, SMILE TRAIN PHILIPPINES.",
        "I am JULIUS BANIQUED, 48 years old from Manila, Philippines. I am suffering from Chronic Kidney Disease (CKD) and has been undergoing treatment. Unfortunately, dialysis treatments are no longer improving my condition and I am suffering from total kidney failure or End Stage Renal Disease which is the last stage (Stage 5) of CKD. My best option to survive is to undergo a kidney transplant.",
        "Bushfires have been ravaging the southern most parts of Australia since October 2019 and the resident population including wildlife have been most vulnerable. The effects of bushfires are devastating and extreme fire conditions expected to kick in tomorrow. Australia is my home and my heart cries at the tragedy that has engulfed the country. We need your help. Please support us in whatever way you can. Donate through this link: all proceeds shall go to Rural Fire Services (NSW & VIC).",
        "Australian wildlife is in crisis. Bushfires and long-term drought are ravaging our beloved country, estimations are that over 1 billion animals have perished from fires alone, many more when the effects of the drought are considered. Please donate urgently today to help give our animals a fighting chance.",
        "Human machine interface for lab abc computer applications",
        "A survey of user opinion of computer system response time",
        "The EPS user interface management system",
        "System and human system engineering testing of EPS",
        "Relation of user perceived response time to error measurement",
        "The generation of random binary unordered trees",
        "The intersection graph of paths in trees",
        "Graph minors IV Widths of trees and well quasi ordering",
        "Graph minors A survey",
    ]

    # remove common words and tokenize
    stoplist = set('for a of the and to in'.split())
    texts = [
        [word for word in document.lower().split() if word not in stoplist]
        for document in documents
    ]

    # remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [
        [token for token in text if frequency[token] > 1]
        for text in texts
    ]

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)


    index = similarities.MatrixSimilarity(lsi[corpus])  # transform corpus to LSI space and index it

    # index.save('tmp\corpus_test.index') # Saves corpus in LSI space to file
    # index = similarities.MatrixSimilarity.load('tmp\corpus_test.index') # load index file


    # User Input (doc)
    # doc = "Firefighter John died while fighting Australian wildfires. Please donate to support!"
    # doc1 = "I have a chronic heart disease and I need money to pay my medical fees. Please support me with donations"
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]  # convert the query to LSI space

    # Check similarity of user input with index
    sims = index[vec_lsi] #Performs a similarity query
    print(sims)
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    for i, s in enumerate(sims):
        # send front_end similarity value s[1] and documents[i]
        return (s[1], documents[i])
