// +build ignore

package main

import "fmt"

func sumOfProperDivisor(n int) int {
	s := 0
	for i := 1; i < n; i++ {
		if n%i == 0 {
			s += i
		}
	}
	return s
}

func main() {
	var d [10005]int
	for i := 1; i < 10000; i++ {
		d[i] = sumOfProperDivisor(i)
	}
	ans := 0
	for i := 1; i < 10000; i++ {
		for j := i + 1; j < 10000; j++ {
			if d[i] == j && d[j] == i {
				ans += i + j
			}
		}
	}
	fmt.Println(ans)
}
