import spacy
from spacy.tokens import Span, Doc
from spacy.matcher import Matcher, PhraseMatcher


nlp = spacy.load('en_core_web_sm')
print(nlp.pipe_names)


# @Language.component('my_pipeline')
def my_pipeline(doc):
    print('Doc length:', len(doc))
    return doc

nlp.add_pipe(my_pipeline)
print(nlp.pipe_names)






























