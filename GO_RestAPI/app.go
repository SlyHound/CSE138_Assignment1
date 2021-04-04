package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message" : "I'm alive!!"}) // 200 status code
	})

	r.POST("/ping", func(c *gin.Context) {
		c.AbortWithStatus(http.StatusMethodNotAllowed) // 405 status code error
	})

	r.POST("/ping/:name", func(c *gin.Context) {
		name := c.Param("name")
		v := "I'm alive, " + name + "!!"
		c.JSON(http.StatusOK, gin.H{"message" : v}) // 200 status code
	})

	r.GET("/ping/:name", func(c *gin.Context) {
		c.AbortWithStatus(http.StatusMethodNotAllowed) // 405 status code error
	})

	r.GET("/echo", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message" : "Get Message Received"}) // 200 status code
	})

	r.POST("/echo", func(c *gin.Context)  {
		m := c.Query("msg")
		if m != "" {
			c.JSON(http.StatusOK, gin.H{"message" : m}) // 200 status code
		} else {
			c.AbortWithStatus(http.StatusBadRequest) // 400 status code error
		}
	})

	r.Run(":8085") // default port number is 8080
}