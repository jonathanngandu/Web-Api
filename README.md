# **Web Api**

#### Commands
###### **gCloud**

* gcloud container builds submit --config cloudbuild.yaml .

###### **Docker**

* docker exec -it -u www-data:www-data webapi_web_1 bash
* docker cp webapi_web_1:/app/src/myGoogle/resources/fileToUpload.jpg src/myGoogle/resources/

###### **Heroku**

* heroku logs --app gentle-mountain-18458
* [Heroku pipline](https://dashboard.heroku.com/apps/gentle-mountain-18458)
* [Herokuapp URL](https://gentle-mountain-18458.herokuapp.com)

#### Commands
###### **Routes**

* _/_ - Home route using **GET** request
* _/image-text_ - Get google vision text using **POST** OR  **PUT** request. Example request body:

```
{
	"filename" : "wakeupcat.jpg"
}
```

#### GitHub

* [Lenki/Web-Api orginal](https://github.com/Lenki/Web-Api)
* [Jonathanngandu/Web-Api](https://github.com/jonathanngandu/Web-Api)

