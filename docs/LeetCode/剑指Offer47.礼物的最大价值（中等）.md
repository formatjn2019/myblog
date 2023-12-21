剑指Offer47.礼物的最大价值

[剑指Offer47.礼物的最大价值](https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/)



解法：动态规划

经典寻路问题

使用长宽+1的矩阵避免越界判定

```go
func maxValue(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	matrix := make([][]int, m+1)
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	for i := 0; i < m+1; i++ {
		matrix[i] = make([]int, n+1)
	}
	for i, arr := range grid {
		for j, num := range arr {
			matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1]) + num
		}
	}
	return matrix[m][n]
}
```
