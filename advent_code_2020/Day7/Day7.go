package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(SolveDay7Part1("Day7_input.txt"))
	fmt.Println(SolveDay7Part2("Day7_input.txt"))
	// fmt.Println(SolveDay7Part1("Day7_test_input.txt"))
	// fmt.Println(SolveDay7Part2("Day7_test_input.txt"))
}

type childObj struct {
	name  string
	count int
}

// Graph is out custom graph Data Structure
type Graph struct {
	m map[string][]childObj
}

func SolveDay7Part1(filename string) int {

	strs := helpers.ReadStr(filename)

	graph := Graph{}
	for _, str := range strs {

		parent, children := parseBagInfo(str)
		graph.updateGraph(parent, children)
	}

	return graph.countParentBags("shiny gold")
}

func SolveDay7Part2(filename string) int {

	strs := helpers.ReadStr(filename)

	graph := Graph{}
	for _, str := range strs {

		parent, children := parseBagInfo(str)
		graph.updateGraph(parent, children)
	}

	return graph.countNumBags("shiny gold")
}

func (g *Graph) updateGraph(parent string, children []childObj) {

	if g.m == nil {
		g.m = make(map[string][]childObj)
	}

	if val, ok := g.m[parent]; !ok {
		g.m[parent] = children
	} else {
		children = append(children, val...)
	}
}

func (g *Graph) findRoots() []string {
	potentialRoots := []string{}

	for k := range g.m {
		potentialRoots = append(potentialRoots, k)
	}

	for _, v := range g.m {

		for _, obj := range v {
			loc := helpers.Locate(potentialRoots, obj.name)
			if loc != -1 {
				potentialRoots[loc] = potentialRoots[len(potentialRoots)-1]

				potentialRoots = potentialRoots[:len(potentialRoots)-1]
			}
		}
	}
	return potentialRoots
}

func (g *Graph) countParentBags(target string) int {

	roots := g.findRoots()

	pathNodeSet := make(map[string]bool)
	for _, root := range roots {
		curPath := []string{}
		storePath(target, root, g, &curPath, pathNodeSet)

	}

	return len(pathNodeSet)
}

func storePath(target string, curNode string, g *Graph, curPath *[]string, pathNodeSet map[string]bool) {

	if curNode == target {
		for _, node := range *curPath {
			pathNodeSet[node] = true
		}
		return
	}

	val, _ := g.m[curNode]
	if len(val) == 0 {
		return
	}

	*curPath = append(*curPath, curNode)

	for _, childObj := range val {
		storePath(target, childObj.name, g, curPath, pathNodeSet)
	}

	*curPath = (*curPath)[:len(*curPath)-1]
}

func (g *Graph) countNumBags(target string) int {

	children := g.m[target]

	if len(children) == 0 {
		return 0
	}

	ans := 0
	for _, obj := range children {

		child, count := obj.name, obj.count

		ans += (count + count*(g.countNumBags(child)))
	}
	return ans
}

func parseBagInfo(info string) (string, []childObj) {

	arr := strings.Split(info, "bag")

	children := []childObj{}
	parent := arr[0][:len(arr[0])-1]

	for _, st := range arr[1:] {

		for j, ch := range st {
			num, err := strconv.Atoi(string(ch))
			if err == nil {
				count := num
				child := st[j+2 : len(st)-1]
				children = append(children, childObj{child, count})
				break
			}
		}

	}

	return parent, children
}
