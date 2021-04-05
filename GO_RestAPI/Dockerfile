FROM golang:latest

WORKDIR /application

COPY go.mod .
COPY go.sum .

RUN go mod download
COPY ./Go_RestAPI .

RUN go build

CMD ["./GO_RestAPI"]