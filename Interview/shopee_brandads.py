
## input: [1,1,2,3,3,5,5](sorted list)


## 0,1,2,3

## First thought: binary search
func FindOdd(arr []int) int {
	i,j := 0, len(arr)-1
	for {
		// if i>j{
		// 	fmt.Println("error, i>j")
		// 	return -1
		// }
		if i == j{
			return arr[i]
		}

		mid := (i+j)/2
		cur := arr[mid]
		//todo: check out of bound
		//check left
		var l, r int
		if arr[mid-1] == cur {
			l,r = mid-1, mid
		}else if arr[mid+1] == cur {
			l,r = mid, mid+1
		}else{ 
			return cur
		}
		
		// check answer is in left or right
        // when index=i, length = l >> there are [i elements on the left], [l-i-1 elements on the right] 
		if (l %2) != 0{
			j = l-1
			continue
		} else {
			i = r +1
			continue
		}

	}
}