package main

import (
	"fmt"
	
)

func main() {
	height := 8

	for i:=0; i<height; i++ {		
		gap := height-i-1
		for j := i ; j>=0; j--{
			printNtimes(" ", gap)
			printHeight(j)
			printNtimes(" ", gap)
		}
		fmt.Println("")
	}
}

func printHeight(i int){	
	fmt.Print("/")
	printNtimes(" ", 2*i)
	fmt.Print("\\")
}

func printNtimes(ch string, n int){
	i := 0
	for i != n {
		fmt.Print(ch)
		i++
	}
}

/// Note
height := 4
   /\   //3 space+ (l+r)
  /  \    /\        // 2space+l+2space+r+4space
 /    \  /  \  /\
/      \/    \/  \/\



i=0 : 

i = 3[/    \, /  \, /\]
i = 4[/      \, /    \, /  \, /\]


0,1,2,3
index: [height-1, height-2, ...2,1,0]

i = height-1
i = height-2 ~ height-1
... 
i = 0 ~ height-1

func: (index[i]) + l + (2*index[-i]) + r




