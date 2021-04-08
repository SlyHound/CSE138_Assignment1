# CSE138_Assignment1

## Note
To whomever is grading my assignment, could you please grade the Go code found in the Go_RestAPI folder please. If my Go application doesn't work, I guess you could attempt to test my Python Flask code found in the Python_RestAPI folder. I had two programs just in-case one failed and to try out Go for the first time!

## Acknowledgments
Patrick Redmond, our TA for this class helped to test my Go application on
the tests provided to us.

## Citations
Since I did the assignment using two different languages, I consulted the documentation for [Flask](https://flask.palletsprojects.com/en/1.1.x/) in Python. For Go I needed a little more than just looking at potential Rest API documentation. Before listing those sources, I went through the guides to learn [how to write Go code](https://golang.org/doc/code), touring the many [components of Go](https://golang.org/doc/), and a more [in-depth guide on Go](https://golang.org/doc/effective_go). I watched a couple of Youtube videos, namely 

<a href="https://www.youtube.com/watch?v=SonwZ6MF5BE&ab_channel=TraversyMedia"><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FSonwZ6MF5BE%2Fmaxresdefault.jpg&f=1&nofb=1" style="max-width: 100%"></a>

to learn Mux and to learn Gin

<a href="https://www.youtube.com/watch?v=LOn1GUsjOF4&list=WL&index=12&t=254s&ab_channel=DavidAlsh"><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FLOn1GUsjOF4%2Fmaxresdefault.jpg&f=1&nofb=1" style="max-width: 100%"></a>

I ended up going with using the [Gin](https://github.com/gin-gonic/gin) package for the Rest API.

Before reading over the [documentation](https://docs.docker.com/get-started/) of Docker, I spent some time watching this Youtube video on the subject,

<a href="https://www.youtube.com/watch?v=fqMOX6JJhGo&list=WL&index=10&t=1746s&ab_channel=freeCodeCamp.org"><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FfqMOX6JJhGo%2Fmaxresdefault.jpg&f=1&nofb=1" style="max-width: 100%"></a>

After that I took a look at the official Docker image on Dockerhub for [Golang](https://hub.docker.com/_/golang/) and [Python](https://hub.docker.com/_/python).