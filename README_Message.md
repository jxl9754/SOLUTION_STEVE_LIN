GitHub:
https://github.com/jxl9754/SOLUTION_STEVE_LIN.git

Challenge #1 - Programming

This is the test for slin to implement a sha256 example

Unit Test
you can run the unit test cases under tests/test_message.py

Without docker - run standalone
1. python3 main.py
2. curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://localhost:8080/messages
3. curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483
4. curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae

Deploy to Docker and run from command line by curl
1. docker build -t paxos-test_v1 .
2. docker run -d -p 8080:8080 paxos-test_v1
3. curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' http://localhost:8080/messages
4. curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483
5. curl http://localhost:8080/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae

Scaling Question ​
What would the bottleneck(s) be in your implementation as you acquire more users? How you might scale your
microservice?
Ans: Currently all the messages and hashes stored in the memory. There is no memory limit imposed by Python. 
However, you will get a MemoryError if you run out of RAM. Also in the docker/Kubernetes environment,
the container allocate memory for the micro-services, so the memory is actually limited. Theoretically, the 
micro-service should be stateless so the data should store in the database or files for future references.


Deployment Question
How would you improve your deployment process if you needed to maintain this application long term?
Ans: Every micro-service should implement health check to make sure the liveness of the process. I used Jenkins 
to do the deployment and automatic regression test. 
