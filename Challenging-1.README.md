Challenge #1 - Programming

Unit Test:
=
> The unit test cases are under `tests/test_message.py`

Without docker - how to run as standalone process
=
`pip3 install -r requirements.txt`
<BR><i>install required packages need to run</i><BR>
`python3 app.py`
<BR><i>Run the standalone program</i><BR>
`curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://localhost:8080/messages`
<BR><i>Run the test to return the hash for FOO</i><BR>
`curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483`
<BR><i>Run the test to return the message but the hash does not exist</i><BR>
`curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae`
<BR><i>Run the test to return the message FOO</i><BR>

How to deploy to Docker and run from command line by curl
=
`docker build -t paxos-test_v1 .`
<BR><i>Build image at docker container</i><BR>
`docker run -d -p 8080:8080 paxos-test_v1`
<BR><i>Run image at docker container</i><BR>
`curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://localhost:8080/messages`
<BR><i>Run the test to return the hash for FOO</i><BR>
`curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483`
<BR><i>Run the test to return the message but the hash does not exist</i><BR>
`curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae`
<BR><i>Run the test to return the message FOO</i><BR>

Questions
=
Scaling Question :​
What would the bottleneck(s) be in your implementation as you acquire more users? How you might scale your
microservice?
> Ans: Currently all the messages and hashes stored in the memory. There is no memory limit imposed by Python. 
However, you will get a MemoryError if you run out of RAM. Also in the docker/Kubernetes environment,
the container allocate memory for the micro-services, so the memory is actually limited. Ideally, the 
micro-service should be stateless so the processing data should store in the `database` or `files` for future references.


Deployment Question:
How would you improve your deployment process if you needed to maintain this application long term?
> Ans: Every micro-service should implement `health check` to make sure the liveness of the process. We can use Jenkins 
to do the `deployment`, `automatic regression test` and `continuous integration test`. The production environment should 
be container-based and cloud-based.  Currently deploy to docker/kubernetes on AWS should be one of the best solutions.
