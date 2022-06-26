package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
)

const portNumber = ":8080"

type User struct {
    Name   string `json:"username"`
    Age    int    `json:"age"`
    Gender string `json:"gender"`
}

func UsersHandler(w http.ResponseWriter, r *http.Request) {

    users := []User{
        {
            Name:   "Sam",
            Age:    52,
            Gender: "Female",
        },
        {
            Name:   "Lakshmi",
            Age:    19,
            Gender: "Female",
        },
        {
            Name:   "Rani",
            Age:    50,
            Gender: "Female",
        },
    }

    usersJson, err := json.Marshal(users)
    if err != nil {
        log.Fatal(err)
    }
    w.Write(usersJson)
}

func main() {

    http.HandleFunc("/users", UsersHandler)
    fmt.Printf("Starting application on port %v\n", portNumber)
    http.ListenAndServe(portNumber, nil)
}

