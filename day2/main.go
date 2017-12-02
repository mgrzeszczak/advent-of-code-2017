package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func handleErr(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	f, e := os.Open(os.Args[1])
	handleErr(e)
	input := bufio.NewReader(f)
	re := regexp.MustCompile("\\d+")
	sum := 0
	lines := 0
	diffs := make(chan int)
	for {
		l, e := input.ReadString('\n')
		if e != nil {
			break
		}
		numbersStr := re.FindAllString(l, -1)
		numbers := make([]int, len(numbersStr))
		for i, s := range numbersStr {
			v, e := strconv.Atoi(s)
			handleErr(e)
			numbers[i] = v
		}
		lines++
		go func() {
			max := numbers[0]
			min := numbers[0]
			for _, v := range numbers {
				if v > max {
					max = v
				}
				if v < min {
					min = v
				}
			}
			diffs <- (max - min)
		}()
	}

	for lines > 0 {
		sum += <-diffs
		lines--
	}
	fmt.Println(sum)
}
