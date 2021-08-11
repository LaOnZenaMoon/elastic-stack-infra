from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

get_index = es.get(index="my_index", doc_type="doc1", id=1)
print(get_index)

search_index = es.search(index="my_index", body={"query": {"match_all": {}}})
print(search_index)
