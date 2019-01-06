# Classic Cookie Lines Challenge #1
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
<pre>[2, 1, 4, 3, 1, 1]</pre>


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
18.     
19. def main(cookie, choco_chip):
20.     m, n = len(cookie), len(cookie[0])
21.     for i, row in enumerate(cookie):
22.         for j, col in enumerate(row):
23.             if col == choco_chip:      # checking if curent_cell is a choco_chip
24.                 neighbour_count.count = 0
25.                 yield neighbour_count(cookie, i, j, choco_chip, m, n)
26. 
27.  
28. if __name__ == '__main__':
29.     choco_chip = 1
30.     cookie_string = """010000
31.                        010000
32.                        101101
33.                        011011
34.                        100100
35.                        000000"""
36.     cookie = [[int(chip) for chip in row.strip()] for row in cookie_string.split('\n')]
37.     print(list(main(cookie, choco_chip)))
```


## Code explanation:  
code enters from line number 28  
<hr>

```python 
29.     choco_chip = 1
```  
This defines the number which should be considered as choco chip.  
It  can be set to zero or one depending upon interviewer.  
<br/>
lines 30-35 sets a random cookie string example.  
<br/>
<hr>

```python 
36. cookie = [[int(chip) for chip in row.strip()] for row in cookie_string.split('\n')]
```  
This is list comprehension that iterates over each row in cookie_string that is found by splitting the string by newline.  
For each row, each element is parsed as int and stored in cookie list.  
<br/>
line 37 calls main function with cookie matrix and choco_chip type.  
<br/>
Inside main function:  
<hr>

```python 
20.     m, n = len(cookie), len(cookie[0])
```  
This sets m and n to dimensions of the cookie matrix.  
m: number of rows.  
n: number of columns.  
<br/>
lines 21, 22 iterates over cookie matrix to get all the cell values in iterative manner.  
line 23 checks if currently cell being assessed is a choco_chip.  
<br/>
<hr>

```python 
24.                 neighbour_count.count = 0
```  
This sets the initial counter to zero before algorithm is executed.  
<br/>
<hr>

```python 
25.                 yield neighbour_count(cookie, i, j, choco_chip, m, n)
```  
Calling function with coordinates of current choco chip cell.  
<br/>
Inside neighbour_count function:  
<hr>

```python 
2.     if (x<m and y<n) and (x>=0 and y>=0):
```  
Making sure that x and y are not out of bounds and it doesn't access an illegal location.  
<br/>
<hr>

```python 
3.         if cookie[x][y] == choco_chip:
```  
Checking if the cell with given coordinates is a choco chip.  
<br/>
<hr>

```python 
6.             neighbour_count.count += 1
```  
Incrementing the counter when current cell is a choco chip.  
<br/>
<hr>

```python 
8.             cookie[x][y] = 1-choco_chip
```  
This line replaces current value of choco chip value  
with it's alternate part's value which represents non choco chip part  
in order to make sure that it is not used again.  
<br/>
lines 11, 12, 13, 14 runs the algorithm for cell to right, left, top, down wrt to current cell being assessed.  

