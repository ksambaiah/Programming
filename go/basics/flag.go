package main

import (
   "flag"
   "fmt"
)

func main() {

   var str1 = flag.String("string1", "somestring", "a string") 
   flag.Parse()
   fmt.Println("String Value is ", *str1)

}
