// +build ignore

package main

import (
	"fmt"
	"os"
)

// N is max size of row and col
const N int = 15

// Declare slice a
var a [][]int

func main() {
	// make a
	a = make([][]int, N)
	for i := range a {
		a[i] = make([]int, N)
	}
	// Read file
	file, err := os.Open("./txt/PE18.txt")
	// error check
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	// input
	for i := 0; i < N; i++ {
		for j := 0; j <= i; j++ {
			fmt.Fscanf(file, "%d", &a[i][j])
		}
	}
	file.Close()
	// Output file
	for i := 0; i < N; i++ {
		fmt.Println(a[i])
	}

	ret := dfs(0, 0)
	fmt.Println(ret)
}

func dfs(i int, j int) int {
	if i == N-1 {
		return a[i][j]
	}
	ret := dfs(i+1, j)
	ret2 := dfs(i+1, j+1)
	if ret < ret2 {
		ret = ret2
	}
	return ret + a[i][j]
}
