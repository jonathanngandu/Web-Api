Web Api

gcloud container builds submit --config cloudbuild.yaml .
docker exec -it -u www-data:www-data webapi_web_1 bash
docker cp webapi_web_1:/app/src/myGoogle/resources/fileToUpload.jpg src/myGoogle/resources/