# Classic Cookie Challenge
### [Problem description here.](https://youtu.be/a4Py6rrf2Dk)


## Problem Description:
Given a cookie in matrix structure, where elements of the matrix are either 1 or 0  representing :

| element |   description   |
| ------- | --------------- |
|   `1`   | a chocolate chip|
|   `0`   |    other part   |

You have to find all the number of chocolate chips in each groups which are there in the chocolate cookie.  
Chocolate cookies are grouped together when they share one edge common between them.  
That is for a piece of cookie chip, possible grouping elements are:
   - [x] top
   - [x] left
   - [x] right
   - [x] down
   - [ ] diagonal
   
  
  
  
<table>
<tr><th>Cookie</th><th>Matrix representation</th><td rowspan=6>When chocolate chip is represented by 1.</td></tr>
<tr><td>

|   |   |   |   |   |   |
| - | - | - | - | - | - |
| &#9634;  | &#11044; | &#9634;  | &#9634;  | &#9634;  | &#9634;  |
| &#9634;  | &#11044; | &#9634;  | &#9634;  | &#9634;  | &#9634;  |
| &#11044; | &#9634;  | &#11044; | &#11044; | &#9634;  | &#11044; |
| &#9634;  | &#11044; | &#11044; | &#9634;  | &#11044; | &#11044; |
| &#11044; | &#9634;  | &#9634;  | &#11044; | &#9634;  | &#9634;  |
| &#9634;  | &#9634;  | &#9634;  | &#9634;  | &#9634;  | &#9634;  |

</td><td>

|   |   |   |   |   |   |
| - | - | - | - | - | - |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 |

</td></tr> </table>    


#### Result of grouping:    
![table](https://user-images.githubusercontent.com/20074475/50734125-cdc24f00-11bf-11e9-8c7c-dc31fa452fa2.png)

Answer of above example would be:
<pre>[1, 1, 1, 2, 3, 4]</pre>


## Solution Approach:
The solution includes iterative approach which iterates over the cookie matrix from up to down and left to right for each row in matrix.  
For each cell in the matrix, an algorithm analogus to boundary fill algorithm from computer graphics is used to find the neighbouring chocolate chips of the current cell which is taken in consideration.  


### Working of neighbouring algorithm:  
<pre>
<b>Algorithm</b> neighbour_count(coords):
</pre>
```python
   1. it takes in coordinates of current cell.  
   2. if current cell is not a chocolate chip:  
         goto step 6
   3. Recolor current cell to not chocolate chip value.  
   4. Increase the choco_chip_count by 1,  
      Indicating that, one more chip is found in the adjacent of previous one.  
   5. neighbour_count(top)  
      neighbour_count(right)  
      neighbour_count(left)  
      neighbour_count(bottom)  
      // this step will count the nearby cells having chocolate chip.  
  6. return choco_chip_count  
```

## Code
```python
1. def neighbour_count(cookie, x, y, choco_chip, m, n):
2.     if (x<m and y<n) and (x>=0 and y>=0):
3.         if cookie[x][y] == choco_chip:
4.             # current chip is chocolate chip.
5.             # counting current chip.
6.             neighbour_count.count += 1
7.             # replacing current cell value to non choco chip value
8.             cookie[x][y] = 1-choco_chip
9.             
10.             # running this algo for neighbouring cells.
11.             neighbour_count(cookie, x+1, y,   choco_chip, m, n) # right
12.             neighbour_count(cookie, x-1, y,   choco_chip, m, n) # left
13.             neighbour_count(cookie, x,   y+1, choco_chip, m, n) # top
14.             neighbour_count(cookie, x,   y-1, choco_chip, m, n) # down
15.                   
16.     return neighbour_count.count
17. 
18. def main(cookie, choco_chip):
19.     m, n = len(cookie), len(cookie[0])
20.     for i, row in enumerate(cookie):
21.         for j, col in enumerate(row):
22.             if col == choco_chip:      # checking if curent_cell is a choco_chip
23.                 neighbour_count.count = 0
24.                 yield neighbour_count(cookie, i, j, choco_chip, m, n)
25. 
26. 
27. if __name__ == '__main__':
28.     choco_chip = 1
29.     cookie_string = """010000
30.                        101101
31.                        011011
32.                        100100
33.                        000000"""
34.     cookie = [[int(chip) for chip in row.strip()] for row in cookie_string.split('\n')]
35.     print(list(main(cookie, choco_chip)))
```
