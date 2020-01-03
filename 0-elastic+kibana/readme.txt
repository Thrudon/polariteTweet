tweets_unlabeled.json est la traduction de unlabeled.xml pour permettre son ajout au réseau Elasticsearch.
Voici les commandes effectués pour la suite Elasticsearch:

curl -X PUT "localhost:9200/test_debat" -H 'Content-Type: application/json' -d @mapping_debat
curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/test_debat/_bulk?pretty' --data-binary @out.json