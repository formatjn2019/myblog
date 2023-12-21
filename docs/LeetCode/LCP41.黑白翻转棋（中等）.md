LCP41.黑白翻转棋

[LCP41.黑白翻转棋](https://leetcode.cn/problems/fHi6rV/)



解法：LFS+哈希表+位压缩



x,y坐标都小于等于8，可使用一个int类型存储x,y坐标，枚举每个空节点四周八个位置，若将白子转换，则将转换的白字放入下层继续枚举。

采用哈希表排除同一个棋子被两个方向的白子进行转换的情况。



```go
func flipChess(chessboard []string) int {
	m, n := len(chessboard), len(chessboard[0])
	matrix := make([][]rune, m)
	for i := 0; i < m; i++ {
		matrix[i] = []rune(chessboard[i])
	}
	var bfsSearch func(idxArr ...int) int
	bfsSearch = func(idxArr ...int) int {
		changedMap := map[int]bool{}
		//尝试翻转
		for _, oldZiped := range idxArr {
			x, y := oldZiped>>5, oldZiped%(1<<5)
			for difX := -1; difX < 2; difX++ {
				for difY := -1; difY < 2; difY++ {
					if !(difX == 0 && difY == 0) {
						var tp []int
						for j := 1; ; j++ {
							tx, ty := x+j*difX, y+j*difY
							if tx >= 0 && ty >= 0 && tx < m && ty < n {
								switch matrix[tx][ty] {
								case 'O':
									tp = append(tp, tx<<5|ty)
									continue
								case 'X':
									for _, ziped := range tp {
										changedMap[ziped] = true
									}
								}
							}
							break
						}
					}
				}
			}
		}
		if len(changedMap) > 0 {
			var keys []int
			//翻转
			for k, _ := range changedMap {
				x, y := k>>5, k%(1<<5)
				matrix[x][y] = 'X'
				keys = append(keys, k)
			}
			nNum := bfsSearch(keys...)
			//回翻
			for k, _ := range changedMap {
				x, y := k>>5, k%(1<<5)
				matrix[x][y] = 'O'
			}
			return len(changedMap) + nNum
		}
		return 0
	}
	result := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == '.' {
				if t := bfsSearch(i<<5 | j); t > result {
					result = t
				}
			}
		}
	}
	return result
}

```
