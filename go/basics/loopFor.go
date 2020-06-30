package main

import "fmt"

func main() {
    i := 1
    for i <= 3 {
        fmt.Println(i)
        i = i + 1
    }

    for i := 0; i <=7; i++ {
        fmt.Println("Value of i is", i)
    }

    if i < 5 {
       fmt.Println("i is smaller than 5 and it is  ", i)
    }

    j := 7

    if j < 5 {
       fmt.Println("j is smaller than 5", j)
    } else {
       fmt.Println("j is bigger than 5 and it is ", j)
    }  
}
