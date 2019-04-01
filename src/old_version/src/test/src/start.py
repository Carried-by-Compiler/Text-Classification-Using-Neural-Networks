from file_reader import FileReader
from doc2vec import D2V
from classifier import NN
import numpy as np


reader = FileReader()
model = D2V()

docs = list()
classifier = NN()
topics = list()
#training_data = list(reader.read_corpus_train())

#model.train(training_data)
model.load(reader.get_models_path(), "model1.d2v")

labels = model.get_labels()

for label in labels:
    docs.append(model.get_doc_vec(label))
    split_string = label.split("__")
    topics.append(split_string[0])
    classifier.add_topic(split_string[0])

# Convert topic in topics list to its vector representation
for i in range(len(topics)):
    topics[i] = classifier.get_topic_vector(topics[i])

new_doc = reader.process_new_doc("travelsample.txt")
doc_vec = model.infer_doc(new_doc)


classifier.train(np.array(docs, ndmin=2), np.array(topics, ndmin=2))
print("Classifier trained!")


results = classifier.predict(x=np.array(doc_vec, ndmin=2))
r = results.flatten()

ts = classifier.get_topics()

for i, t in enumerate(ts):
    print("{}: {}".format(t, r[i] * 100))





