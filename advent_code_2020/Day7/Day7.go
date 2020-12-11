package main

import (
	"fmt"
	"leetcode_problems/EPI/advent_code_2020/helpers"
	"strconv"
	"strings"
)

type childObj struct {
	name  string
	count int
}

type Graph struct {
	m map[string][]childObj
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
	// fmt.Println(len(potentialRoots))
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

func (g *Graph) countParentBags(target string, minCount int) int {

	roots := g.findRoots()
	// fmt.Println("roots", len(roots))
	pathNodeSet := make(map[string]bool)
	for _, root := range roots {
		curPath := []string{}
		storePath(target, root, g, &curPath, pathNodeSet)

	}
	// fmt.Println(pathNodeSet)
	return len(pathNodeSet)
}

func storePath(target string, curNode string, g *Graph, curPath *[]string, pathNodeSet map[string]bool) {

	if curNode == target {
		// fmt.Println(curPath)
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

func main() {
	fmt.Println(SolveDay7Part1("Day7_input.txt"))
	// fmt.Println(SolveDay7Part1("Day7_test_input.txt"))
}

func SolveDay7Part1(filename string) int {

	strs := helpers.ReadStr(filename)

	graph := Graph{}
	for _, str := range strs {

		parent, children := parseBagInfo(str)
		// fmt.Println(parent, children)
		graph.updateGraph(parent, children)
	}

	// fmt.Println(graph)

	return graph.countParentBags("shiny gold", 1)
	// return 1

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
