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

func findDiff(numbers []int, result chan int) {
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
	result <- (max - min)
}

func parseInput() [][]int {
	f, e := os.Open(os.Args[1])
	handleErr(e)
	reader := bufio.NewReader(f)
	re := regexp.MustCompile("\\d+")
	input := [][]int{}
	for {
		l, e := reader.ReadString('\n')
		if e != nil {
			break
		}
		numbers := re.FindAllString(l, -1)
		input = append(input, parseIntSlice(numbers))
	}
	return input
}

func parseIntSlice(strs []string) []int {
	numbers := make([]int, len(strs))
	for i, s := range strs {
		v, e := strconv.Atoi(s)
		handleErr(e)
		numbers[i] = v
	}
	return numbers
}

func main() {
	sum := 0
	lines := 0
	diffs := make(chan int)
	for _, v := range parseInput() {
		go findDiff(v, diffs)
		lines++
	}
	for lines > 0 {
		sum += <-diffs
		lines--
	}
	fmt.Println(sum)
}
