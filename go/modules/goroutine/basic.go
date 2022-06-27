package main


import (
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "strconv"
)

func main() {

    for i := 1; i < 200; i++ {
        go getDataFaster("https://rickandmortyapi.com/api/character/" + strconv.Itoa(i))

    }
}

func getDataFaster(url string) {
    r, err := http.Get(url)
    if err != nil {
        log.Fatal(err)
    }
    defer r.Body.Close()
    body, err := ioutil.ReadAll(r.Body)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(body))
}

