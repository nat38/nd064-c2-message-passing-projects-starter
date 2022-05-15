
In order to build a reliable microservice environment I decided to carve out the location service of the API and split it into two separate services. This results in three micro services in total:

1. Uda-Personservice <br> This is the existing api but the location service is removed
2. Uda-Connectionservice <br> This is a new microservice that can be accessed via grpc interface and adds new connections. The connections are first put into a kafka topic before they get loaded into the database. It replaces the locationservice post functionality.
3. Uda-Locationservice <br> Provides the location information via a rest-interface. It replaces the locationservice get functionality

**Justification**
Since the functionality of the locationservice is not used in the already existing ui this is on of the best services to carve out first since no adaptions to the existing app needs to be made. Using grpc and kafka for adding new connections is done cause we expect high load if multiple users are going to use this app during a conference. The Kafka instance than easily buffers the data and the service stays responsive although the database might need some time to insert the data. Also grpc provides a lightweight solution for transmitting lots of data.

In order to ensure that the locations still can be received by consumers the additional Uda-Locationservice is offered via a simple REST-API. Rest is easy to implement and use. Since we do not expect super high load on that requests using REST and a direct call to the db is sufficient.

**Further considerations**
As next steps one could carve out the service that provides the specific connections of a person. This is a load intensive call and therefore could be done in a service that can scale horizontal. This however would result in a change of the UI.