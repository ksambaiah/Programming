package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "strconv"
)

func main() {

    ch := make(chan string)
    var data []string
    for i := 1; i < 200; i++ {
        go getDataFaster("https://rickandmortyapi.com/api/character/"+strconv.Itoa(i), ch)
        data = append(data, <-ch)
    }
    fmt.Println(data)

}

func getDataFaster(url string, c chan string) {
    r, err := http.Get(url)
    if err != nil {
        log.Fatal(err)
    }
    defer r.Body.Close()
    body, err := ioutil.ReadAll(r.Body)
    if err != nil {
        log.Fatal(err)
    }
    c <- string(body)
}

