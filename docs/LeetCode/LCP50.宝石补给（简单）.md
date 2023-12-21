LCP50.宝石补给

[LCP50.宝石补给](https://leetcode.cn/problems/WHnhjV/)





解法：模拟



```go
func giveGem(gem []int, operations [][]int) int {
	for _, oper := range operations {
		g, r := oper[0], oper[1]
		gem[r] = gem[r] + gem[g]/2
		gem[g] = gem[g] - gem[g]/2
	}
	minv, maxv := gem[0], gem[0]
	for _, v := range gem {
		if minv > v {
			minv = v
		}
		if maxv < v {
			maxv = v
		}
	}
	return maxv - minv
}
```
