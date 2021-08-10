from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

indices = es.cat.indices()
print(indices)

doc={
    "name": "JUN LEE",
    "job": "programmer"
}
index = es.index(index="my_index", doc_type="doc1", id=1, body=doc)
print(index)
