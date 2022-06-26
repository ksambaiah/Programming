package main

import (
    "fmt"
    "strings"
)

func main() {

    fruits := "apple,orange,kiwi,peach"
    fruitSlice := strings.Split(fruits, ",")
    fmt.Println(fruitSlice)
    fmt.Println(len(fruitSlice))
    for i, x := range fruitSlice {
        fmt.Println(i)
        fmt.Println(x)
    }
    i := 0
    for i := 0, i < len(fruitSlice), i++ {
        fmt.Println(i)
        fmt.Println(fruitSlice[i])
    }
}


