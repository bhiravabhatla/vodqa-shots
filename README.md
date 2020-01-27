# vodqa-shots
This repo is a sample/POC for running python selenium tests in a docker container.

##Pre-requisites 
Make sure you have docker and docker-compose installed on your machines before running the tests.

AUT - SPREE - an opensourced e-commerce application. ( Refer - https://github.com/spree/spree )

To run the tests follow below steps :

* Clone the repo - `git clone https://github.com/bhiravabhatla/vodqa-shots.git`
* Run - `docker-compose up --build -d`
* Check the tests log using - `docker logs -f spree-selenium`

Expected outcome -

* A Spree container would spring up.
* Automated tests would run in another selenium container which would interact with spree container
* Tests output should contain list of products in the first page of the application
