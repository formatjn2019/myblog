LCP06.拿硬币（简单）

[LCP06.拿硬币（简单）](https://leetcode.cn/problems/na-ying-bi/)



解法：贪心



```go
func minCount(coins []int) int {
	var result int
	for _, coin := range coins {
		result += (coin + 1) / 2
	}
	return result
}
```
