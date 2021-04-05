FROM golang:latest

WORKDIR /application

COPY go.mod .
COPY go.sum .

RUN go mod download
COPY . .

RUN go build

CMD ["./GO_RestAPI"]